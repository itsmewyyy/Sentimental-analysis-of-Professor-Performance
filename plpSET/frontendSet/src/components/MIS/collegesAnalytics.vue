<script setup lang="ts">
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuPortal,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
  DropdownMenuSubTrigger,
  DropdownMenuSub,
  DropdownMenuSubContent,
} from "@/components/ui/dropdown-menu";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

interface College {
  id: string;
  name: string;
  description: string;
}

const colleges = ref<College[]>([]);
const router = useRouter();

const fetchColleges = async () => {
  try {
    const response = await axios.get<College[]>(
      "http://127.0.0.1:8000/api/colleges/"
    );
    colleges.value = response.data;
    console.log("API response:", response.data);
  } catch (error) {
    console.error("Error fetching colleges:", error);
  }
};

const seeAnalytics = (college: College) => {
  localStorage.setItem("college", college.name);
  router.push({ name: "DeanDashboard", params: { id: college.id } });
};

onMounted(() => {
  fetchColleges();
});
</script>

<template>
  <div
    v-for="(college, collegeIndex) in colleges"
    :key="collegeIndex"
    class="pb-8 pl-6 cursor-pointer"
    :id="`college-${college.name}`"
    @click="seeAnalytics(college)"
  >
    <button
      class="border border-black/20 w-80 h-24 rounded-lg pl-6 hover:bg-darks-50 bg-white"
    >
      <div class="flex items-center text-darks-700 font-bold text-2xl">
        <p>{{ college.name }}</p>
      </div>
      <p class="text-left text-darks-300 text-base">
        {{ college.description }}
      </p>
    </button>
  </div>
</template>
