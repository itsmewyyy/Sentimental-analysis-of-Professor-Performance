import portal from './portal.vue'
import loginStudent_page from './loginStudent.vue'
import registerStudent_page from './registerStudent.vue'
import numericalSet_page from './numericalSet.vue'
import feedbackSet_page from './feedbackSet.vue'
import loginAdmin_page from './loginAdmin.vue'
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {path: '/', component: portal},
    { path: '/StudentLogin', component: loginStudent_page }, 
    {path: '/StudentRegister', component:registerStudent_page},
    { path: '/AdminLogin', component: loginAdmin_page }, 
    {path: '/SETNumericalRating', component:numericalSet_page}

]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router