<template>
  <div class="bg-dark text-white font-sans">
    <Navbar />

    <!-- 英雄区（Hero Section）- 增强图标和响应式 -->
    <section class="hero-screen pt-16 md:pt-20 pb-12 md:pb-20 bg-gradient-to-br from-dark via-darkgray to-dark">
<!--      <div class="hero-container container mx-auto px-4 sm:px-6 lg:px-8 flex flex-col lg:flex-row items-center gap-8 lg:gap-12 max-w-7xl">-->
<!--      <div class="hero-container container mx-auto px-4 sm:px-6 lg:px-8 flex flex-col lg:flex-row items-center gap-8 lg:gap-12 max-w-7xl pt-12 lg:pt-24">-->
      <div class="hero-container container mx-auto px-4 sm:px-6 lg:px-5 flex flex-col lg:flex-row items-center gap-8 lg:gap-12 max-w-7xl py-12 lg:py-24">
      <div class="lg:w-6/12 space-y-4 md:space-y-6">
          <div class="flex items-center gap-3">
<!--            <div class="w-12 h-12 lg:w-20 lg:h-18 rounded-2xl bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center shadow-xl shadow-gold/30">-->
<!--              <i class="fa-solid fa-shield-halved text-gray-900 text-xl lg:text-3xl"></i>-->
<!--            </div>-->
            <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-7xl font-bold leading-tight bg-gradient-to-r from-gold via-yellow-200 to-gold bg-clip-text text-transparent inline-block">
              小微企业的数字法务部
            </h1>
          </div>

          <h2 class="mt-2 text-lg sm:text-xl md:text-2xl font-semibold text-white flex items-center gap-2">
            <i class="fa-solid fa-file-contract text-gold"></i>
            跨境合同AI生成+合规审查
          </h2>

          <p class="text-sm sm:text-base md:text-lg leading-relaxed text-white/70 max-w-xl">
            10分钟生成符合目标国法规的合同，法务成本直降90%，覆盖28个主要贸易国合规标准
          </p>

          <div class="flex flex-col sm:flex-row gap-3 pt-4">
            <router-link to="/trial"
                         class="px-6 py-3 sm:px-8 sm:py-3 bg-gradient-to-r from-gold to-yellow-200 text-dark font-semibold rounded-lg hover:shadow-xl hover:shadow-gold/30 transition-all duration-300 hover:scale-[1.02] flex items-center justify-center gap-2 text-sm sm:text-base">
              <i class="fa-solid fa-rocket"></i>
              免费试用（生成1份合同）
            </router-link>
            <a href="#"
               class="px-6 py-3 sm:px-8 sm:py-3 border border-gold/50 text-gold rounded-lg hover:bg-gold/10 transition-all duration-300 hover:scale-[1.02] flex items-center justify-center gap-2 text-sm sm:text-base">
              <i class="fa-solid fa-play-circle"></i>
              查看演示视频
            </a>
          </div>

          <div class="flex flex-wrap items-center gap-3 lg:gap-4 pt-2 text-white/60 text-xs sm:text-sm">
            <span class="flex items-center gap-1.5 px-3 py-1.5 bg-white/5 rounded-full">
              <i class="fa-solid fa-check-circle text-gold"></i>
              <span>无需信用卡</span>
            </span>
            <span class="flex items-center gap-1.5 px-3 py-1.5 bg-white/5 rounded-full">
              <i class="fa-solid fa-link text-gold"></i>
              <span>区块链存证</span>
            </span>
            <span class="flex items-center gap-1.5 px-3 py-1.5 bg-white/5 rounded-full">
              <i class="fa-solid fa-lock text-gold"></i>
              <span>数据加密</span>
            </span>
          </div>
        </div>

        <!-- 英雄区插图 - 响应式图片 -->
        <div class="lg:w-6/12 w-full mt-8 lg:mt-0 hero-visual-aspect">
          <div class="relative rounded-2xl overflow-hidden shadow-2xl shadow-gold/20 hover:shadow-3xl hover:shadow-gold/30 transition-shadow duration-300">
            <!-- 装饰边框 -->
            <div class="absolute inset-0 border-2 border-gold/20 rounded-2xl pointer-events-none"></div>
            <!-- 图片容器 -->
            <div class="aspect-[4/3] sm:aspect-[16/9] lg:aspect-[4/3] relative overflow-hidden">
              <img src="https://p0.ssl.qhimgs1.com/t04b97659f1c3035604.jpg"
                   alt="跨境合同智能生成演示"
                   class="w-full h-full object-cover transition-transform duration-700 hover:scale-105">
              <!-- 图片叠加效果 -->
              <div class="absolute inset-0 bg-gradient-to-t from-dark/40 to-transparent pointer-events-none"></div>
              <!-- 图片说明 -->
              <div class="absolute bottom-4 left-4 right-4 bg-white/10 backdrop-blur-sm rounded-lg p-3 border border-white/20">
                <div class="flex items-center gap-2">
                  <i class="fa-solid fa-bolt text-gold"></i>
                  <p class="text-white text-sm font-medium">AI智能生成演示 | 实时预览合同条款</p>
                </div>
              </div>
            </div>
            <!-- 装饰角 -->
            <div class="absolute top-0 left-0 w-8 h-8 border-t-2 border-l-2 border-gold rounded-tl-lg"></div>
            <div class="absolute top-0 right-0 w-8 h-8 border-t-2 border-r-2 border-gold rounded-tr-lg"></div>
            <div class="absolute bottom-0 left-0 w-8 h-8 border-b-2 border-l-2 border-gold rounded-bl-lg"></div>
            <div class="absolute bottom-0 right-0 w-8 h-8 border-b-2 border-r-2 border-gold rounded-br-lg"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 核心功能区 - 增强图标和响应式 -->
    <section class="py-12 md:py-20 bg-gradient-to-b from-dark to-darkgray">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl">
        <div class="text-center mb-8 md:mb-16">
          <div class="inline-flex items-center gap-3 mb-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center">
              <i class="fa-solid fa-star text-gray-900"></i>
            </div>
            <h2 class="text-2xl sm:text-3xl md:text-[clamp(1.8rem,3vw,2.5rem)] font-bold">
              核心功能 · 解决跨境法务痛点
            </h2>
          </div>
          <p class="text-sm sm:text-base md:text-xl text-white/60 mt-2 max-w-3xl mx-auto">
            专为跨境小微企业打造，简化法律合规全流程
          </p>
        </div>

        <!-- 功能卡片 - 响应式网格 -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 lg:gap-8">
          <!-- 智能合同生成 -->
          <div class="group bg-white/5 backdrop-blur-sm rounded-2xl p-6 md:p-8 border border-white/10 hover:border-gold/50 transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl hover:shadow-gold/20">
            <div class="relative overflow-hidden rounded-xl mb-6 aspect-[4/3]">
              <!-- 图标叠加在图片上 -->
              <div class="absolute top-4 left-4 z-10">
                <div class="w-12 h-12 rounded-lg bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center shadow-lg">
                  <i class="fa-solid fa-file-contract text-gray-900 text-lg"></i>
                </div>
              </div>
              <!-- 背景图片 -->
              <img src="https://pic.52112.com/2020/01/06/JPG-200106_13/xeBpEnZdQA_small.jpg"
                   alt="智能合同生成示意"
                   class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
              <!-- 图片遮罩 -->
              <div class="absolute inset-0 bg-gradient-to-t from-dark/80 via-dark/40 to-transparent"></div>
              <!-- 图片标签 -->
              <div class="absolute bottom-4 left-4 right-4">
                <span class="inline-block px-3 py-1 bg-gold/90 text-dark text-xs font-semibold rounded-full">
                  AI生成
                </span>
              </div>
            </div>

            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg md:text-xl font-semibold text-gold">智能合同生成</h3>
                <i class="fa-solid fa-arrow-right text-gold/50 group-hover:text-gold group-hover:translate-x-1 transition-all"></i>
              </div>
              <p class="text-white/70 text-sm md:text-base leading-relaxed">
                输入业务需求，AI自动匹配目标法域模板，10分钟生成标准化跨境合同，支持自定义条款补充。
              </p>

              <div class="pt-3 border-t border-white/10">
                <div class="flex flex-wrap gap-2">
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">28个法域</span>
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">AI模板</span>
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">10分钟生成</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 合规审查 -->
          <div class="group bg-white/5 backdrop-blur-sm rounded-2xl p-6 md:p-8 border border-white/10 hover:border-gold/50 transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl hover:shadow-gold/20">
            <div class="relative overflow-hidden rounded-xl mb-6 aspect-[4/3]">
              <div class="absolute top-4 left-4 z-10">
                <div class="w-12 h-12 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-400 flex items-center justify-center shadow-lg">
                  <i class="fa-solid fa-shield-virus text-white text-lg"></i>
                </div>
              </div>
              <img src="https://p0.ssl.qhimgs1.com/sdr/400__/t03191cd514ba3946d6.jpg"
                   alt="合规审查示意"
                   class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
              <div class="absolute inset-0 bg-gradient-to-t from-dark/80 via-dark/40 to-transparent"></div>
              <div class="absolute bottom-4 left-4 right-4">
                <span class="inline-block px-3 py-1 bg-blue-500/90 text-white text-xs font-semibold rounded-full">
                  风险预警
                </span>
              </div>
            </div>

            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg md:text-xl font-semibold text-blue-400">AI合规审查</h3>
                <i class="fa-solid fa-arrow-right text-blue-400/50 group-hover:text-blue-400 group-hover:translate-x-1 transition-all"></i>
              </div>
              <p class="text-white/70 text-sm md:text-base leading-relaxed">
                区块链存证+风险智能标注，高风险条款红色预警，自动提供合规修改建议，降低跨境法律风险。
              </p>

              <div class="pt-3 border-t border-white/10">
                <div class="flex flex-wrap gap-2">
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">区块链存证</span>
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">风险标注</span>
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">自动建议</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 专家咨询 -->
          <div class="group bg-white/5 backdrop-blur-sm rounded-2xl p-6 md:p-8 border border-white/10 hover:border-gold/50 transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl hover:shadow-gold/20">
            <div class="relative overflow-hidden rounded-xl mb-6 aspect-[4/3]">
              <div class="absolute top-4 left-4 z-10">
                <div class="w-12 h-12 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center shadow-lg">
                  <i class="fa-solid fa-user-tie text-white text-lg"></i>
                </div>
              </div>
              <img src="https://p0.ssl.qhimgs1.com/sdr/400__/t01b434b3c4c3f288e0.jpg"
                   alt="专家咨询示意"
                   class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
              <div class="absolute inset-0 bg-gradient-to-t from-dark/80 via-dark/40 to-transparent"></div>
              <div class="absolute bottom-4 left-4 right-4">
                <span class="inline-block px-3 py-1 bg-purple-500/90 text-white text-xs font-semibold rounded-full">
                  专家1v1
                </span>
              </div>
            </div>

            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-lg md:text-xl font-semibold text-purple-400">专家咨询通道</h3>
                <i class="fa-solid fa-arrow-right text-purple-400/50 group-hover:text-purple-400 group-hover:translate-x-1 transition-all"></i>
              </div>
              <p class="text-white/70 text-sm md:text-base leading-relaxed">
                疑难条款匹配专属跨境法律专家，1v1定制化解决方案，响应时间≤4小时，覆盖28个贸易国法域。
              </p>

              <div class="pt-3 border-t border-white/10">
                <div class="flex flex-wrap gap-2">
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">法律专家</span>
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">1v1定制</span>
                  <span class="px-2 py-1 bg-white/5 rounded text-xs text-white/60">4小时响应</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 信任背书区 - 增强图标和响应式 -->
    <section class="py-12 md:py-20 bg-gradient-to-b from-darkgray to-dark">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl">
        <div class="text-center mb-8 md:mb-12">
          <div class="inline-flex items-center gap-3 mb-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center">
              <i class="fa-solid fa-award text-gray-900"></i>
            </div>
            <h2 class="text-2xl sm:text-3xl md:text-[clamp(1.8rem,3vw,2.5rem)] font-bold">
              值得跨境企业信赖
            </h2>
          </div>
          <p class="text-sm sm:text-base md:text-xl text-white/60 mt-2 max-w-3xl mx-auto">
            已服务6000+跨境小微企业，覆盖全球主要贸易区域
          </p>
        </div>

        <!-- 数据统计 + 多语言适配 -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 md:gap-10 mb-8 md:mb-16">
          <!-- 统计数据 -->
          <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 md:p-8 border border-white/10 hover:border-gold/30 transition-all duration-300">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 md:gap-8">
              <div class="text-center group">
                <div class="relative inline-flex items-center justify-center mb-3">
                  <div class="w-20 h-20 rounded-full bg-gradient-to-br from-gold/20 to-transparent flex items-center justify-center">
                    <i class="fa-solid fa-building text-gold text-2xl"></i>
                  </div>
                  <div class="absolute inset-0 animate-ping bg-gold/10 rounded-full"></div>
                </div>
                <p class="text-3xl sm:text-4xl md:text-5xl font-bold text-gold mb-1">6300+</p>
                <p class="text-white/70 text-sm md:text-base">服务跨境小微企业</p>
                <p class="text-gold/60 text-xs mt-1">覆盖28个国家</p>
              </div>

              <div class="text-center group">
                <div class="relative inline-flex items-center justify-center mb-3">
                  <div class="w-20 h-20 rounded-full bg-gradient-to-br from-gold/20 to-transparent flex items-center justify-center">
                    <i class="fa-solid fa-globe-americas text-gold text-2xl"></i>
                  </div>
                  <div class="absolute inset-0 animate-ping bg-gold/10 rounded-full"></div>
                </div>
                <p class="text-3xl sm:text-4xl md:text-5xl font-bold text-gold mb-1">28</p>
                <p class="text-white/70 text-sm md:text-base">覆盖贸易国法域</p>
                <p class="text-gold/60 text-xs mt-1">主要贸易国全合规</p>
              </div>
            </div>
          </div>

          <!-- 多语言适配 -->
          <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 md:p-8 border border-white/10 hover:border-gold/30 transition-all duration-300">
            <div class="flex items-center justify-center gap-3 mb-4 md:mb-6">
              <div class="w-12 h-12 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-400 flex items-center justify-center">
                <i class="fa-solid fa-language text-white text-lg"></i>
              </div>
              <h3 class="text-lg md:text-xl font-semibold text-center">多语言合规适配</h3>
            </div>

            <div class="flex flex-wrap justify-center gap-2 md:gap-3">
              <span class="px-3 md:px-4 py-2 bg-white/5 rounded-lg text-white text-sm md:text-base flex items-center gap-2 hover:bg-white/10 transition-colors">
                <i class="fa-solid fa-check text-gold text-xs"></i>
                简体中文
              </span>
              <span class="px-3 md:px-4 py-2 bg-white/5 rounded-lg text-white text-sm md:text-base flex items-center gap-2 hover:bg-white/10 transition-colors">
                <i class="fa-solid fa-check text-gold text-xs"></i>
                English
              </span>
              <span class="px-3 md:px-4 py-2 bg-white/5 rounded-lg text-white text-sm md:text-base flex items-center gap-2 hover:bg-white/10 transition-colors">
                <i class="fa-solid fa-check text-gold text-xs"></i>
                Español
              </span>
              <span class="px-3 md:px-4 py-2 bg-white/5 rounded-lg text-white text-sm md:text-base flex items-center gap-2 hover:bg-white/10 transition-colors">
                <i class="fa-solid fa-check text-gold text-xs"></i>
                Français
              </span>
              <span class="px-3 md:px-4 py-2 bg-white/5 rounded-lg text-white text-sm md:text-base flex items-center gap-2 hover:bg-white/10 transition-colors">
                <i class="fa-solid fa-check text-gold text-xs"></i>
                Deutsch
              </span>
              <span class="px-3 md:px-4 py-2 bg-white/5 rounded-lg text-white text-sm md:text-base flex items-center gap-2 hover:bg-white/10 transition-colors">
                <i class="fa-solid fa-check text-gold text-xs"></i>
                日本語
              </span>
              <span class="px-3 md:px-4 py-2 bg-gradient-to-r from-gold/20 to-gold/10 text-gold rounded-lg text-sm md:text-base font-semibold flex items-center gap-2">
