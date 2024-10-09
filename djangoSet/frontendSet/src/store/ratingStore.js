import { defineStore } from "pinia";

export const useRatingsStore = defineStore("ratings", {
  state: () => ({
    numericalRatings: {}, // Holds the ratings from the numerical page
    feedbackRatings: {}, // Holds feedback ratings from the feedback page
    studentEnrolledSubjId: null, // Holds the student enrolled subject ID
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
      this.studentEnrolledSubjId = null; // Clear the subject ID as well
    },
  },
});
