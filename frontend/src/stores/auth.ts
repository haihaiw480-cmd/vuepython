import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
    // 数据 (data)
    state: () => ({
        // 菜单权限列表
        authMenuList: [],
    })
});
