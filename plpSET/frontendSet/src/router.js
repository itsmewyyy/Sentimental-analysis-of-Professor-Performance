import portal from "./pages/portal.vue";
import loginStudent_page from "./pages/loginStudent.vue";
import registerStudent_page from "./pages/registerStudent.vue";
import loginAdmin_page from "./pages/loginAdmin.vue";
import dashboardStudent from "./pages/dashboardStudent.vue";
import studentList from "./pages/studentList.vue";
import adminstudentSections from "./pages/adminstudentSections.vue";
import profsubjTagging from "./pages/profsubjTagging.vue";
import evaluationPage from "./pages/evaluationPage.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: portal,
    meta: {
      title:
        "Portal | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/StudentLogin",
    component: loginStudent_page,
    meta: {
      title:
        "Student Login | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/StudentRegister",
    component: registerStudent_page,
    meta: {
      title:
        "Student Register | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  { path: "/AdminLogin", component: loginAdmin_page },

  {
    path: "/StudentDashboard",
    component: dashboardStudent,
    meta: {
      title:
        "Student Dashboard | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  { path: "/Colleges", component: adminstudentSections },
  {
    path: "/StudentList/:sectionId",
    name: "StudentList",
    component: studentList,
  },
  { path: "/Prof-Subject", component: profsubjTagging },
  {
    path: "/evaluation",
    component: evaluationPage,
    meta: {
      title:
        "Student Evaluation of Teaching | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const title = to.meta.title || "Vite App";
  document.title = title;
  next();
});

export default router;
