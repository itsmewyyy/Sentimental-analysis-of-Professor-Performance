import { createApp } from "vue";

import "./index.css";
import portal from "./portal.vue";
import login_Admin from "./login_Admin.vue";
import login_Student from "./login_Student.vue";

createApp(login_Student).mount("#app");