<!--                <i class="fa-solid fa-plus text-xs"></i>-->
                +6种语言
              </span>
            </div>

            <p class="text-center text-white/50 text-xs md:text-sm mt-4">
              支持更多语言定制开发
            </p>
          </div>
        </div>

        <!-- 客户Logo占位 -->
        <div class="mt-12">
          <div class="flex items-center justify-center gap-3 mb-6">
            <i class="fa-solid fa-users text-gold"></i>
            <h3 class="text-lg md:text-xl font-semibold text-white">客户案例</h3>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4 md:gap-6">
            <div v-for="i in 5" :key="i"
                 class="bg-white/5 rounded-xl p-4 md:p-6 border border-white/10 hover:border-gold/30 transition-all duration-300 group hover:scale-105">
              <div class="relative h-10 md:h-12 flex items-center justify-center">
                <img :src="`https://picsum.photos/id/2${8+i}/120/60`"
                     alt="客户Logo"
                     class="h-full w-auto grayscale group-hover:grayscale-0 transition-all duration-300">
              </div>
              <p class="text-center text-white/60 text-xs mt-2 group-hover:text-white/80">合作伙伴</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 底部CTA - 增强图标和响应式 -->
    <section class="py-12 md:py-20 bg-gradient-to-br from-dark via-darkgray to-dark relative overflow-hidden">
      <!-- 背景装饰 -->
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute -top-20 -right-20 w-64 h-64 bg-gradient-to-br from-gold/5 to-transparent rounded-full blur-3xl"></div>
        <div class="absolute -bottom-20 -left-20 w-64 h-64 bg-gradient-to-tr from-gold/5 to-transparent rounded-full blur-3xl"></div>
      </div>

      <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10 max-w-4xl">
        <div class="flex flex-col items-center gap-4 mb-6 md:mb-8">
