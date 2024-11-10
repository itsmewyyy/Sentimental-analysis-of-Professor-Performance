<template>
  <div class="pt-16">
    <professornumericalTable
      :refreshChart="refreshChart"
    ></professornumericalTable>
  </div>
</template>
<script setup lang="ts">
import professornumericalTable from "./professornumericalTable.vue";
defineProps({
  college: String,
  professor: String,
  question: String,
  refreshChart: Boolean,
});
</script>
