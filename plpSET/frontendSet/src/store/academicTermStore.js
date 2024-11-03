// academicTermStore.js
import { reactive, computed } from "vue";

const state = reactive({
  yearSem: localStorage.getItem("year_sem") || "",
  isAcademicTermSet: computed(() => !!state.yearSem),
  isEvaluationPeriodSet: false,
});

function setAcademicTerm(yearSemId) {
  state.yearSem = yearSemId;
  localStorage.setItem("year_sem", yearSemId);
}

function setEvaluationPeriod() {
  state.isEvaluationPeriodSet = true;
}

export default {
  state,
  setAcademicTerm,
  setEvaluationPeriod,
};