<!--          <div class="w-16 h-16 md:w-20 md:h-20 rounded-2xl bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center shadow-xl shadow-gold/30">-->
<!--            <i class="fa-solid fa-rocket text-gray-900 text-2xl md:text-3xl"></i>-->
<!--          </div>-->
          <h2 class="text-2xl sm:text-3xl md:text-[clamp(1.8rem,3vw,2.5rem)] font-bold ">
            开启跨境法务数字化转型
          </h2>
        </div>

        <p class="text-sm sm:text-base md:text-xl text-white/70 mb-6 md:mb-8 max-w-2xl mx-auto leading-relaxed">
          立即注册，免费生成1份跨境合同，体验AI合规审查服务，无需信用卡，无隐藏费用
        </p>

        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link to="/trial"
                       class="px-6 py-3 md:px-10 md:py-4 bg-gradient-to-r from-gold to-yellow-200 text-dark font-semibold rounded-lg hover:shadow-2xl hover:shadow-gold/40 transition-all duration-300 hover:scale-105 flex items-center justify-center gap-3 text-sm md:text-base">
            <i class="fa-solid fa-bolt"></i>
            免费试用 Legal-Guard
          </router-link>

          <router-link
            to="/price"
            class="px-6 py-3 md:px-8 md:py-4 bg-white/10 backdrop-blur-sm border border-white/20 text-white rounded-lg hover:bg-white/20 transition-all duration-300 hover:scale-105 flex items-center justify-center gap-3 text-sm md:text-base">
            <i class="fa-solid fa-comments-dollar"></i>
            查看定价方案
          </router-link>
        </div>

        <div class="mt-8 md:mt-10 grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-3xl mx-auto">
          <div class="flex items-center justify-center gap-2 text-white/60 text-xs md:text-sm">
            <i class="fa-solid fa-shield text-gold"></i>
            <span>数据安全加密</span>
          </div>
          <div class="flex items-center justify-center gap-2 text-white/60 text-xs md:text-sm">
            <i class="fa-solid fa-clock text-gold"></i>
            <span>7天免费试用</span>
          </div>
          <div class="flex items-center justify-center gap-2 text-white/60 text-xs md:text-sm">
            <i class="fa-solid fa-headset text-gold"></i>
            <span>专属客服支持</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 页脚 - 增强图标和响应式 -->
    <footer class="bg-darkgray py-8 md:py-12 border-t border-gold/10">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-8 mb-6 md:mb-8">
          <!-- Logo区域 -->
          <div>
            <div class="flex items-start gap-3 mb-3 md:mb-4">
              <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-gold to-yellow-200 flex items-center justify-center">
                <i class="fa-solid fa-shield-halved text-gray-900"></i>
              </div>
              <div class="flex-1 min-w-0 leading-tight">
              <span class="text-lg md:text-xl font-bold bg-gradient-to-r from-gold to-yellow-200 bg-clip-text text-transparent leading-none">
                Legal-Guard
              </span>
                <p class="text-xs text-white/40 leading-5 break-words">跨境小微企业的数字法务部</p>
              </div>
            </div>
            <p class="text-white/60 text-sm mb-4 md:mb-6">让合规更简单，让跨境更安心</p>

            <!-- 社交媒体 -->
            <div class="flex gap-3 text-white/60">
              <a href="#" class="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center hover:bg-gold hover:text-dark transition-all duration-300 group">
                <i class="fa-brands fa-weixin group-hover:scale-110"></i>
              </a>
              <a href="#" class="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center hover:bg-gold hover:text-dark transition-all duration-300 group">
                <i class="fa-solid fa-paper-plane group-hover:scale-110"></i>
              </a>
              <a href="#" class="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center hover:bg-gold hover:text-dark transition-all duration-300 group">
                <i class="fa-brands fa-github group-hover:scale-110"></i>
              </a>
              <a href="#" class="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center hover:bg-gold hover:text-dark transition-all duration-300 group">
                <i class="fa-brands fa-linkedin group-hover:scale-110"></i>
              </a>
            </div>
          </div>

          <!-- 产品 -->
          <div>
            <h4 class="text-base md:text-lg font-semibold mb-3 md:mb-4 flex items-center gap-2">
              <i class="fa-solid fa-box-open text-gold"></i>
              产品
            </h4>
            <ul class="space-y-2 text-white/60">
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-file-contract text-xs group-hover:translate-x-1 transition-transform"></i>
                  智能合同生成
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-shield-halved text-xs group-hover:translate-x-1 transition-transform"></i>
                  合规审查
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-user-tie text-xs group-hover:translate-x-1 transition-transform"></i>
                  专家咨询
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-link text-xs group-hover:translate-x-1 transition-transform"></i>
                  区块链存证
                </a>
              </li>
            </ul>
          </div>

          <!-- 资源 -->
          <div>
            <h4 class="text-base md:text-lg font-semibold mb-3 md:mb-4 flex items-center gap-2">
              <i class="fa-solid fa-book-open text-gold"></i>
              资源
            </h4>
            <ul class="space-y-2 text-white/60">
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-globe text-xs group-hover:translate-x-1 transition-transform"></i>
                  跨境合规指南
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-briefcase text-xs group-hover:translate-x-1 transition-transform"></i>
                  案例库
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-circle-question text-xs group-hover:translate-x-1 transition-transform"></i>
                  帮助中心
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-code text-xs group-hover:translate-x-1 transition-transform"></i>
                  API文档
                </a>
              </li>
            </ul>
          </div>

          <!-- 关于我们 -->
          <div>
            <h4 class="text-base md:text-lg font-semibold mb-3 md:mb-4 flex items-center gap-2">
              <i class="fa-solid fa-building text-gold"></i>
              关于我们
            </h4>
            <ul class="space-y-2 text-white/60">
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-circle-info text-xs group-hover:translate-x-1 transition-transform"></i>
                  公司介绍
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-envelope text-xs group-hover:translate-x-1 transition-transform"></i>
                  联系我们
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-user-shield text-xs group-hover:translate-x-1 transition-transform"></i>
                  隐私政策
                </a>
              </li>
              <li>
                <a href="#" class="text-sm hover:text-gold transition-colors flex items-center gap-2 group">
                  <i class="fa-solid fa-scale-balanced text-xs group-hover:translate-x-1 transition-transform"></i>
                  服务条款
                </a>
              </li>
            </ul>
          </div>
        </div>

        <!-- 底部版权 -->
        <div class="text-center text-white/40 text-xs md:text-sm pt-6 md:pt-8 border-t border-white/10">
          <div class="flex flex-col md:flex-row items-center justify-between gap-3">
            <p class="order-2 md:order-1">© 2025 Legal-Guard. 保留所有权利。</p>
            <div class="order-1 md:order-2 flex items-center gap-4">
              <a href="#" class="hover:text-white transition-colors text-xs">使用条款</a>
              <a href="#" class="hover:text-white transition-colors text-xs">隐私声明</a>
              <a href="#" class="hover:text-white transition-colors text-xs">Cookie政策</a>
            </div>
          </div>
        </div>
      </div>
    </footer>

    <!-- 回到顶部按钮（小人） -->
    <button
        id="back-to-top"
        aria-label="回到顶部"
        class="fixed bottom-6 right-4 sm:bottom-8 sm:right-8 w-16 h-16 sm:w-20 sm:h-24 bg-transparent p-2 flex items-center justify-center shadow-2xl shadow-gold/30 hover:-translate-y-1 hover:scale-105 transition-transform duration-200 z-50"
    >
      <img id="back-robot-img" src="/lg-robot.svg" alt="Legal-Guard 小人" class="w-full h-full object-contain" />
      <i id="back-arrow" class="fa-solid fa-arrow-up text-gold hidden" aria-hidden="true" style="font-size:1.25rem"></i>
    </button>
  </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue'
