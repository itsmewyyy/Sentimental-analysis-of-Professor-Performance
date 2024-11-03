<script setup lang="ts">
import { ref, onMounted } from "vue";
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Circle } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Pencil } from "lucide-vue-next";
import { useToast } from "@/components/ui/toast/use-toast";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Section } from "@/components/databaseManagement/sections/type";
import { useEdit } from "./composables/sectionMutations";
import axios from "axios";

// Reusable `form` section
const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const { toast } = useToast();

const { mutate: editData } = useEdit();

const sectionId = ref("");
const sectionDescription = ref("");
const program = ref("");
const yearLevel = ref("");

const yearLevelDescriptions = {
  1: "1st Year",
  2: "2nd Year",
  3: "3rd Year",
  4: "4th Year",
};

const fetchInfo = async () => {
  try {
    const response = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/sectioncrud/${sectionId.value}/`
    );
    if (response.status === 200) {
      const info = response.data;
      sectionDescription.value = info.name || "";
      program.value = info.program || "";
      yearLevel.value = yearLevelDescriptions[info.year_level] || "Unknown";
    }
  } catch (error) {
    console.error("Error fetching:", error);
    toast({
      title: "Error",
      description: "Failed to fetch.",
    });
  }
};

onMounted(() => {
  const savedItem = localStorage.getItem("section");
  if (savedItem) {
    sectionId.value = savedItem;
    fetchInfo();
  }
});

const submitForm = async () => {
  try {
    const programResponse = await axios.get(
      `http://127.0.0.1:8000/api/program-list/?program_id=${program.value}`
    );
    const statusResponse = await axios.get(
      `http://127.0.0.1:8000/api/years-list/?year_level_desc=${yearLevel.value}`
    );

    const matchedSection = programResponse.data.find(
      (p) => p.program_id === program.value
    );
    const matchedStatus = statusResponse.data.find(
      (y) => y.year_level_desc === yearLevel.value
    );

    const programId = matchedSection.program_id;
    const yearLevelId = matchedStatus.year_level_id;

    const generateSectionId = () => {
      const programPart = program.value;
      const yearLevelPart = yearLevelId;
      const namePart =
        sectionDescription.value.length === 1 ? sectionDescription.value : "";

      return `${programPart}${yearLevelPart}${namePart}`;
    };

    sectionId.value = generateSectionId();

    const Data: Section = {
      section_id: sectionId.value,
      name: sectionDescription.value,
      program: programId,
      year_level: yearLevelId,
    };

    editData(Data, {
      onSuccess: () => {
        isOpen.value = false;
        toast({
          title: "Success",
          description: "Added successfully!",
        });
      },
    });
  } catch (error) {
    toast({
      title: "Submission Error",
      description: error.message || "Failed to add. Please try again.",
    });
    console.error("Submission Error:", error);
  }
};
</script>

