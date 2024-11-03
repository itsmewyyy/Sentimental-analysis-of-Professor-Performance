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

interface Section {
  section_id: string;
}

interface Program {
  program_desc: string;
  program_id: string;
  sections: Section[];
}

interface Year {
  year_level_id: number;
  year_level_desc: string;
  programs: Program[];
}

interface College {
  id: string;
  name: string;
  description: string;
  years: Year[];
}
const colleges = ref<College[]>([]);
const router = useRouter();

const fetchColleges = async () => {
  try {
    const response = await axios.get<College[]>(
      "https://sentiment-professor-feedback-1.onrender.com/api/colleges/"
    );
    colleges.value = response.data;
    console.log("API response:", response.data);
  } catch (error) {
    console.error("Error fetching colleges:", error);
  }
};

const goToSection = (sectionId: string) => {
  if (router) {
    router.push({ path: `/StudentList/${sectionId}` });
    console.log(`Navigating to section ${sectionId}`);
    localStorage.setItem("section", sectionId);
  } else {
    console.error("Router is not available.");
  }
};

onMounted(() => {
  fetchColleges();
});
</script>

<template>
  <div
    v-for="(college, collegeIndex) in colleges"
    :key="collegeIndex"
    class="pb-8 pl-6"
    :id="`college-${college.name}`"
  >
    <DropdownMenu>
      <DropdownMenuTrigger>
        <button
          class="border border-black/20 w-80 h-24 rounded-lg pl-6 hover:bg-darks-50"
        >
          <div class="flex items-center text-darks-700 font-bold text-2xl">
            <p>{{ college.name }}</p>
          </div>
          <p class="text-left text-darks-300 text-base">
            {{ college.description }}
          </p>
        </button>
      </DropdownMenuTrigger>
      <div
        class="z-40 translate-x-72 -translate-y-20"
        :id="`college-${college.name}`"
      ></div>
      <DropdownMenuContent class="w-80">
        <DropdownMenuSub
          v-if="college.years.length"
          v-for="(year, yearIndex) in college.years"
          :key="yearIndex"
        >
          <DropdownMenuSubTrigger>
            <div class="mr-1"></div>
            <span class="w-64 p-2">{{ year.year_level_desc }}</span>
          </DropdownMenuSubTrigger>
          <DropdownMenuPortal>
            <DropdownMenuSubContent>
              <DropdownMenuSub
                v-if="year.programs.length"
                v-for="(program, programIndex) in year.programs"
                :key="programIndex"
              >
                <DropdownMenuSubTrigger
                  ><span class="p-1">{{
                    program.program_id
                  }}</span></DropdownMenuSubTrigger
                >
                <DropdownMenuPortal>
                  <DropdownMenuSubContent>
                    <DropdownMenuItem
                      v-if="program.sections.length"
                      v-for="(section, sectionIndex) in program.sections"
                      :key="sectionIndex"
                    >
                      <button
                        class="p-1"
                        @click.prevent="goToSection(section.section_id)"
                      >
                        {{ section.section_id }}
                      </button>
                    </DropdownMenuItem>
                  </DropdownMenuSubContent>
                </DropdownMenuPortal>
              </DropdownMenuSub>
            </DropdownMenuSubContent>
          </DropdownMenuPortal>
        </DropdownMenuSub>
      </DropdownMenuContent>
    </DropdownMenu>
  </div>
</template>
