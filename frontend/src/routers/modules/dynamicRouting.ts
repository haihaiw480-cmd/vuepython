// 自动导入 views 下所有组件（Vite 专用）
const modules = import.meta.glob('@/views/**/*.vue')
import { useAuthStore } from "@/stores/auth";
import { type RouteRecordRaw } from "vue-router";
import router from "@/routers/index";

export const dynamicRouter = async () => {
    const authStore = useAuthStore()

    try {

        await authStore.getMenuListAll();

        authStore.authMenuListAllGet.forEach((item) => {
            const component = modules[`/src/views${item.component}.vue`];

            if (!component) {
                console.warn("组件不存在:", item.component);
                return;
            }

            const routeName = item.routeName || `menu_${item.id}`;

            const routerItem: RouteRecordRaw = {
                path: item.path?.replace(/^\//, '') || '',
                name: routeName,
                component,
                meta: {
                    title: item.name,
                    icon: item.icon,
                    isHide: item.isHidden
                }
            };

            // ✅ 防重复
            if (!router.hasRoute(routeName)) {
                router.addRoute("layout", routerItem);
            }
        });

        // ✅ 验证
        const layout = router.getRoutes().find(r => r.name === "layout");
        console.log("layout children:", layout);

    } catch (error) {
        console.log(error);
    }

}
