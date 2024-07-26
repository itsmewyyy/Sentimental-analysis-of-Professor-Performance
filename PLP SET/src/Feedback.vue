<template>
    <section class="font-raleway">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
  <div>

    <CardFeedback
    header="Feedback Questionare"
    size="3xl"
    type="yellow-50">

    <TextAreaComponent
      id="feedback"
      label="1. How do you feel under his/her class?"
      placeholder="Write your feedback here..."
      rows="default"
      cols="default"
      size="md"
      color="blue-50"
    />
    
    
    <TextAreaComponent
      id="feedback"
      label="2. huwasap"
      placeholder="Write your feedback here..."
      rows="default"
      cols="60"
      size="md"
      color="blue-50"
    />

    
    <TextAreaComponent
      id="feedback"
      label="Feedback"
      placeholder="Write your feedback here..."
      rows="default"
      cols="60"
      size="md"
      color="blue-50"
    />

    <TextAreaComponent
      id="feedback"
      label="Feedback"
      placeholder="Write your feedback here..."
      rows="default"
      cols="60"
      size="md"
      color="blue-50"
    />
    <TextAreaComponent
      id="feedback"
      label="Feedback"
      placeholder="Write your feedback here..."
      rows="default"
      cols="60"
      size="md"
      color="blue-50"
    />
    </CardFeedback>

  </div>
  </section>
</template>

<script>
import CardFeedback from './components/CardFeedback.vue';
import TextAreaComponent from './components/TextAreaComponent.vue'; // Adjusted path

export default {
  components: {
    TextAreaComponent,
    CardFeedback
  }
};
</script>
