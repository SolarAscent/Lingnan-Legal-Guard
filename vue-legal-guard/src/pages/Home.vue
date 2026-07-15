<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'

const scrolled = ref(false)
const menuOpen = ref(false)

const onScroll = () => { scrolled.value = window.scrollY > 8 }

let io = null
onMounted(async () => {
  window.addEventListener('scroll', onScroll, { passive: true })
  await nextTick()
  const els = document.querySelectorAll('.reveal')
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reduce || !('IntersectionObserver' in window)) {
    els.forEach((e) => e.classList.add('is-in'))
    return
  }
  io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target) }
    })
  }, { threshold: 0.14, rootMargin: '0px 0px -7% 0px' })
  els.forEach((e) => io.observe(e))
})
onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
  if (io) io.disconnect()
})

const stats = [
  { value: '12+', label: '乡村高频法律场景', sub: '全场景覆盖' },
  { value: '90%', label: '基础法律成本', sub: '直接下降' },
  { value: '30+', label: '服务县区', sub: '正在拓展' },
  { value: '粤语', label: '语音交互', sub: '不识字也能用' },
]

const coreFeatures = [
  {
    icon: 'fa-file-signature',
    title: '智能合同生成',
    desc: '选择场景（"我要卖鹰嘴桃""我要租块地"），填写关键信息，AI 自动生成规范合同文书。支持粤语语音输入，10 分钟搞定，完全免费。',
    tags: ['农产品购销', '土地流转', '劳务用工', '合作社入社', '12+ 场景'],
    cta: { text: '立即生成', to: '/trial' },
  },
  {
    icon: 'fa-shield-halved',
    title: '合规风险审查',
    desc: '已有合同怕有坑？拍照上传、PDF 或 Word 导入，AI 自动扫描风险条款，红黄绿三色标注，哪里有问题、怎么改，一看就懂。',
    tags: ['图片', 'PDF', 'Word', '手机拍照即审'],
  },
  {
    icon: 'fa-book-open',
    title: '法律资源广场',
    desc: '合同模板库、政策白话解读、普法短视频，全部免费开放。农户自己学、村干部带着用，让法律真正"下乡"。',
    tags: ['12 类合同模板', '政策解读', '普法短视频'],
  },
]

const highlights = [
  { icon: 'fa-microphone-lines', title: '粤语语音交互', desc: '2000+ 粤语法律术语库，从语音输入到条款播报全链路支持。"甲乙双方"变"你同佢"，法律真正入乡随俗。' },
  { icon: 'fa-hand-pointer', title: '场景化引导', desc: '不念法律术语，只问"你要做什么"。卖荔枝、租地、雇工、入合作社……点一下，跟着填就行。' },
  { icon: 'fa-mobile-screen-button', title: '三端适配', desc: '微信小程序、手机 H5、电脑端全支持。大字版 + 语音导航，中老年用户也能轻松上手。' },
  { icon: 'fa-language', title: '简繁切换', desc: '一键切换繁体界面，法律文书简繁转换专业准确，服务港澳同胞及海外侨胞。' },
]

const navLinks = [
  { text: '核心功能', href: '#core' },
  { text: '产品特色', href: '#highlights' },
  { text: '法律资源', href: '#core' },
]
</script>

