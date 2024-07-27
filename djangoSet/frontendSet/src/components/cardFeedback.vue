<template>
  <div
    class="flex flex-col round-16 px-28 py-20 space-y-1 bg-plpgreen-100/30 min-w-full"
  >
    <div class="space-y-2 items-center">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardFeedback",
};
</script>

<style scoped>
.round-16 {
  border-radius: 16px;
}
</style>
