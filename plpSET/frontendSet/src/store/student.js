import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("student", {
  state: () => ({
    isAuthenticated: false,
    user: null,
    alertMessage: "", //message from register and login apis
    alertType: "", //success or error, will use for alert component
  }),
  actions: {
    async register(
      student_id,
      password,
      confirm_password,
      dateofbirth,
      student_email
    ) {
      try {
        const response = await axios.post(
          "http://localhost:8000/api/register/",
          {
            student_id,
            password,
            confirm_password,
            dateofbirth,
            student_email,
          }
        );
        this.userInfo = response.data.student;
        return response.data;
      } catch (error) {
        console.error(error);
        throw error.response.data;
      }
    },
    async login(student_acc_number, password, dateofbirth) {
      try {
        const response = await axios.post("http://localhost:8000/api/login/", {
          student_acc_number,
          password,
          dateofbirth,
        });
        this.isAuthenticated = true;
        this.user = response.data;

        console.log(response.data.student_id);
        // Store relevant user info in LocalStorage
        localStorage.setItem("student_id", response.data.student_id);
        localStorage.setItem("user_type", response.data.user_type);

        return response.data;
      } catch (error) {
        this.isAuthenticated = false;
        this.alertMessage = error.response.data.error || "Login failed";
        this.alertType = "error";
        throw error.response.data; // Throw error for handling in the component
      }
    },
    logout() {
      this.isAuthenticated = false;
      this.user = null;

      // Clear session data from LocalStorage
      localStorage.removeItem("student_id");
      localStorage.removeItem("user_type");
      localStorage.removeItem("student_enrolled_subj_id");
    },

    // Restore session from LocalStorage on app load
    restoreSession() {
      const studentId = localStorage.getItem("student_id");
      const userType = localStorage.getItem("user_type");
      if (studentId && userType) {
        this.isAuthenticated = true;
        this.user = { student_id: studentId, user_type: userType };
      }
    },
  },
});
