<template>
  <div class="contract-generator">
    <header class="topbar">
      <router-link to="/" class="brand" aria-label="返回首页">
        <span class="brand-mark"><i class="fa-solid fa-scale-balanced"></i></span>
        <span>岭南法务百县通</span>
      </router-link>
      <router-link to="/" class="back-link">
        <i class="fa-solid fa-arrow-left"></i>
        返回首页
      </router-link>
    </header>

    <main class="workspace">
      <div v-if="catalogLoading" class="catalog-state" role="status">正在加载合同模板…</div>
      <div v-else-if="catalogError" class="catalog-state inline-alert error" role="alert">
        <span>{{ catalogError }}</span><button class="secondary-action" @click="loadTemplates">重新加载</button>
      </div>
      <template v-if="currentTemplate">
      <section class="hero-band">
        <div class="hero-copy">
          <p class="eyebrow">合同生成工作台</p>
          <h1>选对合同，<br />把每一份约定说清楚</h1>
          <p class="hero-description">
            从买卖农产品到土地出租、采摘用工和农业托管，选择适合你的模板，填写双方约定，预览并下载 Word 或 PDF。
          </p>
        </div>
        <div class="hero-status">
          <span>当前选择 · 板块{{ currentTemplate.section }}</span>
          <h2>{{ currentTemplate.title }}</h2>
          <strong>{{ contract ? '已生成合同' : `已填 ${completedFields} / ${requiredFields.length} 项` }}</strong>
        </div>
      </section>

      <section class="scenario-section" aria-label="场景入口">
        <div class="section-title">
          <div>
            <p class="kicker">第一步</p>
            <h2>选择你的合同模板</h2>
            <p>六个板块，对应六种约定。切换模板时，本页填写的内容会为你保留。</p>
          </div>
        </div>
        <div class="scenario-grid" role="group" aria-label="选择合同模板">
          <button
            v-for="scenario in templates"
            :key="scenario.id"
            type="button"
            class="scenario-card"
            :class="{ active: selectedTemplateId === scenario.id }"
            :aria-pressed="selectedTemplateId === scenario.id"
            :disabled="busy"
            @click="selectTemplate(scenario.id)"
          >
            <span class="template-number">板块{{ scenario.section }}</span>
            <span class="scenario-icon"><i :class="templateIcons[scenario.id]" aria-hidden="true"></i></span>
            <span>
              <strong>{{ scenario.scenario }}</strong>
              <small>{{ scenario.title }}</small>
            </span>
            <span class="selection-check" aria-hidden="true">{{ selectedTemplateId === scenario.id ? '✓' : '↗' }}</span>
          </button>
        </div>
        <p class="selection-note" aria-live="polite">{{ currentTemplate.description }}</p>
      </section>

      <Transition name="template-change" mode="out-in">
      <div :key="selectedTemplateId" class="content-grid">
        <section class="form-panel" aria-label="合同信息表单">
          <div class="section-title form-title">
            <div>
              <p class="kicker">第二步</p>
              <h2>合同基础信息</h2>
              <p>标 * 的为必填项，其他约定可在下方展开补充。</p>
            </div>
            <span class="template-pill">板块{{ currentTemplate.section }}</span>
          </div>

          <section class="voice-panel" aria-label="语音输入">
            <div class="voice-header">
              <span class="voice-icon"><i class="fa-solid fa-microphone-lines"></i></span>
              <div>
                <h3>语音填表（粤语 / 普通话）</h3>
                <p>先选语言，把语音转成文字后自动填入表单字段。</p>
              </div>
            </div>
            <div class="voice-lang" role="group" aria-label="识别语言">
              <button
                type="button"
                :class="['lang-chip', { active: voiceLang === 'cantonese' }]"
                :disabled="busy"
                @click="voiceLang = 'cantonese'"
              >
                粤语
              </button>
              <button
                type="button"
                :class="['lang-chip', { active: voiceLang === 'mandarin' }]"
                :disabled="busy"
                @click="voiceLang = 'mandarin'"
              >
                普通话
              </button>
            </div>
            <div class="voice-actions">
              <button type="button" class="secondary-action" :disabled="voiceLoading || loading || recordingStarting" @click="toggleRecording">
                <i :class="isRecording ? 'fa-solid fa-stop' : 'fa-solid fa-microphone'"></i>
                {{ isRecording ? '停止录音' : '开始录音' }}
              </button>
              <label class="upload-action">
                <i class="fa-solid fa-file-audio"></i>
                上传音频
                <input type="file" accept="audio/*" :disabled="busy" @change="handleAudioUpload" />
              </label>
              <span v-if="voiceLoading" class="voice-loading">
                <i class="fa-solid fa-circle-notch fa-spin"></i>
                识别中
              </span>
            </div>
            <div v-if="voiceError" class="inline-alert error" role="alert">
              <i class="fa-solid fa-triangle-exclamation"></i>
              <span>{{ voiceError }}</span>
            </div>
            <div v-if="voiceText" class="transcript-box">
              <span>识别文本</span>
              <p>{{ voiceText }}</p>
            </div>
            <div v-if="missingFields.length" class="missing-fields">
              <span>还需手动补充：</span>
              <strong>{{ missingFieldLabels }}</strong>
            </div>
          </section>

          <form class="contract-form" @submit.prevent="generateContract">
            <ContractField v-for="field in requiredFields" :key="field.key" :field="field"
              :model-value="form[field.key]" :error="errors[field.key]" :disabled="busy"
              @update:model-value="setField(field.key, $event)" />
            <details v-for="group in optionalGroups" :key="group.name" class="optional-group" :open="groupHasError(group)">
              <summary>{{ group.name }}<span>{{ group.fields.length }} 项选填</span></summary>
              <div class="optional-fields">
                <ContractField v-for="field in group.fields" :key="field.key" :field="field"
                  :model-value="form[field.key]" :error="errors[field.key]" :disabled="busy"
                  @update:model-value="setField(field.key, $event)" />
              </div>
            </details>
            <p class="form-note">未填写的补充项将保留空白。生成后请核对全部条款，补齐适用约定，再由双方签署。</p>

            <div class="form-actions">
              <button type="submit" class="primary-action" :disabled="busy">
                <i v-if="loading" class="fa-solid fa-circle-notch fa-spin"></i>
                {{ loading ? '正在生成合同' : '生成合同' }}
              </button>
              <button type="button" class="secondary-action" :disabled="busy" @click="resetForm">
                清空
              </button>
            </div>
          </form>
        </section>

        <aside class="summary-panel" aria-label="合同生成状态">
          <div class="section-title compact">
            <div>
              <p class="kicker">生成状态</p>
              <h2>合同将包含</h2>
              <p>生成后可下载 PDF 与 Word，两者内容一致。</p>
            </div>
          </div>

          <p class="template-source">{{ currentTemplate.source }}</p>
          <ul class="mapping-list">
            <li v-for="(item, index) in currentTemplate.summary" :key="item"><span>{{ index + 1 }}</span>{{ item }}</li>
          </ul>
          <div class="completion-meter" :aria-label="`必填信息已完成 ${completedFields} 项，共 ${requiredFields.length} 项`">
            <div><span>必填信息</span><strong>{{ completedFields }} / {{requiredFields.length}}</strong></div>
            <progress :value="completedFields" :max="requiredFields.length"></progress>
          </div>

          <div v-if="apiError" class="status-box error" role="alert">
            <i class="fa-solid fa-circle-exclamation"></i>
            <div>
              <strong>生成失败</strong>
              <p>{{ apiError }}</p>
            </div>
          </div>

          <div v-else-if="contract" class="status-box success">
            <i class="fa-solid fa-circle-check"></i>
            <div>
              <strong>合同已生成</strong>
              <p>编号：{{ contract.id }}</p>
              <p>{{ normalizeLabel }}</p>
            </div>
          </div>

          <div v-else class="status-box neutral">
            <i class="fa-solid fa-circle-info"></i>
            <div>
              <strong>{{ loading ? '正在生成合同' : '等待生成' }}</strong>
              <p>{{ loading ? '正在排版并转换 PDF，请稍候。' : '提交表单后将在下方显示 PDF 预览。' }}</p>
            </div>
          </div>

          <div v-if="contract" class="download-actions">
            <a :href="contract?.pdfUrl || '#'" :aria-disabled="!contract">
              <i class="fa-solid fa-file-pdf"></i>
              下载 PDF
            </a>
            <a :href="contract?.docxUrl || '#'" :aria-disabled="!contract">
              <i class="fa-solid fa-file-word"></i>
              下载 DOCX
            </a>
          </div>
        </aside>
      </div>

      </Transition>

      <section class="preview-section" aria-label="合同预览">
        <div class="preview-toolbar">
          <div>
            <p class="kicker">第三步</p>
            <h2>合同预览</h2>
            <p>{{ contract ? '合同 PDF 已生成，可在下方预览或下载。' : '生成后将在此展示完整合同 PDF。' }}</p>
          </div>
          <a v-if="contract" class="open-preview" :href="contract.previewUrl" target="_blank" rel="noreferrer">
            <i class="fa-solid fa-up-right-from-square"></i>
            新窗口打开
          </a>
        </div>

        <div class="preview-frame">
          <iframe
            v-if="contract"
            :src="`${contract.previewUrl}#toolbar=1&navpanes=0`"
            :title="`${currentTemplate.title} PDF 预览`"
          ></iframe>
          <div v-else class="preview-empty">
            <i class="fa-regular fa-file-lines"></i>
            <span>暂无合同预览</span>
          </div>
        </div>
      </section>
      </template>
    </main>
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, reactive, ref, watch } from 'vue'
import ContractField from '../components/ContractField.vue'

