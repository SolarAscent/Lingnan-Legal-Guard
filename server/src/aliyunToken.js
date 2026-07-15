import { createHmac, randomUUID } from "node:crypto";

// 阿里云智能语音交互 Token 管理：
// - 优先用静态 ALIYUN_NLS_TOKEN（演示用，24 小时过期）
// - 否则用 AccessKey（ALIYUN_AK_ID + ALIYUN_AK_SECRET）调 CreateToken 动态换取，
//   并在内存缓存，过期前自动刷新，从此永不失效。

const CREATE_TOKEN_HOST = "http://nls-meta.cn-shanghai.aliyuncs.com/";
const REGION_ID = "cn-shanghai";

let cachedToken = null; // { token: string, expireAt: number(ms) }

// 阿里云 POP 专用百分号编码（RFC3986 + 三处特殊替换）。
function percentEncode(value) {
  return encodeURIComponent(value)
    .replace(/\+/g, "%20")
    .replace(/\*/g, "%2A")
    .replace(/%7E/g, "~");
}

function hasStaticToken() {
  return Boolean(process.env.ALIYUN_NLS_TOKEN);
}

function hasAccessKey() {
  return Boolean(process.env.ALIYUN_AK_ID && process.env.ALIYUN_AK_SECRET);
}

export function isTokenSourceConfigured() {
  return hasStaticToken() || hasAccessKey();
}

async function requestCreateToken() {
  const accessKeyId = process.env.ALIYUN_AK_ID;
  const accessKeySecret = process.env.ALIYUN_AK_SECRET;

  const params = {
    AccessKeyId: accessKeyId,
    Action: "CreateToken",
    Format: "JSON",
    RegionId: REGION_ID,
    SignatureMethod: "HMAC-SHA1",
    SignatureNonce: randomUUID(),
    SignatureVersion: "1.0",
    Timestamp: new Date().toISOString().replace(/\.\d{3}Z$/, "Z"),
    Version: "2019-02-28",
  };

  const canonicalized = Object.keys(params)
    .sort()
    .map((key) => `${percentEncode(key)}=${percentEncode(params[key])}`)
    .join("&");

  const stringToSign = `GET&${percentEncode("/")}&${percentEncode(canonicalized)}`;
  const signature = createHmac("sha1", `${accessKeySecret}&`)
    .update(stringToSign)
    .digest("base64");

  const url = `${CREATE_TOKEN_HOST}?Signature=${percentEncode(signature)}&${canonicalized}`;
  const response = await fetch(url, { method: "GET" });
  const payload = await response.json().catch(() => ({}));

  if (!response.ok || !payload?.Token?.Id) {
    const message = payload?.Message || payload?.ErrMsg || `HTTP ${response.status}`;
    const error = new Error(`获取阿里云语音 Token 失败：${message}`);
    error.statusCode = 502;
    error.code = "ALIYUN_TOKEN_FAILED";
    throw error;
  }

  // ExpireTime 是 Unix 秒。
  return {
    token: payload.Token.Id,
    expireAt: Number(payload.Token.ExpireTime) * 1000,
  };
}

// 返回一个可用的 NLS Token；动态模式下带缓存与提前刷新。
export async function getNlsToken() {
  if (hasStaticToken()) {
    return process.env.ALIYUN_NLS_TOKEN;
  }

  if (!hasAccessKey()) {
    const error = new Error(
      "未配置语音 Token 来源：请设置 ALIYUN_NLS_TOKEN，或 ALIYUN_AK_ID + ALIYUN_AK_SECRET",
    );
    error.statusCode = 503;
    error.code = "ALIYUN_TOKEN_NOT_CONFIGURED";
    throw error;
  }

  // 过期前 120 秒即视为需要刷新。
  const now = Date.now();
  if (cachedToken && cachedToken.expireAt - 120_000 > now) {
    return cachedToken.token;
  }

  cachedToken = await requestCreateToken();
  return cachedToken.token;
}