import { onMounted, onBeforeUnmount } from 'vue'

// 回到顶部功能
function showArrow() {
  const robotImg = document.getElementById('back-robot-img')
  const arrow = document.getElementById('back-arrow')
  if (robotImg) robotImg.style.display = 'none'
  if (arrow) arrow.classList.remove('hidden')
}

function checkScroll() {
  const btn = document.getElementById('back-to-top')
  if (!btn) return

  const scrolled = document.documentElement.scrollTop || document.body.scrollTop
  if (scrolled > 300) {
    btn.style.opacity = '1'
    btn.style.pointerEvents = 'auto'
  } else {
    btn.style.opacity = '0'
    btn.style.pointerEvents = 'none'
  }
}

// 鼠标悬停效果
const initHoverEffects = () => {
  const cards = document.querySelectorAll('.group')
  cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const icon = card.querySelector('.fa-arrow-right')
      if (icon) {
        icon.style.transform = 'translateX(4px)'
      }
    })
    card.addEventListener('mouseleave', () => {
      const icon = card.querySelector('.fa-arrow-right')
      if (icon) {
        icon.style.transform = 'translateX(0)'
      }
    })
  })
}

onMounted(() => {
  // 回到顶部按钮
  const robotImg = document.getElementById('back-robot-img')
  const arrow = document.getElementById('back-arrow')
  if (robotImg) {
    robotImg.addEventListener('error', showArrow)
    robotImg.addEventListener('load', () => {
      if (arrow) arrow.classList.add('hidden')
    })
  }

  const btn = document.getElementById('back-to-top')
  if (btn) {
    btn.style.opacity = '0'
    btn.style.pointerEvents = 'none'
    btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }))
  }

  document.addEventListener('scroll', checkScroll, { passive: true })
  checkScroll()

  // 初始化悬停效果
  initHoverEffects()
})

