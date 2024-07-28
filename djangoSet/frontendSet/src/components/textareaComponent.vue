<template>


<div class="px-12 py-8 bg-white rounded-lg space-y-4">
  <label for="textarea-id" class="block text-base font-medium text-darks-800">{{ label }}</label>
  <div class="relative">
    <textarea id="textarea-id" rows="1" style="resize: none;" class="block w-full px-0 text-sm text-darks-800 bg-white border-0 focus:ring-0" placeholder="Write an article..." required></textarea>
    <div class="absolute bottom-0 left-0 w-full h-0.5 bg-gray-100 focus:"></div>
  </div>
</div>

</template>

<script> 
export default {
  name: "TextAreaComponent",
  props: {
    id: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
  
   
  },
 
};
</script>

<style scoped>
</style>





