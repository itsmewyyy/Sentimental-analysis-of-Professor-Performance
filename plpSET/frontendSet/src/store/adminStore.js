// store/adminStore.js
import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("adminStore", {
  state: () => ({
    isAuthenticated: false,
    user: null,
    alertMessage: "",
    alertType: "",
  }),

  actions: {
    async login(adminUsername, password) {
      try {
        const response = await axios.post(
          "http://localhost:8000/api/adminLogin/",
          {
            adminUsername,
            password,
          }
        );
        this.isAuthenticated = true;
        this.user = response.data;

        // Store relevant user info in LocalStorage
        localStorage.setItem("admin_id", response.data.admin_id);
        localStorage.setItem("user_type", response.data.user_type);
        localStorage.setItem("college", response.data.dept_id);

        return response.data;
      } catch (error) {
        this.isAuthenticated = false;
        this.alertMessage = error.response.data.error || "Login failed";
        this.alertType = "error";
        throw error.response.data;
      }
    },

    logout() {
      this.isAuthenticated = false;
      this.user = null;

      localStorage.clear();
    },

    restoreSession() {
      const adminId = localStorage.getItem("admin_id");
      const userType = localStorage.getItem("user_type");
      const deptId = localStorage.getItem("college");

      if (adminId && userType) {
        this.isAuthenticated = true;
        this.user = {
          admin_id: adminId,
          user_type: userType,
          dept_id: deptId,
        };
      }
    },
  },
});