const templates = ref([])
const catalogLoading = ref(true)
const catalogError = ref('')
const selectedTemplateId = ref('sale')
const currentTemplate = computed(() => templates.value.find(t => t.id === selectedTemplateId.value))
const fields = computed(() => currentTemplate.value?.fields || [])
const requiredFields = computed(() => fields.value.filter(f => f.required))
const completedFields = computed(() => requiredFields.value.filter(f => String(form[f.key] || '').trim()).length)
const optionalGroups = computed(() => {
  const groups = new Map()
  fields.value.filter(f => !f.required).forEach(f => {
    if (!groups.has(f.group)) groups.set(f.group, [])
    groups.get(f.group).push(f)
  })
  return [...groups].map(([name, fields]) => ({ name, fields }))
})
const fieldLabelMap = computed(() => Object.fromEntries(fields.value.map(f => [f.key, f.label])))
const templateIcons = { sale: 'fa-solid fa-basket-shopping', 'land-lease': 'fa-solid fa-seedling', 'picking-labor': 'fa-solid fa-leaf', cooperative: 'fa-solid fa-people-group', iou: 'fa-solid fa-pen-nib', 'farm-service': 'fa-solid fa-tractor' }
const drafts = new Map()
const form = reactive({})
const recordingStarting = ref(false)
const busy = computed(() => loading.value || voiceLoading.value || isRecording.value || recordingStarting.value)
let disposed = false
const requestController = new AbortController()
async function loadTemplates() {
  catalogLoading.value = true
  catalogError.value = ''
  try {
    const response = await fetch('/api/templates', { signal: requestController.signal })
    if (!response.ok) throw new Error('模板加载失败，请重新加载。')
    const payload = await response.json()
    if (!Array.isArray(payload.templates) || !payload.templates.length) throw new Error('暂无可用模板，请稍后重试。')
    templates.value = payload.templates
    const requested = new URLSearchParams(window.location.hash.split('?')[1] || '').get('template')
    selectTemplate(templates.value.some(t => t.id === requested) ? requested : 'sale', true)
  } catch (error) {
    if (!disposed) catalogError.value = error.message || '无法连接模板服务，请重新加载。'
  } finally { catalogLoading.value = false }
}
function selectTemplate(id, initial = false) {
  if (busy.value || (!initial && id === selectedTemplateId.value)) return
  if (!initial) drafts.set(selectedTemplateId.value, { ...form })
  selectedTemplateId.value = id
  Object.keys(form).forEach(key => delete form[key])
  Object.assign(form, Object.fromEntries(fields.value.map(f => [f.key, ''])), drafts.get(id) || {})
  clearStatus()
}
function clearStatus() {
  Object.keys(errors).forEach(key => delete errors[key])
  apiError.value = ''; contract.value = null; voiceText.value = ''; voiceError.value = ''; missingFields.value = []
}
function setField(key, value) { form[key] = value; errors[key] = '' }
function groupHasError(group) { return group.fields.some(f => errors[f.key]) || undefined }
onMounted(loadTemplates)
const errors = reactive({})
const loading = ref(false)
const apiError = ref('')
const contract = ref(null)
const voiceText = ref('')
const voiceError = ref('')
const voiceLoading = ref(false)
const isRecording = ref(false)
const missingFields = ref([])
const voiceLang = ref('cantonese')

