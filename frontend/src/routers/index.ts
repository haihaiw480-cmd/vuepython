import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { useUserStore } from '@/stores/user'
const routes: Array<RouteRecordRaw> = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/login/index.vue')
    },
    {
        path: '/',
        name: 'Home',
        component: () => import("@/layouts/index.vue"),

        children: [
            {
                path: "index",
                component: () => import('@/views/home/index.vue'),
                meta: {
                    requiresAuth: true, // 需要登录才能访问
                },
            }

        ]
    },
]

// 创建 router
const router = createRouter({
    history: createWebHistory(),
    routes
})
// 路由守卫（控制登录）
router.beforeEach((to, from, next) => {
    const userStore = useUserStore();
    const token = userStore.access_token;
    console.log('路由守卫', to, from, token)
    // 如果没有 token 并且访问的不是登录页，则重定向到登录页
    if (to.path !== '/login' && !token) {
        next('/login');

    } else {
        next();
    }

})
export default router
