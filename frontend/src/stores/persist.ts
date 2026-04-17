// pinia持久化配置
import { type PersistedStateOptions } from "pinia-plugin-persistedstate";
export const piniaPersistConfig = (key: string, paths?: string[]) => {
    const config: PersistedStateOptions = {
        key: key,
        // 存储方式，默认为 localStorage
        storage: localStorage,
        // 需要持久化的 state 字段，默认为全部字段
        paths: paths,
    };
    return config;
}; 
