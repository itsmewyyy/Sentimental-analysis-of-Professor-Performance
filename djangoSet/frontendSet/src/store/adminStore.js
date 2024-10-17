// store/adminStore.js
import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("adminStore", {
  state: () => ({
    isAuthenticated: false,
    user: null,
    alertMessage: "", // Message from register/login APIs
    alertType: "", // success or error, will be used for alert component
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

      // Clear session data from LocalStorage
      localStorage.removeItem("admin_id");
      localStorage.removeItem("user_type");
    },

    // Restore session from LocalStorage on app load
    restoreSession() {
      const adminId = localStorage.getItem("admin_id");
      const userType = localStorage.getItem("user_type");
      if (adminId && userType) {
        this.isAuthenticated = true;
        this.user = { admin_id: adminId, user_type: userType };
      }
    },
  },
});