<template>
  <div>
    <!-- Reusable Form Template -->
    <UseTemplate>
      <form class="grid items-start gap-4 px-4" @submit.prevent="submitForm">
        <div class="grid gap-2">
          <Label html-for="college" class="">Program</Label>
          <Select class="sm:w-[300px]" v-model="program">
            <SelectTrigger class="sm:w-full">
              <SelectValue placeholder="Select Program" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <div class="flex items-center">
                  <SelectLabel class="flex items-center gap-2 pl-5">
                    <Circle class="w-3.5 h-3.5" color="grey" fill="grey" />
                    College of Computer Studies (CCS)
                  </SelectLabel>
                </div>
                <SelectItem value="BSIT" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Information Technology (BSIT)
                  </div>
                </SelectItem>
                <SelectItem value="BSCS" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Computer Science (BSCS)
                  </div>
                </SelectItem>

                <div class="flex items-center">
                  <SelectLabel class="flex items-center gap-2 pl-5">
                    <Circle class="w-3.5 h-3.5" color="violet" fill="violet" />
                    College of Arts and Sciences (CAS)
                  </SelectLabel>
                </div>
                <SelectItem value="ab-psych" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Arts in Psychology (AB PSYCH)
                  </div>
                </SelectItem>

                <div class="flex items-center">
                  <SelectLabel class="flex items-center gap-2 pl-5">
                    <Circle class="w-3.5 h-3.5" color="yellow" fill="yellow" />
                    College of Business and Accountancy (CBA)
                  </SelectLabel>
                </div>
                <SelectItem value="BSA" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Accountancy (BSA)
                  </div>
                </SelectItem>
                <SelectItem value="BSBA" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Business Administration (BSBA)
                  </div>
                </SelectItem>
                <SelectItem value="BSENT" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Entrepreneurial (BSENT)
                  </div>
                </SelectItem>

                <div class="flex items-center">
                  <SelectLabel class="flex items-center gap-2 pl-5">
                    <Circle class="w-3.5 h-3.5" color="pink" fill="pink" />
                    College of Nursing (CON)
                  </SelectLabel>
                </div>
                <SelectItem value="BSN" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Nursing
                  </div>
                </SelectItem>

                <div class="flex items-center">
                  <SelectLabel class="flex items-center gap-2 pl-5">
                    <Circle color="orange" fill="orange" class="w-3.5 h-3.5" />
                    College of Engineering (COE)
                  </SelectLabel>
                </div>
                <SelectItem value="BSECE" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Electronics and Communications
                    Engineering
                  </div>
                </SelectItem>

                <div class="flex items-center">
                  <SelectLabel class="flex items-center gap-2 pl-5">
                    <Circle color="blue" fill="blue" class="w-3.5 h-3.5" />
                    College of Education (COED)
                  </SelectLabel>
                </div>
                <SelectItem value="BEED" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Elementary Education(BEED)
                  </div>
                </SelectItem>
                <SelectItem value="BSED" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Secondary Education (BSED)
                  </div>
                </SelectItem>

                <div class="flex items-center">
                  <SelectLabel class="flex items-center gap-2 pl-5">
                    <Circle color="red" fill="red" class="w-3.5 h-3.5" />
                    College of International Hospitality Management (CIHM)
                  </SelectLabel>
                </div>
                <SelectItem value="BSHM" class="ml-6">
                  <div class="flex items-center gap-2">
                    Bachelor of Science in Hospitality Management (BSHM)
                  </div>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <div>
          <Label for="department" class="">Year Level</Label>
          <Select class="w-full" v-model="yearLevel">
            <SelectTrigger class="w-full">
              <SelectValue placeholder="Select Year Level" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="1st Year">
                  <div class="flex items-center gap-2">
                    <span>1st Year</span>
                  </div>
                </SelectItem>
                <SelectItem value="2nd Year">
                  <div class="flex items-center gap-2">
                    <span>2nd Year</span>
                  </div>
                </SelectItem>
                <SelectItem value="3rd Year">
                  <div class="flex items-center gap-2">
                    <span>3rd Year</span>
                  </div>
                </SelectItem>
                <SelectItem value="4th Year">
                  <div class="flex items-center gap-2">
                    <span>4th Year</span>
                  </div>
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <div class="grid gap-2">
          <Label html-for="program-description" class="">Section</Label>
          <Input
            id="program-description"
            default-value="A"
            v-model="sectionDescription"
          />
          <p class="text-gray-500 ml-2 italic text-xs">e.g. A, B, C, D</p>
          <!-- Helper Text -->
        </div>
        <Button
          type="submit"
          class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
        >
          Add Section
        </Button>
      </form>
    </UseTemplate>

    <Button
      type="button"
      class="h-6 border-none bg-transparent hover:bg-transparent w-[160px] flex items-center"
      @click="isOpen = true"
      @click.stop
    >
      <div class="relative flex items-center">
        <p class="text-sm text-darks-900 absolute right-12 mr-2">Edit</p>

        <Pencil color="green" width="12" class="absolute left-9 ml-1.5" />
      </div>
    </Button>

    <!-- Dialog for Desktop View -->
    <Dialog v-if="isDesktop" v-model:open="isOpen">
      <DialogTrigger as-child> </DialogTrigger>
      <DialogContent class="sm:max-w-[600px]">
        <DialogHeader>
          <DialogTitle>New Section</DialogTitle>
          <DialogDescription>
            To get started, please enter the information for the new section
          </DialogDescription>
        </DialogHeader>
        <GridForm />
      </DialogContent>
    </Dialog>

    <!-- Drawer for Mobile View -->
    <Drawer v-else v-model:open="isOpen">
      <DrawerTrigger as-child> </DrawerTrigger>
      <DrawerContent>
        <DrawerHeader class="text-left">
          <DrawerTitle>New Section</DrawerTitle>
          <DrawerDescription>Add a new section here</DrawerDescription>
        </DrawerHeader>
        <GridForm />
        <DrawerFooter class="pt-2">
          <DrawerClose as-child>
            <Button variant="outline">Cancel</Button>
          </DrawerClose>
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  </div>
</template>
