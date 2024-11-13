<template>
  <div class="flex justify-center p-2">
    <Table class="border text-sm">
      <TableHeader>
        <TableRow>
          <TableHead class="w-[40px] font-bold border-r p-2"
            >CATEGORY</TableHead
          >
          <TableHead class="w-[40px] font-bold border-r p-2"
            >Questionnaire</TableHead
          >
          <TableHead class="w-[100px] text-center font-bold p-2"
            >Average</TableHead
          >
        </TableRow>
      </TableHeader>
      <TableBody>
        <template
          v-for="(category, categoryIndex) in categories"
          :key="categoryIndex"
        >
          <TableRow class="bg-muted/50">
            <TableCell
              class="font-bold align-top p-2 border-r"
              :rowspan="category.questions.length + 1"
            >
              {{ category.category_desc }}
            </TableCell>
          </TableRow>
          <TableRow
            v-for="(question, questionIndex) in category.questions"
            :key="question.numerical_question_id"
          >
            <TableCell class="border-r p-2">{{ question.question }}</TableCell>
            <TableCell class="text-center p-2">{{
              question.average !== null ? question.average : "N/A"
            }}</TableCell>
          </TableRow>
        </template>
      </TableBody>
    </Table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import axios from "axios";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const categories = ref([]);

const props = defineProps({
  refreshChart: Boolean,
  college: String,
  professor: String,
  question: String,
});

watch(
  () => props.refreshChart,
  () => {
    fetchCategoriesAndAverages();
  }
);

const fetchCategoriesAndAverages = async () => {
  const selectedCollege = localStorage.getItem("college");
  const yearsemIdentifier = localStorage.getItem("current_year_sem");
  if (!selectedCollege || !yearsemIdentifier) {
    console.warn("No college or year/sem selected in localStorage.");
    return;
  }

  try {
    // Fetch categories and questions
    const categoriesResponse = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/categories-and-questions/"
    );
    const allCategories = categoriesResponse.data;

    // Fetch college ratings summary for averages
    const ratingsResponse = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/college-ratings-summary/"
    );

    // Find the data for the specified year and semester
    const yearSemData = ratingsResponse.data.find(
      (item) => item.year_sem === yearsemIdentifier
    );

    if (!yearSemData) {
      console.warn(`No data found for year/sem ${yearsemIdentifier}.`);
      return;
    }

    // Find the college data within the selected year/sem data
    const collegeData = yearSemData.colleges.find(
      (college) => college.name === selectedCollege
    );

    if (collegeData && collegeData.numerical_summary?.[0]?.category_avg) {
      categories.value = allCategories.map((category) => {
        // Find matching category from the college ratings summary
        const categorySummary =
          collegeData.numerical_summary[0].category_avg.find(
            (avgCategory) =>
              avgCategory.category_desc === category.category_desc
          );

        return {
          category_desc: category.category_desc,
          questions: category.questions.map((question) => {
            const questionAvg = categorySummary?.question_avg.find(
              (avgQuestion) =>
                avgQuestion.question_id === question.numerical_question_id
            );

            return {
              numerical_question_id: question.numerical_question_id,
              question: question.question,
              average: questionAvg
                ? parseFloat(questionAvg.average.toFixed(2))
                : null,
            };
          }),
        };
      });
    } else {
      console.warn(
        "No data found for selected college or missing numerical_summary."
      );
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

// Fetch data on component mount
onMounted(fetchCategoriesAndAverages);
</script>
