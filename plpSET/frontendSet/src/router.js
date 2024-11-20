import portal from "./pages/portal.vue";
import loginStudent_page from "./pages/loginStudent.vue";
import registerStudent_page from "./pages/SignUp.vue";
import loginAdmin_page from "./pages/loginAdmin.vue";
import dashboardStudent from "./pages/dashboardStudent.vue";
import studentList from "./pages/studentList.vue";
import studentDatabase from "./pages/dashboardMISDatabasesStudent.vue";
import dashboardSecretary from "./pages/dashboardSecretary.vue";
import evaluationPage from "./pages/evaluationPage.vue";
import dashboardDean from "./pages/dashboardDean.vue";
import dashboardDeanProfessorData from "./pages/dashboardDeanProfessorData.vue";
import dashboardMIS from "./pages/dashboardMIS.vue";
import dashboardMISDatabaseManagement from "./pages/dashboardMISDatabaseManagement.vue";
import dashboardMISAnalytics from "./pages/dashboardMISAnalytics.vue";
import dashboardMISCollegeData from "./pages/dashboardMISCollegeData.vue";
import dashboardMISProfessorData from "./pages/dashboardMISProfessorData.vue";
import StudentProfile from "./pages/StudentProfile.vue";
import DeanProfile from "./pages/DeanProfile.vue";
import SecretaryProfile from "./pages/SecretaryProfile.vue";
import SignUpProf from "./pages/SignUpProf.vue";
import dashboardProfessor from "./pages/dashboardProfessor.vue";
import ProfessorProfile from "./pages/ProfessorProfile.vue";
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
  {
    path: "/AdminLogin",
    component: loginAdmin_page,
    meta: {
      title:
        "Admin Login | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },

  {
    path: "/StudentDashboard",
    component: dashboardStudent,
    meta: {
      title:
        "Student Dashboard | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/DatabaseManagement",
    component: dashboardMISDatabaseManagement,
    meta: {
      title:
        "Database Management | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/StudentDatabase",
    component: studentDatabase,
    meta: {
      title:
        "Colleges | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/StudentList/:sectionId",

    component: studentList,
    meta: {
      title:
        "Student List | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/SecretaryDashboard",
    component: dashboardSecretary,
    meta: {
      title:
        "Secretary Dashboard | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/Evaluation",
    component: evaluationPage,
    meta: {
      title:
        "Student Evaluation of Teaching | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/DeanDashboard",
    component: dashboardDean,
    meta: {
      title:
        "Dean Dashboard | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
    name: "DeanDashboard",
  },
  {
    path: "/MISDashboard-College-Analytics",
    component: dashboardMISCollegeData,
    meta: {
      title:
        "College Analytics | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
    name: "MISCollegeDataDashboard",
  },
  {
    path: "/DeanDashboard-ProfessorAnalytics",
    component: dashboardDeanProfessorData,
    meta: {
      title:
        "Professor Analytics | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/MISDashboard-Professor-Analytics",
    component: dashboardMISProfessorData,
    meta: {
      title:
        "Professor Analytics | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/MISDashboard",
    component: dashboardMIS,
    meta: {
      title:
        "MIS Dashboard | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/professorDashboard",
    component: dashboardProfessor,
    meta: {
      title:
        "Professor Dashboard | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/MISDashboardAnalytics",
    component: dashboardMISAnalytics,
    meta: {
      title:
        "Analytics | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/StudentProfile",
    component: StudentProfile,
    meta: {
      title:
        "Student Profile | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/DeanProfile",
    component: DeanProfile,
    meta: {
      title:
        "Dean Profile | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/ProfProfile",
    component: ProfessorProfile,
    meta: {
      title:
        "Professor Profile | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/SecretaryProfile",
    component: SecretaryProfile,
    meta: {
      title:
        "Secretary Profile | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
    },
  },
  {
    path: "/SignupProf",
    component: SignUpProf,
    meta: {
      title:
        "Register Professor | Pamantasan ng Lungsod ng Pasig Student Evaluation of Teaching",
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
