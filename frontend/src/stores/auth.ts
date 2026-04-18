
import { defineStore } from "pinia";
import { getMenuList } from "@/api/menu/index";
import { piniaPersistConfig } from "@/stores/persist";
import { flatMenuList } from "@/utils/index"
export const useAuthStore = defineStore("auth", {
    // 数据 (data)
    state: () => ({
        // 菜单权限列表
        authMenuList: [] as Menu.MenuOptions[],
    }),
    // store 的计算属性 (computed)
    getters: {
        authMenuListGet: state => state.authMenuList,
        // 扁平化处理router
        authFlatMenuList: state => flatMenuList(state.authMenuList)
    },
    // store 的方法 (methods)
    actions: {
        // 获取菜单权限列表
        async getAuthMenuList() {
            const { data } = await getMenuList()
            this.authMenuList = data
        }
    },
});
