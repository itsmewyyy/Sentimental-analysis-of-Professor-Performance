import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('student', {
  state: () => ({
    isAuthenticated: false,
    user: null,
    alertMessage: '', //message from register and login apis
    alertType: '', //success or error, will use for alert component
  }),
  actions: {
    async register(student_id,password, confirm_password) {
      try {
        const response = await axios.post('http://localhost:8000/api/register/', {
          student_id,
          password,
          confirm_password
        });
        this.userInfo = response.data.student;
        return response.data;
      } catch (error) {
        console.error(error);
        throw error.response.data;
      }
    },
    async login(student_acc_number, password) {
      try {
        const response = await axios.post('http://localhost:8000/api/login/', { student_acc_number, password });
        this.isAuthenticated = true;
        this.user = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
        throw error.response.data;
      }
    },
    logout() {
      this.isAuthenticated = false;
      this.user = null;
    }
  }
});
