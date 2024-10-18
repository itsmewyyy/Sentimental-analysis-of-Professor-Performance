<script setup lang="ts">
import sectionSubject from "@/components/sectionSubject.vue";
import { Plus } from "lucide-vue-next";
</script>

<template>
  <section class="pl-40 rounded pt-32 space-y-24 font-raleway min-h-full">
    <div>
      <div
        class="flex items-center justify-between text-base pl-12 h-14 border-t border-black/25 w-11/12 font-medium text-darks-500 hover:bg-darks-50/80"
      >
        <p class="w-6/12">Subject</p>
        <p class="w-6/12">Section</p>
      </div>
      <div>
        <sectionSubject></sectionSubject>
      </div>
      <button
        class="flex items-center text-base h-14 border-t border-black/25 w-11/12 font-medium text-darks-100 hover:bg-darks-50/80 space-x-1"
      >
        <Plus class="w-5 h-5" />
        <p>New</p>
      </button>
    </div>
  </section>
</template>
