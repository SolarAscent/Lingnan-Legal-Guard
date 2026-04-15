<template>
  <div class="cases-page bg-dark text-white font-sans min-h-screen">
    <Navbar />

    <!-- 顶部导航扩展区：搜索条 -->
    <section class="cases-top">
      <div class="cases-top-inner">
        <!-- 左侧：标题与说明 -->
        <div class="cases-top-left">
<!--          <p class="cases-top-label">核心案例 · Legal-Guard</p>-->
          <h1 class="cases-top-title">快速找到与你业务相似的跨境合同成功案例</h1>
          <p class="cases-top-desc">通过关键词搜索与精选案例，让跨境合规路径一目了然。</p>
        </div>

        <!-- 中间：搜索模块 -->
        <div class="cases-search-bar">
          <div class="cases-search-input-wrap" :class="{ 'is-loading': searchLoading }">
            <i class="fa-solid fa-magnifying-glass cases-search-icon"></i>
            <input
                v-model="searchQuery"
                type="text"
                class="cases-search-input"
                placeholder="搜索跨境合同案例（如：欧盟GDPR合规、SaaS跨境协议）"
                @input="onSearchInput"
                @keydown.enter.prevent="triggerSearch"
            />
            <button
                v-if="searchQuery"
                class="cases-search-clear"
                @click="clearSearch"
                aria-label="清空搜索"
            >
              ×
            </button>
            <button class="cases-search-btn" @click="triggerSearch">搜索</button>
            <span v-if="searchLoading" class="cases-search-loading">
              <i class="fa-solid fa-circle-notch fa-spin"></i>
            </span>
          </div>

          <!-- 联想词下拉 -->
          <ul v-if="showSuggestions" class="cases-suggest-list">
            <li
                v-for="item in filteredSuggestions"
                :key="item"
                class="cases-suggest-item"
                @click="applySuggestion(item)"
            >
              <i class="fa-solid fa-arrow-turn-up"></i>
              <span>{{ item }}</span>
            </li>
            <li v-if="!filteredSuggestions.length" class="cases-suggest-empty">
              无匹配联想词
            </li>
          </ul>

          <!-- 无结果提示 -->
          <p
              v-if="!searchLoading && searchDone && !matchedCases.length"
              class="cases-search-empty"
          >
            未找到该案例，试试这些关键词：
            <button
                v-for="hot in hotKeywords"
                :key="hot"
                class="cases-search-empty-chip"
                @click="applySuggestion(hot)"
            >
              {{ hot }}
            </button>
          </p>
        </div>

        <!-- 右侧：用户入口与试用按钮 -->
        <div class="cases-top-right">
          <button class="cases-user-btn" aria-label="用户中心">
            <i class="fa-solid fa-circle-user"></i>
          </button>
          <router-link to="/trial" class="cases-trial-btn">
            免费试用
          </router-link>
        </div>
      </div>
    </section>

    <!-- 热门关键词区域 -->
    <section class="cases-keywords">
      <div class="cases-keywords-inner">
        <div class="cases-keywords-header">
          <span class="cases-keywords-title">热门搜索关键词：</span>
        </div>
        <div class="cases-keywords-tags">
          <button
              v-for="tag in allKeywordTags"
              :key="tag"
              class="cases-keyword-tag"
              :class="{ active: tag === selectedKeyword }"
              @click="onKeywordClick(tag)"
          >
            {{ tag }}
          </button>
        </div>
      </div>
      <div class="cases-keywords-divider"></div>
    </section>

    <!-- 标杆案例介绍 -->
    <!--    <section class="cases-hero">-->
    <!--      <div class="cases-hero-inner">-->
    <!--        <div class="cases-hero-content">-->
    <!--          <p class="cases-hero-tag">标杆案例 · 欧盟市场合规突破</p>-->
    <!--          <h2 class="cases-hero-title">-->
    <!--            【标杆案例】某跨境SaaS企业欧盟市场合规突破-->
    <!--          </h2>-->
    <!--          <p class="cases-hero-sub">-->
    <!--            跨境SaaS服务商 · 目标市场：欧盟27国 · 痛点：数据跨境传输不合规、多语言合同适配难-->
    <!--          </p>-->

    <!--          <ul class="cases-hero-highlights">-->
    <!--            <li>-->
    <!--              <span class="label">3天内完成</span>-->
    <!--              <span class="value">全量合规审查与关键条款优化</span>-->
    <!--            </li>-->
    <!--            <li>-->
    <!--              <span class="label">0起</span>-->
    <!--              <span class="value">合规纠纷，顺利通过当地合规审查</span>-->
    <!--            </li>-->
    <!--            <li>-->
    <!--              <span class="label">合同签署效率提升</span>-->
    <!--              <span class="value highlight">60%</span>-->
    <!--            </li>-->
    <!--          </ul>-->

    <!--          <div class="cases-hero-actions">-->
    <!--            <button class="cases-hero-btn primary" @click="viewBenchmarkDetail">-->
    <!--              查看完整案例-->
    <!--            </button>-->
    <!--            <button class="cases-hero-btn ghost" @click="viewSimilarCases">-->
    <!--              同类案例推荐-->
    <!--            </button>-->
    <!--          </div>-->
    <!--        </div>-->

    <!--        <div class="cases-hero-visual">-->
    <!--          <div class="cases-hero-globe">-->
    <!--            <div class="globe-core"></div>-->
    <!--            <div class="globe-orbit orbit-1"></div>-->
    <!--            <div class="globe-orbit orbit-2"></div>-->
    <!--            <div class="globe-dot dot-1"></div>-->
    <!--            <div class="globe-dot dot-2"></div>-->
    <!--          </div>-->
    <!--          <p class="cases-hero-caption">数据跨境 · 多法域合规 · 多语言合同适配</p>-->
    <!--        </div>-->
    <!--      </div>-->
    <!--    </section>-->

    <!-- 案例轮播图片区 -->
    <section class="cases-carousel">
      <div class="cases-carousel-header">
        <h3>典型跨境合同成功案例</h3>
        <p>按行业与法域维度精选，帮助你快速匹配相似业务场景。</p>
      </div>

      <div class="cases-carousel-body">
        <button
            class="cases-carousel-arrow left"
            @click="prevSlide"
            aria-label="上一组案例"
        >
          <i class="fa-solid fa-chevron-left"></i>
        </button>

        <div class="cases-carousel-viewport" ref="carouselViewport">
          <div
              class="cases-carousel-track"
              :style="trackStyle"
              @mousedown.prevent="onDragStart"
              @touchstart.passive="onDragStart"
          >
            <!-- 所有卡片统一用 cases-card-link 包裹，tech-export-us 使用真实 PDF 链接 -->
            <template v-for="(item, idx) in matchedCases" :key="item.id + '-' + idx">
              <a
                v-if="item.id === 'tech-export-us'"
                :href="techExportPdfPath"
                target="_blank"
                class="cases-card-link"
              >
                <article class="cases-card">
                  <div class="cases-card-img-wrap">
                    <img :src="item.image" :alt="item.title" class="cases-card-img" />
                    <div class="cases-card-img-border"></div>
                    <span v-if="item.hot" class="cases-card-hot">热门</span>
                  </div>
                  <div class="cases-card-content">
                    <h4 class="cases-card-title">{{ item.title }}</h4>
                    <p class="cases-card-desc">{{ item.highlight }}</p>
                  </div>
                </article>
              </a>

              <a
                v-else
                href="javascript:void(0)"
                class="cases-card-link"
                @click.prevent="openCaseDetail(item)"
              >
                <article class="cases-card">
                  <div class="cases-card-img-wrap">
                    <img :src="item.image" :alt="item.title" class="cases-card-img" />
                    <div class="cases-card-img-border"></div>
                    <span v-if="item.hot" class="cases-card-hot">热门</span>
                  </div>
                  <div class="cases-card-content">
                    <h4 class="cases-card-title">{{ item.title }}</h4>
                    <p class="cases-card-desc">{{ item.highlight }}</p>
                  </div>
                </article>
              </a>
            </template>
          </div>
        </div>

        <button
            class="cases-carousel-arrow right"
            @click="nextSlide"
            aria-label="下一组案例"
        >
          <i class="fa-solid fa-chevron-right"></i>
        </button>
      </div>

      <div class="cases-carousel-dots">
        <button
            v-for="(dot, i) in pageCount"
            :key="i"
            class="cases-dot"
            :class="{ active: i === currentPage }"
            @click="goToPage(i)"
        ></button>
      </div>
    </section>

    <!-- 底部引导区 -->
    <section class="cases-cta">
      <div class="cases-cta-inner">
        <p class="cases-cta-title">
          查看更多跨境合同成功案例，获取专属合规解决方案
        </p>
        <div class="cases-cta-actions">
          <button class="cases-cta-btn primary" @click="viewAllCases">
            查看全部案例
          </button>
          <router-link to="/trial" class="cases-cta-btn ghost">
            免费定制方案
          </router-link>
        </div>
      </div>
      <div class="cases-cta-divider"></div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import './core-cases.css'