let mediaRecorder = null
let mediaStream = null
let recordedChunks = []

function validate() {
  let valid = true
  fields.value.forEach((field) => {
    errors[field.key] = ''
    if (field.required && !String(form[field.key] || '').trim()) {
      errors[field.key] = `${field.label}为必填项`
      valid = false
    }
  })
  return valid
}

async function generateContract() {
  if (busy.value) return
  apiError.value = ''
  contract.value = null
  if (!validate()) return

  loading.value = true
  try {
    const response = await fetch('/api/contracts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ templateId: selectedTemplateId.value, fields: { ...form } }),
      signal: requestController.signal,
    })
    const payload = await response.json().catch(() => ({}))
    if (!response.ok) {
      payload.details?.forEach(issue => { if (Object.hasOwn(form, issue.path)) errors[issue.path] = issue.message })
      throw new Error(payload.error || '合同生成失败，请稍后重试')
    }
    contract.value = payload
  } catch (error) {
    apiError.value = error.message
  } finally {
    loading.value = false
  }
}

function resetForm() {
  if (busy.value) return
  Object.keys(form).forEach(key => { form[key] = '' })
  drafts.delete(selectedTemplateId.value)
  clearStatus()
}
watch(form, () => { contract.value = null; apiError.value = '' }, { flush: 'sync' })

