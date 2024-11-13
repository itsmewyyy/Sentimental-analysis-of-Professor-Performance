<template>
  <section class="pt-12 space-y-10">
    <div class="flex flex-row items-center space-x-32">
      <div class="flex flex-col space-y-16">
        <p class="text-2xl font-bold">Feedback Overview</p>
        <CollegeFeedbackChart :refreshChart="refreshChart" />
      </div>
      <div class="text-base flex flex-col pt-3">
        <div class="flex flex-row space-x-2 items-center">
          <p class="font-bold text-lg text-darks-700">Total Feedbacks:</p>
          <p v-if="collegeData" class="text-lg">
            {{ collegeData.feedback_summary[0].total_feedbacks }}
          </p>
        </div>
        <div class="text-lg">
          <p v-if="collegeData">
            {{ collegeData.feedback_summary[0].total_positive }} /

            {{ collegeData.feedback_summary[0].total_feedbacks }} Positive
            Feedbacks
          </p>
          <p v-if="collegeData">
            {{ collegeData.feedback_summary[0].total_neutral }} /
            {{ collegeData.feedback_summary[0].total_feedbacks }} Neutral
            Feedbacks
          </p>
          <p v-if="collegeData">
            {{ collegeData.feedback_summary[0].total_negative }} /
            {{ collegeData.feedback_summary[0].total_feedbacks }} Negative
            Feedbacks
          </p>
        </div>
      </div>
    </div>
    <div>
      <p class="text-xl font-bold pl-1">Recurring Phrases</p>
      <CollegereccuringphrasesTable
        :refreshChart="refreshChart"
      ></CollegereccuringphrasesTable>
    </div>
  </section>
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

interface FeedbackSummary {
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
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
      "https://sentiment-professor-feedback-1.onrender.com/api/college-ratings-summary/"
    );

    if (response.data && Array.isArray(response.data)) {
      const yearsemIdentifier = localStorage.getItem("current_year_sem");
      const collegeIdentifier = localStorage.getItem("college");

      const selectedYearSem = response.data.find(
        (item) => item.year_sem === yearsemIdentifier
      );

      if (selectedYearSem) {
        const selectedCollege = selectedYearSem.colleges.find(
          (college) => college.name === collegeIdentifier
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
