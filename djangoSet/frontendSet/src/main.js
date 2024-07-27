import { createApp } from "vue";

import "./index.css";
import portal from "./portal.vue";
import loginAdmin from "./loginAdmin.vue";
import loginStudent from "./loginStudent.vue";
import register from "./registerStudent.vue";
import numericalSet from "./numericalSet.vue";
import feedbackSet from "./feedbackSet.vue";

createApp(feedbackSet).mount("#app");