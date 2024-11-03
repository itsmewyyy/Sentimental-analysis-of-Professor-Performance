import { ref, onMounted, watchEffect } from "vue";
import axios from "axios";
import academicTermStore from "@/store/academicTermStore";

export function useAcademicTerm() {
  const isAcademicTermSet = ref(!!localStorage.getItem("year_sem"));
  const isEvaluationPeriodSet = ref(false);
  const yearSem = ref(localStorage.getItem("year_sem") || "");

  async function checkEvaluationStatus() {
    try {
      const response = await axios.get(
        "https://sentiment-professor-feedback-1.onrender.com/api/evaluation-status/"
      );
      isAcademicTermSet.value = response.data.isAcademicTermSet;
      isEvaluationPeriodSet.value = response.data.isEvaluationPeriodSet;

      if (!yearSem.value) {
        yearSem.value = response.data.year_sem || "";
        localStorage.setItem("current_year_sem", yearSem.value);
      }
    } catch (error) {
      console.error("Error fetching evaluation status:", error);
    }
  }

  onMounted(() => {
    if (!localStorage.getItem("year_sem")) {
      checkEvaluationStatus();
    }
  });

  const setAcademicTerm = async (yearSemId) => {
    yearSem.value = yearSemId;
    localStorage.setItem("year_sem", yearSemId);
    isAcademicTermSet.value = true;
    await checkEvaluationStatus();
  };

  const setEvaluationPeriod = () => {
    isEvaluationPeriodSet.value = true;
  };

  watchEffect(() => {
    isAcademicTermSet.value = !!localStorage.getItem("year_sem");
  });

  return {
    isAcademicTermSet,
    isEvaluationPeriodSet,
    yearSem,
    setAcademicTerm,
    setEvaluationPeriod,
    academicTermStore,
  };
}
