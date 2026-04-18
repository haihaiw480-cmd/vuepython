import { createRouter, createWebHistory, createWebHashHistory, type RouteRecordRaw } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useAuthStore } from '@/stores/auth'
import { dynamicRouter } from './modules/dynamicRouting'
import { staticRouter } from "@/routers/modules/staticRouter"

const routes: Array<RouteRecordRaw> = [
    ...staticRouter,
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/login/index.vue')
    },

    {
        path: '/',
        name: 'layout',
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
    history: createWebHashHistory(),
    routes
})
// 路由守卫（控制登录）
router.beforeEach(async (to, from, next) => {
    console.log(to, from, next)
    const userStore = useUserStore();
    const authStore = useAuthStore();
    const token = userStore.access_token;
    console.log(authStore.authFlatMenuList.length);

    // 如果没有 token 并且访问的不是登录页，则重定向到登录页
    if (to.path !== '/login' && !token) {
        next('/login');

    }
    if (!authStore.authFlatMenuList.length && token) {

        await dynamicRouter();
        return next({ ...to, replace: true });
        // next({ ...to, replace: true }); // ❗ 必须
    }
    // 8.正常访问页面
    next();

})
export default router
