<template>
  <div
    v-if="collegeData"
    id="collegeFeedback"
    class="transition-all font-roboto relative"
  ></div>
  <div v-else>Loading...</div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch, nextTick, onBeforeUnmount } from "vue";
import axios from "axios";
import ApexCharts from "apexcharts";

interface FeedbackSummary {
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
}

interface College {
  name: string;
  description: string;
  feedback_summary: FeedbackSummary[];
}

interface Summary {
  year_sem: string;
  summary: College[];
}

const collegeData = ref<College | null>(null);

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

let chart: ApexCharts | null = null;

const renderChart = (feedbackSummary: FeedbackSummary[]) => {
  if (!feedbackSummary || feedbackSummary.length === 0) {
    console.error("No feedback summary available");
    return;
  }

  // Access the first item in the feedback_summary array
  const summary = feedbackSummary[0];

  console.log("Rendering chart with data:", summary); // Check if we get feedback data

  const totalFeedbacks = Number(summary.total_feedbacks) || 1;
  const totalPositive = Number(summary.total_positive);
  const totalNeutral = Number(summary.total_neutral);
  const totalNegative = Number(summary.total_negative);

  // Log the data for debugging
  console.log({
    totalFeedbacks,
    totalPositive,
    totalNeutral,
    totalNegative,
    series: [
      (totalPositive / totalFeedbacks) * 100,
      (totalNeutral / totalFeedbacks) * 100,
      (totalNegative / totalFeedbacks) * 100,
    ],
  });

  const options = {
    series: [
      (totalPositive / totalFeedbacks) * 100,
      (totalNeutral / totalFeedbacks) * 100,
      (totalNegative / totalFeedbacks) * 100,
    ],
    chart: {
      type: "donut",
      height: "100%",
      width: "100%",
      fontFamily: "Roboto",
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
      position: "bottom",
      offsetY: 0,
      fontSize: "14px",
      fontWeight: 400,
      fontFamily: "Roboto",
      horizontalAlign: "center",
    },
  };

  nextTick(() => {
    const chartElement = document.querySelector("#collegeFeedback");
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
  fetchCollegeData();
});

watch(collegeData, (newCollege) => {
  if (newCollege) {
    renderChart(newCollege.feedback_summary);
  }
});

onBeforeUnmount(() => {
  if (chart) {
    chart.destroy();
  }
});
</script>
