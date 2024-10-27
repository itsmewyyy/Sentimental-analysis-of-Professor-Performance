<template>
  <Toaster />
  <navbar :toggleSidebar="toggleSidebar" />
  <sidebarStudent :isSidebarOpen="isSidebarOpen" />
  <section
    class="transition-all duration-300"
    :class="{
      'ml-72': isSidebarOpen,
      'ml-20': !isSidebarOpen,
    }"
  >
    <section
      class="relative bg-white min-h-screen pt-32 overflow-y-auto p-20 pt-32 space-y-16"
    >
      <div class="pl-8">
        <h1 class="font-semibold text-4xl text-darks-500">Enrolled Courses</h1>
        <p class="font-light text-xl text-darks-300">
          Academic Year 2023 - 2024 2nd Semester
        </p>
      </div>
      <div>
        <subjectComponent></subjectComponent>
      </div>
    </section>
  </section>
</template>

<script setup lang="ts">
import subjectComponent from "@/components/SET/subjectComponent.vue";
import navbar from "@/components/navigation/navbar.vue";
import sidebarStudent from "@/components/navigation/sidebarStudent.vue";
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/store/student";
import { Toaster } from "@/components/ui/toast";

const authStore = useAuthStore();
authStore.restoreSession();

//Sidebar
const isSidebarOpen = ref(false);
function toggleSidebar() {
  isSidebarOpen.value = !isSidebarOpen.value;
}
</script>
