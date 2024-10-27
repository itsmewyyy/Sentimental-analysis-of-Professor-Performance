<template>
  <MISNavbar></MISNavbar>
  <section class="p-20 pt-32 space-y-40 overflow-hidden">
    <div class="flex flex-wrap w-fit">
      <collegeDropdown></collegeDropdown>
    </div>
  </section>
</template>

<script setup lang="ts">
import collegeDropdown from "@/components/databaseStudent/collegesDropdown.vue";
import MISNavbar from "@/components/navigation/MISNavbar.vue";
</script>
