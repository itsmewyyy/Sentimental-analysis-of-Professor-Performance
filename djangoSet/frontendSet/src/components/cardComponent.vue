<template>
  <div
    class="flex flex-col round-16 px-28 py-20 space-y-1 bg-plpgreen-100/30 min-w-full"
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
.header-container {
  padding-top: 1rem; /* Add top padding */
  padding-left: 1rem; /* Add left padding */
}

/* Position the number container in the upper-right corner of the card */
.number-container {
  position: absolute;
  top: 1rem; /* Adjust top spacing as needed */
  right: 1rem; /* Adjust right spacing as needed */
}

.round-16 {
  border-radius: 16px;
}
</style>
