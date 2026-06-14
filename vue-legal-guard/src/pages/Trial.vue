<template>
  <div class="contract-generator">
    <header class="topbar">
      <router-link to="/" class="brand" aria-label="返回 Legal-Guard 首页">
        <span class="brand-mark"><i class="fa-solid fa-shield-halved"></i></span>
        <span>Legal-Guard</span>
      </router-link>
      <router-link to="/" class="back-link">
        <i class="fa-solid fa-arrow-left"></i>
        返回首页
      </router-link>
    </header>

    <main class="workspace">
      <section class="intro-band">
        <div>
          <h1>农副产品买卖合同生成</h1>
          <p>填写交易信息后生成与示范文本结构一致的合同，支持在线预览并下载 DOCX / PDF。</p>
        </div>
        <div class="template-chip">
          <i class="fa-solid fa-file-contract"></i>
          <span>GF-2025-0151 示范文本</span>
        </div>
      </section>

      <div class="content-grid">
        <section class="form-panel" aria-label="合同信息表单">
          <div class="section-heading">
            <span class="section-icon"><i class="fa-solid fa-pen-to-square"></i></span>
            <div>
              <h2>合同基础信息</h2>
              <p>所有字段都会写入合同模板对应位置。</p>
            </div>
          </div>

          <form class="contract-form" @submit.prevent="generateContract">
            <div v-for="field in fields" :key="field.key" class="field">
              <label :for="field.key">
                {{ field.label }}
                <span>*</span>
              </label>
              <input
                :id="field.key"
                v-model.trim="form[field.key]"
                :type="field.type || 'text'"
                :placeholder="field.placeholder"
                :aria-invalid="Boolean(errors[field.key])"
                :class="{ invalid: errors[field.key] }"
                @input="errors[field.key] = ''"
              />
              <p v-if="errors[field.key]" class="field-error">{{ errors[field.key] }}</p>
            </div>

            <div class="form-actions">
              <button type="submit" class="primary-action" :disabled="loading">
                <i :class="loading ? 'fa-solid fa-circle-notch fa-spin' : 'fa-solid fa-wand-magic-sparkles'"></i>
                {{ loading ? '正在生成合同' : '生成合同' }}
              </button>
              <button type="button" class="secondary-action" :disabled="loading" @click="resetForm">
                <i class="fa-solid fa-rotate-left"></i>
                清空
              </button>
            </div>
          </form>
        </section>

        <aside class="summary-panel" aria-label="合同生成状态">
          <div class="section-heading compact">
            <span class="section-icon"><i class="fa-solid fa-layer-group"></i></span>
            <div>
              <h2>写入位置</h2>
              <p>当前只处理本阶段所需变量。</p>
            </div>
          </div>

          <ul class="mapping-list">
            <li><span>第 3 页</span>甲方、乙方基础信息</li>
            <li><span>第 4 页</span>产品信息表第 1 行</li>
            <li><span>第 4 页</span>交货时间与交货地点</li>
            <li><span>第 5 页</span>合同价款总价</li>
          </ul>

          <div v-if="apiError" class="status-box error" role="alert">
            <i class="fa-solid fa-triangle-exclamation"></i>
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
            </div>
          </div>

          <div v-else class="status-box neutral">
            <i class="fa-solid fa-circle-info"></i>
            <div>
              <strong>等待生成</strong>
              <p>提交表单后将在下方显示 PDF 预览。</p>
            </div>
          </div>

          <div class="download-actions" :class="{ disabled: !contract }">
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

      <section class="preview-section" aria-label="合同预览">
        <div class="preview-toolbar">
          <div>
            <h2>合同预览</h2>
            <p>{{ contract ? 'PDF 已由后端根据 DOCX 合同生成。' : '生成后将在此展示完整合同 PDF。' }}</p>
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
            title="农副产品买卖合同 PDF 预览"
          ></iframe>
          <div v-else class="preview-empty">
            <i class="fa-regular fa-file-lines"></i>
            <span>暂无合同预览</span>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const initialForm = {
  partyA: '',
  partyB: '',
  productName: '',
  quantity: '',
  unitPrice: '',
  totalPrice: '',
  deliveryTime: '',
  deliveryPlace: '',
}

