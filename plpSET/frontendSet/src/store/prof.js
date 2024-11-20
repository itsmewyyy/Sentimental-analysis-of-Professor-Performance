import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStoreProf = defineStore("prof", {
  state: () => ({
    isAuthenticated: false,
    user: null,
    college: null, // Store college information here
  }),
  actions: {
    async register(professor_id, professor_email, password, confirm_password) {
      try {
        const response = await axios.post(
          "https://sentiment-professor-feedback-1.onrender.com/api/profregister/",
          {
            professor_id,
            professor_email,
            password,
            confirm_password,
          },
          { withCredentials: true }
        );
        this.user = response.data.prof;
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

        localStorage.setItem("professor", professor_id);

        // Fetch college data after login
        await this.fetchCollege(professor_id);

        return response.data;
      } catch (error) {
        this.isAuthenticated = false;
        throw error.response.data;
      }
    },

    async fetchCollege(professor_id) {
      try {
        const response = await axios.get(
          "https://sentiment-professor-feedback-1.onrender.com/api/professor-list/",
          { withCredentials: true }
        );

        // Match the professor account number to fetch college
        const professor = response.data.find(
          (prof) => prof.professor_id === professor_id
        );

        if (professor) {
          this.department = professor.department;
          localStorage.setItem("college", professor.department);
        } else {
          throw new Error("College not found for this professor");
        }
      } catch (error) {
        console.error("Failed to fetch college:", error);
        throw error;
      }
    },

    logout() {
      this.isAuthenticated = false;
      this.user = null;
      this.department = null;
      localStorage.clear();

      return axios
        .post(
          "https://sentiment-professor-feedback-1.onrender.com/api/profLogout/",
          {},
          { withCredentials: true }
        )
        .then(() => {
          console.log("Logged out successfully");
        })
        .catch((error) => {
          console.error("Logout API failed:", error);
        });
    },

    restoreSession() {
      const profId = localStorage.getItem("professor");
      const college = localStorage.getItem("college");

      if (profId) {
        this.isAuthenticated = true;
        this.user = { professor_id: profId };
        this.college = college;
      }
    },
  },
});
