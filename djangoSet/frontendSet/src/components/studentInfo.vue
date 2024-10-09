<script setup lang="ts">
import { defineProps } from "vue";
import { Pen } from "lucide-vue-next";
import { Trash } from "lucide-vue-next";

const props = defineProps<{
  student_id: string;
  name: string;
  section: string;
}>();
</script>

<template>
  <div
    class="h-14 border-t border-black/25 flex items-center justify-center align-center p-6"
  >
    <!-- Student list items -->
    <div class="flex space-x-8" :id="student_id">
      <div class="flex space-x-44 text-sm font-medium">
        <p class="w-32">{{ student_id }}</p>
        <p class="w-72">{{ name }}</p>
        <p class="w-28">{{ section }}</p>
        <div class="flex space-x-5">
          <!-- Edit Button -->
          <button class="z-40 hover:scale-125">
            <Pen color="#5F965E" class="w-4 h-4" />
          </button>
          <!-- Delete Button -->
          <button class="z-40 hover:scale-125">
            <Trash color="#B40D0D" class="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