function preferredMimeType() {
  const options = ['audio/ogg;codecs=opus', 'audio/webm;codecs=opus', 'audio/webm']
  return options.find((type) => window.MediaRecorder?.isTypeSupported(type)) || ''
}

async function toggleRecording() {
  voiceError.value = ''
  if (isRecording.value) {
    mediaRecorder?.stop()
    return
  }

  if (!navigator.mediaDevices?.getUserMedia || !window.MediaRecorder) {
    voiceError.value = '当前浏览器不支持录音，请改用上传音频文件。'
    return
  }

  recordingStarting.value = true
  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true })
    if (disposed) { mediaStream.getTracks().forEach(track => track.stop()); return }
    recordedChunks = []
    const mimeType = preferredMimeType()
    mediaRecorder = new MediaRecorder(mediaStream, mimeType ? { mimeType } : undefined)
    mediaRecorder.ondataavailable = (event) => {
      if (event.data?.size) recordedChunks.push(event.data)
    }
    mediaRecorder.onstop = async () => {
      isRecording.value = false
      mediaStream?.getTracks().forEach((track) => track.stop())
      const blob = new Blob(recordedChunks, { type: mediaRecorder?.mimeType || 'audio/webm' })
      if (!disposed) await submitAudio(blob)
    }
    mediaRecorder.start()
    isRecording.value = true
  } catch (error) {
    voiceError.value = error?.message || '无法打开麦克风，请检查浏览器权限。'
  } finally { recordingStarting.value = false }
}

async function handleAudioUpload(event) {
  const file = event.target.files?.[0]
  event.target.value = ''
  if (!file) return
  await submitAudio(file)
}

function blobToBase64(blob) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => resolve(String(reader.result || '').split(',')[1] || '')
    reader.onerror = reject
    reader.readAsDataURL(blob)
  })
}

async function submitAudio(blob) {
  if (disposed || voiceLoading.value || loading.value) return
  const templateId = selectedTemplateId.value
  voiceLoading.value = true
  voiceError.value = ''
  missingFields.value = []
  try {
    const audioBase64 = await blobToBase64(blob)
    const response = await fetch('/api/speech/cantonese', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      signal: requestController.signal,
      body: JSON.stringify({
        templateId,
        audioBase64,
        mimeType: blob.type || 'audio/wav',
        language: voiceLang.value,
      }),
    })
    const payload = await response.json().catch(() => ({}))
    if (!response.ok) {
      throw new Error(payload.error || '粤语识别失败，请稍后重试')
    }

    if (disposed || templateId !== selectedTemplateId.value) return
    voiceText.value = payload.text || ''
    applyExtractedFields(payload.fields || {})
    missingFields.value = requiredFields.value.filter(f => !form[f.key]).map(f => f.key)
  } catch (error) {
    voiceError.value = error.message
  } finally {
    voiceLoading.value = false
  }
}

