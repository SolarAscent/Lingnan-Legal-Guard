<template>
  <!-- 加载动画 -->
  <div v-if="loading" class="fixed inset-0 bg-gray-900/80 backdrop-blur-sm z-50 flex items-center justify-center">
    <div class="text-center">
      <div class="relative w-32 h-32 mx-auto mb-6">
        <!-- 外圈旋转 -->
        <div class="absolute inset-0 rounded-full border-4 border-transparent border-t-gold border-r-gold animate-spin"></div>
        <!-- 内圈旋转 -->
        <div class="absolute inset-6 rounded-full border-4 border-transparent border-b-gold border-l-gold animate-spin-reverse"></div>
        <!-- 中心logo -->
        <div class="absolute inset-12 rounded-full bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center">
          <i class="fa-solid fa-shield-halved text-gray-900 text-2xl"></i>
        </div>
      </div>
      <p class="text-white/70 animate-pulse">正在加载，请稍候...</p>
    </div>
  </div>

  <!-- 确认弹窗 -->
  <div v-if="showConfirm" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
    <div class="bg-gray-900 rounded-2xl border border-white/10 p-6 max-w-md w-full mx-auto shadow-2xl">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center">
          <i class="fa-solid" :class="confirmIcon",class="text-gray-900"></i>
        </div>
        <h3 class="text-lg font-semibold text-white">{{ confirmTitle }}</h3>
      </div>

      <p class="text-white/70 mb-6">{{ confirmMessage }}</p>

      <div class="flex justify-end gap-3">
        <button @click="confirmCancel"
                class="px-4 py-2 rounded-lg border border-white/10 text-white/80 hover:text-white hover:bg-white/5 transition-colors">
          取消
        </button>
        <button @click="confirmAction"
                class="px-4 py-2 rounded-lg bg-gradient-to-r from-gold to-yellow-200 text-gray-900 font-medium hover:shadow-lg hover:shadow-gold/25 transition-all">
          确认
        </button>
      </div>
    </div>
  </div>

  <!-- 成功提示 -->
  <transition name="slide-up">
    <div v-if="showSuccess" class="fixed top-4 right-4 z-50">
      <div class="bg-gradient-to-r from-green-500 to-emerald-400 text-white px-6 py-4 rounded-xl shadow-lg flex items-center gap-3 min-w-[300px]">
        <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center">
          <i class="fa-solid fa-check"></i>
        </div>
        <div class="flex-1">
          <p class="font-medium">{{ successMessage }}</p>
        </div>
        <button @click="showSuccess = false" class="text-white/60 hover:text-white">
          <i class="fa-solid fa-times"></i>
        </button>
      </div>
    </div>
  </transition>

  <!-- 步骤指示器组件 -->
  <div class="relative">
    <div class="flex items-center justify-between">
      <div v-for="(stepItem, index) in steps" :key="index" class="flex flex-col items-center relative z-10">
        <!-- 连接线 -->
        <div v-if="index > 0" class="absolute -left-1/2 w-full h-0.5 bg-white/10"></div>

        <!-- 步骤圆圈 -->
        <div class="relative">
          <div class="w-12 h-12 rounded-full flex items-center justify-center transition-all duration-300"
               :class="currentStep >= stepItem.id
                 ? 'bg-gradient-to-br from-gold to-yellow-200 text-gray-900'
                 : 'bg-white/5 text-white/40'">
            <i v-if="currentStep > stepItem.id" class="fa-solid fa-check"></i>
            <span v-else>{{ stepItem.id }}</span>
          </div>
          <!-- 激活状态光环 -->
          <div v-if="currentStep === stepItem.id" class="absolute -inset-2 bg-gold/20 rounded-full blur-sm animate-pulse"></div>
        </div>

        <!-- 步骤标签 -->
        <div class="mt-2 text-center">
          <p class="text-sm font-medium"
             :class="currentStep >= stepItem.id ? 'text-white' : 'text-white/40'">
            {{ stepItem.title }}
          </p>
          <p class="text-xs text-white/60 mt-0.5">{{ stepItem.subtitle }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 加载状态
const loading = ref(false)

// 确认弹窗
const showConfirm = ref(false)
const confirmTitle = ref('')
const confirmMessage = ref('')
const confirmIcon = ref('fa-question-circle')
let confirmResolve = null

// 成功提示
const showSuccess = ref(false)
const successMessage = ref('')

// 步骤
const steps = [
  { id: 1, title: '基础信息', subtitle: '填写基本信息' },
  { id: 2, title: '条款选择', subtitle: '选择合同条款' },
  { id: 3, title: '合同预览', subtitle: '预览合同内容' },
  { id: 4, title: '生成合同', subtitle: '下载保存合同' }
]

const currentStep = ref(1)

// 显示确认弹窗
const showConfirmation = ({ title, message, icon = 'fa-question-circle' }) => {
  confirmTitle.value = title
  confirmMessage.value = message
  confirmIcon.value = icon
  showConfirm.value = true

  return new Promise((resolve) => {
    confirmResolve = resolve
  })
}

// 确认操作
const confirmAction = () => {
  showConfirm.value = false
  if (confirmResolve) confirmResolve(true)
}

// 取消操作
const confirmCancel = () => {
  showConfirm.value = false
  if (confirmResolve) confirmResolve(false)
}

// 显示成功提示
const showSuccessMessage = (message) => {
  successMessage.value = message
  showSuccess.value = true

  setTimeout(() => {
    showSuccess.value = false
  }, 3000)
}

// 模拟加载
const simulateLoading = async (duration = 2000) => {
  loading.value = true
  await new Promise(resolve => setTimeout(resolve, duration))
  loading.value = false
}

defineExpose({
  showConfirmation,
  showSuccessMessage,
  simulateLoading,
  loading,
  steps,
  currentStep
})
</script>

<style scoped>
/* 动画定义 */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes spin-reverse {
  from { transform: rotate(0deg); }
  to { transform: rotate(-360deg); }
}

.animate-spin {
  animation: spin 2s linear infinite;
}

.animate-spin-reverse {
  animation: spin-reverse 1.5s linear infinite;
}

/* 滑入动画 */
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s ease;
}

.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* 发光效果 */
.glow {
  filter: drop-shadow(0 0 8px rgba(212, 175, 55, 0.5));
}

.glow:hover {
  filter: drop-shadow(0 0 12px rgba(212, 175, 55, 0.8));
}
</style>