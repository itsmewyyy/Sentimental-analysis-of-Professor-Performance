<template>
  <div id="radar" class="w-full transition-all font-bold font-roboto"></div>
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

interface College {
  name: string;
  description: string;
  numerical_summary: NumericalSummary[];
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
    console.log("API Response:", response.data);

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
    const chartElement = document.querySelector("#radar");
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

// Fetch data and initialize the chart when the component is mounted
onMounted(() => {
  fetchCollegeData();
});

onBeforeUnmount(() => {
  if (chart) {
    chart.destroy(); // Clean up the chart instance on component unmount
  }
});
// Watch for changes in collegeData and update the chart accordingly
watch(collegeData, (newCollege) => {
  if (newCollege && newCollege.numerical_summary.length > 0) {
    renderChart(newCollege.numerical_summary[0].category_avg);
  }
});
</script>
