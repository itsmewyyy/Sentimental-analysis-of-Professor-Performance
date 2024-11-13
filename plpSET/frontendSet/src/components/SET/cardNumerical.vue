<template>
  <div class="flex flex-col px-4 sm:px-8 lg:px-12 py-2 space-y-3.5 w-full">
    <div class="space-y-6 sm:space-y-8 lg:space-y-10">
      <div class="font-bold text-darks-400">
        <div class="flex text-lg sm:text-xl lg:text-2xl">
          <div>{{ header }}</div>
        </div>
      </div>
      <div class="flex flex-row font-bold">
        <div class="flex-1"></div>
        <div
          class="flex items-center space-x-4 sm:space-x-8 lg:space-x-16 pr-4 sm:pr-6 lg:pr-5 pb-2 text-darks-500 text-lg"
        >
          <div class="items-center flex flex-col">
            <p class="text-xs">SA</p>
            <p id="5">5</p>
          </div>
          <div class="items-center flex flex-col">
            <p class="text-xs">A</p>
            <p id="4">4</p>
          </div>
          <div class="items-center flex flex-col">
            <p class="text-xs">N</p>
            <p id="3">3</p>
          </div>
          <div class="items-center flex flex-col">
            <p class="text-xs">D</p>
            <p id="2">2</p>
          </div>
          <div class="items-center flex flex-col">
            <p class="text-xs">SD</p>
            <p id="1">1</p>
          </div>
        </div>
      </div>
    </div>

    <div class="items-center">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineEmits, defineProps, ref, onMounted } from "vue";

const props = defineProps<{
  header: string;
}>();
</script>
