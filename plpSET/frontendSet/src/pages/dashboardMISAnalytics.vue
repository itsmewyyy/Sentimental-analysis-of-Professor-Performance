<script setup lang="ts">
import collegesAnalytics from "@/components/MIS/collegesAnalytics.vue";
import MISNavbar from "@/components/navigation/NavBarMIS.vue";
</script>

<template>
  <MISNavbar></MISNavbar>
  <section class="p-20 pt-32">
    <div class="pl-6 pb-10">
      <h3 class="text-4xl font-bold">Colleges</h3>
      <p class="text-darks-200/75 font-medium text-base">
        Click on a College to View Analytics
      </p>
    </div>
    <div class="flex flex-wrap">
      <collegesAnalytics></collegesAnalytics>
    </div>
  </section>
</template>
