import { createApp } from 'vue'
//import App from './App.vue'

// add this
import './index.css'
import Login from './Login.vue'
import Portal from './Portal.vue'
import Admin from './Admin.vue'
import Register from './Register.vue'

//createApp(Login).mount('#app')
//createApp(Portal).mount('#app')
//createApp(Admin).mount('#app')
createApp(Register).mount('#app')