onBeforeUnmount(() => {
  document.removeEventListener('scroll', checkScroll)
})
</script>


<!--<template>-->
<!--  <div class="bg-dark text-white font-sans">-->
<!--    &lt;!&ndash; 导航栏 &ndash;&gt;-->
<!--    <nav class="bg-darkgray/80 backdrop-blur-md fixed w-full z-50 border-b border-gold/20">-->
<!--      <div class="container mx-auto px-6 py-4 flex justify-between items-center max-w-7xl">-->
<!--        &lt;!&ndash; Logo &ndash;&gt;-->
<!--        <div class="flex items-center gap-2">-->
<!--          <i class="fa-solid fa-shield-halved text-gold text-2xl"></i>-->
<!--          <span class="text-2xl font-bold text-gold">Legal-Guard</span>-->
<!--        </div>-->
<!--        &lt;!&ndash; 导航菜单（桌面端） &ndash;&gt;-->
<!--&lt;!&ndash;        <div class="hidden md:flex items-center gap-8">&ndash;&gt;-->
<!--&lt;!&ndash;          <a href="#" class="text-white hover:text-gold transition-colors">首页</a>&ndash;&gt;-->
<!--&lt;!&ndash;          <a href="#" class="text-white/80 hover:text-gold transition-colors">核心功能</a>&ndash;&gt;-->
<!--&lt;!&ndash;          <a href="#" class="text-white/80 hover:text-gold transition-colors">跨境案例</a>&ndash;&gt;-->
<!--&lt;!&ndash;          <a href="#" class="text-white/80 hover:text-gold transition-colors">定价方案</a>&ndash;&gt;-->
<!--&lt;!&ndash;          <a href="#" class="text-white/80 hover:text-gold transition-colors">帮助中心</a>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--        &lt;!&ndash; 导航菜单（桌面端） &ndash;&gt;-->
<!--        <div class="hidden md:flex items-center gap-8">-->
<!--          <a href="#" class="text-white hover:text-gold transition-colors">-->
<!--            <i class="fa-solid fa-house-chimney mr-1"></i> 首页-->
<!--          </a>-->
<!--          <a href="#" class="text-white/80 hover:text-gold transition-colors">-->
<!--            <i class="fa-solid fa-star mr-1"></i> 核心功能-->
<!--          </a>-->
<!--          <a href="#" class="text-white/80 hover:text-gold transition-colors">-->
<!--            <i class="fa-solid fa-globe mr-1"></i> 跨境案例-->
<!--          </a>-->
<!--          <a href="#" class="text-white/80 hover:text-gold transition-colors">-->
<!--            <i class="fa-solid fa-tags mr-1"></i> 定价方案-->
<!--          </a>-->
<!--          <a href="#" class="text-white/80 hover:text-gold transition-colors">-->
<!--            <i class="fa-solid fa-circle-question mr-1"></i> 帮助中心-->
<!--          </a>-->
<!--        </div>-->