function applyExtractedFields(extractedFields) {
  Object.entries(extractedFields).forEach(([key, value]) => {
    if (key !== 'receiptConfirmed' && Object.hasOwn(form, key) && String(value || '').trim()) {
      form[key] = String(value).trim()
      errors[key] = ''
    }
  })
}

const normalizeLabel = computed(() => {
  if (!contract.value) return ''
  return contract.value.normalizedBy === 'deepseek' ? '已完成内容检查，按你的填写生成' : '字段已按本地规则处理'
})

const missingFieldLabels = computed(() => missingFields.value.map((key) => fieldLabelMap.value[key]).filter(Boolean).join('、'))

onBeforeUnmount(() => {
  disposed = true
  requestController.abort()
  if (isRecording.value) mediaRecorder?.stop()
  mediaStream?.getTracks().forEach((track) => track.stop())
})
</script>

<style scoped>
/* ===== 与主页统一的设计系统 ===== */
.contract-generator {
  --green-950: #052018;
  --green-900: #06281e;
  --green-800: #0b3d2e;
  --green-700: #0f5137;
  --emerald: #10b981;
  --emerald-300: #6ee7b7;
  --gold: #e7c04a;
  --gold-strong: #d4af37;
  --cream: #f5f9f6;
  --ink: #0d1f18;
  --ink-soft: #3f5850;
  --line: rgba(16, 185, 129, 0.16);
  --serif: "Noto Serif SC", "Songti SC", "SimSun", Georgia, serif;

  min-height: 100vh;
  background: var(--cream);
  color: var(--ink);
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
}
.contract-generator * { box-sizing: border-box; }