// 搜索相关状态
const searchQuery = ref('')
const searchLoading = ref(false)
const searchDone = ref(false)
const selectedKeyword = ref('')

// 关键词 / 联想词
const hotKeywords = [
  '欧盟GDPR合规',
  '美国关税协议',
  '东盟分销合规',
  '中日数据跨境',
  'SaaS跨境服务协议',
  '跨境分销合作',
  '国际NDA保密协议',
  '数据跨境整改',
  '关税条款优化',
  '跨境纠纷规避',
]

const allKeywordTags = hotKeywords
const allSuggestions = hotKeywords

const showSuggestions = computed(
    () => searchQuery.value.length >= 3 && !searchLoading.value,
)

const filteredSuggestions = computed(() => {
  const q = searchQuery.value.trim()
  if (q.length < 3) return []
  return allSuggestions.filter((s) =>
      s.toLowerCase().includes(q.toLowerCase()),
  )
})

// 案例数据（前端 mock）
const allCases = ref([
  {
    id: 'asean-distribution',
    title: '跨境分销协议 · 东盟关税合规',
    highlight: '解决关税承担争议，整体跨境成本降低 20%。',
    image: 'https://picsum.photos/id/1015/480/320',
    tags: ['东盟分销合规', '关税条款优化'],
    hot: true,
  },
  {
    id: 'nda-japan',
    title: 'NDA保密协议 · 中日技术合作',
    highlight: '适配日本数据保密法规，保障核心算法与技术安全。',
    image: 'https://picsum.photos/id/1011/480/320',
    tags: ['国际NDA保密协议', '中日数据跨境'],
    hot: true,
  },
  {
    id: 'saas-eu',
    title: 'SaaS跨境服务协议 · 欧盟GDPR',
    highlight: '全面纳入 GDPR 条款，合规上线 27 国本地化服务。',
    image: 'https://picsum.photos/id/1019/480/320',
    tags: ['欧盟GDPR合规', 'SaaS跨境服务协议'],
    hot: true,
  },
  {
    id: 'us-tariff',
    title: '跨境供货合同 · 美国关税协议',
    highlight: '明确关税承担与汇率风险分配，减少结算争议。',
    image: 'https://picsum.photos/id/1025/480/320',
    tags: ['美国关税协议', '关税条款优化'],
    hot: false,
  },
  {
    id: 'data-remedy',
    title: '数据跨境整改 · 多法域合规',
    highlight: '构建统一数据跨境策略，覆盖欧盟、美国及东盟。',
    image: 'https://picsum.photos/id/1027/480/320',
    tags: ['数据跨境整改', '跨境纠纷规避'],
    hot: false,
  },
  {
    id: 'dispute-avoid',
    title: '销售代理协议 · 跨境纠纷规避',
    highlight: '预先设计争议解决条款，将潜在纠纷扼杀在源头。',
    image: 'https://picsum.photos/id/1035/480/320',
    tags: ['跨境纠纷规避'],
    hot: false,
  },
  {
    id: 'tech-export-us',
    title: '技术出海合规 · 美国出口管制',
    highlight: '应对EAR管制，保障软件与技术服务顺利出海。',
    image: 'https://picsum.photos/id/1051/480/320',
    tags: ['美国关税协议', '跨境纠纷规避'],
    hot: false,
  },
  {
    id: 'ecommerce-latam',
    title: '电商平台协议 · 拉美市场',
    highlight: '适配多国电商法规，有效规避平台运营与税务风险。',
    image: 'https://picsum.photos/id/1053/480/320',
    tags: ['跨境分销合作'],
    hot: true,
  },
  {
    id: 'privacy-lgpd-brazil',
    title: '个人信息保护 · 巴西LGPD',
    highlight: '遵从巴西《通用数据保护法》，安全处理本地用户数据。',
    image: 'https://picsum.photos/id/1054/480/320',
    tags: ['数据跨境整改'],
    hot: false,
  },
  {
    id: 'sw-license-india',
    title: '国际软件许可 · 印度市场',
    highlight: '设计符合印度法律的软件许可模式与税务结构。',
    image: 'https://picsum.photos/id/1055/480/320',
    tags: ['SaaS跨境服务协议'],
    hot: false,
  },
])

