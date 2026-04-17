import router from '@/routers/index.ts';
import { createApp } from 'vue';
import ElementPlus from "element-plus";
import 'element-plus/dist/index.css'
import App from './App.vue';
import pinia from './stores';
createApp(App).use(router).use(pinia).use(ElementPlus).mount('#app')
