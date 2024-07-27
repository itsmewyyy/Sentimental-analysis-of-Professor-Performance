<template>
  
      
  <div
    class="flex flex-col rounded-2xl px-28 pt-8 pb-20 space-y-8 bg-plpgreen-100/35 min-w-full"
  >
      <div class="ml-2 font-bold text-darks-800 text-xl">
          Feedback Questionnaire
          
        </div>
  
 
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

</style>
