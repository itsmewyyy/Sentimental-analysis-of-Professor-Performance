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
          "https://sentiment-professor-feedback-1.onrender.com/api/register/",
          {
            student_id,
            password,
            confirm_password,
            dateofbirth,
            student_email,
          },
          { withCredentials: true }
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
        const response = await axios.post(
          "https://sentiment-professor-feedback-1.onrender.com/api/login/",
          {
            student_acc_number,
            password,
            dateofbirth,
          },
          { withCredentials: true } // Add this to include cookies
        );

        // Check if the response contains expected data
        if (
          response.data &&
          response.data.student_id &&
          response.data.user_type
        ) {
          this.isAuthenticated = true;
          this.user = response.data;

          // Store relevant user info in LocalStorage
          localStorage.setItem("student_id", response.data.student_id);
          localStorage.setItem("user_type", response.data.user_type);

          return response.data; // Return the response for further use
        } else {
          throw new Error("Login response did not contain expected data.");
        }
      } catch (error) {
        // Handle login failure
        this.isAuthenticated = false;
        this.alertMessage = error.response?.data?.error || "Login failed";
        this.alertType = "error";
        throw error.response?.data; // Throw error for handling in the component
      }
    },

    logout() {
      return axios
        .post(
          "https://sentiment-professor-feedback-1.onrender.com/api/studentLogout/",
          {},
          { withCredentials: true }
        ) // Add withCredentials here
        .then((response) => {
          // If the logout request succeeds, clear the state and local storage
          if (response.status === 200) {
            this.isAuthenticated = false;
            this.user = null;
            localStorage.clear();

            this.alertMessage = "Logged out successfully";
            this.alertType = "success";
          } else {
            // Handle cases where logout was not successful
            console.error("Logout response was not successful:", response);
            this.alertMessage = "Logout failed. Please try again.";
            this.alertType = "error";
          }
        })
        .catch((error) => {
          console.error("Logout API failed:", error);
          this.alertMessage = "Logout failed. Please try again.";
          this.alertType = "error";
        });
    },

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
