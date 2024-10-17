<script setup lang="ts">
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardTitle,
  CardHeader,
  CardDescription,
  CardFooter,
} from "@/components/ui/card";
import { CircleCheckBig } from "lucide-vue-next";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

// Define interfaces
interface ProfessorInfo {
  surname: string;
  first_name: string;
}

interface SubjectName {
  subject_code: string;
  subject_desc: string;
}

interface Subject {
  student_enrolled_subj_id: string;
  prof_info: ProfessorInfo;
  subj_name: SubjectName;
  is_evaluated: boolean;
}

interface EnrolledSubject {
  student_id: string;
  section: string;
  subjects: Subject[];
}

const enrolledSubjects = ref<EnrolledSubject[]>([]);
const router = useRouter();

// Fetch student's subjects from API
const fetchSubjects = async () => {
  try {
    const student_id = localStorage.getItem("student_id"); // Fetch student ID from localStorage
    const response = await axios.get<Subject[]>(
      `http://127.0.0.1:8000/api/enrolled_subjs/${student_id}`
    );

    // Assign response directly if it's an array of subjects
    enrolledSubjects.value = [
      { student_id, section: "", subjects: response.data },
    ];
    console.log("API response:", response.data);
  } catch (error) {
    console.error("Error fetching subjects:", error);
  }
};

// Store the `student_enrolled_subj_id` in localStorage
function evaluateSubject(subject: Subject) {
  localStorage.setItem(
    "student_enrolled_subj_id",
    subject.student_enrolled_subj_id
  );
  router.push("/evaluation");
}

onMounted(() => {
  fetchSubjects();
});
</script>

<template>
  <div
    v-for="(enrolledSubj, enrolledSubjIndex) in enrolledSubjects"
    :key="enrolledSubjIndex"
    class="flex flex-wrap w-fit"
  >
    <div
      v-for="(subject, subjectIndex) in enrolledSubj.subjects"
      :key="subjectIndex"
      :id="`${subject.student_enrolled_subj_id}`"
      class="pb-8 pl-8"
    >
      <Card class="w-80 h-52 relative rounded-lg border border-black/15">
        <div
          class="absolute top-0 left-0 w-full h-1/2 bg-yellow-100/80 rounded-t-lg"
        ></div>
        <div class="relative h-full flex flex-col">
          <CardHeader>
            <CardTitle class="text-base font-medium">
              {{ subject.subj_name.subject_desc }}
            </CardTitle>
            <CardDescription class="text-sm text-gray-600">
              {{ subject.prof_info.first_name }}
              {{ subject.prof_info.surname }}
            </CardDescription>
          </CardHeader>
          <CardFooter class="flex justify-center mt-auto">
            <!-- If the subject is not yet evaluated, show "Evaluate" button -->
            <Button
              v-if="!subject.is_evaluated"
              class="bg-plpgreen-200 hover:bg-plpgreen-400 w-1/2 text-sm font-medium"
              @click="evaluateSubject(subject)"
            >
              Evaluate
            </Button>

            <!-- If already evaluated, show a div -->
            <div
              v-else
              class="font-medium flex space-x-1 items-center mb-2.5 cursor-not-allowed"
            >
              <p class="text-plpgreen-400 text-sm">Evaluated</p>
              <CircleCheckBig class="w-5 h-5" color="#5F965E" />
            </div>
          </CardFooter>
          <Avatar
            class="absolute right-4 top-1/2 transform -translate-y-1/2 w-14 h-14 rounded-full"
          >
            <AvatarImage
              src="https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg"
            />
            <AvatarFallback>PLP</AvatarFallback>
          </Avatar>
        </div>
      </Card>
    </div>
  </div>
</template>
