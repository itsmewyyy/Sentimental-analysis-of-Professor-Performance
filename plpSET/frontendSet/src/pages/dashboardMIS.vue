<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import MISNavbar from "@/components/navigation/NavBarMIS.vue";
import year_semester from "@/components/MIS/year_semester.vue";
import evaluationPeriod from "@/components/MIS/evaluationPeriod.vue";
import axios from "axios";
import { useAuthStore } from "@/store/adminStore";
import studentsubmissionsTable from "@/components/MIS/studentsubmissionsTable/studentsubmissionsTable.vue";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
const authStore = useAuthStore();
authStore.restoreSession();

interface Counts {
  enrolled_students: number;
  registered_accounts: number;
  submitted_evaluations: number;
}

const Count = ref<Counts | null>(null);

const props = defineProps({
  refreshData: Boolean,
});

const fetchCounts = async () => {
  try {
    const response = await fetch(
      "https://sentiment-professor-feedback-1.onrender.com/api/students-summary/"
    );
    if (!response.ok) {
      throw new Error(`An error occurred: ${response.statusText}`);
    }
    const data = await response.json();

    Count.value = data as Counts;
  } catch (error) {
    console.error("Failed to fetch counts:", error);
    Count.value = null;
  }

  const yearSemResponse = await axios.get(
    "https://sentiment-professor-feedback-1.onrender.com/api/current-year-sem/",
    { withCredentials: true }
  );

  if (yearSemResponse.status === 200) {
    const currentYearSem = yearSemResponse.data;
    console.log("Year-Sem Response:", yearSemResponse.data);
    localStorage.setItem("current_year_sem", currentYearSem.year_sem_id);
  } else {
    console.error("Failed to fetch or parse year-sem data.");
  }
};

onMounted(fetchCounts);
</script>

<template>
  <ScrollArea class="h-svh w-full">
    <MISNavbar />

    <section class="p-20 pt-32 space-y-6">
      <div class="grid grid-cols-6 grid-rows-11 gap-4 h-[750px]">
        <div class="col-span-2 row-span-2 border border-black/15 rounded-md">
          <div class="p-7 pt-9">
            <p class="text-sm text-darks-200/50 font-medium">
              Enrolled Students
            </p>
            <p class="text-3xl font-bold text-plpgreen-100">
              {{ Count?.enrolled_students ?? "Loading..." }}
            </p>
          </div>
        </div>
        <div
          class="col-span-2 row-span-2 col-start-3 border border-black/15 rounded-md"
        >
          <div class="p-7 pt-9">
            <p class="text-sm text-darks-200/50 font-medium">
              Registered Accounts
            </p>
            <p class="text-3xl font-bold text-plpyellow-200">
              {{ Count?.registered_accounts ?? "Loading..." }}
            </p>
          </div>
        </div>
        <div
          class="col-span-2 row-span-2 col-start-5 border border-black/15 rounded-md"
        >
          <div class="p-7 pt-9">
            <p class="text-sm text-darks-200/50 font-medium">
              Submitted Evaluations
            </p>
            <p class="text-3xl font-bold text-plpgreen-200">
              {{ Count?.submitted_evaluations ?? "Loading..." }}
            </p>
          </div>
        </div>
        <div
          class="col-span-6 row-span-9 row-start-3 border border-black/15 rounded-md px-4"
        >
          <studentsubmissionsTable></studentsubmissionsTable>
        </div>
      </div>

      <div class="grid grid-cols-6 grid-rows-3 gap-4 h-[200px]">
        <div
          class="col-span-3 row-span-2 col-start-1 row-start-2 border border-black/15 rounded-md pt-1"
        >
          <year_semester :refreshData="refreshData"></year_semester>
        </div>
        <div
          class="col-span-3 row-span-2 col-start-4 row-start-2 border border-black/15 rounded-md pt-1"
        >
          <evaluationPeriod :refreshData="refreshData"></evaluationPeriod>
        </div>
        <div class="col-span-6 col-start-1 row-start-1">
          <p class="font-semibold text-xl pt-4">Lorem Ipsum</p>
        </div>
      </div>
    </section>
  </ScrollArea>
</template>
