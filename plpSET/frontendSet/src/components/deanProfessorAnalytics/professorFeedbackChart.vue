<template>
  <div
    v-if="professorData"
    id="professorFeedback"
    class="transition-all font-roboto relative"
  ></div>
  <div v-else>Loading...</div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch, nextTick } from "vue";
import axios from "axios";
import ApexCharts from "apexcharts";

interface QuestionSummary {
  feedback_question: string;
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

interface Professors {
  id: string;
  name: string;
  dept_id: string;
  feedback_summary: FeedbackSummary[];
}

interface Summary {
  year_sem: string;
  professors: Professors[];
}

const professorData = ref<Professors | null>(null);
const professorIdentifier = localStorage.getItem("professor");
const yearsemIdentifier = localStorage.getItem("current_year_sem");

const fetchProfessorData = async () => {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/professor-ratings-summary/"
    );

    if (response.data.length && yearsemIdentifier) {
      // Find the year_sem
      const selectedYearSem = response.data.find(
        (summary: Summary) => summary.year_sem === yearsemIdentifier
      );

      if (selectedYearSem && professorIdentifier) {
        // Within the selected year_sem, find the specific professor
        const selectedProfessor = selectedYearSem.professors.find(
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
        console.error("No matching year_sem found or invalid identifiers.");
      }
    } else {
      console.error("No data received or year_sem identifier is invalid.");
    }
  } catch (error) {
    console.error("Error fetching professor data:", error);
  }
};

let chart: ApexCharts | null = null;

const renderChart = (feedbackSummary: FeedbackSummary[]) => {
  if (!feedbackSummary || feedbackSummary.length === 0) {
    console.error("No feedback summary available");
    return;
  }

  // Access the first item in the feedback_summary array
  const summary = feedbackSummary[0];

  const totalFeedbacks = Number(summary.total_feedbacks) || 1;
  const totalPositive = Number(summary.total_positive);
  const totalNeutral = Number(summary.total_neutral);
  const totalNegative = Number(summary.total_negative);

  const options = {
    series: [
      (totalPositive / totalFeedbacks) * 100,
      (totalNeutral / totalFeedbacks) * 100,
      (totalNegative / totalFeedbacks) * 100,
    ],
    chart: {
      fontFamily: "Roboto",
      type: "donut",
      height: "100%",
      width: "100%",
    },
    labels: ["Positive", "Neutral", "Negative"],
    colors: ["#77A275", "#ECCC35", "#B40D0D"],
    dataLabels: {
      enabled: false,
    },
    tooltip: {
      enabled: true,
      y: {
        formatter: function (val, { seriesIndex }) {
          const totals = [totalPositive, totalNeutral, totalNegative];
          return `${val.toFixed(2)}% <br>${
            totals[seriesIndex]
          } of ${totalFeedbacks} feedbacks`;
        },
        title: {
          formatter: function () {
            return "";
          },
        },
      },
      style: {
        fontSize: "12px",
        fontFamily: "Roboto",
      },
    },
    legend: {
      position: "right",
      offsetY: 50,
      offsetX: 20,
      fontSize: "13px",
      fontWeight: 400,
      fontFamily: "Roboto",
      verticalAlign: "center",
    },
  };

  nextTick(() => {
    const chartElement = document.querySelector("#professorFeedback");
    if (chartElement) {
      if (chart) {
        chart.updateOptions(options);
      } else {
        chart = new ApexCharts(chartElement, options);
        chart.render();
      }
    } else {
      console.error("Chart element not found.");
    }
  });
};

onMounted(() => {
  fetchProfessorData();
});

watch(professorData, (newProfessor) => {
  if (newProfessor) {
    renderChart(newProfessor.feedback_summary);
  }
});
</script>
