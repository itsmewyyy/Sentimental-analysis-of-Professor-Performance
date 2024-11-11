<template>
  <Toaster />
  <navbar />
  <ScrollArea class="h-svh w-full">
    <section
      class="relative bg-white min-h-screen overflow-y-auto p-20 pt-32 space-y-16 w-full"
    >
      <div class="pl-8">
        <h1 class="font-semibold text-4xl text-darks-500">Enrolled Courses</h1>
        <p class="font-light text-xl text-darks-300">
          Start Evaluating your professors.
        </p>
      </div>
      <div>
        <subjectComponent></subjectComponent>
      </div>
    </section>
  </ScrollArea>
</template>

<script setup lang="ts">
import subjectComponent from "@/components/SET/subjectComponent.vue";
import navbar from "@/components/navigation/NavBarStudent.vue";
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/store/student";
import { Toaster } from "@/components/ui/toast";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";

const authStore = useAuthStore();
authStore.restoreSession();
</script>
