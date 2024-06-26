import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import { apolloProvider } from "@/apollo-config";
import { createPinia } from "pinia";


createApp(App).use(createPinia()).use(router).use(apolloProvider).mount("#app");