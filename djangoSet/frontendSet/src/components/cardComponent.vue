<template>
  <div
    class="flex flex-col rounded-xl px-28 py-20 space-y-1 bg-plpgreen-100/30 min-w-full"
  >
    <div class="space-y-16">
      <div class="ml-4 font-bold text-darks-800">
        <div v-if="header" class="flex text-2xl">
          <div>{{ header }}</div>
        </div>
      </div>
      <div class="flex flex-row font-bold">
        <div class="flex-1"></div>
        <div class="flex items-center space-x-24 mr-12 pb-2 text-darks-700">
          <p>5</p>
          <p>4</p>
          <p>3</p>
          <p>2</p>
          <p>1</p>
        </div>
      </div>
    </div>

    <div class="space-y-2 items-center">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardComponent",
  props: {
    header: String,
  },
};
</script>

<style scoped>

</style>
