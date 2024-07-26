<template>
    <CardComponent 
      header="A. Teacher " 
      size="3xl" 
      type="white"
    >
      <div class="space-y-6"> 
        <QuestionComponent
          body="Articulates course policies, procedures and gnfdngkdj"
          size="3xl"
          type="yellow-50"
          class="p-4" 
        />
        <QuestionComponent
          body="Question 2"
          size="3xl"
          type="yellow-50"
          class="p-4" 
        />
      </div>
    </CardComponent>
</template>

<script>
import CardComponent from '@/components/CardComponent.vue';
import QuestionComponent from '@/components/QuestionComponent.vue';

export default {
  name: 'ParentComponent',
  components: {
    CardComponent,
    QuestionComponent
  },
};
</script>

<style scoped>
</style>
