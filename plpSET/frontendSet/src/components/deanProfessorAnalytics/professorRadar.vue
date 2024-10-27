<template>
  <div
    id="professorradar"
    class="w-full transition-all font-bold font-roboto"
  ></div>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch, nextTick } from "vue";
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
  numerical_summary: NumericalSummary[];
}

interface Summary {
  year_sem: string;
  professors: Professors[];
}
const professorData = ref<Professors | null>(null);
const professorIdentifier = localStorage.getItem("professor");
const yearsemIdentifier = "24-25-1";
//const yearsemIdentifier = localStorage.getItem("year_sem");

const fetchProfessorData = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/professor-ratings-summary/"
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

const renderChart = (categoryAvg: CategoryAvg[]) => {
  if (!categoryAvg || categoryAvg.length === 0) {
    console.error("No averages available");
    return;
  }

  // Extracting averages for each category
  const averages = categoryAvg.reduce((acc, category) => {
    acc[category.category_id] = category.average;
    return acc;
  }, {} as Record<string, number>);

  // Assigning values per category
  const categoryA = averages["A"] || 0;
  const categoryB = averages["B"] || 0;
  const categoryC = averages["C"] || 0;
  const categoryD = averages["D"] || 0;
  const categoryE = averages["E"] || 0;

  const xAxisCategories = categoryAvg.map((category) => category.category_desc);

  // Prepare the chart options
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
    zoom: {
      enabled: true,
    },
    series: [
      {
        name: "Average Rating",
        data: [categoryA, categoryB, categoryC, categoryD, categoryE],
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
        chart.updateOptions(options);
      } else {
        chart = new ApexCharts(chartElement, options);
        chart.render();
      }
    } else {
      console.error("Chart element still not found.");
    }
  });
};

onMounted(() => {
  fetchProfessorData();
});

watch(professorData, (newprofessor) => {
  if (newprofessor && newprofessor.numerical_summary.length > 0) {
    renderChart(newprofessor.numerical_summary[0].category_avg);
  }
});
</script>