<!--        &lt;!&ndash; 登录/注册按钮 &ndash;&gt;-->
<!--        <div class="flex items-center gap-4">-->
<!--          <a href="#" class="px-4 py-2 text-white/80 hover:text-gold transition-colors">登录</a>-->
<!--          <a href="#" class="px-6 py-2 bg-gold text-dark font-medium rounded-md hover:bg-gold/90 transition-colors shadow-lg shadow-gold/20">免费注册</a>-->
<!--        </div>-->
<!--        &lt;!&ndash; 移动端菜单按钮 &ndash;&gt;-->
<!--        <button class="md:hidden text-white text-xl">-->
<!--          <i class="fa-solid fa-bars"></i>-->
<!--        </button>-->
<!--      </div>-->
<!--    </nav>-->

<!--    &lt;!&ndash; 英雄区（Hero Section） &ndash;&gt;-->
<!--    <section class="pt-32 pb-20 bg-gradient-gold-dark">-->
<!--      <div class="container mx-auto px-6 flex flex-col md:flex-row items-center gap-10 max-w-7xl">-->
<!--        <div class="md:w-1/2 lg:w-6/12 space-y-6">-->
<!--          <div class="flex items-center gap-3">-->
<!--            <i class="fa-solid fa-shield-halved text-gold text-3xl"></i>-->
<!--            <h1 class="text-[clamp(2.2rem,4.5vw,4.5rem)] lg:text-[5rem] font-bold leading-tight text-gold text-shadow-gold">-->
<!--              小微企业的数字法务部-->
<!--            </h1>-->
<!--          </div>-->
<!--          <h2 class="mt-2 text-[clamp(1.0rem,2.5vw,1.75rem)] font-semibold text-white">跨境合同AI生成+合规审查</h2>-->
<!--          <p class="text-base lg:text-lg leading-relaxed text-white/70 max-w-lg">-->
<!--            10分钟生成符合目标国法规的合同，法务成本直降90%，覆盖28个主要贸易国合规标准-->
<!--          </p>-->
<!--          <div class="flex flex-wrap gap-4 pt-4">-->
<!--            <router-link to="/trial" class="px-8 py-3 bg-gold text-dark font-semibold rounded-md hover:bg-gold/90 transition-colors shadow-lg shadow-gold/30 hover-scale">-->
<!--              免费试用（生成1份合同）-->
<!--            </router-link>-->
<!--            <a href="#" class="px-8 py-3 border border-gold/50 text-gold rounded-md hover:bg-gold/10 transition-colors hover-scale">-->
<!--              <i class="fa-solid fa-play-circle mr-1"></i> 查看演示视频-->
<!--            </a>-->
<!--          </div>-->
<!--          <div class="flex items-center gap-4 pt-2 text-white/60 text-sm">-->
<!--            <span><i class="fa-solid fa-check-circle text-gold mr-1"></i> 无需信用卡</span>-->
<!--            <span><i class="fa-solid fa-check-circle text-gold mr-1"></i> 区块链存证</span>-->
<!--            <span><i class="fa-solid fa-check-circle text-gold mr-1"></i> 数据加密</span>-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash; 英雄区插图 &ndash;&gt;-->
<!--        <div class="md:w-1/2 lg:w-6/12 aspect-[16/9] lg:aspect-[4/3] rounded-xl overflow-hidden shadow-2xl shadow-gold/10">-->
<!--          <img src="https://p0.ssl.qhimgs1.com/t04b97659f1c3035604.jpg" alt="跨境合同智能生成演示" class="w-full h-full object-cover" />-->
<!--        </div>-->
<!--      </div>-->
<!--    </section>-->

<!--    &lt;!&ndash; 核心功能区 &ndash;&gt;-->
<!--    <section class="py-20 bg-dark">-->
<!--      <div class="container mx-auto px-6 max-w-7xl">-->
<!--        <div class="text-center mb-16">-->
<!--          <h2 class="text-[clamp(1.8rem,3vw,2.5rem)] font-bold">核心功能 · 解决跨境法务痛点</h2>-->
<!--        </div>-->
<!--        &lt;!&ndash; 功能卡片（对齐 demo.html 的 icon+img 同容器布局） &ndash;&gt;-->
<!--        <div class="grid md:grid-cols-3 gap-8">-->
<!--          <div class="bg-lightgray rounded-xl p-8 border border-gold/10 hover-scale shadow-lg shadow-dark/50">-->
<!--            <div class="w-25 h-25 bg-gold/10 rounded-lg flex items-center justify-center mb-6 overflow-hidden">-->
<!--              <i class="fa-solid fa-file-contract text-gold text-2xl"></i>-->
<!--              <img-->
<!--                src="https://pic.52112.com/2020/01/06/JPG-200106_13/xeBpEnZdQA_small.jpg"-->
<!--                alt="智能合同生成示意"-->
<!--                class="w-full h-full object-cover"-->
<!--              />-->
<!--            </div>-->
<!--            <h3 class="text-gold text-xl font-semibold mb-2">智能合同生成</h3>-->
<!--            <p class="text-white/70">-->
<!--              输入业务需求，AI自动匹配目标法域模板，10分钟生成标准化跨境合同，支持自定义条款补充。-->
<!--            </p>-->
<!--          </div>-->

