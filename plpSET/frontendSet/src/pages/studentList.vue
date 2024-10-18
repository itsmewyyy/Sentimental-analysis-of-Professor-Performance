<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router"; // Import useRoute to access route parameters
import axios from "axios";
import StudentInfo from "@/components/studentInfo.vue";
import { Search } from "lucide-vue-next";
import { Plus } from "lucide-vue-next";
import { SlidersHorizontal } from "lucide-vue-next";
import { FileUp } from "lucide-vue-next";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";

interface Student {
  student_id: string;
  full_name: string;
  section: string;
}

const route = useRoute();
const sectionId = ref<string>(route.params.sectionId as string); // Access sectionId from the route params
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
    students.value = []; // Ensure students is set to an empty array in case of an error
  }
};

onMounted(() => {
  fetchStudents();
});
</script>

<template>
  <div
    class="fixed top-0 left-0 z-40 w-collapsed-sidebar h-screen bg-darks-50"
    tabindex="-1"
    aria-labelledby="drawer-navigation-label"
  ></div>
  <div class="fixed top-0 z-40 h-navbar w-full bg-darks-100"></div>

  <section class="pl-40 rounded pt-32 space-y-24 font-raleway min-h-full">
    <div
      class="flex items-center pl-8 w-11/12 h-24 border border-black/15 rounded-md"
    >
      <h1 class="font-bold text-2xl">{{ sectionId }}</h1>
    </div>

    <div class="space-y-4">
      <div class="flex items-center justify-between w-11/12">
        <div class="w-1/5 space-x-1">
          <Search class="h-4 w-4 translate-x-4 translate-y-6" color="#5F6368" />
          <input
            type="text"
            placeholder="Search..."
            class="border border-darks-200 p-4 rounded-md w-full text-sm text-gray-900 h-8 pl-8 focus:ring-plpgreen-200 focus:border-plpgreen-100"
          />
        </div>
        <div class="space-x-2 flex items-center justify-end">
          <button
            class="w-8 h-8 border border-black/40 rounded-md pl-2 hover:bg-darks-100/50"
          >
            <SlidersHorizontal class="w-3.5 h-4" />
          </button>
          <button
            class="w-8 h-8 bg-plpgreen-100 rounded-md pl-2 hover:bg-lime-900/40"
          >
            <Plus class="w-4 h-4" />
          </button>
        </div>
      </div>
      <div>
        <div
          class="flex items-center justify-center space-x-44 text-sm h-14 border-y border-black/25 w-11/12 font-medium text-darks-300 hover:bg-darks-50/80"
        >
          <p class="w-32">Student ID</p>
          <p class="w-72">Name</p>
          <p class="w-28">Section</p>
          <div class="space-x-6">
            <div class="w-4"></div>
            <div class="w-8"></div>
          </div>
        </div>
        <ScrollArea class="h-72 w-11/12">
          <div v-if="students && students.length > 0">
            <div
              v-for="(student, index) in students"
              :key="index"
              class="hover:bg-darks-50/80"
            >
              <StudentInfo
                :student_id="student.student_id"
                :name="student.full_name"
                :section="student.section"
              />
            </div>
          </div>
          <div
            v-else
            class="flex flex-col items-center justify-center pt-52 space-y-3.5"
          >
            <p class="text-base text-red-800">
              No students in this section. Please upload a class list.
            </p>
            <button
              class="flex items-center justify-center w-1/12 h-10 bg-plpgreen-200/80 rounded text-white text-sm font-semibold hover:bg-plpgreen-300/90"
            >
              <FileUp class="w-5 h-5 mr-1" />
              Upload
            </button>
          </div>
        </ScrollArea>
      </div>
    </div>
  </section>
</template>

<style scoped>
.w-collapsed-sidebar {
  width: 76px;
}
.h-navbar {
  height: 64px;
}
</style>
