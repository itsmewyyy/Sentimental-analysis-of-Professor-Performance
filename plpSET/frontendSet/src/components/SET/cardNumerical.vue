<template>
  <div class="flex flex-col px-12 py-2 space-y-3.5 w-full">
    <div class="space-y-10">
      <div class="font-bold text-darks-400">
        <div class="flex text-2xl">
          <div>{{ header }}</div>
        </div>
      </div>
      <div class="flex flex-row font-bold">
        <div class="flex-1"></div>
        <div
          class="flex items-center space-x-16 pr-9 pb-2 text-darks-500 text-sm"
        >
          <p id="5">5</p>
          <p id="4">4</p>
          <p id="3">3</p>
          <p id="2">2</p>
          <p id="1">1</p>
        </div>
      </div>
    </div>

    <div class="items-center">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "cardComponent",

  props: {
    header: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped></style>
