<template>
  <section class="pt-12 space-y-10">
    <div class="space-y-4">
      <div class="flex flex-col">
        <p class="text-2xl font-bold">Feedback Overview</p>
        <CollegeFeedbackChart :refreshChart="refreshChart" />
      </div>
      <div class="text-base flex flex-col">
        <div class="flex flex-row space-x-2 items-center">
          <p class="font-bold text-lg text-darks-700">Total Feedbacks:</p>
          <p v-if="collegeData" class="text-lg">
            {{ collegeData.total_feedbacks }}
          </p>
        </div>
        <div class="text-lg">
          <p v-if="collegeData">
            {{ collegeData.total_positive }} /
            {{ collegeData.total_feedbacks }} Positive Feedbacks
          </p>
          <p v-if="collegeData">
            {{ collegeData.total_neutral }} /
            {{ collegeData.total_feedbacks }} Neutral Feedbacks
          </p>
          <p v-if="collegeData">
            {{ collegeData.total_negative }} /
            {{ collegeData.total_feedbacks }} Negative Feedbacks
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import CollegeFeedbackChart from "@/components/reportsGeneration/exportComponents/collegeFeedbackQuestionOverview/collegeFeedbackChart.vue";
import axios from "axios";
import { ref, watch } from "vue";

const props = defineProps({
  refreshChart: Boolean,
  college: String,
  professor: String,
  question: String,
});

interface QuestionSummary {
  question_id: string;
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
}

const collegeData = ref<QuestionSummary | null>(null);

watch(
  () => props.refreshChart,
  () => {
    fetchCollegeData();
  }
);

const fetchCollegeData = async () => {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/pi/college-ratings-summary/"
    );
    console.log("API Response:", response.data);

    if (response.data && response.data.summary) {
      const yearsemIdentifier = localStorage.getItem("current_year_sem");
      const collegeIdentifier = localStorage.getItem("college");
      const questionIdentifier = localStorage.getItem("question");

      // Filter based on the year_sem
      const selectedYearSem = response.data.year_sem === yearsemIdentifier;

      if (selectedYearSem) {
        const selectedCollege = response.data.summary.find(
          (collegeSummary: any) => collegeSummary.name === collegeIdentifier
        );

        if (selectedCollege) {
          // Filter for specific question summary
          const questionSummary =
            selectedCollege.feedback_summary[0].question_summary.find(
              (question: QuestionSummary) =>
                question.question_id === questionIdentifier
            );

          if (questionSummary) {
            collegeData.value = questionSummary;
          } else {
            console.error(
              "No matching question found for identifier:",
              questionIdentifier
            );
          }
        } else {
          console.error(
            "No matching college found for the identifier:",
            collegeIdentifier
          );
        }
      } else {
        console.error(
          "No matching year_sem found for identifier:",
          yearsemIdentifier
        );
      }
    } else {
      console.error("No data received or invalid year_sem identifier.");
    }
  } catch (error) {
    console.error("Error fetching college data:", error);
  }
};
</script>
