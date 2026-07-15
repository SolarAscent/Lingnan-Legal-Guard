import { getNlsToken, isTokenSourceConfigured } from "./aliyunToken.js";

const DEFAULT_ALIYUN_ASR_ENDPOINT = "https://nls-gateway-cn-shanghai.aliyuncs.com/stream/v1/asr";
const MAX_AUDIO_BYTES = 10 * 1024 * 1024;

export const SUPPORTED_LANGUAGES = ["cantonese", "mandarin"];

// 按语言选择对应项目的 Appkey；兼容旧的单一 NLS_APP_KEY。
function resolveAppKey(language) {
  if (language === "mandarin") {
    return process.env.NLS_APP_KEY_MANDARIN || process.env.NLS_APP_KEY || "";
  }
  return process.env.NLS_APP_KEY_CANTONESE || process.env.NLS_APP_KEY || "";
}

function makeHttpError(message, statusCode, code) {
  const error = new Error(message);
  error.statusCode = statusCode;
  error.code = code;
  return error;
}

function normalizeAudioPayload(audioBase64) {
  const cleaned = String(audioBase64 || "").replace(/^data:[^;]+;base64,/, "").trim();
  if (!cleaned) {
    throw makeHttpError("请先录制或上传一段粤语音频", 400, "SPEECH_AUDIO_MISSING");
  }

  const buffer = Buffer.from(cleaned, "base64");
  if (!buffer.length) {
    throw makeHttpError("音频内容为空，请重新上传", 400, "SPEECH_AUDIO_EMPTY");
  }
  if (buffer.length > MAX_AUDIO_BYTES) {
    throw makeHttpError("音频文件过大，请上传 60 秒以内的音频", 413, "SPEECH_AUDIO_TOO_LARGE");
  }
  return buffer;
}

function inferFormat(mimeType = "") {
  const normalized = mimeType.toLowerCase();
  if (normalized.includes("wav")) return "wav";
  if (normalized.includes("mpeg") || normalized.includes("mp3")) return "mp3";
  if (normalized.includes("aac")) return "aac";
  if (normalized.includes("amr")) return "amr";
  if (normalized.includes("ogg")) return "opus";
  if (normalized.includes("webm")) return "opus";
  if (normalized.includes("pcm")) return "pcm";
  return process.env.ALIYUN_NLS_AUDIO_FORMAT || "wav";
}

// 至少配置了一个 Appkey，且有可用的 Token 来源（静态 Token 或 AccessKey）。
export function isAliyunSpeechConfigured() {
  const hasAnyAppKey = Boolean(
    process.env.NLS_APP_KEY_CANTONESE ||
      process.env.NLS_APP_KEY_MANDARIN ||
      process.env.NLS_APP_KEY,
  );
  return hasAnyAppKey && isTokenSourceConfigured();
}

export async function transcribeSpeechAudio({ audioBase64, mimeType, sampleRate, language = "cantonese" }) {
  const lang = SUPPORTED_LANGUAGES.includes(language) ? language : "cantonese";
  const label = lang === "mandarin" ? "普通话" : "粤语";

  const appKey = resolveAppKey(lang);
  if (!appKey || !isTokenSourceConfigured()) {
    throw makeHttpError(
      `请先配置${label} Appkey（NLS_APP_KEY_${lang === "mandarin" ? "MANDARIN" : "CANTONESE"}）以及 Token 来源` +
        "（ALIYUN_NLS_TOKEN 或 ALIYUN_AK_ID + ALIYUN_AK_SECRET），且该 Appkey 需在阿里云控制台绑定对应语言的识别模型",
      503,
      "ALIYUN_SPEECH_NOT_CONFIGURED",
    );
  }

  const token = await getNlsToken();
  const audioBuffer = normalizeAudioPayload(audioBase64);
  const endpoint = process.env.ALIYUN_NLS_ASR_ENDPOINT || DEFAULT_ALIYUN_ASR_ENDPOINT;
  const url = new URL(endpoint);
  url.searchParams.set("appkey", appKey);
  url.searchParams.set("format", inferFormat(mimeType));
  url.searchParams.set("sample_rate", String(sampleRate || process.env.ALIYUN_NLS_SAMPLE_RATE || 16000));
  url.searchParams.set("enable_punctuation_prediction", "true");
  url.searchParams.set("enable_inverse_text_normalization", "true");
  url.searchParams.set("enable_voice_detection", "true");

  const response = await fetch(url, {
    method: "POST",
    headers: {
      "X-NLS-Token": token,
      "Content-Type": "application/octet-stream",
      "Content-Length": String(audioBuffer.length),
    },
    body: audioBuffer,
  });

  const payload = await response.json().catch(() => ({}));
  if (!response.ok || payload.status !== 20000000) {
    const message = payload.message || `HTTP ${response.status}`;
    throw makeHttpError(`${label}识别失败：${message}`, 502, "ALIYUN_SPEECH_FAILED");
  }

  return {
    text: String(payload.result || "").trim(),
    taskId: payload.task_id,
    provider: "aliyun-nls",
    language: lang,
  };
}

// 兼容旧调用名。
export const transcribeCantoneseAudio = transcribeSpeechAudio;
