import { defineStore } from "pinia";
import { piniaPersistConfig } from "@/stores/persist";
export const useUserStore = defineStore("user", {
    // 数据 (data)
    state: () => ({
        access_token: "",
    }),
    // store 的计算属性 (computed)
    getters: {},
    // store 的方法 (methods)
    actions: {
        setToken(token: string) {
            this.access_token = token;
        },
    },
    persist: piniaPersistConfig("user", ["access_token"]),
});
