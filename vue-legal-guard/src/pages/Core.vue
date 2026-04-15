<template>
  <div class="core-page">
    <!-- 顶部导航（如果该页面需要导航，可以取消下一行注释并确保已存在 Navbar 组件） -->
     <Navbar />

    <!-- 核心能力：跨境合同智能生成（Hero） -->
    <section class="core-hero">
<!--      <div class="core-hero-inner">-->
<!--        <div class="core-hero-text">-->
<!--          <h1 class="core-hero-title">跨境合同智能生成</h1>-->
<!--          <p class="core-hero-subtitle">-->
<!--            专为跨境小微企业打造的智能合同生成工具，3分钟生成符合目标法域合规要求的标准化合同，无需专业法务知识。-->
<!--          </p>-->
<!--          <ul class="core-hero-bullets">-->
<!--            <li>适配28个贸易国法域合规要求</li>-->
<!--            <li>支持6种多语言生成</li>-->
<!--            <li>基础信息一键填充，直接复用无需大幅修改</li>-->
<!--          </ul>-->
<!--        </div>-->
<!--        <div class="core-hero-visual">-->
<!--          <div class="core-globe"></div>-->
<!--          <p class="core-hero-note">多法域适配 · 多语言生成 · 一键填充</p>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="core-divider"></div>-->
    </section>

    <!-- 可生成的跨境合同种类（表格展示） -->
    <section class="core-templates" aria-label="跨境合同模板">
      <h2 class="section-title">可生成的跨境合同种类</h2>
      <p class="section-subtitle">覆盖跨境业务核心场景，所有合同模板均适配多法域合规要求，可直接生成使用</p>

      <div class="template-table-wrap">
        <table class="template-table">
          <thead>
            <tr>
              <th>合同类型</th>
              <th>适用场景</th>
              <th>跨境适配亮点</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="tpl-name">SaaS服务协议</td>
              <td>
                跨境软件授权、云端服务合作、订阅式服务合作等
              </td>
              <td>
                <ul>
                  <li>包含数据跨境传输合规条款</li>
                  <li>多语言服务说明</li>
                  <li>跨国服务级别（SLA）承诺</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td class="tpl-name">分销合作协议</td>
              <td>
                跨境产品分销、代理合作、渠道拓展等
              </td>
              <td>
                <ul>
                  <li>关税承担与汇率结算机制</li>
                  <li>跨境物流责任划分</li>
                  <li>目标市场合规要求条款</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td class="tpl-name">保密协议（NDA）</td>
              <td>
                跨境商业谈判、技术合作、核心数据共享等
              </td>
              <td>
                <ul>
                  <li>适配不同法域保密期限规定</li>
                  <li>跨境数据保密合规条款</li>
                  <li>违约赔偿计算标准</li>
                </ul>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 快速体验入口（CTA） -->
    <section class="core-cta">
      <div class="cta-inner">
        <h2>快速体验入口</h2>
        <p>点击下方按钮，免费试用生成跨境合同，无需注册即可预览模板</p>
        <div class="cta-actions">
          <button class="cta-btn primary" @click="goTrial">免费试用生成合同</button>
          <button class="cta-btn" @click="viewAll">查看全部合同模板</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
const router = useRouter()

function goTrial() {
  router.push('/trial')
}
function viewAll() {
  // 若有模板总览路由可改为 '/templates'；当前先指向试用页或保留占位。
  router.push('/trial')
}
</script>

<style src="./core.css" scoped></style>
