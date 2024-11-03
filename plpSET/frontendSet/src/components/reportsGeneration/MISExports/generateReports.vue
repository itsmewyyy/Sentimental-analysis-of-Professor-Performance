<template>
  <UseTemplate>
    <div class="flex w-full h-full">
      <!-- Sidebar for Export Options -->
      <div
        class="w-1/5 min-w-[250px] h-full bg-gray-100 rounded-l-md grid grid-rows-5 pt-8 pl-6 pr-4 gap-6"
      >
        <div class="text-2xl font-bold row-start-1 pl-9">Export Reports</div>

        <div class="row-start-2 space-y-4">
          <Select v-model="rating">
            <SelectTrigger>
              <SelectValue placeholder="Select Ratings" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Reports</SelectLabel>
                <SelectItem value="numerical">Numerical Ratings</SelectItem>
                <SelectItem value="feedback">Feedback Ratings</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>

          <!-- Conditional Question Select -->
          <div v-if="rating === 'feedback' && !selectedProfessor">
            <Select v-model="selectedQuestion">
              <SelectTrigger>
                <SelectValue placeholder="Select Question" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Question</SelectLabel>
                  <SelectItem value="1">Question 1</SelectItem>
                  <SelectItem value="2">Question 2</SelectItem>
                  <SelectItem value="3">Question 3</SelectItem>
                  <SelectItem value="4">Question 4</SelectItem>
                  <SelectItem value="5">Question 5</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </div>
        </div>

        <!-- College and Professor Selection -->
        <div class="row-start-3 space-y-4">
          <Select v-model="selectedCollege">
            <SelectTrigger>
              <SelectValue placeholder="Select College" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Colleges</SelectLabel>
                <SelectItem
                  v-for="college in colleges"
                  :key="college.name"
                  :value="college.name"
                >
                  {{ college.description }}
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>

          <Select v-model="selectedProfessor" v-if="selectedCollege">
            <SelectTrigger>
              <SelectValue placeholder="Select Professor" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Professors</SelectLabel>
                <SelectItem
                  v-for="professor in filteredProfessors"
                  :key="professor.professor_id"
                  :value="professor.professor_id"
                >
                  {{ professor.full_name }}
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>

        <!-- Action Buttons -->
        <div class="row-start-4 space-x-2 pt-8">
          <Button variant="outline" class="px-8" @click="generateReports"
            >Generate</Button
          >
          <Button class="bg-plpgreen-200 px-9" @click="exportPDF"
            >Export</Button
          >
        </div>
      </div>

      <!-- Content Area -->
      <div class="flex-grow bg-plpgreen-100/50 p-8 rounded-r-md h-full">
        <ScrollArea class="rounded-md bg-plpgreen-100/50">
          <div class="max-h-[75vh]">
            <div
              class="w-full bg-white rounded-md shadow-md p-4"
              id="contentToExport"
            >
              <div class="space-y-12 items-center flex-col flex">
                <div class="flex flex-col items-center pt-8">
                  <div class="flex flex-row items-center">
                    <div class="translate-y-3">
                      <svg
                        width="60"
                        height="60"
                        viewBox="0 0 240 240"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                      >
                        <rect
                          width="240"
                          height="240"
                          fill="url(#pattern0_1926_3)"
                        />
                        <defs>
                          <pattern
                            id="pattern0_1926_3"
                            patternContentUnits="objectBoundingBox"
                            width="1"
                            height="1"
                          >
                            <use
                              xlink:href="#image0_1926_3"
                              transform="scale(0.00416667)"
                            />
                          </pattern>
                          <image
                            id="image0_1926_3"
                            width="240"
                            height="240"
                            xlink:href="data:image/png;base64,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"
                          />
                        </defs>
                      </svg>
                    </div>
                    <p class="text-2xl font-bold pl-2">
                      Pamantasan ng Lungsod ng Pasig
                    </p>
                  </div>
                  <P class="text-xs"
                    >Alcalde, Jose Street, Kapasigan, Pasig City</P
                  >
                </div>
                <div class="flex flex-col items-center font-semibold text-lg">
                  <p>Student Evaluation of Teaching</p>
                  <p>Academic Year 2024 - 2025 1st Semester</p>
                </div>
              </div>
              <div class="pt-10 pl-8">
                <div
                  class="flex flex-row space-x-4"
                  v-if="selectedProfessor != null"
                >
                  <p class="font-semibold">Name of Faculty:</p>
                  <p>{{ selectedProfessorFullName }}</p>
                </div>
                <div class="flex flex-row space-x-4">
                  <p class="font-semibold">Department:</p>
                  <p>{{ selectedCollege }}</p>
                </div>
              </div>
              <div class="px-8 pb-28">
                <component
                  :is="selectedReportComponent"
                  :college="selectedCollege"
                  :professor="selectedProfessor"
                  :question="selectedQuestion"
                  :refreshChart="refreshChart"
                />
              </div>
            </div>
          </div>
        </ScrollArea>
      </div>
    </div>
  </UseTemplate>

  <!-- Desktop Dialog for Editing Profile -->
  <Dialog v-if="isDesktop" v-model="isOpen">
    <DialogTrigger as-child>
      <Button
        @click.stop
        class="border-none bg-transparent hover:bg-transparent w-full h-3 pl-0 py-2.5"
        ><div
          class="flex items-center space-x-3 w-full cursor-pointer text-black"
        >
          <Download class="w-4 h-4" />
          <span class="text-sm">Generate Reports</span>
        </div></Button
      >
    </DialogTrigger>
    <DialogContent class="sm:max-w-[1440px] h-5/6 p-0">
      <GridForm />
    </DialogContent>
  </Dialog>

  <!-- Mobile Drawer for Editing Profile -->
  <Drawer v-else v-model="isOpen">
    <DrawerTrigger as-child>
      <Button variant="outline">Edit Profile</Button>
    </DrawerTrigger>
    <DrawerContent>
      <DrawerHeader class="text-left">
        <DrawerTitle>Edit Profile</DrawerTitle>
        <DrawerDescription>
          Make changes to your profile here. Click save when you're done.
        </DrawerDescription>
      </DrawerHeader>
      <GridForm />
      <DrawerFooter class="pt-2">
        <DrawerClose as-child>
          <Button variant="outline">Cancel</Button>
        </DrawerClose>
      </DrawerFooter>
    </DrawerContent>
  </Drawer>
