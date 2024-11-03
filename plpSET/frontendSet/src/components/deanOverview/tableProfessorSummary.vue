<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import axios from "axios";
import { Table, TableBody, TableCell, TableRow } from "@/components/ui/table";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
import { useRouter } from "vue-router";

interface Professor {
  id: string;
  name: string;
  avatarUrl: string;
  initials: string;
  total_avg: number;
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
  positive_percentage?: number;
  neutral_percentage?: number;
  negative_percentage?: number;
  rating_label?: string;
  rating_color?: string;
}

interface College {
  name: string;
  description: string;
  professor_list: Professor[];
}

interface Summary {
  year_sem: string;
  summary: College[];
}

const router = useRouter();
const collegeData = ref<College | null>(null);

const fetchCollegeData = async () => {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/college-ratings-summary/"
    );

    if (response.data && response.data.summary) {
      const yearsemIdentifier = localStorage.getItem("current_year_sem");
      const collegeIdentifier = localStorage.getItem("college");

      const selectedYearSem = response.data.year_sem === yearsemIdentifier;

      if (selectedYearSem) {
        const selectedCollege = response.data.summary.find(
          (collegeSummary: College) => collegeSummary.name === collegeIdentifier
        );

        if (selectedCollege) {
          collegeData.value = selectedCollege;
          calculateFeedbackPercentages(selectedCollege.professor_list);
        } else {
          console.error(
            "No matching college found for the identifier:",
            collegeIdentifier
          );
        }
      } else {
        console.error(
          "No matching year_sem found for identifier:",
          yearsemIdentifier
        );
      }
    } else {
      console.error("No data received or invalid year_sem identifier.");
    }
  } catch (error) {
    console.error("Error fetching college data:", error);
  }
};

// Function to determine rating label based on average score
const getRatingLabel = (avg: number) => {
  if (avg >= 4.6) return "Outstanding";
  if (avg >= 4.0) return "Very Satisfactory";
  if (avg >= 3.4) return "Satisfactory";
  if (avg >= 3.0) return "Fair";
  return "Poor";
};

// Function to determine color class based on rating label
const getRatingColor = (label: string) => {
  switch (label) {
    case "Outstanding":
      return "text-plpgreen-400";
    case "Very Satisfactory":
      return "text-plpgreen-200";
    case "Satisfactory":
      return "text-yellow-500";
    case "Fair":
      return "text-orange-500";
    case "Poor":
      return "text-red-700";
    default:
      return "text-gray-500";
  }
};

const calculateFeedbackPercentages = (professorList: Professor[]) => {
  for (const professor of professorList) {
    const totalFeedbacks = professor.total_feedbacks;
    professor.positive_percentage = totalFeedbacks
      ? (professor.total_positive / totalFeedbacks) * 100
      : 0;
    professor.neutral_percentage = totalFeedbacks
      ? (professor.total_neutral / totalFeedbacks) * 100
      : 0;
    professor.negative_percentage = totalFeedbacks
      ? (professor.total_negative / totalFeedbacks) * 100
      : 0;

    // Assign the rating label and color based on total_avg
    professor.rating_label = getRatingLabel(professor.total_avg);
    professor.rating_color = getRatingColor(professor.rating_label);
  }
};

onMounted(() => {
  fetchCollegeData();
});

const onRowClick = (professor: Professor) => {
  localStorage.setItem("professor", professor.id);
  router.push("/DeanDashboard-ProfessorAnalytics");
};
</script>

<template>
  <ScrollArea class="h-[364px] w-full">
    <div v-if="collegeData">
      <Table>
        <TableBody>
          <TableRow
            v-for="professor in collegeData.professor_list"
            :key="professor.id"
            @click="onRowClick(professor)"
            class="cursor-pointer hover:bg-gray-100"
          >
            <TableCell>
              <div class="flex items-center space-x-2">
                <Avatar class="w-8 h-8">
                  <AvatarImage :src="professor.avatarUrl" />
                  <AvatarFallback>{{ professor.initials }}</AvatarFallback>
                </Avatar>
                <p>{{ professor.name }}</p>
              </div>
            </TableCell>
            <TableCell>
              <div class="flex flex-col items-center">
                <p class="text-xs font-bold">
                  {{ professor.total_avg.toFixed(2) }}
                </p>
                <p :class="professor.rating_color" class="text-xs">
                  {{ professor.rating_label }}
                </p>
              </div>
            </TableCell>
            <TableCell>
              <div class="flex flex-col items-center text-center">
                <p class="text-xs font-bold">
                  {{ professor.positive_percentage?.toFixed(1) }}%
                </p>
                <p class="text-xs text-darks-200">Positive Feedbacks</p>
              </div>
            </TableCell>
            <TableCell>
              <div class="flex flex-col items-center text-center">
                <p class="text-xs font-bold">
                  {{ professor.neutral_percentage?.toFixed(1) }}%
                </p>
                <p class="text-xs text-darks-200">Neutral Feedbacks</p>
              </div>
            </TableCell>
            <TableCell>
              <div class="flex flex-col items-center text-center">
                <p class="text-xs font-bold">
                  {{ professor.negative_percentage?.toFixed(1) }}%
                </p>
                <p class="text-xs text-darks-200">Negative Feedbacks</p>
              </div>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
    <div v-else>
      <p>Loading college data...</p>
    </div>
  </ScrollArea>
</template>
