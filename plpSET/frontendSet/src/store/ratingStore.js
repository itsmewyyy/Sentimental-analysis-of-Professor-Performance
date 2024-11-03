import { defineStore } from "pinia";
import axios from "axios"; // Import axios to make API calls

export const useRatingsStore = defineStore("ratings", {
  state: () => ({
    numericalRatings: {}, // Holds the ratings from the numerical page
    feedbackRatings: {}, // Holds feedback ratings from the feedback page
    studentEnrolledSubjId: "", // Holds the student enrolled subject ID
    alertMessage: "", // Holds the alert message
    alertType: "", // Holds the alert type (success or error)
  }),
  actions: {
    // Set numerical rating for a specific question
    setNumericalRating(questionId, rating) {
      this.numericalRatings[questionId] = rating;
    },

    // Set feedback for a specific question
    setFeedbackRating(questionId, feedback) {
      this.feedbackRatings[questionId] = feedback;
    },

    // Set student enrolled subject ID
    setStudentEnrolledSubjId(id) {
      this.studentEnrolledSubjId = id;
    },

    // Clear both numerical and feedback ratings
    clearAllRatings() {
      this.numericalRatings = {};
      this.feedbackRatings = {};
      this.studentEnrolledSubjId = "";
      this.alertMessage = "";
      this.alertType = "";
    },

    // Submit ratings to the backend
    async submitRatings() {
      try {
        const response = await axios.post(
          "http://localhost:8000/api/submit-ratings/",
          {
            numericalRatings: this.numericalRatings,
            feedbackRatings: this.feedbackRatings,
            studentEnrolledSubjId: this.studentEnrolledSubjId,
          },
          { withCredentials: true }
        );

        return response.data;
      } catch (error) {
        throw error;
      }
    },
  },
});
