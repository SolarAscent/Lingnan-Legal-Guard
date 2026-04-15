import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import Demo from './pages/Demo.vue'
import Trial from './pages/Trial.vue'
import Price from './pages/Price.vue'
import Core from './pages/Core.vue'
import CoreCases from './pages/CoreCases.vue'

const routes = [
	{ path: '/', component: Demo },
	{ path: '/trial', component: Trial },
	{ path: '/price', component: Price },
	{ path: '/core', component: Core },
	{ path: '/cases', component: CoreCases },
]

const router = createRouter({
	history: createWebHashHistory(),
	routes,
})

createApp(App).use(router).mount('#app')