<!--          <div class="bg-lightgray rounded-xl p-8 border border-gold/10 hover-scale shadow-lg shadow-dark/50">-->
<!--            <div class="w-25 h-25 bg-gold/10 rounded-lg flex items-center justify-center mb-6 overflow-hidden">-->
<!--              <i class="fa-solid fa-shield-virus text-gold text-2xl"></i>-->
<!--              <img-->
<!--                src="https://p0.ssl.qhimgs1.com/sdr/400__/t03191cd514ba3946d6.jpg"-->
<!--                alt="合规审查示意"-->
<!--                class="w-full h-full object-cover"-->
<!--              />-->
<!--            </div>-->
<!--            <h3 class="text-gold text-xl font-semibold mb-2">AI合规审查</h3>-->
<!--            <p class="text-white/70">-->
<!--              区块链存证+风险智能标注，高风险条款红色预警，自动提供合规修改建议，降低跨境法律风险。-->
<!--            </p>-->
<!--          </div>-->

<!--          <div class="bg-lightgray rounded-xl p-8 border border-gold/10 hover-scale shadow-lg shadow-dark/50">-->
<!--            <div class="w-25 h-25 bg-gold/10 rounded-lg flex items-center justify-center mb-6 overflow-hidden">-->
<!--              <i class="fa-solid fa-user-tie text-gold text-2xl"></i>-->
<!--              <img-->
<!--                src="https://p0.ssl.qhimgs1.com/sdr/400__/t01b434b3c4c3f288e0.jpg"-->
<!--                alt="专家咨询示意"-->
<!--                class="w-full h-full object-cover"-->
<!--              />-->
<!--            </div>-->
<!--            <h3 class="text-gold text-xl font-semibold mb-2">专家咨询通道</h3>-->
<!--            <p class="text-white/70">-->
<!--              疑难条款匹配专属跨境法律专家，1v1定制化解决方案，响应时间≤4小时，覆盖28个贸易国法域。-->
<!--            </p>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </section>-->

<!--    &lt;!&ndash; 信任背书区 &ndash;&gt;-->
<!--    <section class="py-20 bg-darkgray">-->
<!--      <div class="container mx-auto px-6 max-w-7xl">-->
<!--        <div class="text-center mb-12 flex items-center justify-center gap-3">-->
<!--          <i class="fa-solid fa-handshake-simple text-gold"></i>-->
<!--          <h2 class="text-[clamp(1.8rem,3vw,2.5rem)] font-bold">值得跨境企业信赖</h2>-->
<!--        </div>-->
<!--        <div class="grid md:grid-cols-2 gap-10 mb-16">-->
<!--          <div class="bg-dark rounded-xl p-8 border border-gold/10">-->
<!--            <div class="grid grid-cols-2 gap-8">-->
<!--              <div class="text-center">-->
<!--                <p class="text-5xl font-bold text-gold">6300+</p>-->
<!--                <p class="text-white/70 mt-2">服务跨境小微企业</p>-->
<!--              </div>-->
<!--              <div class="text-center">-->
<!--                <p class="text-5xl font-bold text-gold">28</p>-->
<!--                <p class="text-white/70 mt-2">覆盖贸易国法域</p>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="bg-dark rounded-xl p-8 border border-gold/10">-->
<!--            <h3 class="text-xl font-semibold mb-4 text-center">多语言合规适配</h3>-->
<!--            <div class="flex flex-wrap justify-center gap-4 text-lg">-->
<!--              <span class="px-4 py-2 bg-lightgray rounded-md">简体中文</span>-->
<!--              <span class="px-4 py-2 bg-lightgray rounded-md">English</span>-->
<!--              <span class="px-4 py-2 bg-lightgray rounded-md">Español</span>-->
<!--              <span class="px-4 py-2 bg-lightgray rounded-md">Français</span>-->
<!--              <span class="px-4 py-2 bg-lightgray rounded-md">Deutsch</span>-->
<!--              <span class="px-4 py-2 bg-lightgray rounded-md">日本語</span>-->
<!--              <span class="px-4 py-2 bg-gold/20 text-gold rounded-md">+6种语言</span>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="flex flex-wrap justify-center items-center gap-12 opacity-70">-->
<!--          <div class="text-2xl font-semibold text-white/50">客户案例</div>-->
<!--          <img src="https://picsum.photos/id/29/120/60" alt="客户Logo" class="h-10 grayscale" />-->
<!--          <img src="https://picsum.photos/id/30/120/60" alt="客户Logo" class="h-10 grayscale" />-->
<!--          <img src="https://picsum.photos/id/31/120/60" alt="客户Logo" class="h-10 grayscale" />-->
<!--          <img src="https://picsum.photos/id/32/120/60" alt="客户Logo" class="h-10 grayscale" />-->
<!--          <img src="https://picsum.photos/id/33/120/60" alt="客户Logo" class="h-10 grayscale" />-->
<!--        </div>-->
<!--      </div>-->
<!--    </section>-->

<!--    &lt;!&ndash; 底部CTA &ndash;&gt;-->
<!--    <section class="py-20 bg-gradient-gold-dark">-->
<!--      <div class="container mx-auto px-6 text-center max-w-7xl">-->
<!--        <div class="flex items-center justify-center gap-3 mb-6">-->
<!--          <i class="fa-solid fa-rocket text-gold"></i>-->
<!--          <h2 class="text-[clamp(1.8rem,3vw,2.5rem)] font-bold">开启跨境法务数字化转型</h2>-->
<!--        </div>-->
<!--        <p class="text-xl text-white/70 mb-8 max-w-2xl mx-auto">-->
<!--          立即注册，免费生成1份跨境合同，体验AI合规审查服务，无需信用卡，无隐藏费用-->
<!--        </p>-->
<!--        <router-link to="/trial" class="px-10 py-4 bg-gold text-dark font-semibold rounded-md hover:bg-gold/90 transition-colors shadow-lg shadow-gold/30 text-lg hover-scale">-->
<!--          免费试用 Legal-Guard-->
<!--        </router-link>-->
<!--      </div>-->
<!--    </section>-->

