<template>
  <div
    class="rounded-lg flex flex-row items-center content-center bg-white p-4 min-w-full"
  >
    <div class="pt-4 flex-1 pl-2 question">
      <span v-if="body" class="mb-3 font-medium text-darks-800 block">{{ body }}</span>
      <span v-else class="mb-3 font-medium text-darks-800 block">No question available</span>
    </div>
    
    <div class="flex items-center space-x-20 p-4">
      <input type="radio" :value="1" v-model="selected" class="radio-large text-plpgreen-400 focus:ring-plpgreen-200" />
      <input type="radio" :value="2" v-model="selected" class="radio-large text-plpgreen-200 focus:ring-plpgreen-200" />
      <input type="radio" :value="3" v-model="selected" class="radio-large text-plpgreen-200 focus:ring-plpgreen-200" />
      <input type="radio" :value="4" v-model="selected" class="radio-large text-plpgreen-200 focus:ring-plpgreen-200" />
      <input type="radio" :value="5" v-model="selected" class="radio-large text-plpgreen-200 focus:ring-plpgreen-200" />
    </div>
  </div>
</template>

<script>
export default {
  name: "questionComponent",
  data() {
    return {
      selected: null,
    };
  },
  props: {
    body: String,
  },


};
</script>

<style scoped>
.radio-large {
  width: 22px;
  height: 22px;
  

}
</style>
