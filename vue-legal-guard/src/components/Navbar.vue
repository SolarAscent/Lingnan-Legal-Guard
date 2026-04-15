<template>
  <nav class="navbar-fixed bg-darkgray/90 backdrop-blur-lg border-b border-gold/20">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-3 lg:py-4 flex justify-between items-center max-w-7xl">
      <!-- Logo -->
      <div class="flex items-center gap-2 lg:gap-3">
        <div class="relative">
          <i class="fa-solid fa-shield-halved text-gold text-xl lg:text-2xl animate-pulse"></i>
          <div class="absolute -inset-1 bg-gold/20 rounded-full blur-sm"></div>
        </div>
        <span class="text-lg lg:text-2xl font-bold bg-gradient-to-r from-gold to-yellow-200 bg-clip-text text-transparent">
          Legal-Guard
        </span>
      </div>

      <!-- 桌面导航菜单 -->
      <div class="hidden lg:flex items-center gap-6 xl:gap-8">
        <router-link to="/" class="group text-white/80 hover:text-gold transition-all duration-300 flex items-center gap-2">
          <i class="fa-solid fa-house-chimney text-sm group-hover:scale-110 transition-transform"></i>
          <span class="text-sm font-medium">首页</span>
        </router-link>
        <router-link to="/core" class="group text-white/80 hover:text-gold transition-all duration-300 flex items-center gap-2">
          <i class="fa-solid fa-star text-sm group-hover:scale-110 transition-transform"></i>
          <span class="text-sm font-medium">核心功能</span>
        </router-link>
        <router-link to="/cases" class="group text-white/80 hover:text-gold transition-all duration-300 flex items-center gap-2">
          <i class="fa-solid fa-globe text-sm group-hover:scale-110 transition-transform"></i>
          <span class="text-sm font-medium">核心案例</span>
        </router-link>
        <router-link to="/price" class="group text-white/80 hover:text-gold transition-all duration-300 flex items-center gap-2">
          <i class="fa-solid fa-tags text-sm group-hover:scale-110 transition-transform"></i>
          <span class="text-sm font-medium">定价方案</span>
        </router-link>
        <a href="#" class="group text-white/80 hover:text-gold transition-all duration-300 flex items-center gap-2">
          <i class="fa-solid fa-circle-question text-sm group-hover:scale-110 transition-transform"></i>
          <span class="text-sm font-medium">关于我们</span>
        </a>
      </div>

      <!-- 登录/注册按钮 -->
      <div class="flex items-center gap-2 lg:gap-4">
        <a href="#" class="px-3 py-1.5 lg:px-4 lg:py-2 text-white/80 hover:text-gold transition-colors text-sm lg:text-base flex items-center gap-1">
          <i class="fa-solid fa-right-to-bracket"></i>
          <span class="hidden sm:inline">登录</span>
        </a>
        <a href="#" class="px-3 py-1.5 lg:px-6 lg:py-2 bg-gold text-dark font-medium rounded-md hover:bg-gold/90 transition-colors shadow-lg shadow-gold/20 text-sm lg:text-base flex items-center gap-2">
          <i class="fa-solid fa-user-plus"></i>
          <span class="hidden sm:inline">免费注册</span>
          <span class="sm:hidden">注册</span>
        </a>
      </div>

      <!-- 移动端汉堡按钮 -->
      <button class="lg:hidden text-white text-xl hover:text-gold transition-colors" @click="drawerOpen = !drawerOpen" aria-label="打开菜单">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>

    <!-- 抽屉菜单（移动端） -->
    <transition name="fade">
      <div v-if="drawerOpen" class="lg:hidden bg-darkgray/95 border-t border-gold/20">
        <div class="px-4 py-3 space-y-2 max-w-7xl mx-auto">
          <router-link to="/" class="block px-3 py-2 rounded-lg text-white/90 hover:bg-white/10">首页</router-link>
          <router-link to="/core" class="block px-3 py-2 rounded-lg text-white/80 hover:bg-white/10">核心功能</router-link>
          <router-link to="/cases" class="block px-3 py-2 rounded-lg text-white/80 hover:bg-white/10">核心案例</router-link>
          <router-link to="/price" class="block px-3 py-2 rounded-lg text-white/90 hover:bg-white/10">定价方案</router-link>
          <a href="#" class="block px-3 py-2 rounded-lg text-white/80 hover:bg-white/10">关于我们</a>
        </div>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const drawerOpen = ref(false)
</script>

<style scoped>
.navbar-fixed {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 1000; /* 高于页面内容 */
}
.fade-enter-active, .fade-leave-active { transition: opacity .2s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
