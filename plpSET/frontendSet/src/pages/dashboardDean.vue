<script setup lang="ts">
import navbar from "@/components/navigation/deanNavbar.vue";
import { ref, onMounted, computed } from "vue";
import { useAuthStore } from "@/store/student";
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
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Button } from "@/components/ui/button";
import collegeFeedbackChart from "@/components/deanOverview/collegeFeedbackChart.vue";
import collegeNumericalRadar from "@/components/deanOverview/collegeRadar.vue";
import tableProfessorSummary from "@/components/deanOverview/tableProfessorSummary.vue";
import axios from "axios";
import facultyStars from "@/components/deanOverview/facultyStars.vue";
import focusAreas from "@/components/deanOverview/focusAreas.vue";

const authStore = useAuthStore();
authStore.restoreSession();

interface FeedbackSummary {
  total_feedbacks: number;
  total_positive: number;
  total_neutral: number;
  total_negative: number;
}

interface NumericalSummary {
  total_avg: number;
}

interface College {
  name: string;
  description: string;
  feedback_summary: FeedbackSummary[];
  numerical_summary: NumericalSummary[];
}

interface Summary {
  year_sem: string;
  summary: College[];
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
      // Find the year_sem
      const selectedYearSem = response.data.find(
        (summary: Summary) => summary.year_sem === yearsemIdentifier
      );

      if (selectedYearSem && collegeIdentifier) {
        // Within the selected year_sem, find the specific professor
        const selectedCollege = selectedYearSem.summary.find(
          (collegeSummary: College) => collegeSummary.name === collegeIdentifier
        );

        console.log("Selected Professor:", selectedCollege);

        if (selectedCollege) {
          collegeData.value = selectedCollege;
          console.log("professorData updated:", collegeData.value);
        } else {
          console.error(
            "No matching professor found for the identifier:",
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
    console.error("Error fetching professor data:", error);
  }
};

// Computed property to determine the rating label
const ratingLabel = computed(() => {
  const avg = collegeData.value?.numerical_summary[0].total_avg || 0;
  if (avg >= 4.6) return "Outstanding";
  if (avg >= 4.0) return "Very Satisfactory";
  if (avg >= 3.4) return "Satisfactory";
  if (avg >= 3.0) return "Fair";
  return "Poor";
});

// Computed property to return the color based on the rating label
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

// Computed property to determine the highest feedback score (positive, neutral, or negative)
const feedbackScore = computed(() => {
  const feedback = collegeData.value?.feedback_summary[0];
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

//Assign colors for highest feedback sentiment
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
  fetchCollegeData();
});
</script>

<template>
  <navbar />
  <section class="transition-all duration-300">
    <section class="p-20 pt-32 space-y-12">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <Avatar class="w-16 h-16">
            <AvatarImage
              src="https://i1.sndcdn.com/artworks-NuIfnZ3ZMRhLnlEz-QHsZQA-t500x500.jpg"
            />
            <AvatarFallback>PLP</AvatarFallback>
          </Avatar>
          <div class="w-4/6">
            <p class="font-bold text-3xl">Overview of Faculty Performance</p>
            <p class="text-sm text-darks-400/60 font-medium">
              This performance overview provides insights into faculty
              effectiveness, drawn from student feedback and ratings for the
              academic year 2024-2025, second semester.
            </p>
          </div>
        </div>
        <div class="flex space-x-2">
          <Select>
            <SelectTrigger
              class="h-10 font-medium text-sm text-plpgreen-400 border border-plpgreen-200/40 focus:ring-plpgreen-200 px-4"
            >
              <SelectValue placeholder="Select Year and Semester" />
            </SelectTrigger>

            <SelectContent>
              <SelectGroup>
                <SelectLabel>Year and Semesters</SelectLabel>
                <SelectItem value="sample">
                  2024 - 2025 2nd Semester
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
          <Button
            class="px-4 h-10 rounded-md font-medium text-sm bg-plpgreen-100 text-gray-800 hover:bg-plpgreen-200/80 hover:text-white"
          >
            Compare
          </Button>
        </div>
      </div>

      <!---Summary---->
      <div class="space-y-4">
        <div class="grid grid-cols-10 grid-rows-8 gap-4 h-[480px]">
          <div class="col-span-3 row-span-2 border border-black/15 rounded-md">
            <div class="p-7">
              <p class="text-sm text-darks-200/50 font-medium">
                Faculty Rating
              </p>
              <TooltipProvider>
                <Tooltip>
                  <TooltipTrigger>
                    <p
                      v-if="collegeData?.numerical_summary?.length"
                      :class="`text-2xl font-bold ${ratingColor}`"
                    >
                      {{ collegeData.numerical_summary[0]?.total_avg }} -
                      {{ ratingLabel }}
                    </p></TooltipTrigger
                  >
                  <TooltipContent>
                    <div class="p-8">
                      <div><p>Adjectival Rating Scale:</p></div>
                      <div></div>
                    </div>
                  </TooltipContent>
                </Tooltip>
              </TooltipProvider>
            </div>
          </div>

          <div
            class="col-span-3 row-span-2 col-start-4 border border-black/15 rounded-md"
          >
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
            class="col-span-4 row-span-2 col-start-7 border border-black/15 rounded-md"
          ></div>
          <div
            class="col-span-3 row-span-6 row-start-3 border border-black/15 rounded-md"
          >
            <collegeNumericalRadar />
          </div>
          <div
            class="col-span-3 row-span-6 col-start-4 row-start-3 border border-black/15 rounded-md p-7"
          >
            <collegeFeedbackChart />
          </div>
          <div
            class="col-span-4 row-span-6 col-start-7 row-start-3 border border-black/15 rounded-md"
          ></div>
        </div>

        <!---Professors---->

        <div class="grid grid-cols-5 grid-rows-6 gap-4 h-[480px]">
          <div class="col-span-3 font-semibold text-xl pt-10">
            Professor Performance Summary
          </div>
          <div
            class="col-span-3 row-span-5 col-start-1 row-start-2 border border-black/15 rounded-md p-4"
          >
            <tableProfessorSummary />
          </div>
          <div
            class="col-span-2 col-start-4 row-start-1 font-semibold text-xl pt-10"
          >
            Faculty Stars
          </div>
          <div
            class="col-span-2 row-span-2 col-start-4 row-start-2 border border-black/15 rounded-md p-2"
          >
            <facultyStars />
          </div>
          <div
            class="col-span-2 col-start-4 row-start-4 font-semibold text-xl pt-10"
          >
            Focus Areas
          </div>
          <div
            class="col-span-2 row-span-2 col-start-4 row-start-5 border border-black/15 rounded-md p-2"
          >
            <focusAreas />
          </div>
        </div>
      </div>
    </section>
  </section>
</template>
