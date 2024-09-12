<template>
  <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar h-screen bg-darks-50"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>

  <section class="max-w-full">
    <section
      class="relative bg-white min-h-screen pt-20 overflow-y-auto font-raleway pb-40 pl-40 pr-8"
    >
      <div
        class="relative bg-darks-50 rounded-3xl w-full pt-12 pb-28 space-y-8 p-20 border border-black/10"
      >
        <div class="flex flex-col space-y-3 text-darks-700">
          <div class="flex flex-row text-4xl space-x-2">
            <h1>You are currently evaluating</h1>
            <h1 class="font-bold text-plpgreen-400">Riegie Tan</h1>
          </div>
          <p class="text-sm font-normal text-darks-200/80">
            Want to evaluate a different instructor? Select a course from the
            dropdown menu and the corresponding professor will be displayed
            automatically.
          </p>
        </div>

        <form action="">
          <div class="space-y-4">
            <div class="flex flex-col items-center space-y-8">
              <cardComponent
                header=" A. The Teacher"
              >
                <template #content>
                  <questioncomponent
                    body="Articulates course policies, procedures, and grading criteria clearly"
                  />
                  <questioncomponent body="Communicates clearly and utilizes synchronous and asynchronous methods effectively." />
                  <questioncomponent body="Demonstrates mastery of the subject matter and effectively relates it to other disciplines." />
                  <questioncomponent body="Stimulates the student to think critically." />
                  <questioncomponent body="Provides timely, constructive feedback to students." />
                 
                </template>
              </cardComponent>
              <cardComponent  header="B. The Module/Learning Materials">
                <template #content>
                  <questioncomponent
                    body="The module/learning materials are clearly structured and well-organized."
                  />
                  <questioncomponent body="The module/learning materials are structured in a logical sequence." />
                  <questioncomponent body="The module/learning materials provide a balanced representation of the course content." />
                  <questioncomponent body="The length and difficulty level of the module/learning materials are appropriate." />
                  <questioncomponent body="The module/learning materials are easily accessible." />
                </template>
              </cardComponent>
              <cardComponent  header="C. The Use of Learning Management System (LMS)">
                <template #content>
                  <questioncomponent
                    body="The teacher creates and manages classes, assignments, and resources on the LMS effectively."
                  />
                  <questioncomponent body="The teacher adds material to the assignments regularly." />
                  <questioncomponent body="The teacher uses the LMS to post announcements and updates promptly." />
                  <questioncomponent body="The teacher engages students in question-driven discussions using the LMS." />
                  <questioncomponent body="The teacher uses a video conferencing app to conduct synchronous classes effectively." />
                </template>
              </cardComponent>
              <cardComponent  header="C-1. The Use of Social Media Platforms (e.g., Facebook, Google Classroom)">
                <template #content>
                  <questioncomponent
                    body="The teacher uses the Social Media platform effectively for class activities."
                  />
                  <questioncomponent body="The teacher communicates regularly using the Social Media platform." />
                  <questioncomponent body="TThe teacher provides opportunities for student interaction on the Social Media platform." />
                  <questioncomponent body="The teacher invites students to post information and resources on the Social Media platform." />
                  <questioncomponent body="The teacher uses the Social Media platform to post important information and updates." />
                </template>
              </cardComponent>
              <cardComponent  header="D. General Observation">
                <template #content>
                  <questioncomponent
                    body="Rapport between teacher and students."
                  />
                  <questioncomponent body="Overall teacher impact." />
                </template>
              </cardComponent>
            </div>
            <div>
            <router-link to = "/SETFeedback">
              <button
                type="button"
                class="text-plpgreen-400 bg-white border border-plpgreen-100 focus:outline-none hover:bg-plpgreen-400 hover:text-white focus:ring-4 focus:ring-gray-100 font-semibold rounded text-sm px-12 py-2.5 me-2 mb-2"
             >
                Next
              </button>
            </router-link>
          </div>
          </div>
        </form>
      </div>
    </section>
  </section>
</template>

<script>
import cardComponent from "@/components/cardNumerical.vue";
import questioncomponent from "@/components/questionComponent.vue";


export default {
  components: {
    cardComponent,
    questioncomponent,
  },
};
</script>

<style scoped>
.w-collapsed-sidebar {
  width: 102px;
}
</style>