<!--    &lt;!&ndash; 页脚 &ndash;&gt;-->
<!--    <footer class="bg-darkgray py-12 border-t border-gold/10">-->
<!--      <div class="container mx-auto px-6 max-w-7xl">-->
<!--        <div class="grid md:grid-cols-4 gap-8 mb-8">-->
<!--          <div>-->
<!--            <div class="flex items-center gap-2 mb-4">-->
<!--              <i class="fa-solid fa-shield-halved text-gold text-xl"></i>-->
<!--              <span class="text-xl font-bold text-gold">Legal-Guard</span>-->
<!--            </div>-->
<!--            <p class="text-white/60 mb-4">跨境小微企业的数字法务部，让合规更简单</p>-->
<!--            <div class="flex gap-4 text-white/60">-->
<!--              &lt;!&ndash; 微信 &ndash;&gt;-->
<!--              <a href="#" class="hover:text-gold transition-colors" aria-label="微信">-->
<!--                <i class="fa-brands fa-weixin text-xl"></i>-->
<!--              </a>-->
<!--              &lt;!&ndash; 飞书：用纸飞机代替 &ndash;&gt;-->
<!--              <a href="#" class="hover:text-gold transition-colors" aria-label="飞书">-->
<!--                <i class="fa-solid fa-paper-plane text-xl"></i>-->
<!--              </a>-->
<!--              &lt;!&ndash; GitHub &ndash;&gt;-->
<!--              <a href="#" class="hover:text-gold transition-colors" aria-label="GitHub">-->
<!--                <i class="fa-brands fa-github text-xl"></i>-->
<!--              </a>-->
<!--            </div>-->
<!--          </div>-->
<!--          <div>-->
<!--            <h4 class="text-lg font-semibold mb-4 flex items-center gap-2">-->
<!--              <i class="fa-solid fa-box-open text-gold"></i>-->
<!--              产品-->
<!--            </h4>-->
<!--            <ul class="space-y-2 text-white/60">-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-file-contract mr-2"></i> 智能合同生成</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-shield-halved mr-2"></i> 合规审查</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-user-tie mr-2"></i> 专家咨询</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-link mr-2"></i> 区块链存证</a></li>-->
<!--            </ul>-->
<!--          </div>-->
<!--          <div>-->
<!--            <h4 class="text-lg font-semibold mb-4 flex items-center gap-2">-->
<!--              <i class="fa-solid fa-book-open text-gold"></i>-->
<!--              资源-->
<!--            </h4>-->
<!--            <ul class="space-y-2 text-white/60">-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-globe mr-2"></i> 跨境合规指南</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-briefcase mr-2"></i> 案例库</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-circle-question mr-2"></i> 帮助中心</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-code mr-2"></i> API文档</a></li>-->
<!--            </ul>-->
<!--          </div>-->
<!--          <div>-->
<!--            <h4 class="text-lg font-semibold mb-4 flex items-center gap-2">-->
<!--              <i class="fa-solid fa-building text-gold"></i>-->
<!--              关于我们-->
<!--            </h4>-->
<!--            <ul class="space-y-2 text-white/60">-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-circle-info mr-2"></i> 公司介绍</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-envelope mr-2"></i> 联系我们</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-user-shield mr-2"></i> 隐私政策</a></li>-->
<!--              <li><a href="#" class="hover:text-gold transition-colors"><i class="fa-solid fa-scale-balanced mr-2"></i> 服务条款</a></li>-->
<!--            </ul>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="text-center text-white/40 text-sm pt-8 border-t border-white/10">© 2025 Legal-Guard. 保留所有权利。</div>-->
<!--      </div>-->
<!--    </footer>-->

<!--    &lt;!&ndash; 回到顶部按钮（小人） &ndash;&gt;-->
<!--    <button-->
<!--      id="back-to-top"-->
<!--      aria-label="回到顶部"-->
<!--      class="fixed bottom-8 right-8 w-24 h-24 bg-transparent p-2 flex items-center justify-center shadow-2xl shadow-gold/30 hover:-translate-y-1 hover:scale-105 transition-transform duration-200 z-50"-->
<!--    >-->
<!--      <img id="back-robot-img" src="/lg-robot.svg" alt="Legal-Guard 小人" class="w-[92%] h-[92%] object-contain" />-->
<!--      <i id="back-arrow" class="fa-solid fa-arrow-up text-gold hidden" aria-hidden="true" style="font-size:1.25rem"></i>-->
<!--    </button>-->
<!--  </div>-->
<!--</template>-->

<!--<script setup>-->
<!--import { onMounted, onBeforeUnmount } from 'vue'-->

<!--function showArrow() {-->
<!--  const robotImg = document.getElementById('back-robot-img')-->
<!--  const arrow = document.getElementById('back-arrow')-->
<!--  if (robotImg) robotImg.style.display = 'none'-->
<!--  if (arrow) arrow.classList.remove('hidden')-->
<!--}-->

<!--function checkScroll() {-->
<!--  const btn = document.getElementById('back-to-top')-->
<!--  if (!btn) return-->

<!--  const scrolled = document.documentElement.scrollTop || document.body.scrollTop-->
<!--  if (scrolled > 300) {-->
<!--    btn.style.opacity = '1'-->
<!--    btn.style.pointerEvents = 'auto'-->
<!--  } else {-->
<!--    btn.style.opacity = '0'-->
<!--    btn.style.pointerEvents = 'none'-->
<!--  }-->
<!--}-->

<!--onMounted(() => {-->
<!--  const robotImg = document.getElementById('back-robot-img')-->
<!--  const arrow = document.getElementById('back-arrow')-->
<!--  if (robotImg) {-->
<!--    robotImg.addEventListener('error', showArrow)-->
<!--    robotImg.addEventListener('load', () => {-->
<!--      if (arrow) arrow.classList.add('hidden')-->
<!--    })-->
<!--  }-->

<!--  const btn = document.getElementById('back-to-top')-->
<!--  if (btn) {-->
<!--    btn.style.opacity = '0'-->
<!--    btn.style.pointerEvents = 'none'-->
<!--    btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }))-->
<!--  }-->

<!--  document.addEventListener('scroll', checkScroll, { passive: true })-->
<!--  checkScroll()-->
<!--})-->

<!--onBeforeUnmount(() => {-->
<!--  document.removeEventListener('scroll', checkScroll)-->
<!--})-->
<!--</script>-->

<!--<style src="./demo.css" scoped></style>-->
