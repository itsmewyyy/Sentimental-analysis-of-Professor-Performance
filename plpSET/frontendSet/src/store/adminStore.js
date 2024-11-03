// store/adminStore.js
import { defineStore } from "pinia";
import axios from "axios";
import axiosInstance from "@/axios-config";

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
        const response = await axiosInstance.post(
          "/api/adminLogin/",
          {
            adminUsername,
            password,
          },
          { withCredentials: true }
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
      // Clear user data and local storage
      this.isAuthenticated = false;
      this.user = null;
      localStorage.clear();

      // Call the backend API to complete the logout process
      return axiosInstance
        .post("/api/adminLogout/", {}, { withCredentials: true }) // Explicitly set withCredentials
        .then(() => {
          this.alertMessage = "Logged out successfully";
          this.alertType = "success";
        })
        .catch((error) => {
          console.error("Logout API failed:", error);
          this.alertMessage = "Logout failed";
          this.alertType = "error";
        });
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
