<script setup lang="ts">
import subjectComponent from "@/components/SET/subjectComponent.vue";
import navbar from "@/components/navigation/NavBarMIS.vue";
import { ref, onMounted, computed } from "vue";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Button } from "@/components/ui/button";
import professorHeatmap from "@/components/deanProfessorAnalytics/professorHeatmap.vue";
import professorFeedbackChart from "@/components/deanProfessorAnalytics/professorFeedbackChart.vue";
import professorRadar from "@/components/deanProfessorAnalytics/professorRadar.vue";
import professorFeedbacksTable from "@/components/feedbacks/professorFeedbacksTable.vue";
import profreccuringphrasesTable from "@/components/profsrecurringPhrases/profreccuringphrasesTable.vue";
import AdjetiveRating from "@/components/AdjetiveRating.vue";
import axios from "axios";
import { useAuthStore } from "@/store/adminStore";
const authStore = useAuthStore();
authStore.restoreSession();

interface CategoryAvg {
  category_id: string;
  category_desc: string;
  rating_label?: string;
  average: number;
}

interface NumericalSummary {
  total_avg: number;
  category_avg: CategoryAvg[];
}

interface FeedbackSummary {
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
}

interface Professors {
  id: string;
  name: string;
  dept_id: string;
  dept_desc: string;
  avatarUrl: string;
  feedback_summary: FeedbackSummary[];
  numerical_summary: NumericalSummary;
}

interface Summary {
  year_sem: string;
  professors: Professors[];
}

const professorData = ref<Professors | null>(null);
const professorIdentifier = localStorage.getItem("professor");
const yearsemIdentifier = localStorage.getItem("current_year_sem");

const fetchProfessorData = async () => {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/professor-ratings-summary/"
    );
    console.log("API response:", response.data);

    if (response.data.length && yearsemIdentifier) {
      const selectedYearSem = response.data.find(
        (summary: Summary) => summary.year_sem === yearsemIdentifier
      );

      if (selectedYearSem && professorIdentifier) {
        const selectedProfessor = selectedYearSem.professors.find(
          (professorSummary: Professors) =>
            professorSummary.id === professorIdentifier
        );

        console.log("Selected Professor:", selectedProfessor);

        if (selectedProfessor) {
          professorData.value = selectedProfessor;
          console.log("professorData updated:", professorData.value);
        } else {
          console.error(
            "No matching professor found for the identifier:",
            professorIdentifier
          );
        }
      } else {
        console.error("No matching year_sem found or invalid identifiers.");
      }
    } else {
      console.error("No data received or year_sem identifier is invalid.");
    }
  } catch (error) {
    console.error("Error fetching professor data:", error);
  }
};

// Determine the rating label
const ratingLabel = computed(() => {
  const avg = professorData.value?.numerical_summary.total_avg || 0;
  if (avg >= 4.6) return "Outstanding";
  if (avg >= 4.0) return "Very Satisfactory";
  if (avg >= 3.4) return "Satisfactory";
  if (avg >= 3.0) return "Fair";
  return "Poor";
});

