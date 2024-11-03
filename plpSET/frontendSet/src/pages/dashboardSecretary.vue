<script setup lang="ts">
import { ref, onMounted } from "vue";
import { Plus, Trash } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import subjectTagging from "@/components/subject-sectionTagging/subjectTagging.vue";
import sectionTagging from "@/components/subject-sectionTagging/sectionTagging.vue";
import secretaryNavbar from "@/components/navigation/NavBarSecretary.vue";
import axios from "axios";
const subjectsectionTags = ref<Array<number>>([]);

const professors = ref<Array<any>>([]);
const selectedProfessor = ref("");
const rows = ref<Array<{ subjects: Array<string>; sections: Array<string> }>>([
  { subjects: [], sections: [] },
]);

const selectedCollege = localStorage.getItem("college");
const year_sem = localStorage.getItem("current_year_sem");
const students = ref<Array<any>>([]); // Holds students for each section

// Load students for a given section
const loadStudents = async (sectionId: string) => {
  try {
    const response = await axios.get(
      `https://sentiment-professor-feedback-1.onrender.com/api/section/${sectionId}`
    );
    students.value = response.data;
    console.log(response.data);
  } catch (error) {
    console.error("Error loading students:", error);
  }
};

const updateSubjects = (selectedSubjects, index: number) => {
  if (rows.value[index]) {
    rows.value[index].subjects = selectedSubjects.map(
      (subject) => subject.value
    );
    console.log(
      `Updated subjects for row ${index}:`,
      rows.value[index].subjects
    );
  }
};

const updateSections = (selectedSections, index: number) => {
  if (rows.value[index]) {
    rows.value[index].sections = selectedSections.map(
      (section) => section.value
    );
    console.log(
      `Updated sections for row ${index}:`,
      rows.value[index].sections
    );
  }
};

const addSubjectSectionTag = () => {
  subjectsectionTags.value.push(subjectsectionTags.value.length + 1);
  rows.value.push({ subjects: [], sections: [] });
};

const removeSubjectSectionTag = (index: number) => {
  subjectsectionTags.value.splice(index, 1);
  rows.value.splice(index, 1);
};

// Load professors based on college
const loadProfessors = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/professor-list/"
    );
    professors.value = response.data.filter(
      (professor: any) => professor.department === selectedCollege
    );
  } catch (error) {
    console.error("Error loading professors:", error);
  }
};

const submitData = async () => {
  if (!selectedProfessor.value) {
    alert("Please select a professor.");
    return;
  }

  const profSubjectsData = rows.value.flatMap((row) =>
    row.subjects.flatMap((subject) =>
      row.sections.map((section) => ({
        prof_subjects_id: `${year_sem}_${subject}_${selectedProfessor.value}_${section}`,
        year_sem_id: year_sem,
        professor_id: selectedProfessor.value,
        subject_code: subject,
        section_id: section,
      }))
    )
  );

  try {
    for (const entry of profSubjectsData) {
      try {
        const profSubjectResponse = await axios.post(
          "http://127.0.0.1:8000/api/prof-subjs/",
          entry
        );
        console.log("Prof subjects response:", profSubjectResponse.data);

        // Ensure you reference the correct key for the ID
        const profSubjectsId = profSubjectResponse.data.prof_subjects_id; // or the correct key if it's different

        if (!profSubjectsId) {
          console.error(
            "Failed to retrieve prof_subjects_id for entry:",
            entry
          );
          continue; // Skip if the ID is not valid
        }

        // Load students for the current section
        await loadStudents(entry.section_id);

        const enrollments = students.value.map((student) => ({
          student_enrolled_subj_id: `${profSubjectsId}_${student.student_id}`,
          student_id: student.student_id,
          prof_subj_id: profSubjectsId, // Use the ID retrieved from the previous post
        }));

        console.log("Enrollments to be posted:", enrollments);

        for (const enrollment of enrollments) {
          if (!enrollment.prof_subj_id) {
            console.error("prof_subj_id is null for enrollment:", enrollment);
          } else {
            const response = await axios.post(
              "http://127.0.0.1:8000/api/enrolled-subjs/",
              enrollment
            );
            console.log("Enrollment response:", response.data);
          }
        }
      } catch (error) {
        console.error(
          "Error posting to prof-subjs:",
          error.response?.data || error
        );
      }
    }
    alert("Data and student enrollments submitted successfully.");
  } catch (error) {
    console.error("Error submitting data:", error.response?.data || error);
    alert("Failed to submit data.");
  }
};

onMounted(() => {
  loadProfessors();
});
</script>

<template>
  <secretaryNavbar></secretaryNavbar>
  <section class="p-20 pt-32 rounded space-y-14 font-raleway">
    <div class="flex items-center space-x-2">
      <Avatar class="w-16 h-16">
        <AvatarImage
          src="https://i1.sndcdn.com/artworks-NuIfnZ3ZMRhLnlEz-QHsZQA-t500x500.jpg"
        />
        <AvatarFallback>PLP</AvatarFallback>
      </Avatar>
      <div class="w-full">
        <Select v-model="selectedProfessor">
          <SelectTrigger
            class="sm:max-w-fit ring-0 border-0 focus-visible:ring-offset-0 focus-visible:ring-0 text-3xl font-bold text-darks-500"
          >
            <SelectValue placeholder="Select Professor" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectLabel>Professors</SelectLabel>
              <SelectItem
                v-for="professor in professors"
                :key="professor.professor_id"
                :value="professor.professor_id"
              >
                <div class="flex items-center gap-2">
                  <span>{{ professor.full_name }}</span>
                </div>
              </SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>

        <p class="text-base text-darks-400/60 font-medium pl-3.5">
          {{ selectedCollege }}
        </p>
      </div>
    </div>
    <div>
      <div class="text-xs pb-2 text-darks-200/70 font-medium pl-0 pt-8">
        Assign subjects and sections to this professor for the current semester.
      </div>
      <div class="border border-black/25 rounded-md">
        <div
          class="flex items-center justify-between border-b border-black/15 text-sm h-14 p-4 pl-5 font-medium text-darks-200/80 hover:bg-darks-50/80 p-2 w-full rounded-t-md"
        >
          <p class="w-6/12">Subject</p>
          <p class="w-6/12 mr-14">Section</p>
        </div>
        <div>
          <div
            v-for="(tag, index) in subjectsectionTags"
            :key="tag"
            class="flex items center pr-12 border-b border-black/15 hover:bg-darks-50/80 space-x-8"
          >
            <div class="flex items-center space-x-4 p-2 w-full">
              <subjectTagging
                @updateSubjects="(subjects) => updateSubjects(subjects, index)"
              />
              <sectionTagging
                @updateSections="(sections) => updateSections(sections, index)"
              />
            </div>

            <button
              @click="removeSubjectSectionTag(index)"
              class="text-red-500 hover:text-red-700"
            >
              <Trash class="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
      <button
        @click="addSubjectSectionTag"
        class="flex items-center h-14 text-sm w-full font-medium text-darks-100 hover:bg-darks-50/80 space-x-1 rounded-md"
      >
        <Plus class="w-5 h-5" />
        <p>New</p>
      </button>
      <div class="flex justify-end mt-4">
        <Button
          class="bg-plpgreen-200 hover:bg-plpgreen-400"
          @click="submitData"
          >Submit</Button
        >
      </div>
    </div>
  </section>
</template>