/* ===== 顶栏（深绿，呼应主页导航）===== */
.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px clamp(18px, 4vw, 52px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(6, 40, 30, 0.92);
  backdrop-filter: blur(14px) saturate(140%);
}
.brand,
.back-link {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}
.brand { font-size: 17px; font-weight: 800; letter-spacing: .3px; color: #f4fbf7; }
.brand-mark,
.voice-icon,
.scenario-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
}
.brand-mark {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: linear-gradient(135deg, var(--gold), var(--gold-strong));
  color: #241c00;
  box-shadow: 0 6px 16px -6px rgba(212, 175, 55, 0.6);
}
.back-link { color: rgba(223, 245, 236, 0.82); font-size: 14px; font-weight: 600; transition: color .15s; }
.back-link:hover { color: #fff; }

.workspace {
  width: min(1220px, calc(100% - 36px));
  margin: 0 auto;
  padding: 36px 0 64px;
}

/* ===== 卡片/面板 ===== */
.hero-band {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 280px;
  gap: 20px;
  align-items: stretch;
  margin-bottom: 22px;
}
.hero-copy,
.hero-status,
.scenario-section,
.form-panel,
.summary-panel,
.preview-section {
  border: 1px solid var(--line);
  border-radius: 20px;
  background: #ffffff;
  box-shadow: 0 30px 60px -46px rgba(6, 40, 30, 0.28);
}
.hero-copy { padding: clamp(26px, 4vw, 44px); }

.eyebrow,
.kicker {
  margin: 0 0 12px;
  font-family: var(--serif);
  font-weight: 700;
  font-size: 15px;
  letter-spacing: 2px;
  color: var(--emerald);
}
.hero-copy h1 {
  margin: 0;
  max-width: 820px;
  font-family: var(--serif);
  font-weight: 900;
  font-size: clamp(28px, 4.2vw, 46px);
  line-height: 1.22;
  letter-spacing: .5px;
  color: var(--ink);
}
.hero-description {
  margin: 20px 0 0;
  max-width: 720px;
  color: var(--ink-soft);
  font-size: 16px;
  line-height: 1.85;
}
.hero-status {
  display: grid;
  align-content: space-between;
  gap: 16px;
  padding: 24px;
  background: linear-gradient(150deg, rgba(16, 185, 129, 0.1), rgba(231, 192, 74, 0.09));
}
.hero-status span {
  font-size: 13px;
  font-weight: 700;
  color: var(--green-700);
  letter-spacing: .5px;
}
.hero-status strong {
  font-family: var(--serif);
  font-size: 26px;
  font-weight: 900;
  line-height: 1.2;
  color: var(--ink);
}
.template-pill {
  display: inline-flex;
  align-items: center;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 700;
  color: var(--green-700);
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid var(--line);
}

.scenario-section,
.form-panel,
.summary-panel { padding: 26px; }

/* ===== 区块标题 ===== */
.section-title,
.preview-toolbar,
.voice-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.section-title { margin-bottom: 22px; }
.section-title.compact,
.form-title { align-items: flex-start; }
.section-title h2,
.preview-toolbar h2 {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(22px, 2.6vw, 28px);
  font-weight: 900;
  line-height: 1.3;
  color: var(--ink);
}
.voice-header h3 {
  margin: 0 0 4px;
  font-family: var(--serif);
  font-size: 19px;
  font-weight: 700;
  color: var(--ink);
}
.section-title h2 + p,
.section-title .kicker + h2 { margin-top: 6px; }
.section-title p,
.preview-toolbar p,
.voice-header p,
.status-box p {
  margin: 8px 0 0;
  color: var(--ink-soft);
  font-size: 15px;
  line-height: 1.7;
}
.voice-header p { margin-top: 2px; font-size: 14px; }

/* ===== 场景卡 ===== */
.scenario-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 14px;
}
.scenario-card {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 88px;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: #fff;
  color: var(--ink);
  text-align: left;
  cursor: pointer;
  transition: transform .2s cubic-bezier(.2,.7,.2,1), border-color .2s ease, box-shadow .2s ease, background .2s ease;
}
.scenario-card:hover { transform: translateY(-4px); border-color: rgba(16, 185, 129, 0.4); box-shadow: 0 24px 44px -34px rgba(6, 40, 30, 0.4); }
.scenario-card.active {
  border-color: var(--emerald);
  background: rgba(16, 185, 129, 0.08);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.12);
}
.scenario-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  font-size: 18px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(110, 231, 183, 0.3));
  color: var(--green-800);
}
.scenario-card strong,
.scenario-card small { display: block; }
.scenario-card strong { margin-bottom: 4px; font-size: 15px; font-weight: 700; }
.scenario-card small { color: var(--ink-soft); font-size: 12px; }

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 340px;
  gap: 22px;
  align-items: start;
  margin-top: 22px;
}

/* ===== 语音面板 ===== */
.voice-panel {
  margin-bottom: 22px;
  padding: 20px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: rgba(16, 185, 129, 0.05);
}
.voice-header { justify-content: flex-start; margin-bottom: 14px; }
.voice-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  font-size: 18px;
  background: linear-gradient(135deg, var(--emerald-300), var(--emerald));
  color: #052018;
}
.voice-lang {
  display: inline-flex;
  gap: 4px;
  margin-bottom: 14px;
  padding: 4px;
  border-radius: 999px;
  background: rgba(13, 31, 24, 0.05);
  border: 1px solid var(--line);
}
.lang-chip {
  border: none;
  background: transparent;
  color: var(--ink-soft);
  font-size: 13px;
  font-weight: 700;
  padding: 7px 18px;
  border-radius: 999px;
  cursor: pointer;
  transition: background .18s, color .18s;
}
.lang-chip:hover:not(:disabled) { color: var(--ink); }
.lang-chip.active { background: var(--green-700); color: #f4fbf7; }
.lang-chip:disabled { opacity: 0.55; cursor: not-allowed; }

.voice-actions,
.form-actions,
.download-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
}
.voice-loading { color: var(--green-700); font-size: 13px; font-weight: 700; }
.upload-action input { display: none; }

