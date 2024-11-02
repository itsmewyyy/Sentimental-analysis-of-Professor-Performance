<template>
  <div>college question overview</div>
</template>
<script setup lang="ts">
import CollegeFeedbackChart from "@/components/reportsGeneration/exportComponents/collegeFeedbackOverview/collegeFeedbackChart.vue";
import CollegereccuringphrasesTable from "@/components/reportsGeneration/exportComponents/collegeFeedbackOverview/collegerecurringPhrases/collegereccuringphrasesTable.vue";
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

interface FeedbackSummary {
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
  question_summary: QuestionSummary[];
}

interface NumericalSummary {
  total_avg: number;
}

interface College {
  name: string;
  description: string;
  feedback_summary: FeedbackSummary[];
  numerical_summary: NumericalSummary[];
}

interface Summary {
  year_sem: string;
  summary: College[];
}

const collegeData = ref<College | null>(null);

watch(
  () => props.refreshChart,
  () => {
    fetchCollegeData();
  }
);

const fetchCollegeData = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/college-ratings-summary/"
    );

    if (response.data && response.data.summary) {
      const yearsemIdentifier = localStorage.getItem("current_year_sem");
      const collegeIdentifier = localStorage.getItem("college");

      const selectedYearSem = response.data.year_sem === yearsemIdentifier;

      if (selectedYearSem) {
        const selectedCollege = response.data.summary.find(
          (collegeSummary: College) => collegeSummary.name === collegeIdentifier
        );

        if (selectedCollege) {
          collegeData.value = selectedCollege;
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
