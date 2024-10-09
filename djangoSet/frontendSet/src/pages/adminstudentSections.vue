<template>
    <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar h-screen bg-darks-50"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>
    <div class="fixed top-0 z-40 h-navbar w-full bg-darks-100"></div>
    
    
 <section class="pl-44 pt-32 space-y-40 font-raleway overflow-hidden">
    <div class="flex flex-wrap w-fit">
        <collegeDropdown></collegeDropdown>
      
    </div>
 </section>   
   


</template>

<script setup lang = "ts">
import collegeDropdown from '@/components/collegesDropdown.vue';
</script>

<style scoped>
.w-collapsed-sidebar {
  width: 76px;
}
.h-navbar{
    height: 64px;
}
</style>
