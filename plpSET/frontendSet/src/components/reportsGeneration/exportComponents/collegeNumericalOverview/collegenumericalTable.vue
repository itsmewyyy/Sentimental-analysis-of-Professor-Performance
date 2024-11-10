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

// Get selected college from localStorage

const fetchCategoriesAndAverages = async () => {
  const selectedCollege = localStorage.getItem("college");
  try {
    // Fetch categories and questions
    const categoriesResponse = await axios.get(
      "http://127.0.0.1:8000/api/categories-and-questions/"
    );
    const allCategories = categoriesResponse.data;

    // Fetch college ratings summary for averages
    const ratingsResponse = await axios.get(
      "http://127.0.0.1:8000/api/college-ratings-summary/"
    );
    const collegeData = ratingsResponse.data.summary.find(
      (college) => college.name === selectedCollege
    );

    // If the selected college has data, map it to categories with averages
    if (collegeData) {
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
            // Find the question's average if it exists in the summary
            const questionAvg = categorySummary?.question_avg.find(
              (avgQuestion) =>
                avgQuestion.question_id === question.numerical_question_id
            );

            return {
              numerical_question_id: question.numerical_question_id,
              question: question.question,
              average: questionAvg ? questionAvg.average : null,
            };
          }),
        };
      });
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

// Fetch data on component mount
onMounted(fetchCategoriesAndAverages);
</script>