// 将 PDF 常量路径添加在顶层，便于模板绑定使用
const techExportPdfPath = '/pdf/CISG-online 7501.pdf'

// 根据搜索词 / 标签过滤
const matchedCases = computed(() => {
  const q = searchQuery.value.trim()
  const tag = selectedKeyword.value
  if (!q && !tag) return allCases.value

  return allCases.value.filter((c) => {
    const text = `${c.title} ${c.highlight} ${c.tags.join(' ')}`
    const matchQuery = q
        ? text.toLowerCase().includes(q.toLowerCase())
        : true
    const matchTag = tag ? c.tags.includes(tag) : true
    return matchQuery && matchTag
  })
})

// 轮播相关
const carouselViewport = ref(null)
const currentPage = ref(0)
const autoTimer = ref(null)

// 不同设备上一页展示多少张
const cardsPerPage = ref(4)

const updateCardsPerPage = () => {
  const width = window.innerWidth
  if (width < 640) cardsPerPage.value = 1
  else if (width < 1024) cardsPerPage.value = 2
  else cardsPerPage.value = 4
}

const pageCount = computed(() => {
  const total = matchedCases.value.length
  return total === 0 ? 1 : Math.ceil(total / cardsPerPage.value)
})

const visibleCases = computed(() => {
  const start = currentPage.value * cardsPerPage.value
  return matchedCases.value.slice(start, start + cardsPerPage.value)
})

