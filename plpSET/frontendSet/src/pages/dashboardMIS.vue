<script setup lang="ts">
import submissionChart from "@/components/MIS/submissionChart.vue";
import MISNavbar from "@/components/navigation/NavBarMIS.vue";
</script>

<template>
  <MISNavbar />
  <section class="p-20 pt-20">
    <div class="grid grid-cols-6 grid-rows-7 gap-4 h-[480px]">
      <div class="col-span-2 row-span-2 border border-black/15 rounded-md">
        <div class="p-7">
          <p class="text-sm text-darks-200/50 font-medium">Enrolled Students</p>
        </div>
      </div>
      <div
        class="col-span-2 row-span-2 col-start-3 border border-black/15 rounded-md"
      >
        <div class="p-7">
          <p class="text-sm text-darks-200/50 font-medium">
            Registered Accounts
          </p>
        </div>
      </div>
      <div
        class="col-span-2 row-span-2 col-start-5 border border-black/15 rounded-md"
      >
        <div class="p-7">
          <p class="text-sm text-darks-200/50 font-medium">
            Submitted Evaluations
          </p>
        </div>
      </div>
      <div
        class="col-span-4 row-span-5 row-start-3 border border-black/15 rounded-md"
      ></div>
      <div
        class="col-span-2 row-span-5 col-start-5 row-start-3 border border-black/15 rounded-md"
      ></div>
    </div>
  </section>
</template>
