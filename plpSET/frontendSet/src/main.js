import { createApp } from "vue";
import { createPinia } from "pinia";
import "./index.css";
import App from "./pages/App.vue";
import "flowbite";
import "./axios-config";
import router from "./router";
import { VueQueryPlugin, QueryClient } from "@tanstack/vue-query";

const queryClient = new QueryClient();
const app = createApp(App);
const pinia = createPinia();

app.use(VueQueryPlugin, {
  queryClient,
});
app.use(pinia);
app.use(router);
app.mount("#app");
