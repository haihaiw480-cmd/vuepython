import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/login',
        name: 'Home',
        component: () => import('@/views/login/index.vue')
    },
]

// 创建 router
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
