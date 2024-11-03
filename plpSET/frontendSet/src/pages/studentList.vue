<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import StudentList from "@/components/databaseStudent/studentListTable.vue";
import MISNavbar from "@/components/navigation/NavBarMIS.vue";

interface Student {
  student_id: string;
  full_name: string;
  section: string;
}

const route = useRoute();
const sectionId = ref<string>(route.params.sectionId as string);
const students = ref<Student[]>([]);
import Toaster from "@/components/ui/toast/Toaster.vue";

const fetchStudents = async () => {
  if (!sectionId.value) {
    console.error("Section ID is missing");
    return;
  }

  try {
    const response = await axios.get<Student[]>(
      `https://sentiment-professor-feedback-1.onrender.com/api/section/${sectionId.value}/`
    );

    if (Array.isArray(response.data)) {
      students.value = response.data;
    } else {
      console.warn(
        "No students found or unexpected response structure:",
        response.data
      );
      students.value = [];
    }
  } catch (error) {
    console.error("Error fetching students:", error);
    students.value = [];
  }
};

onMounted(() => {
  fetchStudents();
});
</script>

<template>
  <Toaster />
  <MISNavbar></MISNavbar>
  <section class="p-20 pt-20 min-h-full">
    <div class="w-full border border-black/25 rounded-md px-9 pt-9">
      <div class="border-b border-black/15 pb-6">
        <h1 class="font-bold text-3xl">{{ sectionId }}</h1>
        <p class="font-medium text-base text-darks-200/60">
          Displayed below are the students enrolled in this section.
        </p>
      </div>

      <div><StudentList></StudentList></div>
    </div>
  </section>
</template>