</template>

<script lang="ts" setup>
import html2canvas from "html2canvas";
import { jsPDF } from "jspdf";
import { Button } from "@/components/ui/button";
import { Download } from "lucide-vue-next";
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
import { createReusableTemplate, useMediaQuery } from "@vueuse/core";
import { ref, computed, watch, onMounted } from "vue";
import axios from "axios";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import feedbackOverview from "@/components/reportsGeneration/exportComponents/collegeFeedbackOverview/feedbackOverview.vue";
import numericalOverview from "@/components/reportsGeneration/exportComponents/collegeNumericalOverview/numericalOverview.vue";
import numericalProfessor from "@/components/reportsGeneration/exportComponents/numericalProfessor.vue";
import feedbackProfessor from "@/components/reportsGeneration/exportComponents/feedbackProfessorOverview/feedbackProfessor.vue";
import feedbackQuestionOverview from "@/components/reportsGeneration/exportComponents/collegeFeedbackQuestionOverview/feedbackQuestionOverview.vue";

const [UseTemplate, GridForm] = createReusableTemplate();
const isDesktop = useMediaQuery("(min-width: 768px)");
const isOpen = ref(false);
const rating = ref(null);
const selectedCollege = ref(null);
const selectedProfessor = ref(null);
const selectedQuestion = ref(null);

const refreshChart = ref(false);

const colleges = ref([]);
const professors = ref([]);

const selectedProfessorFullName = computed(() => {
  const professor = professors.value.find(
    (prof) => prof.professor_id === selectedProfessor.value
  );
  return professor ? professor.full_name : "";
});

// Fetch the data on mount
onMounted(async () => {
  try {
    const collegeResponse = await axios.get(
      "http://127.0.0.1:8000/api/colleges/"
    );
    const professorResponse = await axios.get(
      "http://127.0.0.1:8000/api/professor-list/"
    );
    colleges.value = collegeResponse.data;
    professors.value = professorResponse.data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});

const filteredProfessors = computed(() => {
  if (!selectedCollege.value) return [];
  return professors.value.filter(
    (professor) => professor.department === selectedCollege.value
  );
});

watch(selectedProfessor, (newVal) => {
  if (newVal) {
    selectedQuestion.value = null;
  }
});

const selectedReportComponent = computed(() => {
  if (rating.value === "numerical") {
    if (selectedCollege.value && selectedProfessor.value) {
      return numericalProfessor;
    } else if (selectedCollege.value) {
      return numericalOverview;
    }
  } else if (rating.value === "feedback") {
    if (selectedCollege.value && selectedQuestion.value) {
      return feedbackQuestionOverview;
    } else if (selectedCollege.value && selectedProfessor.value) {
      return feedbackProfessor;
    } else if (selectedCollege.value) {
      return feedbackOverview;
    }
  }
  return null;
});

const generateReports = () => {
  localStorage.setItem("college", selectedCollege.value);
  localStorage.setItem("question", selectedQuestion.value);
  localStorage.setItem("professor", selectedProfessor.value);
  refreshChart.value = !refreshChart.value;
};

function exportPDF(): void {
  const element = document.getElementById("contentToExport");
  if (element) {
    html2canvas(element).then((canvas) => {
      const imgData = canvas.toDataURL("image/png");
      const pdf = new jsPDF();
      const imgWidth = 190; // Width of the image in PDF
      const pageHeight = pdf.internal.pageSize.height; // Height of the PDF page
      const imgHeight = (canvas.height * imgWidth) / canvas.width; // Calculate image height maintaining aspect ratio
      let heightLeft = imgHeight; // Remaining height to add pages
      let position = 0; // Initial position for the image

      // Add the first image to the PDF
      pdf.addImage(imgData, "PNG", 10, position, imgWidth, imgHeight);
      heightLeft -= pageHeight; // Update height left after adding the first page

      // Loop to add additional pages if necessary
      while (heightLeft > 0) {
        pdf.addPage(); // Add a new page
        position = 0; // Reset position to the top of the new page
        pdf.addImage(imgData, "PNG", 10, position, imgWidth, imgHeight); // Add the image
        heightLeft -= pageHeight; // Update height left
      }

      pdf.save("exported-content.pdf");
    });
  } else {
    console.error('Element with id "contentToExport" not found.');
  }
}
</script>

<style scoped>
.sidebar {
  min-width: 250px;
}
</style>