<template>
  <div class="lg-home">
    <!-- ============ 导航 ============ -->
    <header class="nav" :class="{ 'nav--solid': scrolled }">
      <div class="nav__inner">
        <a href="#top" class="brand">
          <span class="brand__mark"><i class="fa-solid fa-scale-balanced"></i></span>
          <span class="brand__name">岭南法务百县通</span>
        </a>

        <nav class="nav__links">
          <a v-for="l in navLinks" :key="l.text" :href="l.href">{{ l.text }}</a>
        </nav>

        <div class="nav__actions">
          <router-link to="/trial" class="btn btn--ghost-nav">登录</router-link>
          <router-link to="/trial" class="btn btn--gold">免费生成合同</router-link>
        </div>

        <button class="nav__burger" @click="menuOpen = !menuOpen" aria-label="菜单">
          <i :class="menuOpen ? 'fa-solid fa-xmark' : 'fa-solid fa-bars'"></i>
        </button>
      </div>
      <transition name="drawer">
        <div v-if="menuOpen" class="nav__drawer" @click="menuOpen = false">
          <a v-for="l in navLinks" :key="l.text" :href="l.href">{{ l.text }}</a>
          <router-link to="/trial" class="btn btn--gold btn--block">免费生成合同</router-link>
        </div>
      </transition>
    </header>

    <!-- ============ 英雄区 ============ -->
    <section id="top" class="hero">
      <div class="hero__aurora"></div>
      <div class="hero__grid"></div>
      <div class="hero__content">
        <p class="hero__kicker anim">你的乡村法律管家</p>
        <h1 class="hero__title anim anim--1">
          让法律<span class="hl">真正下乡</span>，<br />
          农户也能轻松签好每一份合同
        </h1>
        <p class="hero__sub anim anim--2">
          岭南法务百县通用 AI + 粤语语音，把复杂的法律条款变成"你要做什么"。
          选场景、说句话，10 分钟生成一份规范合同，基础法律成本直降 90%。
        </p>
        <div class="hero__cta anim anim--3">
          <router-link to="/trial" class="btn btn--gold btn--lg">免费生成合同</router-link>
          <a href="#core" class="btn btn--glass btn--lg">了解核心功能</a>
        </div>
        <p class="hero__chips anim anim--4">
          完全免费<span class="sep"></span>粤语语音输入<span class="sep"></span>10 分钟搞定
        </p>
      </div>
      <div class="hero__slant"></div>
    </section>

    <!-- ============ 数据统计 ============ -->
    <section class="stats">
      <div class="stats__inner">
        <div v-for="(s, i) in stats" :key="s.label" class="stat reveal" :style="{ '--i': i }">
          <div class="stat__value">{{ s.value }}</div>
          <div class="stat__label">{{ s.label }}</div>
          <div class="stat__sub">{{ s.sub }}</div>
        </div>
      </div>
    </section>

    <!-- ============ 核心功能 ============ -->
    <section id="core" class="section section--light">
      <div class="wrap">
        <div class="section__head reveal">
          <p class="kicker">核心功能</p>
          <h2>三件事，把乡村法律<br />从"看不懂"变"用得上"</h2>
          <p class="lede">从生成、审查到学习，一条链路覆盖农户与村干部的高频法律需求。</p>
        </div>
        <div class="cards cards--3">
          <article v-for="(f, i) in coreFeatures" :key="f.title" class="card reveal" :style="{ '--i': i }">
            <div class="card__icon"><i :class="`fa-solid ${f.icon}`"></i></div>
            <h3>{{ f.title }}</h3>
            <p>{{ f.desc }}</p>
            <div class="card__tags">
              <span v-for="t in f.tags" :key="t">{{ t }}</span>
            </div>
            <router-link v-if="f.cta" :to="f.cta.to" class="card__link">{{ f.cta.text }} →</router-link>
          </article>
        </div>
      </div>
    </section>

    <!-- ============ 产品特色 ============ -->
    <section id="highlights" class="section section--dark">
      <div class="section__aurora"></div>
      <div class="wrap">
        <div class="section__head section__head--light reveal">
          <p class="kicker kicker--onDark">产品特色</p>
          <h2>为乡村而生的<br />每一处设计</h2>
          <p class="lede">让不识字、说粤语、用手机的用户，也能把法律工具真正用起来。</p>
        </div>
        <div class="cards cards--2">
          <article v-for="(h, i) in highlights" :key="h.title" class="feature reveal" :style="{ '--i': i }">
            <div class="feature__icon"><i :class="`fa-solid ${h.icon}`"></i></div>
            <div>
              <h3>{{ h.title }}</h3>
              <p>{{ h.desc }}</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- ============ CTA ============ -->
    <section class="cta">
      <div class="wrap cta__inner reveal">
        <div>
          <h2>10 分钟，免费生成你的第一份合同</h2>
          <p>选个场景，说句粤语，剩下的交给 AI。</p>
        </div>
        <router-link to="/trial" class="btn btn--gold btn--lg">立即免费体验</router-link>
      </div>
    </section>

    <!-- ============ 页脚 ============ -->
    <footer class="foot">
      <div class="wrap foot__grid">
        <div class="foot__brand">
          <a href="#top" class="brand">
            <span class="brand__mark"><i class="fa-solid fa-scale-balanced"></i></span>
            <span class="brand__name">岭南法务百县通</span>
          </a>
          <p class="foot__slogan">你的乡村法律管家</p>
          <p class="foot__disclaimer">免责声明：AI 生成合同仅供参考，重大交易建议咨询专业律师。</p>
        </div>

        <div class="foot__col">
          <h4>产品</h4>
          <router-link to="/trial">智能合同生成</router-link>
          <router-link to="/trial">合规风险审查</router-link>
          <a href="#core">法律资源广场</a>
        </div>

        <div class="foot__col">
          <h4>项目背景</h4>
          <p>广东省大学生创新创业训练计划省级立项项目</p>
          <p class="foot__muted">项目编号：S202610559007</p>
          <p>暨南大学"百千万工程"突击队</p>
          <p class="foot__muted">合作单位：连州市保安镇党委、政府</p>
        </div>
      </div>

      <div class="wrap foot__bar">
        <span>© 2026 岭南法务百县通</span>
        <span class="foot__links">
          <a href="#top">使用条款</a><span class="dot">·</span><a href="#top">隐私政策</a>
        </span>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* ---------- 基础与配色 ---------- */
