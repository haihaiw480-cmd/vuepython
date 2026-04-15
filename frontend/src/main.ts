import router from '@/routers/index.ts';
import { createApp } from 'vue';
import App from './App.vue';
import './style.css';
createApp(App).use(router).mount('#app')
