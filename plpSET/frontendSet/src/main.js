import { createApp } from "vue";
import { createPinia } from 'pinia';
import "./index.css";
import App from './pages/App.vue'
import "flowbite";
import './axios-config';
import router from './router'


const app = createApp(App);
const pinia = createPinia();


app.use(pinia);
app.use(router);
app.mount('#app');