/* ===== 按钮（主页胶囊风）===== */
.primary-action,
.secondary-action,
.upload-action,
.download-actions a,
.open-preview {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 999px;
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
  transition: transform .2s cubic-bezier(.2,.7,.2,1), box-shadow .2s ease, background .2s ease, color .2s ease;
}
.primary-action {
  border: 0;
  background: linear-gradient(135deg, var(--gold), var(--gold-strong));
  color: #241c00;
  box-shadow: 0 10px 26px -10px rgba(212, 175, 55, 0.6);
}
.primary-action:not(:disabled):hover { transform: translateY(-2px); box-shadow: 0 16px 32px -10px rgba(212, 175, 55, 0.72); }
.secondary-action,
.upload-action,
.open-preview,
.download-actions a {
  border: 1px solid var(--line);
  background: #fff;
  color: var(--green-700);
}
.secondary-action:not(:disabled):hover,
.upload-action:hover,
.open-preview:hover,
.download-actions a:hover { background: rgba(16, 185, 129, 0.07); border-color: rgba(16, 185, 129, 0.4); }
.primary-action:disabled,
.secondary-action:disabled { cursor: not-allowed; opacity: 0.55; }

/* ===== 提示条 ===== */
.inline-alert,
.transcript-box,
.missing-fields { margin-top: 12px; }
.inline-alert {
  display: flex;
  gap: 10px;
  padding: 12px 14px;
  border-radius: 12px;
  font-size: 13.5px;
  line-height: 1.6;
}
.inline-alert.error {
  border: 1px solid rgba(225, 29, 72, 0.28);
  background: rgba(225, 29, 72, 0.07);
  color: #b3123a;
}
.transcript-box {
  padding: 14px;
  border-radius: 12px;
  background: #fff;
  border: 1px solid var(--line);
}
.transcript-box span,
.missing-fields span {
  display: block;
  margin-bottom: 5px;
  color: var(--green-700);
  font-size: 12px;
  font-weight: 700;
}
.transcript-box p { margin: 0; color: var(--ink); line-height: 1.75; }
.missing-fields strong { color: var(--ink); }

/* ===== 表单 ===== */
.contract-form {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}
.field label {
  display: flex;
  gap: 4px;
  margin-bottom: 8px;
  color: var(--ink);
  font-size: 14px;
  font-weight: 700;
}
.field label span,
.field-error { color: #e11d48; }
.field input {
  width: 100%;
  min-height: 46px;
  padding: 11px 14px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: #fff;
  color: var(--ink);
  font: inherit;
  outline: none;
  transition: border-color .15s, box-shadow .15s;
}
.field input::placeholder { color: rgba(63, 88, 80, 0.55); }
.field input:focus { border-color: var(--emerald); box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15); }
.field input.invalid { border-color: rgba(225, 29, 72, 0.7); }
.field-error { margin: 6px 0 0; min-height: 18px; font-size: 12px; }
.form-actions { grid-column: 1 / -1; padding-top: 8px; }

/* ===== 摘要面板 ===== */
.mapping-list {
  display: grid;
  gap: 10px;
  margin: 0 0 18px;
  padding: 0;
  list-style: none;
}
.mapping-list li {
  display: grid;
  gap: 4px;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: rgba(16, 185, 129, 0.05);
  color: var(--ink);
  font-size: 14px;
}
.mapping-list span { color: var(--green-700); font-weight: 700; font-size: 13px; }

