<template>
  <div
    class="flex flex-col rounded-2xl px-24 py-11 space-y-1 bg-plpgreen-100/35 w-full"
  >
    <div class="space-y-16">
      <div class="ml-2 font-bold text-darks-800">
        <div class="flex text-xl">
          <div>{{ header }}</div>
        </div>
      </div>
      <div class="flex flex-row font-bold">
        <div class="flex-1"></div>
        <div class="flex items-center space-x-24 mr-8 pb-4 text-darks-700">
          <p id = "5">5</p>
          <p id = "4">4</p>
          <p id = "3">3</p>
          <p id = "2">2</p>
          <p id = "1">1</p>
        </div>
      </div>
    </div>

    <div class="space-y-2 items-center">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "cardComponent",

  props:{
    header: {
      type: String,
      required: true
    }
  }
 

};
</script>

<style scoped>

</style>
