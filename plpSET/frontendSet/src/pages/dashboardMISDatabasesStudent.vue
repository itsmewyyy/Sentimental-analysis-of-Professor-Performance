<template>
  <MISNavbar></MISNavbar>
  <section class="p-20 pt-14">
    <div class="pl-6 pb-10">
      <h3 class="text-4xl font-bold">Colleges</h3>
      <p class="text-darks-200/75 font-medium text-base">
        This is a sample text Lorem Ipsum Dolor Sip
      </p>
    </div>
    <div class="flex flex-wrap">
      <collegeDropdown></collegeDropdown>
    </div>
  </section>
</template>

<script setup lang="ts">
import collegeDropdown from "@/components/databaseStudent/collegesDropdown.vue";
import MISNavbar from "@/components/navigation/NavBarMIS.vue";
</script>
