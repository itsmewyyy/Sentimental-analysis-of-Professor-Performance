<script setup lang="ts">
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import Button from "../ui/button/Button.vue";
import { ref, onMounted } from "vue";
import axios from "axios";
import Input from "../ui/input/Input.vue";
import { useAcademicTerm } from "@/components/MIS/UseAcademicTerm";

const selectedYear = ref("");
const selectedSemester = ref("");
const {
  isAcademicTermSet,
  isEvaluationPeriodSet,
  yearSem,
  setAcademicTerm,
  setEvaluationPeriod,
} = useAcademicTerm();

async function onSetAcademicTerm() {
  const yearSemId = `${selectedYear.value}-${selectedSemester.value}`;
  try {
    await axios.post("http://127.0.0.1:8000/api/set-academic-term/", {
      year_sem_id: yearSemId,
      acad_year: selectedYear.value,
      semester_desc:
        selectedSemester.value === "1" ? "1st Semester" : "2nd Semester",
    });
    setAcademicTerm(yearSemId);
  } catch (error) {
    console.error("Error setting academic term:", error);
  }
}
</script>

<template>
  <div class="flex justify-between p-7 pt-10">
    <div class="">
      <Input
        id="acad_year"
        type="text"
        placeholder="Academic Year"
        v-model="selectedYear"
      />
      <p class="text-sm text-darks-200/50">e.g. 24-25</p>
    </div>
    <div>
      <Select v-model="selectedSemester">
        <SelectTrigger class="px-4">
          <SelectValue placeholder="Semester" />
        </SelectTrigger>
        <SelectContent>
          <SelectGroup>
            <SelectLabel>Semester</SelectLabel>
            <SelectItem value="1">1st Semester</SelectItem>
            <SelectItem value="2">2nd Semester</SelectItem>
          </SelectGroup>
        </SelectContent>
      </Select>
    </div>
    <div>
      <Button
        class="bg-plpgreen-200 hover:bg-plpgreen-300"
        :disabled="isAcademicTermSet"
        @click="onSetAcademicTerm"
      >
        Set Academic Term
      </Button>
    </div>
  </div>
</template>