.lg-home {
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

  font-family: Inter, system-ui, -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
  color: var(--ink);
  background: #ffffff;
  overflow-x: hidden;
}
.lg-home * { box-sizing: border-box; }
.wrap { width: 100%; max-width: 1160px; margin: 0 auto; padding: 0 24px; }

/* ---------- 按钮 ---------- */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  font-weight: 700; font-size: 15px; line-height: 1; cursor: pointer;
  border-radius: 999px; padding: 12px 22px; text-decoration: none;
  border: 1px solid transparent;
  transition: transform .2s cubic-bezier(.2,.7,.2,1), box-shadow .2s ease, background .2s ease, color .2s ease;
  white-space: nowrap;
}
.btn--lg { padding: 15px 30px; font-size: 16px; }
.btn--block { width: 100%; }
.btn--gold {
  background: linear-gradient(135deg, var(--gold) 0%, var(--gold-strong) 100%);
  color: #241c00; box-shadow: 0 8px 24px -8px rgba(212, 175, 55, .55);
}
.btn--gold:hover { transform: translateY(-2px); box-shadow: 0 16px 34px -8px rgba(212, 175, 55, .72); }
.btn--glass {
  background: rgba(255, 255, 255, .08); color: #eafff5;
  border-color: rgba(255, 255, 255, .22); backdrop-filter: blur(6px);
}
.btn--glass:hover { background: rgba(255, 255, 255, .16); transform: translateY(-2px); }
.btn--ghost-nav { background: transparent; color: #dff5ec; padding: 10px 14px; }
.btn--ghost-nav:hover { color: #fff; }

/* ---------- 导航 ---------- */
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 50;
  transition: background .3s ease, box-shadow .3s ease, border-color .3s ease;
  border-bottom: 1px solid transparent;
}
.nav--solid {
  background: rgba(6, 40, 30, .82); backdrop-filter: blur(14px) saturate(140%);
  border-bottom-color: rgba(255, 255, 255, .08);
  box-shadow: 0 10px 30px -20px rgba(0, 0, 0, .8);
}
.nav__inner { max-width: 1160px; margin: 0 auto; padding: 15px 24px; display: flex; align-items: center; gap: 20px; }
.brand { display: inline-flex; align-items: center; gap: 10px; text-decoration: none; }
.brand__mark {
  width: 34px; height: 34px; border-radius: 10px; display: grid; place-items: center;
  background: linear-gradient(135deg, var(--gold), var(--gold-strong)); color: #241c00;
  font-size: 16px; box-shadow: 0 6px 16px -6px rgba(212, 175, 55, .6);
}
.brand__name { font-weight: 800; font-size: 17px; color: #f4fbf7; letter-spacing: .3px; }
.nav__links { display: none; gap: 28px; margin-left: 16px; flex: 1; }
.nav__links a { color: #cfe9de; text-decoration: none; font-size: 15px; font-weight: 600; transition: color .15s; }
.nav__links a:hover { color: #fff; }
.nav__actions { display: none; align-items: center; gap: 10px; margin-left: auto; }
.nav__burger { margin-left: auto; background: transparent; border: 0; color: #eafff5; font-size: 22px; cursor: pointer; width: 40px; height: 40px; display: grid; place-items: center; }
.nav__drawer {
  display: flex; flex-direction: column; gap: 6px; padding: 12px 24px 20px;
  background: rgba(6, 40, 30, .96); backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, .08);
}
.nav__drawer a { color: #dff5ec; text-decoration: none; font-weight: 600; padding: 12px 6px; border-radius: 10px; }
.nav__drawer a:hover { background: rgba(255, 255, 255, .06); }
.nav__drawer .btn { margin-top: 8px; }
.drawer-enter-active, .drawer-leave-active { transition: opacity .2s ease, transform .2s ease; }
.drawer-enter-from, .drawer-leave-to { opacity: 0; transform: translateY(-8px); }

/* ---------- 英雄区 ---------- */
.hero {
  position: relative; padding: 156px 0 200px;
  background: linear-gradient(160deg, var(--green-950) 0%, var(--green-800) 52%, var(--green-900) 100%);
  isolation: isolate; overflow: hidden;
}
.hero__aurora {
  position: absolute; inset: -20% -10% 0; z-index: -2;
  background:
    radial-gradient(45% 55% at 12% 8%, rgba(16, 185, 129, .42), transparent 60%),
    radial-gradient(42% 55% at 88% 12%, rgba(45, 212, 191, .32), transparent 58%),
    radial-gradient(55% 60% at 72% 96%, rgba(231, 192, 74, .20), transparent 58%),
    radial-gradient(40% 50% at 30% 100%, rgba(16, 185, 129, .18), transparent 60%);
  filter: saturate(120%);
  animation: drift 20s ease-in-out infinite alternate;
}
@keyframes drift {
  from { transform: translate3d(0, 0, 0) scale(1); }
  to { transform: translate3d(-2%, -1.6%, 0) scale(1.07); }
}
.hero__grid {
  position: absolute; inset: 0; z-index: -1; opacity: .5;
  background-image:
    linear-gradient(rgba(255, 255, 255, .04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, .04) 1px, transparent 1px);
  background-size: 54px 54px;
  mask-image: radial-gradient(circle at 50% 30%, #000 40%, transparent 78%);
}
.hero__content { position: relative; max-width: 920px; margin: 0 auto; padding: 0 24px; text-align: center; }
.hero__kicker {
  margin: 0 0 20px; font-family: var(--serif); font-weight: 600; font-size: 17px;
  letter-spacing: 2px; color: var(--emerald-300);
}
.hero__title {
  margin: 0; font-family: var(--serif); font-weight: 900; letter-spacing: .5px; color: #f6fdf9;
  font-size: clamp(34px, 6.4vw, 66px); line-height: 1.14;
}
.hero__title .hl {
  background: linear-gradient(120deg, var(--emerald-300), var(--gold));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero__sub {
  margin: 26px auto 0; max-width: 660px; font-size: clamp(16px, 2.2vw, 19px);
  line-height: 1.8; color: rgba(224, 244, 236, .82);
}
.hero__cta { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin-top: 40px; }
.hero__chips {
  display: flex; flex-wrap: wrap; gap: 10px 0; justify-content: center; align-items: center;
  margin: 30px 0 0; color: rgba(224, 244, 236, .66); font-size: 14px; font-weight: 500;
}
.hero__chips .sep { display: inline-block; width: 4px; height: 4px; margin: 0 16px; border-radius: 50%; background: rgba(110, 231, 183, .6); }

/* 英雄区入场动画 */
.anim { opacity: 0; transform: translateY(22px); animation: rise .9s cubic-bezier(.2,.7,.2,1) forwards; }
.anim--1 { animation-delay: .08s; }
.anim--2 { animation-delay: .16s; }
.anim--3 { animation-delay: .24s; }
.anim--4 { animation-delay: .32s; }
@keyframes rise { to { opacity: 1; transform: translateY(0); } }

.hero__slant {
  position: absolute; left: 0; right: 0; bottom: -1px; height: 96px; z-index: 1;
  background: var(--cream);
  clip-path: polygon(0 100%, 100% 100%, 100% 22%, 0 78%);
}

/* ---------- 滚动进场（Stripe 式）---------- */
.reveal { opacity: 0; transform: translateY(28px); transition: opacity .7s cubic-bezier(.2,.7,.2,1), transform .7s cubic-bezier(.2,.7,.2,1); transition-delay: calc(var(--i, 0) * 90ms); }
.reveal.is-in { opacity: 1; transform: translateY(0); }
@media (prefers-reduced-motion: reduce) {
  .anim, .reveal { opacity: 1 !important; transform: none !important; animation: none !important; }
}

/* ---------- 数据统计 ---------- */
.stats { background: var(--cream); padding: 8px 0 66px; }
.stats__inner {
  max-width: 1160px; margin: -74px auto 0; position: relative; z-index: 2;
  padding: 0 24px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px;
}
.stat { background: #fff; border: 1px solid var(--line); border-radius: 18px; padding: 28px 24px; box-shadow: 0 24px 50px -34px rgba(6, 40, 30, .5); text-align: left; }
.stat__value {
  font-family: var(--serif); font-size: clamp(32px, 5vw, 46px); font-weight: 900; line-height: 1;
  background: linear-gradient(120deg, var(--green-800), var(--emerald));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.stat__label { margin-top: 12px; font-weight: 700; font-size: 15px; color: var(--ink); }
.stat__sub { margin-top: 4px; font-size: 13px; color: var(--ink-soft); }

/* ---------- 通用区块 ---------- */
.section { padding: 100px 0; position: relative; }
.section--light { background: var(--cream); }
.section--dark { background: linear-gradient(165deg, var(--green-900), var(--green-800)); color: #eafff5; overflow: hidden; isolation: isolate; }
.section__aurora {
  position: absolute; inset: 0; z-index: -1; opacity: .9;
  background:
    radial-gradient(40% 60% at 90% 5%, rgba(16, 185, 129, .28), transparent 60%),
    radial-gradient(45% 55% at 5% 95%, rgba(231, 192, 74, .14), transparent 60%);
}
.section__head { max-width: 720px; margin: 0 auto 58px; text-align: center; }
.kicker {
  margin: 0 0 16px; font-family: var(--serif); font-weight: 700; font-size: 19px;
  letter-spacing: 3px; color: var(--emerald);
}
.kicker--onDark { color: var(--emerald-300); }
.section__head h2 {
  margin: 0; font-family: var(--serif); font-size: clamp(30px, 4.6vw, 46px); font-weight: 900;
  letter-spacing: .5px; line-height: 1.24; color: var(--ink);
}
.section__head .lede { margin: 20px 0 0; font-size: 16.5px; line-height: 1.8; color: var(--ink-soft); }
.section__head--light h2 { color: #f6fdf9; }
.section__head--light .lede { color: rgba(224, 244, 236, .78); }

/* ---------- 卡片 ---------- */
.cards { display: grid; gap: 22px; }
.cards--3 { grid-template-columns: 1fr; }
.cards--2 { grid-template-columns: 1fr; }
.card {
  background: #fff; border: 1px solid var(--line); border-radius: 20px; padding: 32px 28px;
  display: flex; flex-direction: column; gap: 14px;
  box-shadow: 0 30px 60px -44px rgba(6, 40, 30, .45);
}
.card.is-in { transition: opacity .7s cubic-bezier(.2,.7,.2,1), transform .7s cubic-bezier(.2,.7,.2,1), box-shadow .25s ease, border-color .25s ease; }
.card:hover { transform: translateY(-8px); border-color: rgba(16, 185, 129, .4); box-shadow: 0 42px 74px -40px rgba(6, 40, 30, .5); }
.card__icon {
  width: 54px; height: 54px; border-radius: 15px; display: grid; place-items: center; font-size: 23px;
  color: var(--green-800); background: linear-gradient(135deg, rgba(16, 185, 129, .2), rgba(110, 231, 183, .28));
  border: 1px solid var(--line);
}
.card h3 { margin: 6px 0 0; font-family: var(--serif); font-size: 23px; font-weight: 700; color: var(--ink); }
.card p { margin: 0; font-size: 15px; line-height: 1.75; color: var(--ink-soft); flex: 1; }
.card__tags { display: flex; flex-wrap: wrap; gap: 8px; }
.card__tags span { font-size: 12.5px; font-weight: 600; color: var(--green-700); padding: 5px 11px; border-radius: 999px; background: rgba(16, 185, 129, .1); border: 1px solid var(--line); }
.card__link { margin-top: 4px; align-self: flex-start; font-weight: 700; font-size: 15px; color: var(--green-700); text-decoration: none; transition: color .15s; }
.card__link:hover { color: var(--emerald); }

/* 特色（深色区）*/
.feature {
  display: flex; gap: 18px; padding: 28px;
  background: rgba(255, 255, 255, .04); border: 1px solid rgba(255, 255, 255, .1); border-radius: 18px;
}
.feature.is-in { transition: opacity .7s cubic-bezier(.2,.7,.2,1), transform .7s cubic-bezier(.2,.7,.2,1), background .25s ease, border-color .25s ease; }
.feature:hover { background: rgba(255, 255, 255, .07); transform: translateY(-6px); border-color: rgba(16, 185, 129, .35); }
.feature__icon { flex: 0 0 auto; width: 50px; height: 50px; border-radius: 14px; display: grid; place-items: center; font-size: 21px; color: #052018; background: linear-gradient(135deg, var(--emerald-300), var(--emerald)); }
.feature h3 { margin: 2px 0 0; font-family: var(--serif); font-size: 20px; font-weight: 700; color: #f6fdf9; }
.feature p { margin: 10px 0 0; font-size: 14.5px; line-height: 1.75; color: rgba(224, 244, 236, .78); }

/* ---------- CTA ---------- */
.cta { background: linear-gradient(135deg, var(--green-800), var(--green-700)); padding: 66px 0; color: #eafff5; position: relative; overflow: hidden; }
.cta::after { content: ''; position: absolute; inset: 0; z-index: 0; background: radial-gradient(50% 120% at 85% 50%, rgba(231, 192, 74, .18), transparent 60%); }
.cta__inner { position: relative; z-index: 1; display: flex; flex-wrap: wrap; gap: 26px; align-items: center; justify-content: space-between; }
.cta h2 { margin: 0; font-family: var(--serif); font-size: clamp(24px, 3.6vw, 34px); font-weight: 900; }
.cta p { margin: 12px 0 0; color: rgba(224, 244, 236, .8); font-size: 16px; }

/* ---------- 页脚 ---------- */
.foot { background: var(--green-950); color: #cfe9de; padding: 66px 0 30px; }
.foot__grid { display: grid; grid-template-columns: 1fr; gap: 40px; }
.foot__brand .brand__name { color: #f4fbf7; }
.foot__slogan { margin: 16px 0 0; font-size: 15px; color: rgba(207, 233, 222, .85); }
.foot__disclaimer { margin: 16px 0 0; font-size: 13px; line-height: 1.7; color: rgba(207, 233, 222, .55); max-width: 340px; }
.foot__col h4 { margin: 0 0 16px; font-family: var(--serif); font-size: 16px; font-weight: 700; color: #f4fbf7; letter-spacing: 1px; }
.foot__col a, .foot__col p { display: block; margin: 0 0 10px; font-size: 14px; line-height: 1.6; color: rgba(207, 233, 222, .78); text-decoration: none; }
.foot__col a:hover { color: #fff; }
.foot__muted { color: rgba(207, 233, 222, .5) !important; font-size: 13px !important; margin-top: -4px !important; }
.foot__bar { margin-top: 44px; padding-top: 22px; border-top: 1px solid rgba(255, 255, 255, .08); display: flex; flex-wrap: wrap; gap: 12px; justify-content: space-between; font-size: 13px; color: rgba(207, 233, 222, .6); }
.foot__links a { color: rgba(207, 233, 222, .7); text-decoration: none; }
.foot__links a:hover { color: #fff; }
.foot__links .dot { margin: 0 8px; }

/* ---------- 响应式 ---------- */
@media (min-width: 640px) {
  .stats__inner { grid-template-columns: repeat(4, 1fr); }
  .cards--2 { grid-template-columns: 1fr 1fr; }
}
@media (min-width: 900px) {
  .nav__links, .nav__actions { display: flex; }
  .nav__burger { display: none; }
  .cards--3 { grid-template-columns: repeat(3, 1fr); }
  .foot__grid { grid-template-columns: 2fr 1fr 1.4fr; gap: 60px; }
}
</style>
