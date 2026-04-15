<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white font-sans relative ">
    <!-- 背景装饰元素 -->
    <div class="absolute top-0 left-0 w-full h-full  pointer-events-none">
      <div class="absolute top-20 left-10 w-72 h-72 bg-gradient-to-r from-gold/5 to-transparent rounded-full blur-3xl"></div>
      <div class="absolute bottom-20 right-10 w-96 h-96 bg-gradient-to-l from-gold/5 to-transparent rounded-full blur-3xl"></div>
    </div>

    <nav class="bg-gray-900/80 backdrop-blur-lg border-b border-gold/20 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-6 py-3 flex items-center justify-between">
        <div class="flex items-center gap-3 group cursor-pointer">
          <div class="relative">
            <i class="fa-solid fa-shield-halved text-gold text-2xl float-animation"></i>
            <div class="absolute -inset-2 bg-gold/10 rounded-full blur-sm group-hover:scale-150 transition-transform duration-300"></div>
          </div>
          <span class="font-bold text-xl bg-gradient-to-r from-gold to-yellow-200 bg-clip-text text-transparent">Legal-Guard</span>
          <span class="ml-3 text-sm text-white/60 px-3 py-1 bg-white/5 rounded-full">试用 · 生成一份合同</span>
        </div>
        <router-link to="/" class="group text-sm text-white/70 hover:text-gold transition-all duration-300 flex items-center gap-2">
          <i class="fa-solid fa-arrow-left transition-transform group-hover:-translate-x-1"></i>
          返回首页
        </router-link>
      </div>
    </nav>

    <!-- 顶部通知条 - 增强视觉 -->
    <div class="relative  bg-gradient-to-r from-orange-500 to-orange-600 text-white text-sm px-6 py-3 text-center font-bold">
      <div class="flex items-center justify-center gap-2">
        <i class="fa-solid fa-clock animate-pulse"></i>
        免费试用合同有效期 7 天
        <i class="fa-solid fa-gift ml-2"></i>
      </div>
      <!-- 进度条 -->
      <div class="absolute bottom-0 left-0 w-full h-1 bg-white/20">
        <div class="h-full bg-white/50 pulse-animation" :style="{ width: '100%' }"></div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 py-8 pb-32 flex gap-6 relative z-10">
      <!-- 左侧导航栏美化 -->
      <aside class="w-64 bg-gray-900/60 backdrop-blur-sm rounded-2xl p-6 flex flex-col gap-6 sticky top-24 border border-white/10 shadow-2xl shadow-black/50">
        <div class="flex items-center gap-3 mb-4">
          <div class="relative">
            <div class="w-10 h-10 bg-gradient-to-br from-gold to-yellow-200 rounded-xl flex items-center justify-center shadow-lg shadow-gold/20">
              <i class="fa-solid fa-file-contract text-gray-900 text-lg"></i>
            </div>
            <div class="absolute -inset-1 bg-gold/20 rounded-xl blur-sm"></div>
          </div>
          <div>
            <span class="text-lg font-bold bg-gradient-to-r from-gold to-yellow-200 bg-clip-text text-transparent">合同向导</span>
            <p class="text-xs text-white/40">5步完成</p>
          </div>
        </div>

        <nav class="flex-1">
          <ul class="space-y-2">
            <li v-for="(item, index) in steps" :key="index"
                @click="step = item.id"
                class="group p-3 rounded-xl transition-all duration-300 cursor-pointer"
                :class="step === item.id
                  ? 'bg-gradient-to-r from-gold/20 to-gold/10 border border-gold/30 shadow-lg shadow-gold/10'
                  : 'hover:bg-white/5 border border-transparent hover:border-white/10'">
              <div class="flex items-center gap-3">
                <div class="relative">
                  <div class="w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-300"
                       :class="step === item.id
                         ? 'bg-gradient-to-br from-gold to-yellow-200 text-gray-900'
                         : 'bg-white/5 text-white/60 group-hover:bg-gold/20 group-hover:text-gold'">
                    <i :class="item.icon"></i>
                  </div>
                  <div v-if="step === item.id" class="absolute -inset-1 bg-gold/20 rounded-lg blur-sm"></div>
                </div>
                <div class="flex-1">
                  <div class="flex items-center justify-between">
                    <span class="font-medium text-sm"
                          :class="step === item.id ? 'text-gold' : 'text-white/80 group-hover:text-white'">
                      {{ item.title }}
                    </span>
                    <span class="text-xs px-2 py-0.5 rounded-full"
                          :class="step === item.id
                            ? 'bg-gold/20 text-gold'
                            : 'bg-white/5 text-white/40'">
                      {{ item.id }}
                    </span>
                  </div>
                  <p class="text-xs mt-1"
                     :class="step === item.id ? 'text-gold/80' : 'text-white/40 group-hover:text-white/60'">
                    {{ item.description }}
                  </p>
                </div>
              </div>
            </li>
          </ul>
        </nav>

        <!-- 进度指示器 -->
        <div class="mt-4 p-3 bg-white/5 rounded-xl">
          <div class="flex items-center justify-between text-xs mb-2">
            <span class="text-white/60">整体进度</span>
            <span class="text-gold font-semibold">{{ Math.round((step-1)/4*100) }}%</span>
          </div>
          <div class="h-2 bg-white/10 rounded-full ">
            <div class="h-full bg-gradient-to-r from-gold to-yellow-200 rounded-full transition-all duration-500"
                 :style="{ width: ((step-1)/4*100) + '%' }"></div>
          </div>
        </div>
      </aside>

      <!-- 主内容区域美化 -->
      <main class="flex-1 bg-gradient-to-br from-gray-900/80 to-gray-800/80 backdrop-blur-sm rounded-2xl p-8 pb-28 border border-white/10 shadow-2xl shadow-black/50">
        <!-- 顶部步骤指示器 -->
        <div class="flex items-center justify-between mb-8">
          <div class="flex items-center gap-4">
            <div class="text-sm text-white/60 px-3 py-1.5 bg-white/5 rounded-lg">
              步骤 <span class="font-bold text-gold text-lg">{{ step }}</span>/5
            </div>
            <div class="w-64 bg-white/10 rounded-full h-2 ">
              <div class="h-2 bg-gradient-to-r from-gold to-yellow-200 rounded-full transition-all duration-500"
                   :style="{ width: ((step-1)/4*100) + '%' }"></div>
            </div>
          </div>

          <!-- 模板选择器美化 -->
          <!-- 在 Trial.vue 的模板选择器处添加 items-center -->
          <div class="relative group">
            <div class="flex items-center gap-0.5 text-sm px-0.5 py-1.5 bg-white/5 rounded-xl border border-white/10 group-hover:border-gold/30 transition-colors">
              <i class="fa-solid fa-layer-group text-gold/80"></i>
              <label for="template-select" class="text-white/70">模板：</label>
              <select id="template-select" v-model="form.template" class="bg-transparent text-gold font-bold border-none outline-none cursor-pointer">
                <option value="standard">标准模板</option>
                <option value="custom">定制模板</option>
              </select>

            </div>
            <div class="absolute bottom-0 left-0 w-full h-0.5 bg-gradient-to-r from-transparent via-gold to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </div>

        </div>

        <!-- 步骤内容区域 -->
        <div class="min-h-[50vh]">
          <!-- STEP 1: 基础信息 -->
          <transition name="fade-slide" mode="out-in">
            <section v-if="step === 1" class="space-y-8">
              <div class="flex items-center gap-3 mb-2">
                <div class="w-10 h-10 bg-gradient-to-br from-gold to-yellow-200 rounded-xl flex items-center justify-center shadow-lg shadow-gold/20">
                  <i class="fa-solid fa-id-card-clip text-gray-900 text-lg"></i>
                </div>
                <h2 class="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                  基础信息
                </h2>
              </div>
              <p class="text-white/60 mb-6">请填写合同相关的基础信息，所有带 <span class="text-red-400">*</span> 的为必填项</p>

              <div class="grid grid-cols-2 gap-6">
                <div class="space-y-2" v-for="field in formFields" :key="field.id">
                  <label :for="field.id" class="block text-white/70 text-sm font-medium flex items-center gap-1">
                    {{ field.label }}
                    <span v-if="field.required" class="text-red-400">*</span>
                  </label>

                  <!-- 输入 + 图标 一行 -->
                  <div class="relative group">
                    <input v-if="!field.options"
                           :id="field.id"
                           v-model="form[field.model]"
                           :placeholder="field.placeholder"
                           class="w-full px-4 pr-10 py-3 rounded-xl bg-white/5 text-white border border-white/10 focus:border-gold/50 focus:ring-2 focus:ring-gold/20 transition-all duration-300 outline-none group-hover:border-white/20"
                           :class="errors[field.model] ? 'border-red-400/50 focus:border-red-400' : ''" />

                    <select v-else
                            :id="field.id"
                            v-model="form[field.model]"
                            class="w-full px-4 pr-10 py-3 rounded-xl bg-white/5 text-white border border-white/10 focus:border-gold/50 focus:ring-2 focus:ring-gold/20 transition-all duration-300 outline-none appearance-none group-hover:border-white/20">
                      <option v-for="option in field.options" :key="option.value" :value="option.value">{{ option.label }}</option>
                    </select>

                    <!-- 右侧小图标：始终相对输入行垂直居中，不受错误提示影响 -->
                    <div v-if="field.icon"
                         class="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-white/40 group-hover:text-gold transition-colors">
                      <i :class="field.icon"></i>
                    </div>
                  </div>

                  <!-- 错误提示：单独一行，不改变输入+图标这一行的高度 -->
                  <p v-if="errors[field.model]" class="mt-1 text-sm text-red-400 flex items-center gap-2">
                    <i class="fa-solid fa-circle-exclamation"></i>
                    {{ errors[field.model] }}
                  </p>
                </div>
              </div>
            </section>
          </transition>

          <!-- STEP 2: 条款选择 -->
          <transition name="fade-slide" mode="out-in">
            <section v-if="step === 2" class="space-y-6">
              <div class="flex items-center gap-3 mb-2">
                <div class="w-10 h-10 bg-gradient-to-br from-gold to-yellow-200 rounded-xl flex items-center justify-center shadow-lg shadow-gold/20">
                  <i class="fa-solid fa-list-check text-gray-900 text-lg"></i>
                </div>
                <h2 class="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                  条款选择
                </h2>
              </div>

              <div class="flex items-center justify-between p-4 bg-white/5 rounded-xl border border-white/10">
                <div class="flex items-center gap-3">
                  <i class="fa-solid fa-lightbulb text-gold/80"></i>
                  <div>
                    <p class="text-sm text-white/90">根据业务场景，选择需要纳入合同的条款</p>
                    <p class="text-xs text-white/50">建议至少选择 <span class="text-gold font-semibold">2项</span> 核心条款</p>
                  </div>
                </div>
                <label class="inline-flex items-center gap-3 cursor-pointer">
                  <div class="relative">
                    <input type="checkbox" v-model="selectAll" class="sr-only peer" />
                    <div class="w-12 h-6 bg-white/10 rounded-full peer peer-checked:bg-gold/30 transition-colors"></div>
                    <div class="absolute top-1 left-1 w-4 h-4 bg-white rounded-full transition-transform peer-checked:translate-x-6"></div>
                  </div>
                  <span class="text-sm font-medium">{{ selectAll ? '全选' : '自定义' }}</span>
                </label>
              </div>

              <!-- 条款折叠面板 -->
              <div class="space-y-4">
                <div v-for="panel in termPanels" :key="panel.id"
                     class="bg-white/5 rounded-xl border border-white/10  transition-all duration-300 hover:border-gold/30">
                  <button @click="togglePanel(panel.id)"
                          class="w-full flex items-center justify-between p-4 text-left group hover:bg-white/2 transition-colors">
                    <div class="flex items-center gap-3">
                      <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-gold/20 to-gold/10 flex items-center justify-center">
                        <i :class="panel.icon" class="text-blue"></i>
                      </div>
                      <div>
                        <h3 class="font-semibold text-black">{{ panel.title }}</h3>
                        <p class="text-xs text-black/70 mt-0.5">{{ panel.description }}</p>
                      </div>
                    </div>
                    <div class="flex items-center gap-3">
                      <span class="text-xs px-2 py-1 rounded-full bg-white/5 text-black/60">
                        {{ getSelectedCount(panel.id) }}/{{ panel.terms.length }}
                      </span>
                      <i :class="panels[panel.id] ? 'fa-solid fa-chevron-up' : 'fa-solid fa-chevron-down'"
                         class="text-white group-hover:text-gold transition-colors"></i>
                    </div>
                  </button>

                  <transition name="expand">
                    <div v-show="panels[panel.id]" class="px-4 pb-4">
                      <div class="grid grid-cols-2 gap-3">
                        <label v-for="term in panel.terms" :key="term.value"
                               class="flex items-center gap-3 p-3 rounded-lg cursor-pointer transition-all duration-300"
                               :class="terms.includes(term.value)
                                 ? 'bg-gold/10 border border-gold/20'
                                 : 'hover:bg-white/5 border border-transparent'">
                          <div class="relative flex items-center">
                            <!-- peer 放在 input 上 -->
                            <input type="checkbox"
                                   v-model="terms"
                                   :value="term.value"
                                   class="sr-only peer" />

                            <!-- 小方框：用 peer-checked 控制背景和边框 -->
                            <div class="w-5 h-5 rounded border border-white/30 flex items-center justify-center transition-all duration-300
                                        peer-checked:bg-white peer-checked:border-gold peer-checked:shadow-md peer-checked:shadow-gold/30">
                            </div>

                            <!-- 对勾图标：作为 input 的兄弟，用 peer-checked 控制显隐和缩放，通过负 margin 叠加在方框上 -->
                            <i class="fa-solid fa-check text-black text-xs opacity-0 scale-75 ml-[-1.1rem]
                                       transition-all duration-300
                                       peer-checked:opacity-100 peer-checked:scale-110"></i>
                          </div>

                          <div class="flex-1">
                            <span class="text-sm font-medium text-white">{{ term.label }}</span>
                            <p class="text-xs text-white/50 mt-0.5">{{ term.description }}</p>
                          </div>
                          <i :class="term.icon" class="text-gold/60"></i>
                        </label>
                      </div>
                    </div>
                  </transition>
                </div>
              </div>
            </section>
          </transition>

          <!-- STEP 3: 合同预览 -->
          <transition name="fade-slide" mode="out-in">
            <section v-if="step === 3" class="space-y-6">
              <div class="flex items-center gap-3 mb-2">
                <div class="w-10 h-10 bg-gradient-to-br from-gold to-yellow-200 rounded-xl flex items-center justify-center shadow-lg shadow-gold/20">
                  <i class="fa-solid fa-file-lines text-gray-900 text-lg"></i>
                </div>
                <h2 class="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                  合同预览
                </h2>
              </div>

              <div class="mb-6 p-4 bg-white/5 rounded-xl border border-white/10">
                <div class="flex items-center justify-between">
                  <p class="text-sm text-white/80">预览已根据您填写的信息生成合同草案</p>
                  <div class="flex items-center gap-2">
                    <span class="text-xs text-white/50 px-2 py-1 bg-white/5 rounded">自动保存</span>
                    <i class="fa-solid fa-circle-check text-green-400 text-xs"></i>
                  </div>
                </div>
              </div>

              <!-- 预览控制栏 -->
              <div class="flex items-center justify-between mb-4 p-3 bg-white/5 rounded-xl border border-white/10">
                <div class="flex items-center gap-4">
                  <div class="flex items-center gap-2">
                    <button @click="zoomOut"
                            class="w-8 h-8 rounded-lg flex items-center justify-center bg-white/5 hover:bg-white/10 transition-colors"
                            :disabled="zoom <= 50">
                      <i class="fa-solid fa-magnifying-glass-minus"></i>
                    </button>
                    <span class="text-sm font-medium min-w-[60px] text-center">{{ zoom }}%</span>
                    <button @click="zoomIn"
                            class="w-8 h-8 rounded-lg flex items-center justify-center bg-white/5 hover:bg-white/10 transition-colors"
                            :disabled="zoom >= 200">
                      <i class="fa-solid fa-magnifying-glass-plus"></i>
                    </button>
                  </div>

                  <div class="h-6 w-px bg-white/20"></div>

                  <div class="flex items-center gap-2">
                    <button @click="toggleFullscreen"
                            class="px-2 py-1 text-sm rounded-lg flex items-center bg-white/5 hover:bg-white/10 transition-colors">
                      <i class="fa-solid" :class="isFullscreen ? 'fa-compress' : 'fa-expand'"></i>
                      {{ isFullscreen ? '退出全屏' : '全屏预览' }}
                    </button>
                    <button @click="printPreview"
                            class="px-3 py-1 text-sm rounded-lg flex items-center bg-white/5 hover:bg-white/10 transition-colors">
                      <i class="fa-solid fa-print"></i>
                      打印
                    </button>
                  </div>
                </div>

                <div class="flex items-center gap-1 text-sm">
                  <span class="text-white/60 whitespace-nowrap ml-1">预览模式</span>
                  <div class="flex bg-white/5 rounded-lg p-0.5 gap-2">
                    <button @click="previewMode = 'single'"
                            class="px-3 py-1 rounded-md transition-all"
                            :class="previewMode === 'single' ? 'bg-white/10 text-white' : 'text-white/60'">
                      单页
                    </button>
                    <button @click="previewMode = 'continuous'"
                            class="px-3 py-1 rounded-md transition-all"
                            :class="previewMode === 'continuous' ? 'bg-white/10 text-white' : 'text-white/60'">
                      连续
                    </button>
                  </div>
                </div>
              </div>

              <!-- 合同预览区域 -->
              <div class="relative">
                <!-- 水印背景（仅在非全屏时显示，以免干扰阅读） -->
                <div v-if="!isFullscreen" class="absolute inset-0 flex items-center justify-center pointer-events-none">
                  <div class="text-center opacity-5">
                    <div class="text-6xl font-bold mb-4">LEGAL-GUARD</div>
                    <div class="text-2xl">试用预览版</div>
                  </div>
                </div>

                <!-- 全屏滚动进度条，仅在全屏时显示在预览容器顶部 -->
                <div v-if="isFullscreen" class="fixed top-0 left-0 w-full z-[9999] bg-black/60 flex items-center justify-center py-2">
                  <div class="w-[70%] max-w-3xl flex items-center gap-3 text-xs text-gray-200">
                    <span class="whitespace-nowrap">阅读进度</span>
                    <div class="flex-1 h-1.5 rounded-full bg-white/20 overflow-hidden">
                      <div class="h-full bg-gradient-to-r from-gold to-yellow-200" :style="{ width: fullscreenProgress + '%' }"></div>
                    </div>
                    <span class="w-10 text-right">{{ fullscreenProgress }}%</span>
                  </div>
                </div>

                <!-- 预览容器：普通模式为卡片，浏览器全屏时占满视口高度并允许内部滚动 -->
                <div
                  ref="previewContainer"
                  :class="[
                    'bg-white text-gray-900 rounded-xl border-2 border-gold/20 shadow-2xl relative',
                    isFullscreen
                      ? 'mx-auto mt-8 mb-8 max-w-5xl h-screen overflow-y-auto'
                      : 'p-8 pb-24 min-h-[60vh] overflow-y-auto max-h-[70vh]'
                  ]"
                >
                  <!-- 合同页面：A4 纸质排版，无 transform -->
                  <div
                    id="contract-preview"
                    class="mx-auto bg-white text-gray-900 contract-page"
                  >
                    <!-- 合同头部 -->
                    <div class="text-center mb-8 pb-4 border-b border-gray-300">
                      <h1 class="contract-title">服务协议（试用版）</h1>
                      <p class="contract-subtitle">（以下简称“本协议”）</p>
                      <div class="flex justify-center items-center gap-6 contract-meta">
                        <div class="flex items-center gap-1.5">
                          <span class="font-medium">合同编号：</span>
                          <span class="font-mono">LG-{{ generateContractNumber() }}</span>
                        </div>
                        <div class="h-4 w-px bg-gray-300"></div>
                        <div class="flex items-center gap-1.5">
                          <span class="font-medium">生成日期：</span>
                          <span>{{ new Date().toLocaleDateString('zh-CN') }}</span>
                        </div>
                      </div>
                    </div>

                    <!-- 合同主体 -->
                    <div class="contract-body">
                      <!-- 合同方信息 -->
                      <section class="clause-block">
                        <h2 class="clause-title">
                          一、合同方信息
                        </h2>
                        <p class="clause-paragraph">
                          甲方（服务提供方）：<span class="font-medium">{{ form.company || '[请填写公司名称]' }}</span>
                        </p>
                        <p class="clause-paragraph">
                          乙方（服务接收方）：<span class="font-medium">{{ form.counterparty || '[请填写相对方名称]' }}</span>
                        </p>
                        <p class="clause-note">
                          适用法域：{{ getJurisdictionLabel(form.jurisdiction) }}；合同类型：{{ getContractTypeLabel(form.contractType) }}
                        </p>
                      </section>

                      <!-- 合同条款 -->
                      <section class="clause-block">
                        <h2 class="clause-title">
                          二、合同条款
                        </h2>

                        <!-- 基础条款 -->
                        <div v-if="hasSelectedTerms('base')" class="clause-sub-block">
                          <h3 class="clause-sub-title">（一）基础条款</h3>
                          <div class="clause-sub-content">
                            <div v-if="terms.includes('payment')" class="clause-item">
                              <p class="clause-item-title">1. 支付条款</p>
                              <p class="clause-paragraph">
                                双方确认，本协议项下服务费用按照附件一《服务费用明细》执行，乙方应在收到甲方发票后十五（15）个工作日内完成支付。具体支付方式、币种及开票信息由双方另行以书面形式确认。
                              </p>
                            </div>

                            <div v-if="terms.includes('delivery')" class="clause-item">
                              <p class="clause-item-title">2. 交付条款</p>
                              <p class="clause-paragraph">
                                甲方应在本协议生效之日起十（10）个工作日内，按照附件二《服务交付标准》的约定完成服务交付。乙方应在合理期限内对交付结果进行验收，并将验收意见以书面形式反馈甲方。
                              </p>
                            </div>

                            <div v-if="terms.includes('warranty')" class="clause-item">
                              <p class="clause-item-title">3. 质量保证</p>
                              <p class="clause-paragraph">
                                甲方保证其提供的服务符合国家及行业相关质量标准，自服务最终交付之日起，质量保证期为十二（12）个月。在质量保证期内，如因甲方原因导致服务存在缺陷，甲方应负责免费修复或重新提供服务。
                              </p>
                            </div>
                          </div>
                        </div>

                        <!-- 数据安全条款 -->
                        <div v-if="hasSelectedTerms('data')" class="clause-sub-block">
                          <h3 class="clause-sub-title">（二）数据安全条款</h3>
                          <div class="clause-sub-content">
                            <div v-if="terms.includes('encryption')" class="clause-item">
                              <p class="clause-item-title">1. 数据加密</p>
                              <p class="clause-paragraph">
                                双方确认，所有涉及个人信息、商业秘密及其他敏感信息的数据，在传输及存储过程中均应采用符合行业标准的加密技术（包括但不限于 AES-256 等），以确保数据在传输链路及存储介质上的安全性。
                              </p>
                            </div>

                            <div v-if="terms.includes('backup')" class="clause-item">
                              <p class="clause-item-title">2. 数据备份</p>
                              <p class="clause-paragraph">
                                甲方应建立完善的数据备份与灾难恢复机制，对关键业务数据进行每日自动备份，备份数据的保留期限不少于三十（30）天。发生重大故障时，甲方应在合理时间内完成数据恢复，并尽最大努力降低对乙方业务的影响。
                              </p>
                            </div>

                            <div v-if="terms.includes('privacy')" class="clause-item">
                              <p class="clause-item-title">3. 隐私保护</p>
                              <p class="clause-paragraph">
                                双方应严格遵守适用法律法规（包括但不限于《个人信息保护法》《网络安全法》及 GDPR 等）关于个人信息和隐私保护的规定，未经信息主体明示同意，不得超出约定目的收集、使用或向第三方提供相关个人信息。
                              </p>
                            </div>
                          </div>
                        </div>

                        <!-- 服务范围条款 -->
                        <div v-if="hasSelectedTerms('scope')" class="clause-sub-block">
                          <h3 class="clause-sub-title">（三）服务范围条款</h3>
                          <div class="clause-sub-content">
                            <div v-if="terms.includes('support')" class="clause-item">
                              <p class="clause-item-title">1. 技术支持</p>
                              <p class="clause-paragraph">
                                甲方应向乙方提供与本协议项下服务相关的技术支持，包括但不限于故障处理、功能咨询及配置指导等。常规技术支持服务时间为 7×24 小时，响应时间一般不超过二（2）小时，重大故障的解决方案提供时间不超过二十四（24）小时。
                              </p>
                            </div>

                            <div v-if="terms.includes('sla')" class="clause-item">
                              <p class="clause-item-title">2. 服务级别协议</p>
                              <p class="clause-paragraph">
                                甲方承诺，其所提供在线服务在自然月内的可用性不低于 99.5%。如服务可用性低于前述标准，双方可参照附件三《服务赔偿方案》对服务费用进行相应调整或补偿。
                              </p>
                            </div>

                            <div v-if="terms.includes('training')" class="clause-item">
                              <p class="clause-item-title">3. 培训服务</p>
                              <p class="clause-paragraph">
                                为确保乙方能够有效使用本协议项下服务，甲方应提供不少于八（8）小时的操作培训，并向乙方交付完整的产品使用文档及常见问题说明。培训方式可以包括现场培训、线上培训或录制课程等形式。
                              </p>
                            </div>
                          </div>
                        </div>

                        <!-- 未选择条款提示 -->
                        <div v-if="terms.length === 0" class="mt-6 p-6 bg-yellow-50 border border-yellow-200 rounded text-center text-sm text-gray-700">
                          尚未选择任何合同条款，请返回步骤二进行配置，以生成完整的合同文本。
                        </div>
                      </section>

                      <!-- 签署区域 -->
                      <section class="signature-block">
                        <div class="signature-grid">
                          <div class="signature-column">
                            <div class="signature-box"></div>
                            <div class="signature-text">
                              <p class="font-medium">甲方：{{ form.company || '[甲方名称]' }}</p>
                              <p>授权代表（签字或盖章）：_________________________</p>
                              <p>日期：________年____月____日</p>
                            </div>
                          </div>
                          <div class="signature-column">
                            <div class="signature-box"></div>
                            <div class="signature-text">
                              <p class="font-medium">乙方：{{ form.counterparty || '[乙方名称]' }}</p>
                              <p>授权代表（签字或盖章）：_________________________</p>
                              <p>日期：________年____月____日</p>
                            </div>
                          </div>
                        </div>
                      </section>
                    </div>
                  </div>
                </div>

                <!-- 页码 -->
                <div class="mt-4 flex justify-between items-center text-sm text-gray-500">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-file-pdf text-red-500"></i>
                    <span>总页数: 1</span>
                  </div>
                  <div class="flex items-center gap-4">
                    <span>预览缩放: {{ zoom }}%</span>
                    <span>最后更新: {{ new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' }) }}</span>
                  </div>
                </div>
              </div>
            </section>
          </transition>

          <!-- STEP 4: 合规审查 -->
          <transition name="fade-slide" mode="out-in">
            <section v-if="step === 4" class="space-y-6">
              <div class="flex items-center gap-3 mb-2">
                <div class="w-10 h-10 bg-gradient-to-br from-gold to-yellow-200 rounded-xl flex items-center justify-center shadow-lg shadow-gold/20">
                  <i class="fa-solid fa-scale-balanced text-gray-900 text-lg"></i>
                </div>
                <h2 class="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                  合规审查
                </h2>
              </div>

              <!-- 顶部提示条：多法域适配说明 -->
              <div class="p-4 bg-white/5 rounded-xl border border-white/10 flex items-center justify-between gap-4">
                <div class="flex items-center gap-3">
                  <div class="w-9 h-9 rounded-lg bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center">
                    <i class="fa-solid fa-globe text-gray-900"></i>
                  </div>
                  <div>
                    <p class="text-sm text-white/90">跨境多法域合规适配</p>
                    <p class="text-xs text-white/50">支持 28 个主要贸易法域，自动匹配本合同的合规规则库（示例数据）</p>
                  </div>
                </div>
                <div class="flex items-center gap-2 text-sm">
                  <span class="text-white/60">目标法域</span>
                  <select v-model="complianceJurisdiction"
                          class="px-3 py-1.5 rounded-lg bg-white/10 text-white text-sm border border-white/20 outline-none cursor-pointer">
                    <option value="EU">欧盟（GDPR）</option>
                    <option value="US">美国（UCC）</option>
                    <option value="CN">中国（外贸法）</option>
                    <option value="ASEAN">东盟自贸区</option>
                  </select>
                </div>
              </div>

              <!-- 风险分级总览 -->
              <div class="grid grid-cols-3 gap-4">
                <div class="bg-white/5 rounded-xl p-4 border border-red-500/30 flex flex-col gap-1">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-triangle-exclamation text-red-400"></i>
                    <span class="text-sm font-semibold text-red-300">高风险</span>
                  </div>
                  <p class="text-xs text-white/60">可能违反目标法域强制性法规，影响合同效力或引发财务处罚。</p>
                </div>
                <div class="bg-white/5 rounded-xl p-4 border border-amber-400/30 flex flex-col gap-1">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-circle-exclamation text-amber-300"></i>
                    <span class="text-sm font-semibold text-amber-200">中风险</span>
                  </div>
                  <p class="text-xs text-white/60">条款存在瑕疵或模糊表述，易引发跨境纠纷。</p>
                </div>
                <div class="bg-white/5 rounded-xl p-4 border border-blue-400/30 flex flex-col gap-1">
                  <div class="flex items-center gap-2">
                    <i class="fa-solid fa-circle-info text-blue-300"></i>
                    <span class="text-sm font-semibold text-blue-200">低风险</span>
                  </div>
                  <p class="text-xs text-white/60">不影响法律效力，但建议优化术语、语言或细节描述。</p>
                </div>
              </div>

              <!-- 风险详情与一键优化列表（示例静态数据） -->
              <div class="grid grid-cols-3 gap-6">
                <!-- 左：风险清单 -->
                <div class="col-span-2 space-y-3">
                  <h3 class="text-sm font-semibold text-white flex items-center gap-2">
                    <i class="fa-solid fa-list-check text-gold"></i>
                    风险清单（示例）
                  </h3>
                  <div v-for="(risk, idx) in complianceRisks" :key="idx"
                       class="bg-white/5 rounded-xl p-4 border border-white/10 hover:border-gold/40 transition-all duration-300">
                    <div class="flex items-start justify-between gap-3">
                      <div class="flex items-start gap-3">
                        <div class="mt-0.5">
                          <div class="w-8 h-8 rounded-lg flex items-center justify-center"
                               :class="risk.color === 'red' ? 'bg-red-500/20 text-red-300' : risk.color === 'amber' ? 'bg-amber-500/20 text-amber-200' : 'bg-blue-500/20 text-blue-200'">
                            <i :class="risk.icon"></i>
                          </div>
                        </div>
                        <div>
                          <div class="flex items-center gap-2">
                            <span class="text-xs px-2 py-0.5 rounded-full border border-white/10"
                                  :class="risk.color === 'red' ? 'text-red-300 border-red-500/40' : risk.color === 'amber' ? 'text-amber-200 border-amber-400/40' : 'text-blue-200 border-blue-400/40'">
                              {{ risk.level }}
                            </span>
                            <span class="text-xs text-white/60 truncate">{{ risk.law }}</span>
                          </div>
                          <p class="mt-1 text-sm text-white/90 font-medium">{{ risk.clause }}</p>
                          <p class="mt-1 text-xs text-white/60">{{ risk.description }}</p>
                          <p class="mt-2 text-xs text-gold/80">建议：{{ risk.suggestion }}</p>
                        </div>
                      </div>
                      <button class="text-xs px-3 py-1 rounded-full bg-gold/20 text-gold hover:bg-gold/30 transition-colors">
                        一键优化
                      </button>
                    </div>
                  </div>
                </div>

                <!-- 右：多语言对照与报告导出 -->
                <div class="space-y-4">
                  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
                    <h3 class="text-sm font-semibold text-white flex items-center gap-2 mb-2">
                      <i class="fa-solid fa-language text-gold"></i>
                      多语言对照审查
                    </h3>
                    <p class="text-xs text-white/60 mb-2">支持中英文对照，风险标注同步显示，解决跨境语言理解差异。（此处为示意）</p>
                    <div class="h-24 bg-black/40 rounded-lg border border-white/10 flex items-center justify-center text-xs text-white/40">
                      示例：中英文对照预览区域，可在后续接入真实合同文本
                    </div>
                  </div>

                  <div class="bg-white/5 rounded-xl p-4 border border-white/10 flex flex-col gap-3">
                    <h3 class="text-sm font-semibold text-white flex items-center gap-2">
                      <i class="fa-solid fa-file-shield text-gold"></i>
                      合规审查报告
                    </h3>
                    <p class="text-xs text-white/60">生成包含风险清单、整改建议、法规依据的报告，支持 PDF / Word / 文本导出。</p>
                    <button @click="exportComplianceReport"
                            class="mt-1 px-4 py-2 rounded-lg bg-gradient-to-r from-gold to-yellow-200 text-gray-900 text-xs font-semibold flex items-center justify-center gap-2 hover:scale-105 transition-transform">
                      <i class="fa-solid fa-file-arrow-down"></i>
                      导出合规审查报告（示例）
                    </button>
                  </div>
                </div>
              </div>
            </section>
          </transition>

          <!-- STEP 5: 生成合同 -->
          <transition name="fade-slide" mode="out-in">
            <section v-if="step === 5" class="space-y-8">
              <div class="flex items-center gap-3 mb-2">
                <div class="w-10 h-10 bg-gradient-to-br from-gold to-yellow-200 rounded-xl flex items-center justify-center shadow-lg shadow-gold/20">
                  <i class="fa-solid fa-circle-check text-gray-900 text-lg"></i>
                </div>
                <h2 class="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                  生成合同
                </h2>
              </div>

              <!-- 成功状态 -->
              <div class="bg-gradient-to-r from-green-500/10 to-emerald-500/10 border border-green-500/30 rounded-2xl p-8 text-center">
                <div class="w-20 h-20 bg-gradient-to-br from-green-500 to-emerald-400 rounded-full flex items-center justify-center mx-auto mb-6 shadow-lg shadow-green-500/30">
                  <i class="fa-solid fa-check text-white text-3xl"></i>
                </div>
                <h3 class="text-2xl font-bold text-white mb-3">合同已准备就绪！</h3>
                <p class="text-white/70 mb-6 max-w-2xl mx-auto">
                  试用合同已成功生成，您可以选择下载或保存到草稿箱，试用期间您可以在控制台中继续查看与编辑此合同。
                </p>

                <!-- 合同信息卡片 -->
                <div class="grid grid-cols-3 gap-4 mb-8 max-w-3xl mx-auto">
                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-gold mb-2">
                      <i class="fa-solid fa-file-contract text-lg"></i>
                    </div>
                    <p class="text-sm text-white/70">合同编号</p>
                    <p class="font-mono font-bold text-white">LG-{{ generateContractNumber() }}</p>
                  </div>

                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-gold mb-2">
                      <i class="fa-solid fa-calendar text-lg"></i>
                    </div>
                    <p class="text-sm text-white/70">生成时间</p>
                    <p class="font-bold text-white">{{ new Date().toLocaleDateString('zh-CN') }}</p>
                  </div>

                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-gold mb-2">
                      <i class="fa-solid fa-layer-group text-lg"></i>
                    </div>
                    <p class="text-sm text-white/70">合同模板</p>
                    <p class="font-bold text-white">{{ form.template === 'standard' ? '标准模板' : '定制模板' }}</p>
                  </div>
                </div>

                <!-- 操作按钮 -->
                <div class="flex flex-wrap justify-center gap-4">
                  <button @click="downloadPdf"
                          class="px-8 py-4 rounded-xl flex items-center gap-3 transition-all duration-300 hover:scale-105 bg-gradient-to-r from-gold to-yellow-200 text-gray-900 font-semibold shadow-lg shadow-gold/30 hover:shadow-xl hover:shadow-gold/40">
                    <i class="fa-solid fa-download text-lg"></i>
                    下载 PDF 格式
                  </button>

                  <button @click="downloadWord"
                          class="px-8 py-4 rounded-xl flex items-center gap-3 transition-all duration-300 hover:scale-105 bg-gradient-to-r from-blue-500 to-cyan-400 text-white font-semibold shadow-lg shadow-blue-500/30">
                    <i class="fa-solid fa-file-word text-lg"></i>
                    下载 Word 格式
                  </button>

                  <button @click="saveToDraft"
                          class="px-8 py-4 rounded-xl flex items-center gap-3 transition-all duration-300 hover:scale-105 bg-white/10 text-white font-bold border border-white/20 hover:border-gold/50">
                    <i class="fa-solid fa-box-archive"></i>
                    保存到草稿箱
                  </button>
                </div>

                <!-- 额外选项 -->
                <div class="mt-8 pt-6 border-t border-white/10">
                  <div class="flex flex-wrap justify-center gap-6 ">
                    <button @click="printContract"
                            class="px-4 py-2 rounded-lg flex items-center gap-2 text-white/70 hover:text-white transition-colors">
                      <i class="fa-solid fa-print"></i>
                      直接打印
                    </button>

                    <button @click="shareContract"
                            class="px-4 py-2 rounded-lg flex items-center gap-2 text-white/70 hover:text-white transition-colors">
                      <i class="fa-solid fa-share-nodes"></i>
                      分享合同
                    </button>

<!--                    <button @click="copyContractLink"-->
<!--                            class="px-4 py-2 rounded-lg flex items-center gap-2 text-white/70 hover:text-white transition-colors">-->
<!--                      <i class="fa-solid fa-link"></i>-->
<!--                      复制链接-->
<!--                    </button>-->

                    <button @click="startNewContract"
                            class="px-4 py-2 rounded-lg flex items-center gap-2 text-white/70 hover:text-white transition-colors">
                      <i class="fa-solid fa-plus"></i>
                      新建合同
                    </button>
                  </div>
                </div>
              </div>

              <!-- 下一步建议 -->
              <div class="bg-gradient-to-r from-blue-500/10 to-indigo-500/10 border border-blue-500/30 rounded-2xl p-6 mt-8">
                <h4 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
                  <i class="fa-solid fa-lightbulb text-blue-400"></i>
                  下一步建议
                </h4>
                <div class="grid grid-cols-3 gap-4">
                  <div class="bg-white/5 p-4 rounded-xl hover:bg-white/10 transition-colors cursor-pointer group"
                       @click="$router.push('/expert-review')">
                    <div class="flex items-center gap-3 mb-2">
                      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-500 flex items-center justify-center">
                        <i class="fa-solid fa-user-tie text-white"></i>
                      </div>
                      <div>
                        <p class="font-medium text-white">专家审查</p>
                        <p class="text-xs text-white/50">由专业律师审查</p>
                      </div>
                    </div>
                    <p class="text-sm text-white/70 group-hover:text-white/80">获得法律专家1对1合同审查服务</p>
                  </div>

                  <div class="bg-white/5 p-4 rounded-xl hover:bg-white/10 transition-colors cursor-pointer group"
                       @click="$router.push('/signature')">
                    <div class="flex items-center gap-3 mb-2">
                      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center">
                        <i class="fa-solid fa-signature text-white"></i>
                      </div>
                      <div>
                        <p class="font-medium text-white">电子签约</p>
                        <p class="text-xs text-white/50">在线完成签署</p>
                      </div>
                    </div>
                    <p class="text-sm text-white/70 group-hover:text-white/80">使用电子签名快速完成合同签署</p>
                  </div>

                  <div class="bg-white/5 p-4 rounded-xl hover:bg-white/10 transition-colors cursor-pointer group"
                       @click="$router.push('/management')">
                    <div class="flex items-center gap-3 mb-2">
                      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
                        <i class="fa-solid fa-folder-tree text-white"></i>
                      </div>
                      <div>
                        <p class="font-medium text-white">合同管理</p>
                        <p class="text-xs text-white/50">归档与跟踪</p>
                      </div>
                    </div>
                    <p class="text-sm text-white/70 group-hover:text-white/80">将合同归档到合同管理系统</p>
                  </div>
                </div>
              </div>
            </section>
          </transition>
        </div>
      </main>

      <!-- 右侧面板美化 -->
      <aside class="w-80 bg-gray-900/60 backdrop-blur-sm rounded-2xl p-6 border border-white/10 shadow-2xl shadow-black/50 sticky top-24 h-[70vh] flex flex-col">
        <!-- 根据步骤显示不同内容 -->
        <div class="flex flex-col h-full">
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center gap-2">
              <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center">
                <i :class="currentPanel.icon" class="text-gray-900 text-sm"></i>
              </div>
              <h3 class="text-lg font-semibold text-white">{{ currentPanel.title }}</h3>
            </div>
            <button @click="toggleHints"
                    class="text-xs px-3 py-1.5 rounded-lg transition-all duration-300"
                    :class="showHints
                      ? 'bg-white/10 text-white/70 hover:bg-white/15'
                      : 'bg-gold/20 text-gold hover:bg-gold/30'">
              {{ showHints ? '隐藏' : '显示' }}
            </button>
          </div>

          <transition name="fade" mode="out-in">
            <div v-if="showHints" class="space-y-4 flex-1 overflow-y-auto pr-2">
              <!-- 步骤3特有的快速修改入口 -->
              <div v-if="step === 3" class="space-y-3">
                <div @click="step = 1"
                     class="p-4 bg-white/5 rounded-xl border border-white/10 hover:border-gold/50 transition-all duration-300 cursor-pointer group hover:translate-x-1">
                  <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-3">
                      <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-gold/20 to-gold/10 flex items-center justify-center">
                        <i class="fa-solid fa-building text-gold"></i>
                      </div>
                      <span class="text-sm font-medium text-white">基础信息</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-white/30 group-hover:text-gold transition-colors"></i>
                  </div>
                  <p class="text-xs text-white/50">公司名称、法域、相对方...</p>
                  <div v-if="form.company" class="mt-2 text-xs px-2 py-1 bg-gold/10 text-gold rounded-full inline-block">
                    已填写: {{ form.company.substring(0, 12) }}{{ form.company.length > 12 ? '...' : '' }}
                  </div>
                </div>

                <div @click="step = 2"
                     class="p-4 bg-white/5 rounded-xl border border-white/10 hover:border-gold/50 transition-all duration-300 cursor-pointer group hover:translate-x-1">
                  <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-3">
                      <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-gold/20 to-gold/10 flex items-center justify-center">
                        <i class="fa-solid fa-file-contract text-gold"></i>
                      </div>
                      <span class="text-sm font-medium text-white">条款内容</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-white/30 group-hover:text-gold transition-colors"></i>
                  </div>
                  <p class="text-xs text-white/50">支付、交付、违约责任...</p>
                  <div v-if="terms.length > 0" class="mt-2 text-xs px-2 py-1 bg-gold/10 text-gold rounded-full inline-block">
                    已选择: {{ terms.length }}项条款
                  </div>
                </div>
              </div>

              <!-- 智能提示内容 -->
              <div v-else class="space-y-3">
                <div v-for="hint in currentHints" :key="hint.id"
                     class="bg-white/5 rounded-xl p-4 border border-white/10 hover:border-gold/30 transition-all duration-300 group hover:translate-x-1">
                  <div class="flex items-center gap-3 mb-2">
                    <div class="w-8 h-8 rounded-lg flex items-center justify-center"
                         :class="hint.color === 'gold'
                           ? 'bg-gold/10 text-gold'
                           : 'bg-blue-500/10 text-blue-400'">
                      <i :class="hint.icon"></i>
                    </div>
                    <div class="flex-1">
                      <div class="flex items-center justify-between">
                        <span class="text-sm font-medium text-white">{{ hint.title }}</span>
                        <span class="text-xs px-2 py-0.5 rounded-full"
                              :class="hint.color === 'gold'
                                ? 'bg-gold/20 text-gold'
                                : 'bg-blue-500/20 text-blue-400'">
                          {{ hint.value }}
                        </span>
                      </div>
                      <p class="text-xs text-white/50 mt-1">{{ hint.description }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </transition>

          <!-- 底部统计 -->
          <div class="mt-6 pt-4 border-t border-white/10">
            <div class="grid grid-cols-2 gap-3 text-xs">
              <div class="text-center">
                <div class="text-lg font-bold text-gold">{{ terms.length }}</div>
                <div class="text-white/50">已选条款</div>
              </div>
              <div class="text-center">
                <div class="text-lg font-bold text-gold">{{ stepCompletionTime }}</div>
                <div class="text-white/50">步骤用时</div>
              </div>
            </div>
          </div>
        </div>
      </aside>
    </div>

    <!-- 底部导航栏美化 -->
    <div class="fixed left-1/2 -translate-x-1/2 bottom-6 w-[min(1000px,96%)] z-40">
      <div class="bg-gray-900/95 backdrop-blur-xl border border-white/10 rounded-2xl px-6 py-4 flex items-center justify-between shadow-2xl shadow-black/50">
        <div class="flex items-center gap-3">
          <button @click="saveDraft"
                  class="px-4 py-2.5 rounded-xl flex items-center gap-2 transition-all duration-300 hover:scale-105"
                  :class="draftSaving
                    ? 'bg-green-500/20 text-green-400 border border-green-500/30'
                    : 'bg-white/10 text-white/90 hover:bg-white/15 hover:text-white border border-white/10'">
            <i :class="draftSaving ? 'fa-solid fa-spinner animate-spin' : 'fa-solid fa-save'"></i>
            {{ draftSaving ? '保存中...' : '保存草稿' }}
          </button>
          <div class="hidden md:block">
            <div class="flex items-center gap-2 text-xs text-white/50">
              <i class="fa-solid fa-lock"></i>
              <span>试用期间生成的合同将自动加密存储</span>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-3">
          <button v-if="step > 1"
                  @click="prev"
                  class="px-5 py-2.5 rounded-xl flex items-center gap-2 transition-all duration-300 hover:scale-105 border border-white/10 hover:border-gold/30 bg-white/5 hover:bg-white/10">
            <i class="fa-solid fa-arrow-left"></i>
            上一步
          </button>

          <button v-if="step < 5"
                  @click="next"
                  class="px-6 py-2.5 rounded-xl flex items-center gap-2 transition-all duration-300 hover:scale-105 bg-gradient-to-r from-gold to-yellow-200 text-gray-900 font-semibold shadow-lg shadow-gold/25 hover:shadow-xl hover:shadow-gold/40">
            <span>{{ step === 4 ? '生成合同' : '下一步' }}</span>
            <i class="fa-solid fa-arrow-right"></i>
          </button>

          <button v-if="step === 5"
                  @click="downloadPdf"
                  class="px-6 py-2.5 rounded-xl flex items-center gap-2 transition-all duration-300 hover:scale-105 bg-gradient-to-r from-green-500 to-emerald-400 text-white font-semibold shadow-lg shadow-green-500/25">
            <i class="fa-solid fa-download"></i>
            下载 PDF
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, watch, computed, onMounted, onBeforeUnmount } from 'vue'

const step = ref(1)
const form = reactive({
  company: '',
  jurisdiction: 'CN',
  counterparty: '',
  contractType: 'saas',
  template: 'standard',
})

// 新增变量
const zoom = ref(100)
const isFullscreen = ref(false)
const previewMode = ref('single')
const stepCompletionTime = ref('0:00')
const startTime = ref(Date.now())
const fullscreenProgress = ref(0)
let previewContainerEl = null

// 定义步骤信息
const steps = [
  { id: 1, icon: 'fa-solid fa-id-card-clip', title: '基础信息', description: '填写合同基本信息' },
  { id: 2, icon: 'fa-solid fa-list-check', title: '条款选择', description: '选择合同条款内容' },
  { id: 3, icon: 'fa-solid fa-file-lines', title: '合同预览', description: '预览生成的合同' },
  { id: 4, icon: 'fa-solid fa-scale-balanced', title: '合规审查', description: '检测跨境合规风险' },
  { id: 5, icon: 'fa-solid fa-circle-check', title: '生成合同', description: '下载或保存合同' }
]

// 定义表单字段
const formFields = [
  { id: 'company', label: '公司名称', model: 'company', placeholder: '请输入公司营业主体全称', required: true, icon: 'fa-solid fa-building' },
  { id: 'counterparty', label: '相对方名称', model: 'counterparty', placeholder: '请输入合作方公司名称', required: true, icon: 'fa-solid fa-handshake' },
  { id: 'jurisdiction', label: '适用法域', model: 'jurisdiction', options: [
      { value: 'CN', label: '中国（CN）' },
      { value: 'US', label: '美国（US）' },
      { value: 'UK', label: '英国（UK）' },
      { value: 'EU', label: '欧盟（EU）' }
    ], icon: 'fa-solid fa-globe' },
  { id: 'contract-type', label: '合同类型', model: 'contractType', options: [
      { value: 'saas', label: 'SaaS 服务协议' },
      { value: 'distribution', label: '分销合作协议' },
      { value: 'nda', label: '保密协议（NDA）' }
    ], icon: 'fa-solid fa-file-contract' }
]

// 定义条款面板
const termPanels = [
  {
    id: 'base',
    icon: 'fa-solid fa-list',
    title: '基础条款',
    description: '建议至少选择 2 项核心条款',
    terms: [
      { value: 'payment', label: '支付条款', description: '付款方式、账期、违约金', icon: 'fa-solid fa-credit-card' },
      { value: 'delivery', label: '交付条款', description: '交付时间、标准、方式', icon: 'fa-solid fa-truck-fast' },
      { value: 'warranty', label: '质量保证', description: '质量标准、检验、保修期', icon: 'fa-solid fa-certificate' }
    ]
  },
  {
    id: 'data',
    icon: 'fa-solid fa-shield-halved',
    title: '数据安全条款',
    description: '确保数据合规与安全',
    terms: [
      { value: 'encryption', label: '数据加密', description: '数据传输与存储加密', icon: 'fa-solid fa-lock' },
      { value: 'backup', label: '数据备份', description: '定期备份与灾难恢复', icon: 'fa-solid fa-hard-drive' },
      { value: 'privacy', label: '隐私保护', description: 'GDPR/个人信息保护', icon: 'fa-solid fa-user-shield' }
    ]
  },
  {
    id: 'scope',
    icon: 'fa-solid fa-briefcase',
    title: '服务范围条款',
    description: '明确技术支持与服务承诺',
    terms: [
      { value: 'support', label: '技术支持', description: '7x24小时技术支持', icon: 'fa-solid fa-headset' },
      { value: 'sla', label: '服务级别（SLA）', description: '服务可用性承诺', icon: 'fa-solid fa-chart-line' },
      { value: 'training', label: '培训服务', description: '操作培训与文档', icon: 'fa-solid fa-graduation-cap' }
    ]
  }
]

const errors = reactive({ company: '', counterparty: '' })
const terms = ref([])
const selectAll = ref(false)
const panels = reactive({ base: true, data: false, scope: false })
const showHints = ref(true)
const draftSaving = ref(false)

// 计算当前面板信息
const currentPanel = computed(() => {
  if (step.value === 3) {
    return {
      icon: 'fa-solid fa-wand-magic-sparkles',
      title: '快速修改'
    }
  }
  return {
    icon: 'fa-solid fa-lightbulb',
    title: '智能提示'
  }
})

// 计算当前提示信息
const currentHints = computed(() => {
  const hints = [
    {
      id: 'selected-terms',
      icon: 'fa-solid fa-check-circle',
      title: '已选条款',
      value: `${terms.value.length}项`,
      description: step.value === 2 ? '建议至少选择 2 项核心条款以保障交易安全' : '当前已选择的合同条款',
      color: 'gold'
    },
    {
      id: 'current-template',
      icon: 'fa-solid fa-layer-group',
      title: '当前模板',
      value: form.template === 'standard' ? '标准模板' : '定制模板',
      description: '模板可在顶部选择器中切换',
      color: 'blue'
    }
  ]

  if (step.value === 1 && form.company) {
    hints.push({
      id: 'company-info',
      icon: 'fa-solid fa-building',
      title: '公司信息',
      value: form.company.length > 10 ? form.company.substring(0, 10) + '...' : form.company,
      description: '已填写公司信息',
      color: 'gold'
    })
  }

  return hints
})

// 辅助函数
const getJurisdictionLabel = (value) => {
  const map = {
    'CN': '中国',
    'US': '美国',
    'UK': '英国',
    'EU': '欧盟'
  }
  return map[value] || value
}

const getContractTypeLabel = (value) => {
  const map = {
    'saas': 'SaaS 服务协议',
    'distribution': '分销合作协议',
    'nda': '保密协议（NDA）'
  }
  return map[value] || value
}

const hasSelectedTerms = (panelId) => {
  const panel = termPanels.find(p => p.id === panelId)
  if (!panel) return false
  return panel.terms.some(term => terms.value.includes(term.value))
}

const getSelectedCount = (panelId) => {
  const panel = termPanels.find(p => p.id === panelId)
  if (!panel) return 0
  return panel.terms.filter(term => terms.value.includes(term.value)).length
}

// 生成合同编号
const generateContractNumber = () => {
  const date = new Date()
  const random = Math.floor(Math.random() * 1000).toString().padStart(3, '0')
  return `${date.getFullYear()}${(date.getMonth() + 1).toString().padStart(2, '0')}${date.getDate().toString().padStart(2, '0')}-${random}`
}

// 监听全选/取消全选
watch(selectAll, (v) => {
  if (v) {
    terms.value = termPanels.flatMap(panel => panel.terms.map(term => term.value))
  } else {
    terms.value = []
  }
})

// 监听条款变化
watch(terms, (newTerms) => {
  if (newTerms.length === termPanels.flatMap(panel => panel.terms).length) {
    selectAll.value = true
  } else if (newTerms.length === 0) {
    selectAll.value = false
  }
})

// 监听步骤变化，更新时间
watch(step, () => {
  const currentTime = Date.now()
  const elapsed = Math.floor((currentTime - startTime.value) / 1000)
  const minutes = Math.floor(elapsed / 60)
  const seconds = elapsed % 60
  stepCompletionTime.value = `${minutes}:${seconds.toString().padStart(2, '0')}`
  startTime.value = currentTime
})

function togglePanel(key) {
  panels[key] = !panels[key]
}

function zoomIn() {
  if (zoom.value < 200) {
    zoom.value = Math.min(200, zoom.value + 10)
  }
}

function zoomOut() {
  if (zoom.value > 50) {
    zoom.value = Math.max(50, zoom.value - 10)
  }
}

// 恢复浏览器原生全屏：以预览容器作为全屏对象，配合 CSS 高度 + overflow 解决截断
function toggleFullscreen() {
  const container = previewContainerEl || document.querySelector('#contract-preview')?.parentElement
  if (!container) return

  if (!document.fullscreenElement) {
    if (container.requestFullscreen) {
      container.requestFullscreen()
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen()
    }
  }
}

function printPreview() {
  window.print()
}

function validateStep1() {
  errors.company = ''
  if (!form.company || form.company.trim() === '') {
    errors.company = '公司名称为必填项'
    return false
  }
  if (!form.counterparty || form.counterparty.trim() === '') {
    errors.counterparty = '相对方名称为必填项'
    return false
  }
  return true
}

function next() {
  if (step.value === 1) {
    if (!validateStep1()) return
  }
  if (step.value < 5) {
    step.value++
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

function prev() {
  if (step.value > 1) {
    step.value--
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

async function saveDraft() {
  draftSaving.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1500))
    console.log('保存草稿：', { form: { ...form }, terms: terms.value })
    showNotification('草稿已成功保存', 'success')
  } catch (error) {
    showNotification('保存失败，请重试', 'error')
  } finally {
    draftSaving.value = false
  }
}

async function saveToDraft() {
  draftSaving.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    showNotification('合同已保存到草稿箱', 'success')
  } catch (error) {
    showNotification('保存失败，请重试', 'error')
  } finally {
    draftSaving.value = false
  }
}

function downloadPdf() {
  showNotification('正在生成PDF文件...', 'info')

  setTimeout(() => {
    const content = `服务协议（试用版）
合同编号: LG-${generateContractNumber()}
生成日期: ${new Date().toLocaleDateString('zh-CN')}

甲方（服务提供方）: ${form.company || '[请填写公司名称]'}
乙方（服务接收方）: ${form.counterparty || '[请填写相对方名称]'}
适用法域: ${getJurisdictionLabel(form.jurisdiction)}
合同类型: ${getContractTypeLabel(form.contractType)}

合同条款:
${terms.value.map((term, index) => `${index + 1}. ${term}`).join('\n')}

签署区域:
甲方: _________________________
乙方: _________________________
日期: ________年____月____日`

    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `LegalGuard-合同-${generateContractNumber()}.txt`
    a.click()
    URL.revokeObjectURL(url)

    showNotification('合同下载成功！', 'success')
  }, 2000)
}

function downloadWord() {
  showNotification('正在生成Word文档...', 'info')
  setTimeout(() => {
    showNotification('Word文档生成成功！', 'success')
  }, 1500)
}

function printContract() {
  showNotification('正在准备打印...', 'info')
  setTimeout(() => {
    window.print()
  }, 500)
}

function shareContract() {
  showNotification('复制分享链接成功！', 'success')
}

function copyContractLink() {
  navigator.clipboard.writeText(`${window.location.origin}/contract/${generateContractNumber()}`)
  showNotification('合同链接已复制到剪贴板', 'success')
}

function startNewContract() {
  if (confirm('确定要开始新的合同吗？当前进度将会丢失。')) {
    // 重置表单
    Object.keys(form).forEach(key => {
      if (key !== 'template') {
        form[key] = key === 'jurisdiction' ? 'CN' : key === 'contractType' ? 'saas' : ''
      }
    })
    terms.value = []
    step.value = 1
    showNotification('已开始新的合同', 'success')
  }
}

function toggleHints() {
  showHints.value = !showHints.value
}

function showNotification(message, type = 'info') {
  const notification = document.createElement('div')
  notification.className = `fixed top-4 right-4 px-4 py-3 rounded-xl shadow-lg z-50 transition-all duration-300 transform translate-x-full ${type === 'success' ? 'bg-green-500/90' : type === 'error' ? 'bg-red-500/90' : 'bg-blue-500/90'}`
  notification.innerHTML = `
   <div class="flex items-center gap-3">
      <i class="fa-solid ${type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle'}"></i>
      <span>${message}</span>
    </div>
  `

  document.body.appendChild(notification)

  setTimeout(() => {
    notification.style.transform = 'translateX(0)'
  }, 10)

  setTimeout(() => {
    notification.style.transform = 'translateX(100%)'
    setTimeout(() => {
      document.body.removeChild(notification)
    }, 300)
  }, 3000)
}

// 添加键盘快捷键支持
onMounted(() => {
  document.addEventListener('keydown', (e) => {
    if (e.ctrlKey || e.metaKey) return

    if (e.key === 'ArrowRight' && step.value < 5) {
      e.preventDefault()
      next()
    } else if (e.key === 'ArrowLeft' && step.value > 1) {
      e.preventDefault()
      prev()
    } else if (e.key === 'Enter' && step.value < 5) {
      e.preventDefault()
      next()
    } else if (e.key === '+' && step.value === 3) {
      e.preventDefault()
      zoomIn()
    } else if (e.key === '-' && step.value === 3) {
      e.preventDefault()
      zoomOut()
    } else if (e.key === 'f' && step.value === 3) {
      e.preventDefault()
      toggleFullscreen()
    }
  })

  // 监听浏览器原生全屏变化，同步 isFullscreen 状态
  document.addEventListener('fullscreenchange', () => {
    isFullscreen.value = !!document.fullscreenElement
  })

  previewContainerEl = document.querySelector('#contract-preview')?.parentElement
  if (previewContainerEl) {
    previewContainerEl.addEventListener('scroll', updateFullscreenProgress, { passive: true })
  }
})

onBeforeUnmount(() => {
  if (previewContainerEl) {
    previewContainerEl.removeEventListener('scroll', updateFullscreenProgress)
  }
})

const updateFullscreenProgress = () => {
  if (!previewContainerEl) return
  const scrollTop = previewContainerEl.scrollTop
  const scrollHeight = previewContainerEl.scrollHeight - previewContainerEl.clientHeight
  const ratio = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0
  fullscreenProgress.value = Math.round(ratio)
}
</script>

<style src="./trial.css" scoped></style>
<style scoped>


/* 仅针对步骤1表单中的两个选择框，设置下拉项为金色 */
select#jurisdiction option,
select#contract-type option {
  color: #232222; /* 金色字体 */
  background-color: #ffffff; /* 金色背景 */
}

/* 合同预览纸质排版样式 */
.contract-page {
  /* 近似 A4 比例：宽度固定，居中显示 */
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 56px 56px;
  font-size: 14px;
  line-height: 1.8;
  letter-spacing: 0.02em;
}

.contract-title {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: #111827;
  margin-bottom: 6px;
}

.contract-subtitle {
  font-size: 13px;
  color: #4b5563;
}

.contract-meta {
  margin-top: 8px;
  font-size: 12px;
  color: #6b7280;
}

.contract-body {
  margin-top: 24px;
}

.clause-block {
  margin-bottom: 24px;
}

.clause-title {
  font-size: 16px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 8px;
}

.clause-sub-block {
  margin-top: 12px;
}

.clause-sub-title {
  font-size: 15px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 4px;
}

.clause-sub-content {
  margin-left: 1.5em;
}

.clause-item {
  margin-top: 6px;
}

.clause-item-title {
  font-weight: 600;
  color: #111827;
}

.clause-paragraph {
  text-indent: 2em;
  margin-top: 4px;
  color: #374151;
  font-size: 14px;
}

.clause-note {
  margin-top: 4px;
  font-size: 12px;
  color: #6b7280;
}

.signature-block {
  margin-top: 32px;
  padding-top: 16px;
  border-top: 1px solid #d1d5db;
}

.signature-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 32px;
}

.signature-column {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
}

.signature-box {
  width: 100%;
  height: 96px;
  border: 1px dashed #9ca3af;
}

.signature-text {
  font-size: 13px;
  color: #374151;
}

@media (max-width: 1024px) {
  .contract-page {
    padding: 32px 24px 40px;
    max-width: 100%;
  }
}

</style>
