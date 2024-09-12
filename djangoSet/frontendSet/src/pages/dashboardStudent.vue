<template>
    <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar h-screen bg-darks-50"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>
    <section  class="relative bg-white min-h-screen pt-20 overflow-y-auto font-raleway pb-40 pl-40 pr-12 space-y-10">
        <studentinfoComponent></studentinfoComponent>
        <studentcoursesComponent></studentcoursesComponent>
    </section>
</template>

<script>
import studentinfoComponent from '@/components/studentinfoComponent.vue';
import studentcoursesComponent from '@/components/studentcoursesComponent.vue';



export default {
  components: {
    studentinfoComponent,
    studentcoursesComponent,
  },
};
</script>

<style scoped>
.w-collapsed-sidebar {
  width: 102px;
}
</style>


