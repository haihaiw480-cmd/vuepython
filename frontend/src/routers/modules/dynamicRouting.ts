// 自动导入 views 下所有组件（Vite 专用）
const modules = import.meta.glob('@/views/**/*.vue')
import { useAuthStore } from "@/stores/auth";
import { type RouteRecordRaw } from "vue-router";
import router from "@/routers/index";

export const dynamicRouter = async () => {
    const authStore = useAuthStore()

    try {
        // 获取菜单权限列表
        await authStore.getAuthMenuList()

        // 添加路由
        authStore.authFlatMenuList.forEach((item) => {
            item.children && delete item.children
            // 拼接模块
            item.component = modules[`/src/views${item.component}.vue`];

            router.addRoute("layout", item as unknown as RouteRecordRaw);

        })
    } catch (error) {
        console.log(error)
    }

}
