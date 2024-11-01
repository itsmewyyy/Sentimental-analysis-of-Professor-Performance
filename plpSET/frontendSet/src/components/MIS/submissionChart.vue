<template>
  <div id="charts"></div>
</template>

<script setup lang="ts">
import { onMounted, defineComponent, ref } from "vue";
import ApexCharts from "apexcharts";
let chart: ApexCharts | null = null;
const initializeChart = async () => {
  if (chart) {
    chart.destroy();
  }
  const options = {
    series: [
      {
        name: "Submissions",
        data: [10, 41, 35, 51, 49, 62, 69, 91, 148],
      },
    ],
    chart: {
      fontFamily: "Roboto",
      height: "80%",
      width: "100%",
      type: "line",
      zoom: {
        enabled: false,
      },
      toolbar: {
        show: false,
        tools: {
          download: false,
        },
      },
    },
    colors: ["#5F965E"],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "smooth",
    },
    grid: {
      row: {
        colors: ["#fff", "transparent"],
        opacity: 0.5,
      },
    },
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
      ],
    },
  };

  chart = new ApexCharts(document.querySelector("#charts"), options);
  await chart.render();
};

onMounted(async () => {
  initializeChart();
});
</script>
