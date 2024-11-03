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

const props = defineProps({
  refreshChart: Boolean,
});

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

interface College {
  id: string;
  name: string;
  professors: Professors[];
}

interface Summary {
  year_sem: string;
  colleges: College[];
}

watch(
  () => props.refreshChart,
  () => {
    fetchProfessorData();
  }
);

const professorData = ref<Professors | null>(null);

const fetchProfessorData = async () => {
  try {
    const professorIdentifier = localStorage.getItem("professor");
    const collegeIdentifier = localStorage.getItem("college");
    const yearsemIdentifier = localStorage.getItem("current_year_sem");
    const response = await axios.get(
      "http://127.0.0.1:8000/api/professor-ratings-summary/"
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
      enabled: true,
      style: {
        fontSize: "28px",
        fontWeight: "bold",
        colors: ["#333"],
      },
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
      position: "left",
      offsetY: 40,
      offsetX: -20,
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