.status-box {
  display: flex;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 14px;
  margin-bottom: 14px;
  font-size: 14px;
}
.status-box i { margin-top: 2px; }
.status-box strong { display: block; margin-bottom: 4px; }
.status-box.success { border: 1px solid rgba(16, 185, 129, 0.3); background: rgba(16, 185, 129, 0.08); color: var(--green-700); }
.status-box.error { border: 1px solid rgba(225, 29, 72, 0.28); background: rgba(225, 29, 72, 0.07); color: #b3123a; }
.status-box.neutral { border: 1px solid var(--line); background: rgba(16, 185, 129, 0.05); color: var(--ink-soft); }
.status-box.neutral strong { color: var(--ink); }

.download-actions { display: grid; grid-template-columns: 1fr 1fr; }
.download-actions.disabled { opacity: 0.45; pointer-events: none; }

/* ===== 预览 ===== */
.preview-section { margin-top: 22px; padding: 24px; }
.preview-toolbar { margin-bottom: 18px; }
.preview-frame {
  min-height: 620px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: #fff;
  overflow: hidden;
}
.preview-frame iframe { width: 100%; height: 720px; border: 0; background: #fff; }
.preview-empty {
  min-height: 620px;
  display: grid;
  place-items: center;
  gap: 12px;
  color: var(--ink-soft);
}
.preview-empty i { font-size: 46px; color: rgba(16, 185, 129, 0.45); }

/* ===== 响应式 ===== */
@media (max-width: 980px) {
  .hero-band,
  .content-grid { grid-template-columns: 1fr; }
  .scenario-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 680px) {
  .topbar,
  .section-title,
  .preview-toolbar { align-items: flex-start; }
  .section-title,
  .preview-toolbar { flex-direction: column; }
  .workspace { width: min(100% - 24px, 1220px); padding-top: 24px; }
  .scenario-grid,
  .contract-form,
  .download-actions { grid-template-columns: 1fr; }
  .hero-copy,
  .scenario-section,
  .form-panel,
  .summary-panel,
  .preview-section { padding: 18px; }
  .preview-frame,
  .preview-empty { min-height: 460px; }
  .preview-frame iframe { height: 520px; }
}

/* Template selection uses the existing homepage palette. */
.catalog-state { padding: 36px; text-align: center; }
.hero-status h2 { font-family: var(--serif); font-size: 23px; line-height: 1.5; margin: 14px 0 24px; }
.hero-status strong { font-size: 24px; }
.scenario-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.scenario-card { position: relative; display: grid; grid-template-columns: 42px minmax(0, 1fr) 20px; gap: 12px; padding: 40px 18px 20px; min-height: 134px; text-align: left; transition: transform .2s ease, background .2s ease, border-color .2s ease, box-shadow .2s ease; }
.scenario-card:hover:not(:disabled) { transform: translateY(-3px); border-color: var(--green-700); }
.scenario-card.active { background: #edf7f0; border-color: var(--green-700); box-shadow: inset 0 3px 0 var(--green-700); }
.scenario-card:focus-visible, button:focus-visible, a:focus-visible, summary:focus-visible { outline: 3px solid var(--green-700); outline-offset: 4px; }
.scenario-card:disabled { cursor: wait; }
.template-number { position: absolute; top: 13px; left: 18px; color: var(--ink-soft); font-size: 11px; letter-spacing: 2px; }
.scenario-card strong { font-size: 16px; line-height: 1.5; }
.scenario-card small { line-height: 1.5; }
.selection-check { align-self: center; color: var(--green-700); font-weight: 800; }
.selection-note { border-top: 1px solid var(--line); padding-top: 16px; margin: 20px 0 0; color: var(--ink-soft); line-height: 1.7; font-size: 14px; }
.optional-group { grid-column: 1 / -1; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
.optional-group summary { padding: 16px; cursor: pointer; font-size: 14px; font-weight: 700; background: var(--cream); }
.optional-group summary span { float: right; font-size: 12px; color: var(--ink-soft); font-weight: 400; }
.optional-fields { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; padding: 18px; }
.form-note { grid-column: 1 / -1; font-size: 13px; color: var(--ink-soft); line-height: 1.7; margin: 0; }
.template-source { font-size: 12px; line-height: 1.7; color: var(--ink-soft); }
.completion-meter { padding: 18px 0; border-top: 1px solid var(--line); margin-bottom: 12px; }
.completion-meter div { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 10px; }
.completion-meter progress { width: 100%; height: 7px; accent-color: var(--green-700); }
.template-change-enter-active, .template-change-leave-active { transition: opacity .15s ease, transform .15s ease; }
.template-change-enter-from { opacity: 0; transform: translateY(8px); }
.template-change-leave-to { opacity: 0; transform: translateY(-4px); }
@media (max-width: 980px) { .scenario-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 680px) { .scenario-grid, .optional-fields { grid-template-columns: 1fr; } .hero-status { padding: 20px; } .scenario-card { min-height: 120px; } }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition: none !important; animation: none !important; scroll-behavior: auto !important; } .scenario-card:hover:not(:disabled) { transform: none; } }
</style>