const trackStyle = computed(() => {
  const offset = currentPage.value * (100 / pageCount.value)
  return {
    transform: `translateX(-${offset}%)`,
    width: `${pageCount.value * 100}%`,
  }
})

const goToPage = (i) => {
  if (i < 0 || i >= pageCount.value) return
  currentPage.value = i
  pauseAutoPlay()
}

const nextSlide = () => {
  if (pageCount.value <= 1) return
  currentPage.value = (currentPage.value + 1) % pageCount.value
  pauseAutoPlay()
}

const prevSlide = () => {
  if (pageCount.value <= 1) return
  currentPage.value =
      (currentPage.value - 1 + pageCount.value) % pageCount.value
  pauseAutoPlay()
}

const startAutoPlay = () => {
  clearInterval(autoTimer.value)
  autoTimer.value = setInterval(() => {
    if (pageCount.value <= 1) return
    currentPage.value = (currentPage.value + 1) % pageCount.value
  }, 5000)
}

const pauseAutoPlay = () => {
  clearInterval(autoTimer.value)
  autoTimer.value = null
}

// 简单拖拽占位：这里只触发暂停轮播
const onDragStart = () => {
  pauseAutoPlay()
}

// 搜索交互函数
let searchTimer

const onSearchInput = () => {
  searchDone.value = false
  if (searchTimer) clearTimeout(searchTimer)
  searchTimer = setTimeout(() => {
    if (searchQuery.value.trim().length === 0) {
      searchLoading.value = false
    }
  }, 200)
}

const triggerSearch = () => {
  searchLoading.value = true
  searchDone.value = false

  setTimeout(() => {
    searchLoading.value = false
    searchDone.value = true
    currentPage.value = 0
  }, 500)
}

const clearSearch = () => {
  searchQuery.value = ''
  searchDone.value = false
  selectedKeyword.value = ''
  currentPage.value = 0
}

const applySuggestion = (text) => {
  searchQuery.value = text
  selectedKeyword.value = text
  triggerSearch()
}

const onKeywordClick = (tag) => {
  if (selectedKeyword.value === tag) {
    selectedKeyword.value = ''
  } else {
    selectedKeyword.value = tag
    searchQuery.value = tag
  }
  triggerSearch()
}

const router = useRouter()

const openCaseDetail = (item) => {
  // 预留详情页路由
  console.log('open case detail', item.id)
}

const viewBenchmarkDetail = () => {
  console.log('view benchmark detail')
}

const viewSimilarCases = () => {
  selectedKeyword.value = 'SaaS跨境服务协议'
  searchQuery.value = selectedKeyword.value
  triggerSearch()
}

const viewAllCases = () => {
  console.log('查看全部案例')
}

onMounted(() => {
  updateCardsPerPage()
  window.addEventListener('resize', updateCardsPerPage)
  startAutoPlay()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateCardsPerPage)
  clearInterval(autoTimer.value)
  if (searchTimer) clearTimeout(searchTimer)
})
</script>