const ratingColor = computed(() => {
  switch (ratingLabel.value) {
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
});

const topCategory = computed(() => {
  if (!professorData.value || !professorData.value.numerical_summary) {
    console.log("professorData or numerical_summary is missing");
    return null;
  }

  const { category_avg } = professorData.value.numerical_summary;
  if (!category_avg.length) return null;

  const sortedCategories = [...category_avg].sort(
    (a, b) => b.average - a.average
  );
  console.log("Top category:", sortedCategories[0]);
  return sortedCategories[0];
});

const bottomCategory = computed(() => {
  if (!professorData.value || !professorData.value.numerical_summary) {
    console.log("professorData or numerical_summary is missing");
    return null;
  }

  const { category_avg } = professorData.value.numerical_summary;
  if (!category_avg.length) return null;

  const sortedCategories = [...category_avg].sort(
    (a, b) => a.average - b.average
  );
  console.log("Bottom category:", sortedCategories[0]);
  return sortedCategories[0];
});

const feedbackScore = computed(() => {
  const feedback = professorData.value?.feedback_summary[0];
  if (!feedback) return "Loading...";

  const totalFeedbacks = feedback.total_feedbacks || 1;
  const positivePercentage = (feedback.total_positive / totalFeedbacks) * 100;
  const neutralPercentage = (feedback.total_neutral / totalFeedbacks) * 100;
  const negativePercentage = (feedback.total_negative / totalFeedbacks) * 100;

  if (
    positivePercentage >= neutralPercentage &&
    positivePercentage >= negativePercentage
  ) {
    return `${positivePercentage.toFixed(1)}% Positive`;
  } else if (
    neutralPercentage >= positivePercentage &&
    neutralPercentage >= negativePercentage
  ) {
    return `${neutralPercentage.toFixed(1)}% Neutral`;
  } else {
    return `${negativePercentage.toFixed(1)}% Negative`;
  }
});

const feedbackColor = computed(() => {
  const feedback = feedbackScore.value;

  if (feedback.includes("Positive")) {
    return "text-plpgreen-400";
  } else if (feedback.includes("Neutral")) {
    return "text-yellow-500";
  } else if (feedback.includes("Negative")) {
    return "text-red-500";
  } else {
    return "text-gray-500";
  }
});

onMounted(() => {
  fetchProfessorData();
});
</script>

<template>
  <navbar />

  <section class="transition-all duration-300">
    <section class="p-20 pt-32 space-y-12">
      <div
        class="flex items-center justify-between"
        v-if="professorData?.numerical_summary?.category_avg?.length"
      >
        <div class="flex items-center space-x-2">
          <Avatar class="w-16 h-16">
            <AvatarImage :src="professorData.avatarUrl" />
            <AvatarFallback>PLP</AvatarFallback>
          </Avatar>
          <div class="w-full">
            <p class="font-bold text-3xl">{{ professorData.name }}</p>
            <p class="text-base text-darks-400/60 font-medium">
              {{ professorData.dept_desc }}
            </p>
          </div>
        </div>
        <div class="flex space-x-2">
          <Button
            class="px-4 h-10 rounded-md font-medium text-sm bg-plpgreen-100 text-gray-700 hover:bg-plpgreen-200/80 hover:text-white"
          >
            Compare
          </Button>
        </div>
      </div>
      <!----Numerical Ratings-->
      <div class="grid grid-cols-9 grid-rows-8 gap-4 h-[480px]">
        <div class="col-span-3 row-span-2 border border-black/15 rounded-md">
          <div class="p-7">
            <p class="text-sm text-darks-200/50 font-medium">Average Rating</p>
            <TooltipProvider>
              <Tooltip>
                <TooltipTrigger>
                  <p
                    v-if="
                      professorData?.numerical_summary?.category_avg?.length
                    "
                    :class="`text-2xl font-bold ${ratingColor}`"
                  >
                    {{
                      professorData.numerical_summary.category_avg[0]?.average
                    }}
                    -
                    {{ ratingLabel }}
                  </p></TooltipTrigger
                >
                <TooltipContent>
                  <AdjetiveRating></AdjetiveRating>
                </TooltipContent>
              </Tooltip>
            </TooltipProvider>
          </div>
        </div>
        <div
          class="col-span-3 row-span-2 col-start-4 border border-black/15 rounded-md"
        >
          <div class="p-7">
            <p class="text-sm text-darks-200/50 font-medium">Strength Areas</p>
            <p
              class="text-2xl font-bold text-plpgreen-200"
              v-if="professorData?.numerical_summary?.category_avg?.length"
            >
              {{ topCategory.category_desc }}
            </p>
          </div>
        </div>
        <div
          class="col-span-3 row-span-2 col-start-7 border border-black/15 rounded-md"
        >
          <div class="p-7">
            <p class="text-sm text-darks-200/50 font-medium">Focus Areas</p>
            <p
              class="text-2xl font-bold text-reds-800"
              v-if="professorData?.numerical_summary?.category_avg?.length"
            >
              {{ bottomCategory.category_desc }}
            </p>
          </div>
        </div>
        <div
          class="col-span-3 row-span-6 row-start-3 border border-black/15 rounded-md"
        >
          <professorRadar />
        </div>
        <div
          class="col-span-6 row-span-6 col-start-4 row-start-3 border border-black/15 rounded-md p-6 pb-14"
        >
          <p class="text-base text-darks-200/50 font-medium">
            Rating Distribution
          </p>
          <professorHeatmap />
        </div>
      </div>

      <!----Feedback Ratings-->
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <p class="font-semibold text-xl">Feedback and Sentiment Insights</p>
        </div>
        <div class="grid grid-cols-9 grid-rows-12 gap-4 h-[720px]">
          <div class="col-span-3 row-span-2 border border-black/15 rounded-md">
            <div class="p-7">
              <p class="text-sm text-darks-200/50 font-medium">
                Feedback Score
              </p>
              <p class="text-2xl font-bold" :class="feedbackColor">
                {{ feedbackScore }}
              </p>
            </div>
          </div>
          <div
            class="col-span-3 row-span-4 row-start-3 border border-black/15 rounded-md py-2 px-1"
          >
            <professorFeedbackChart />
          </div>
          <div
            class="col-span-6 row-span-6 col-start-4 border border-black/15 rounded-md"
          >
            <profreccuringphrasesTable></profreccuringphrasesTable>
          </div>

          <div
            class="col-span-9 row-span-6 row-start-7 border border-black/15 rounded-md"
          >
            <professorFeedbacksTable />
          </div>
        </div>
      </div>
    </section>
  </section>
</template>