const fields = [
  { key: 'partyA', label: '甲方名称', placeholder: '例如：河源市某某商贸有限公司' },
  { key: 'partyB', label: '乙方名称', placeholder: '例如：连平县某某种植专业合作社' },
  { key: 'productName', label: '产品名称', placeholder: '例如：鹰嘴桃' },
  { key: 'quantity', label: '数量', placeholder: '例如：1000 斤' },
  { key: 'unitPrice', label: '单价', placeholder: '例如：12 元/斤' },
  { key: 'totalPrice', label: '总价', placeholder: '例如：12000' },
  { key: 'deliveryTime', label: '交货时间', placeholder: '例如：2026 年 7 月 1 日' },
  { key: 'deliveryPlace', label: '交货地点', placeholder: '例如：广东省河源市连平县' },
]

const form = reactive({ ...initialForm })
const errors = reactive({})
const loading = ref(false)
const apiError = ref('')
const contract = ref(null)

function validate() {
  let valid = true
  fields.forEach((field) => {
    errors[field.key] = ''
    if (!String(form[field.key] || '').trim()) {
      errors[field.key] = `${field.label}为必填项`
      valid = false
    }
  })
  return valid
}

async function generateContract() {
  apiError.value = ''
  contract.value = null
  if (!validate()) return

  loading.value = true
  try {
    const response = await fetch('/api/contracts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })
    const payload = await response.json().catch(() => ({}))
    if (!response.ok) {
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
  Object.assign(form, initialForm)
  Object.keys(errors).forEach((key) => {
    errors[key] = ''
  })
  apiError.value = ''
  contract.value = null
}

</script>

<style scoped>
.contract-generator {
  min-height: 100vh;
  background:
    radial-gradient(circle at 18% 12%, rgba(212, 175, 55, 0.13), transparent 28rem),
    radial-gradient(circle at 90% 8%, rgba(59, 130, 246, 0.12), transparent 24rem),
    linear-gradient(135deg, #0b0f19 0%, #121212 48%, #050505 100%);
  color: #f8fafc;
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px clamp(18px, 4vw, 52px);
  border-bottom: 1px solid rgba(212, 175, 55, 0.18);
  background: rgba(10, 10, 10, 0.82);
  backdrop-filter: blur(16px);
}

.brand,
.back-link {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: inherit;
  text-decoration: none;
}

.brand {
  font-size: 20px;
  font-weight: 800;
  color: #f7d86b;
}

.brand-mark {
  display: inline-flex;
  width: 34px;
  height: 34px;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  background: linear-gradient(135deg, #d4af37, #f7ef8a);
  color: #111827;
}

.back-link {
  color: rgba(248, 250, 252, 0.72);
  font-size: 14px;
}

.workspace {
  width: min(1180px, calc(100% - 36px));
  margin: 0 auto;
  padding: 34px 0 56px;
}

.intro-band {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 24px;
}

.intro-band h1 {
  margin: 0 0 10px;
  font-size: clamp(30px, 4vw, 48px);
  line-height: 1.12;
  letter-spacing: 0;
}

.intro-band p,
.section-heading p,
.preview-toolbar p,
.status-box p {
  margin: 0;
  color: rgba(226, 232, 240, 0.68);
}

.template-chip {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 42px;
  padding: 0 14px;
  border: 1px solid rgba(212, 175, 55, 0.34);
  border-radius: 8px;
  background: rgba(212, 175, 55, 0.1);
  color: #f7d86b;
  white-space: nowrap;
}

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 340px;
  gap: 20px;
  align-items: start;
}

.form-panel,
.summary-panel,
.preview-section {
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.62);
  box-shadow: 0 18px 48px rgba(0, 0, 0, 0.28);
}

.form-panel,
.summary-panel {
  padding: 22px;
}

.section-heading,
.preview-toolbar {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 18px;
}

.section-heading.compact {
  align-items: flex-start;
}

.section-heading h2,
.preview-toolbar h2 {
  margin: 0 0 4px;
  font-size: 18px;
  line-height: 1.3;
}

.section-icon {
  display: inline-flex;
  width: 38px;
  height: 38px;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  background: linear-gradient(135deg, #d4af37, #f7ef8a);
  color: #111827;
  flex: 0 0 auto;
}

.contract-form {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.field label {
  display: flex;
  gap: 4px;
  margin-bottom: 7px;
  color: rgba(248, 250, 252, 0.82);
  font-size: 14px;
  font-weight: 650;
}

.field label span,
.field-error {
  color: #fb7185;
}

.field input {
  width: 100%;
  box-sizing: border-box;
  min-height: 44px;
  padding: 10px 12px;
  border: 1px solid rgba(255, 255, 255, 0.13);
  border-radius: 8px;
  background: rgba(2, 6, 23, 0.48);
  color: #f8fafc;
  font: inherit;
  outline: none;
}

.field input:focus {
  border-color: rgba(247, 216, 107, 0.78);
  box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.14);
}

.field input.invalid {
  border-color: rgba(251, 113, 133, 0.8);
}

.field-error {
  margin: 6px 0 0;
  min-height: 18px;
  font-size: 12px;
}

.form-actions {
  grid-column: 1 / -1;
  display: flex;
  gap: 12px;
  padding-top: 8px;
}

.primary-action,
.secondary-action,
.download-actions a,
.open-preview {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 42px;
  padding: 0 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 750;
  text-decoration: none;
}

.primary-action {
  border: 0;
  background: linear-gradient(135deg, #d4af37, #f7ef8a);
  color: #111827;
  cursor: pointer;
}

.secondary-action {
  border: 1px solid rgba(255, 255, 255, 0.14);
  background: rgba(255, 255, 255, 0.06);
  color: #f8fafc;
  cursor: pointer;
}

.primary-action:disabled,
.secondary-action:disabled {
  cursor: not-allowed;
  opacity: 0.64;
}

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
  padding: 12px;
  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.045);
  color: rgba(248, 250, 252, 0.86);
  font-size: 13px;
}

.mapping-list span {
  color: #f7d86b;
  font-weight: 800;
}

.status-box {
  display: flex;
  gap: 12px;
  padding: 14px;
  border-radius: 8px;
  margin-bottom: 14px;
}

.status-box strong {
  display: block;
  margin-bottom: 4px;
}

.status-box.success {
  border: 1px solid rgba(34, 197, 94, 0.32);
  background: rgba(22, 163, 74, 0.12);
  color: #bbf7d0;
}

.status-box.error {
  border: 1px solid rgba(251, 113, 133, 0.32);
  background: rgba(190, 18, 60, 0.16);
  color: #fecdd3;
}

.status-box.neutral {
  border: 1px solid rgba(96, 165, 250, 0.28);
  background: rgba(37, 99, 235, 0.1);
  color: #bfdbfe;
}

.download-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.download-actions a,
.open-preview {
  border: 1px solid rgba(212, 175, 55, 0.28);
  background: rgba(212, 175, 55, 0.11);
  color: #f7d86b;
}

.download-actions.disabled a {
  pointer-events: none;
  opacity: 0.45;
}

.preview-section {
  margin-top: 20px;
  padding: 18px;
}

.preview-toolbar {
  justify-content: space-between;
}

.preview-frame {
  min-height: 680px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: #111827;
  overflow: hidden;
}

.preview-frame iframe {
  width: 100%;
  height: 680px;
  border: 0;
  background: #fff;
}

.preview-empty {
  display: grid;
  min-height: 680px;
  place-items: center;
  align-content: center;
  gap: 12px;
  color: rgba(226, 232, 240, 0.48);
}

.preview-empty i {
  font-size: 42px;
}

@media (max-width: 960px) {
  .intro-band,
  .preview-toolbar {
    align-items: flex-start;
    flex-direction: column;
  }

  .content-grid {
    grid-template-columns: 1fr;
  }

}

@media (max-width: 680px) {
  .topbar {
    padding: 12px 16px;
  }

  .brand {
    font-size: 17px;
  }

  .back-link {
    font-size: 13px;
  }

  .workspace {
    width: min(100% - 24px, 1180px);
    padding-top: 24px;
  }

  .contract-form,
  .download-actions {
    grid-template-columns: 1fr;
  }

  .form-actions {
    flex-direction: column;
  }

  .preview-frame,
  .preview-frame iframe,
  .preview-empty {
    min-height: 520px;
    height: 520px;
  }
}
</style>
