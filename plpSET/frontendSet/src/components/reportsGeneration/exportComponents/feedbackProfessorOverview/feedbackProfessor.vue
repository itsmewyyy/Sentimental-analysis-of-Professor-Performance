<template>
  <section class="pt-12 space-y-10">
    <div class="flex flex-row items-center space-x-32">
      <div class="flex flex-col space-y-16">
        <p class="text-2xl font-bold">Feedback Overview</p>
        <professorFeedbackChart :refreshChart="refreshChart" />
      </div>
      <div class="text-base flex flex-col pt-8">
        <div class="flex flex-row space-x-2 items-center">
          <p class="font-bold text-lg text-darks-700">Total Feedbacks:</p>
          <p v-if="professorData" class="text-lg">
            {{ professorData.feedback_summary[0].total_feedbacks }}
          </p>
        </div>
        <div class="text-lg">
          <p v-if="professorData">
            {{ professorData.feedback_summary[0].total_positive }} /

            {{ professorData.feedback_summary[0].total_feedbacks }} Positive
            Feedbacks
          </p>
          <p v-if="professorData">
            {{ professorData.feedback_summary[0].total_neutral }} /
            {{ professorData.feedback_summary[0].total_feedbacks }} Neutral
            Feedbacks
          </p>
          <p v-if="professorData">
            {{ professorData.feedback_summary[0].total_negative }} /
            {{ professorData.feedback_summary[0].total_feedbacks }} Negative
            Feedbacks
          </p>
        </div>
      </div>
    </div>
    <div>
      <p class="text-xl font-bold pl-1">Recurring Phrases</p>
      <profreccuringphrasesTable
        :refreshChart="refreshChart"
      ></profreccuringphrasesTable>
    </div>
    <div>
      <p class="text-xl font-bold pl-1">Feedbacks</p>
      <professorFeedbacksTable
        :refreshChart="refreshChart"
      ></professorFeedbacksTable>
    </div>
  </section>
</template>
<script setup lang="ts">
import { ref, watch } from "vue";
import axios from "axios";
import professorFeedbackChart from "./professorFeedbackChart.vue";
import profreccuringphrasesTable from "./profsrecurringPhrases/profreccuringphrasesTable.vue";
import professorFeedbacksTable from "./feedbacks/professorFeedbacksTable.vue";

interface CategoryAvg {
  category_id: string;
  category_desc: string;
  rating_label?: string;
  average: number;
}

interface NumericalSummary {
  total_avg: number;
  category_avg: CategoryAvg[];
}

interface FeedbackSummary {
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
}

interface Professors {
  id: string;
  name: string;
  dept_id: string;
  dept_desc: string;
  avatarUrl: string;
  feedback_summary: FeedbackSummary[];
  numerical_summary: NumericalSummary;
}

interface Summary {
  year_sem: string;
  professors: Professors[];
}

const props = defineProps({
  refreshChart: Boolean,
  college: String,
  professor: String,
  question: String,
});

const professorData = ref<Professors | null>(null);

watch(
  () => props.refreshChart,
  () => {
    fetchProfessorData();
  }
);

const fetchProfessorData = async () => {
  try {
    const professorIdentifier = localStorage.getItem("professor");
    const collegeIdentifier = localStorage.getItem("college");
    const yearsemIdentifier = localStorage.getItem("current_year_sem");
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/professor-ratings-summary/"
    );

    if (response.data.length && yearsemIdentifier) {
      // Find the year_sem
      const selectedYearSem = response.data.find(
        (summary: Summary) => summary.year_sem === yearsemIdentifier
      );

      if (selectedYearSem) {
        // Find professors within the specified college
        const collegeProfessors = selectedYearSem.professors.filter(
          (professor: Professors) => professor.dept_id === collegeIdentifier
        );

        if (collegeProfessors.length > 0 && professorIdentifier) {
          // Find specific professor within the selected college
          const selectedProfessor = collegeProfessors.find(
            (professorSummary: Professors) =>
              professorSummary.id === professorIdentifier
          );

          if (selectedProfessor) {
            professorData.value = selectedProfessor;
          } else {
            console.error(
              "No matching professor found for the identifier:",
              professorIdentifier
            );
          }
        } else {
          console.error("No professors found for the specified college.");
        }
      } else {
        console.error("No matching year_sem found or invalid identifiers.");
      }
    } else {
      console.error("No data received or year_sem identifier is invalid.");
    }
  } catch (error) {
    console.error("Error fetching professor data:", error);
  }
};
</script>
