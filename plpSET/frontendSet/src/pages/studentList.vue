<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import StudentList from "@/components/databaseStudent/studentListTable.vue";
import MISNavbar from "@/components/navigation/MISNavbar.vue";

interface Student {
  student_id: string;
  full_name: string;
  section: string;
}

const route = useRoute();
const sectionId = ref<string>(route.params.sectionId as string);
const students = ref<Student[]>([]);

const fetchStudents = async () => {
  if (!sectionId.value) {
    console.error("Section ID is missing");
    return;
  }

  try {
    const response = await axios.get<Student[]>(
      `http://127.0.0.1:8000/api/section/${sectionId.value}/`
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
  <MISNavbar></MISNavbar>
  <section class="p-20 rounded pt-32 font-raleway min-h-full">
    <div class="w-full border border-black/15 rounded-md space-y-6">
      <div>
        <h1 class="font-bold text-3xl pl-7 pt-7">{{ sectionId }}</h1>
        <p class="font-medium text-base pl-7 text-darks-200/60">
          Displayed below are the students enrolled in this section.
        </p>
      </div>

      <StudentList></StudentList>
    </div>
  </section>
</template>
