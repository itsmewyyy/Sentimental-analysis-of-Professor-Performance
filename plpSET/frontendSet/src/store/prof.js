import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStoreProf = defineStore("prof", {
  state: () => ({
    isAuthenticated: false,
    user: null,
  }),
  actions: {
    async register(professor_id, password, confirm_password, professor_email) {
      try {
        const response = await axios.post(
          "https://sentiment-professor-feedback-1.onrender.com/api/profregister/",
          {
            professor_id,
            password,
            confirm_password,
            professor_email,
          },
          { withCredentials: true }
        );
        this.userInfo = response.data.prof;
        return response.data;
      } catch (error) {
        console.error(error);
        throw error.response.data;
      }
    },

    async login(professor_id, password) {
      try {
        const response = await axios.post(
          "https://sentiment-professor-feedback-1.onrender.com/api/profLogin/",
          {
            professor_id,
            password,
          },
          { withCredentials: true }
        );
        this.isAuthenticated = true;
        this.user = response.data;

        localStorage.setItem("professor", response.data.professor_id);
        localStorage.setItem("college", response.data.college);

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

      return axios
        .post(
          "https://sentiment-professor-feedback-1.onrender.com/api/profLogout/",
          {},
          { withCredentials: true }
        )
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
      const profId = localStorage.getItem("professor");
      const deptId = localStorage.getItem("college");

      if (adminId && userType) {
        this.isAuthenticated = true;
        this.user = {
          professor_id: profId,
          user_type: userType,
          dept_id: deptId,
        };
      }
    },
  },
});
