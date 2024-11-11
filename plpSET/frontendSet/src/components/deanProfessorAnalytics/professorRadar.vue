<template>
  <div
    id="professorradar"
    class="w-full transition-all font-bold font-roboto"
  ></div>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch, nextTick, onBeforeUnmount } from "vue";
import axios from "axios";
import ApexCharts from "apexcharts";

interface CategoryAvg {
  category_id: string;
  category_desc: string;
  rating_label: string;
  average: number;
}

interface NumericalSummary {
  total_avg: number;
  category_avg: CategoryAvg[];
}

interface Professors {
  id: string;
  name: string;
  dept_id: string;
  numerical_summary: NumericalSummary;
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
      const selectedYearSem = response.data.find(
        (summary: Summary) => summary.year_sem === yearsemIdentifier
      );

      if (selectedYearSem && professorIdentifier) {
        const selectedProfessor = selectedYearSem.professors.find(
          (professorSummary: Professors) =>
            professorSummary.id === professorIdentifier
        );

        if (selectedProfessor) {
          professorData.value = selectedProfessor;
          console.log("Professor Data:", professorData.value);
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

const renderChart = (categoryAvg: CategoryAvg[]) => {
  if (!categoryAvg || categoryAvg.length === 0) {
    console.error("No averages available");
    return;
  }

  const averages = categoryAvg.reduce((acc, category) => {
    acc[category.category_id] = category.average;
    return acc;
  }, {} as Record<string, number>);

  const dataSeries = [
    averages["A"] || 0,
    averages["B"] || 0,
    averages["C"] || 0,
    averages["D"] || 0,
    averages["E"] || 0,
  ];

  const xAxisCategories = categoryAvg.map((category) => category.category_desc);

  const options = {
    chart: {
      type: "radar",
      height: "100%",
      width: "100%",
      fontFamily: "Roboto",
      toolbar: {
        show: false,
        tools: {
          download: false,
        },
      },
    },
    series: [
      {
        name: "Average Rating",
        data: dataSeries,
      },
    ],
    xaxis: {
      categories: xAxisCategories,
      labels: {
        show: false,
      },
    },
    stroke: {
      show: true,
      width: 1,
      colors: ["#C9D8C2"],
      dashArray: 0,
    },
    markers: {
      size: 4,
      hover: {
        size: 5,
      },
    },
    fill: {
      opacity: 0.4,
      colors: ["#C9D8C2"],
    },
    plotOptions: {
      radar: {
        polygons: {
          fill: {
            colors: ["#f8f8f8", "#fff"],
          },
        },
      },
    },
  };

  nextTick(() => {
    const chartElement = document.querySelector("#professorradar");
    if (chartElement) {
      if (chart) {
        chart.destroy(); // Destroy previous instance if exists
      }
      chart = new ApexCharts(chartElement, options);
      chart.render();
    } else {
      console.error("Chart element not found.");
    }
  });
};

onMounted(() => {
  fetchProfessorData();
});

watch(professorData, (newProfessor) => {
  if (
    newProfessor &&
    newProfessor.numerical_summary &&
    Array.isArray(newProfessor.numerical_summary.category_avg) &&
    newProfessor.numerical_summary.category_avg.length > 0
  ) {
    renderChart(newProfessor.numerical_summary.category_avg);
  }
});

onBeforeUnmount(() => {
  if (chart) {
    chart.destroy(); // Clean up the chart instance on component unmount
  }
});
</script>
