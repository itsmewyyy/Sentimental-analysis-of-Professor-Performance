import portal from './pages/portal.vue'
import loginStudent_page from './pages/loginStudent.vue'
import registerStudent_page from './pages/registerStudent.vue'
import numericalSet_page from './pages/numericalSet.vue'
import feedbackSet_page from './pages/feedbackSet.vue'
import loginAdmin_page from './pages/loginAdmin.vue'
import dashboardStudent from './pages/dashboardStudent.vue'
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {path: '/', component: portal},
    {path: '/StudentLogin', component: loginStudent_page }, 
    {path: '/StudentRegister', component:registerStudent_page},
    { path: '/AdminLogin', component: loginAdmin_page }, 
    {path: '/SETNumericalRating', component: numericalSet_page},
    {path: '/SETFeedback', component: feedbackSet_page
    },
    {path: '/StudentDashboard', component: dashboardStudent
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router