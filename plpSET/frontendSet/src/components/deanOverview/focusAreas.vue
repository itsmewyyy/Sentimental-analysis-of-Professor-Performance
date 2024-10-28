<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import axios from "axios";
import { Table, TableBody, TableCell, TableRow } from "@/components/ui/table";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";

interface Professor {
  id: number;
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
  summary: Summary[];
}

const collegeData = ref<College | null>(null);
const collegeIdentifier = localStorage.getItem("college");
const yearsemIdentifier = "24-25-1";
//const yearsemIdentifier = localStorage.getItem("year_sem");

const fetchCollegeData = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/college-ratings-summary/"
    );

    if (response.data.length && yearsemIdentifier) {
      // First, find the specific year_sem data
      const selectedYearSem = response.data.find(
        (summary: Summary) => summary.year_sem === yearsemIdentifier
      );

      if (selectedYearSem && collegeIdentifier) {
        // Next, find the specific college within the selected year_sem
        const selectedCollege = selectedYearSem.summary.find(
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
        console.error("No matching year_sem found or invalid identifiers.");
      }
    } else {
      console.error("No data received or year_sem identifier is invalid.");
    }
  } catch (error) {
    console.error("Error fetching college data:", error);
  }
};

const normalize = (value: number, max: number) => (value / max) * 100;

// Function to determine the rating label based on average score
const getRatingLabel = (avg: number) => {
  if (avg >= 4.6) return "Outstanding";
  if (avg >= 4.0) return "Very Satisfactory";
  if (avg >= 3.4) return "Satisfactory";
  if (avg >= 3.0) return "Fair";
  return "Poor";
};

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

// Function to calculate feedback percentages for each professor
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

    // Assign the rating label based on total_avg
    professor.rating_label = getRatingLabel(professor.total_avg);
    professor.rating_color = getRatingColor(professor.rating_label);
  }
};

// Function to calculate feedback score for a given professor
const calculateFeedbackScore = (professor: Professor) => {
  const { positive_percentage, neutral_percentage, negative_percentage } =
    professor;

  if (
    positive_percentage >= neutral_percentage &&
    positive_percentage >= negative_percentage
  ) {
    return `${positive_percentage.toFixed(1)}% Positive`;
  } else if (
    neutral_percentage >= positive_percentage &&
    neutral_percentage >= negative_percentage
  ) {
    return `${neutral_percentage.toFixed(1)}% Neutral`;
  } else {
    return `${negative_percentage.toFixed(1)}% Negative `;
  }
};

// Calculate composite score for each professor
const calculateCompositeScore = (professor: Professor) => {
  const numericalAvg = normalize(professor.total_avg, 5); // assuming 5 is the max numerical score
  const positivePercentage = professor.positive_percentage;

  // Composite score combining 60% numerical average and 40% positive feedback percentage
  const compositeScore = numericalAvg * 0.6 + positivePercentage * 0.4;
  return compositeScore;
};

// Computed property to get sorted professors by composite score
const sortedProfessors = computed(() => {
  if (!collegeData.value?.professor_list?.length) return [];

  return collegeData.value.professor_list
    .map((professor) => ({
      ...professor,
      compositeScore: calculateCompositeScore(professor),
    }))
    .sort((a, b) => b.compositeScore - a.compositeScore); // Sort in descending order
});

// Extract top 3 professors
const bottom3Professors = computed(() => sortedProfessors.value.slice(-3));

onMounted(() => {
  fetchCollegeData();
});
</script>

<template>
  <ScrollArea class="h-32 w-full">
    <div v-if="collegeData">
      <Table>
        <TableBody>
          <TableRow v-for="professor in bottom3Professors" :key="professor.id">
            <TableCell>
              <div class="flex items-center space-x-2">
                <p>{{ professor.name }}</p>
              </div>
            </TableCell>

            <TableCell>
              <div class="flex flex-col items-center text-center">
                <p class="text-xs font-bold">
                  {{ professor.total_avg }}
                </p>
                <p class="text-xs" :class="professor.rating_color">
                  {{ professor.rating_label }}
                </p>
              </div>
            </TableCell>
            <TableCell>
              <div class="flex flex-col items-center text-center">
                <p class="text-xs font-medium">
                  {{ calculateFeedbackScore(professor) }}
                </p>
              </div>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div></ScrollArea
  >
</template>
