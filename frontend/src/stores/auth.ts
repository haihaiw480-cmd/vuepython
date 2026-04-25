
import { defineStore } from "pinia";
import { getMenuListAll } from "@/api/menu/index";
import { piniaPersistConfig } from "@/stores/persist";
import { flatMenuList, makeMenuTree } from "@/utils/index"

export const useAuthStore = defineStore("auth", {
    // 数据 (data)
    state: () => ({
        // 菜单权限列表
        authMenuList: [],
        authMenuListAll: [] as Menu.MenuItem[]
    }),
    // store 的计算属性 (computed)
    getters: {
        authMenuListGet: state => state.authMenuList,


        authMenuListAllGet: state => state.authMenuListAll,
        authMenuListAllTree: state => makeMenuTree(state.authMenuListAll),

    },
    // store 的方法 (methods)
    actions: {
        async getMenuListAll() {
            const { data } = await getMenuListAll()
            const list = Array.isArray(data) ? data : data.list
            this.authMenuListAll = list
        }
    },
});
