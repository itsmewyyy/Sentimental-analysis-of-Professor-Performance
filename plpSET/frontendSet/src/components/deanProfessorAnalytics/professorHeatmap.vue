<template>
  <div id="professorHeatmap" class="transition-all font-roboto w-full"></div>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch, nextTick, onBeforeUnmount } from "vue";
import axios from "axios";
import ApexCharts from "apexcharts";

interface QuestionAvg {
  question_id: string;
  question_desc: string;
  average: number;
}

interface CategoryAvg {
  category_id: string;
  category_desc: string;
  average: number;
  question_avg: QuestionAvg[];
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

const fetchProfessorData = async () => {
  const professorIdentifier = localStorage.getItem("professor");
  const yearsemIdentifier = localStorage.getItem("current_year_sem");
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

const initializeChart = async () => {
  if (chart) {
    chart.destroy();
  }

  const options = {
    series: generateSeriesData(),
    chart: {
      fontFamily: "Roboto",
      height: "100%",
      width: "100%",
      type: "heatmap",
      toolbar: {
        show: false,
        tools: {
          download: false,
        },
      },
    },
    xaxis: {
      labels: {
        show: false,
      },
    },
    dataLabels: {
      enabled: false,
    },
    plotOptions: {
      heatmap: {
        shadeIntensity: 0.5,
        useFillColorAsStroke: false,
      },
    },
    grid: {
      show: false,
      xaxis: { lines: { show: false } },
      yaxis: { lines: { show: false } },
    },
    colors: ["#EBE186"],
  };

  await nextTick();
  const chartElement = document.querySelector("#professorHeatmap");
  if (chartElement) {
    chart = new ApexCharts(chartElement, options);
    await chart.render();
  } else {
    console.error("Chart element not found.");
  }
};

const generateSeriesData = () => {
  if (!professorData.value) return [];

  return professorData.value.numerical_summary.category_avg
    .slice()
    .reverse()
    .map((category) => ({
      name: category.category_desc,
      data: category.question_avg.map((question) => ({
        x: question.question_desc,
        y: question.average,
      })),
    }));
};

onMounted(async () => {
  await fetchProfessorData();
  await initializeChart();
});

watch(professorData, () => {
  if (chart) {
    chart.updateSeries(generateSeriesData());
  }
});

onBeforeUnmount(() => {
  if (chart) {
    chart.destroy();
  }
});
</script>
