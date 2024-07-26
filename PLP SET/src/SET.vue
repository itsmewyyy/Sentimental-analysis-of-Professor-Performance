<template>
  <section class="font-raleway">
     <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
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
          <QuestionComponent
          body="Question 2"
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
          <QuestionComponent
          body="Question 2"
          size="3xl"
          type="yellow-50"
          class="p-4" 
        />

      </div>
    </CardComponent>
    </section>
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
