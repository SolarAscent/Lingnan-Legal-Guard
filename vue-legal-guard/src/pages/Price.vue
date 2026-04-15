<template>
  <div class="price-page">
    <Navbar />

    <!-- 顶部价值引导区（整体靠上，与首页一致由 App 的 padding 控制距离） -->
    <section class="price-hero">
      <div class="price-hero-inner">
        <div class="price-hero-text">
          <p class="price-hero-tag">定价方案 · Legal-Guard</p>
          <h1 class="price-hero-title">跨境法务数字化，按需求灵活付费</h1>
          <p class="price-hero-subtitle">
            比传统法律顾问成本直降90%，覆盖28个贸易国法域合规需求，按需选择更省心
          </p>
          <div class="price-hero-actions">
            <div class="billing-toggle">
              <span :class="{ 'active': billingMode === 'monthly' }" @click="billingMode = 'monthly'">月付</span>
              <span :class="{ 'active': billingMode === 'yearly' }" @click="billingMode = 'yearly'">
                年付
                <span class="billing-tag">立省2个月费用</span>
              </span>
            </div>
            <p class="billing-desc">支持随时升级套餐，按团队规模灵活扩展</p>
          </div>
        </div>
        <div class="price-hero-visual">
          <div class="globe-wrap">
            <div class="globe"></div>
            <div class="globe-orbit globe-orbit-1"></div>
            <div class="globe-orbit globe-orbit-2"></div>
            <div class="globe-orbit-dot globe-orbit-dot-1"></div>
            <div class="globe-orbit-dot globe-orbit-dot-2"></div>
          </div>
          <p class="globe-caption">跨境合同 · 多法域合规 · 一站式数字化管理</p>
        </div>
      </div>
      <div class="price-hero-divider"></div>
    </section>

    <!-- 核心套餐展示区：作为第二块内容，保持当前间距即可 -->
    <section class="price-plans" aria-label="定价套餐">
      <div class="price-plans-grid">
        <!-- 基础版 -->
        <article class="plan-card plan-basic">
          <header class="plan-header">
            <h2 class="plan-name">基础版 · 免费试用</h2>
            <p class="plan-desc">适合初创跨境小微企业，先用起来再升级</p>
            <p class="plan-price">
              <span class="plan-price-main">¥0</span>
              <span class="plan-price-period">/ 永久</span>
            </p>
          </header>
          <ul class="plan-features">
            <li>1份/月 跨境合同AI生成（支持中/美/欧3个主流法域）</li>
            <li>基础合规风险检测（仅标注高风险条款）</li>
            <li>合同PDF导出（无水印）</li>
            <li>单账号使用，基础区块链存证</li>
          </ul>
          <footer class="plan-footer">
            <p class="plan-scenario">适用场景：初创跨境小微企业，每月跨境合同量≤1份，需基础合规校验</p>
            <button class="plan-btn plan-btn-outline" type="button">立即激活</button>
          </footer>
        </article>

        <!-- 标准版（主推） -->
        <article class="plan-card plan-standard">
          <div class="plan-badge">主推</div>
          <header class="plan-header">
            <h2 class="plan-name">标准版 · 成长企业首选</h2>
            <p class="plan-desc">覆盖28个贸易国法域的全流程跨境合规护航</p>
            <!-- 新增条形计费切换器（更明显） -->
            <div class="billing-switch">
              <button :class="{ active: billingMode === 'monthly' }" @click="billingMode = 'monthly'">月付</button>
              <button :class="{ active: billingMode === 'yearly' }" @click="billingMode = 'yearly'">年付 <span class="save-tag">立省589元</span></button>
            </div>
            <p class="plan-price">
              <span v-if="billingMode === 'monthly'" class="plan-price-main">¥299</span>
              <span v-else class="plan-price-main">¥2599</span>
              <span v-if="billingMode === 'monthly'" class="plan-price-period">/ 月</span>
              <span v-else class="plan-price-period">/ 年</span>
            </p>
            <p class="plan-price-extra" v-if="billingMode === 'monthly'">
              年付推荐价：<span>¥2599 / 年</span>，立省 <strong>589元</strong>
            </p>
            <p class="plan-price-extra" v-else>
              对比月付：全年节省 <strong>589元</strong>，相当于 <strong>2个月免费</strong>
            </p>
          </header>
          <ul class="plan-features">
            <li>10份/月 跨境合同AI生成（覆盖28个贸易国法域）</li>
            <li>全维度合规风险检测（高/中/低风险分级标注，附跨境法规依据）</li>
            <li>合同双语对照（中英/中西/中日等6种语言）</li>
            <li>无限次合同PDF/Word导出，高级区块链存证（可用于业务备案）</li>
            <li>1次/月 跨境法律专家线上咨询（4小时响应）</li>
            <li>多设备登录，1个团队协作账号</li>
          </ul>
          <footer class="plan-footer">
            <p class="plan-scenario">适用场景：中小型跨境企业，每月跨境合同量2-10份，需全流程合规保障</p>
            <button class="plan-btn plan-btn-primary" type="button">立即购买</button>
          </footer>
        </article>

        <!-- 企业版 -->
        <article class="plan-card plan-enterprise">
          <header class="plan-header">
            <h2 class="plan-name">企业版 · 定制服务</h2>
            <p class="plan-desc">面向大型跨境企业的专属合规与专家团队支持</p>
            <p class="plan-price">
              <span class="plan-price-main">¥999</span>
              <span class="plan-price-period">/ 月起</span>
            </p>
            <p class="plan-price-extra">年付享 <strong>8折</strong> 优惠，支持个性化定制</p>
          </header>
          <ul class="plan-features">
            <li>无限量跨境合同AI生成与合规审查（专属定制法域规则库）</li>
            <li>专属跨境法律专家1v1对接（2小时响应，每月不限次咨询）</li>
            <li>定制化合同模板（贴合企业特定跨境业务场景，如跨境分销、技术授权）</li>
            <li>团队多账号协作（最多10个账号），权限分级管理</li>
            <li>合规审查报告定制导出（含整改方案、行业对比分析）</li>
            <li>API 对接企业现有系统（如 CRM、ERP）</li>
          </ul>
          <footer class="plan-footer plan-footer-enterprise">
            <p class="plan-scenario">适用场景：大型跨境企业/集团，每月跨境合同量≥10份，需定制化合规体系与深度专家支持</p>
            <button class="plan-btn plan-btn-contact" type="button">联系客服定制</button>
            <div class="plan-enterprise-tag">定制化</div>
          </footer>
        </article>
      </div>
    </section>

    <!-- 增值服务区（整卡彩色背景） -->
    <section class="addons" aria-label="增值服务">
      <div class="section-header mt-20">
        <h2>增值服务 · 按需叠加</h2>
        <p>在基础套餐之上，灵活购买适合当前业务阶段的增值能力</p>
      </div>
      <div class="addons-grid">
        <article class="addon-card addon-gold">
          <h3>额外跨境合同生成包</h3>
          <p class="addon-price">¥29/份 <span>（10份起购 ¥25/份）</span></p>
          <p class="addon-desc">适用于基础版/标准版用户临时增加合同量</p>
          <!-- 底部透明条 + 右下角箭头 -->
          <div>
            <button class="addon-arrow mt-6 justify-end" aria-label="查看详情" @click="onAddonClick('extra-contracts')">
              <i class="fa-solid fa-arrow-right "></i>
            </button>
          </div>
        </article>
        <article class="addon-card addon-blue">
          <h3>跨境法律专家深度咨询</h3>
          <p class="addon-price">¥599/小时 <span>（包年10小时 ¥4999）</span></p>
          <p class="addon-desc">针对复杂跨境合规问题（如关税争议、数据跨境纠纷）</p>

            <button class="addon-arrow mt-2" aria-label="查看详情" @click="onAddonClick('expert-deep')">
              <i class="fa-solid fa-arrow-right"></i>
            </button>

        </article>
        <article class="addon-card addon-purple">
          <h3>定制化合同模板开发</h3>
          <p class="addon-price">¥1999/个</p>
          <p class="addon-desc">贴合企业特定跨境业务场景，专家审核确认</p>

            <button class="addon-arrow mt-6" aria-label="查看详情" @click="onAddonClick('custom-template')">
              <i class="fa-solid fa-arrow-right"></i>
            </button>

        </article>
        <article class="addon-card addon-green">
          <h3>跨境合规培训</h3>
          <p class="addon-price">¥3999/场 <span>（线上/线下可选）</span></p>
          <p class="addon-desc">针对企业团队开展目标法域合规知识培训</p>

            <button class="addon-arrow mt-6" aria-label="查看详情" @click="onAddonClick('compliance-training')">
              <i class="fa-solid fa-arrow-right"></i>
            </button>

        </article>
      </div>
    </section>

    <!-- 底部信任与答疑区 -->
    <section class="trust-faq mb-20">
      <div class="trust-panel">
        <h2>为什么跨境企业选择 Legal-Guard？</h2>
        <div class="trust-items">
          <div class="trust-item">
            <div class="trust-icon">✓</div>
            <div class="trust-content">
              <p class="trust-title">6300+ 跨境企业选择</p>
              <p class="trust-desc">覆盖跨境电商、外贸工厂、SaaS 出海等多个行业场景</p>
            </div>
          </div>
          <div class="trust-item">
            <div class="trust-icon">✓</div>
            <div class="trust-content">
              <p class="trust-title">28 国法域合规认证</p>
              <p class="trust-desc">联合多国律所与合规机构共建规则库，动态更新</p>
            </div>
          </div>
          <div class="trust-item">
            <div class="trust-icon">✓</div>
            <div class="trust-content">
              <p class="trust-title">数据加密安全认证</p>
              <p class="trust-desc">全链路加密 + 区块链存证，确保合同与数据安全可追溯</p>
            </div>
          </div>
        </div>
      </div>

      <div class="faq-panel">
        <h2>常见问题</h2>
        <div class="faq-list">
          <details class="border border-gray-200 rounded-xl p-4 mb-3 hover:border-gold/50 transition-colors">
            <summary class="flex justify-between items-center cursor-pointer list-none">
              <span class="font-medium text-white">Q1：不同套餐的法域覆盖有什么区别？</span>
              <i class="fas fa-chevron-down text-gray-400 text-sm
             transition-transform duration-300 details-open:rotate-180"></i>
            </summary>
            <div class="mt-3 pt-3 border-t border-gray-100">
              <p class="text-gray-600">
                基础版仅覆盖中、美、欧3个主流法域；标准版覆盖28个全球主要贸易国法域；企业版可根据企业业务范围定制专属法域规则库（如新增东南亚、非洲等新兴市场）。
              </p>
            </div>
          </details>
          <details class="border border-gray-200 rounded-xl p-4 mb-3 hover:border-gold/50 transition-colors">
            <summary class="flex justify-between items-center cursor-pointer list-none">
              <span class="font-medium text-white">Q2：年付套餐可以退款吗？</span>
              <i class="fas fa-chevron-down text-gray-400 text-sm
             transition-transform duration-300 details-open:rotate-180"></i>
            </summary>
            <div class="mt-3 pt-3 border-t border-gray-100">
              <p class="text-gray-600">
                年付套餐购买后7天内无使用记录可全额退款；使用后按实际使用月数折算退款（已享受的优惠需扣除）。
              </p>
            </div>
          </details>
          <details class="border border-gray-200 rounded-xl p-4 mb-3 hover:border-gold/50 transition-colors">
            <summary class="flex justify-between items-center cursor-pointer list-none">
              <span class="font-medium text-white">Q3：增值服务可以单独购买吗？</span>
              <i class="fas fa-chevron-down text-gray-400 text-sm
             transition-transform duration-300 details-open:rotate-180"></i>
            </summary>
            <div class="mt-3 pt-3 border-t border-gray-100">
              <p class="text-gray-600">
                可以，所有增值服务支持非套餐用户单独购买，套餐用户享受8折优惠。
              </p>
            </div>
          </details>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'

const billingMode = ref('monthly')

function onAddonClick(key) {
  console.log('点击增值服务：', key)
}
</script>

<style src="./price.css" scoped></style>
