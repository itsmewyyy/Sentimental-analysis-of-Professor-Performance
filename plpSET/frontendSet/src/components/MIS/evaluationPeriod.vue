<script setup lang="ts">
import { Button } from "@/components/ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { Calendar } from "@/components/ui/v-calendar";
import { cn } from "@/lib/utils";
import { addDays, format } from "date-fns";
import { Calendar as CalendarIcon } from "lucide-vue-next";
import { ref } from "vue";
import academicTermStore from "@/store/academicTermStore";
import axios from "axios";

const { state, setEvaluationPeriod } = academicTermStore;
const evaluationPeriod = ref({ start: null, end: null });

const date = ref({
  start: new Date(2022, 0, 20),
  end: addDays(new Date(2022, 0, 20), 20),
});

async function onSetEvaluationPeriod() {
  const { start, end } = date.value;

  if (start && end) {
    try {
      const formattedStart = format(start, "yyyy-MM-dd'T'HH:mm:ssxxx");
      const formattedEnd = format(end, "yyyy-MM-dd'T'HH:mm:ssxxx");
      const newlyset_acadyearsem = localStorage.getItem("year_sem");
      await axios.post(
        "https://sentiment-professor-feedback-1.onrender.com/api/evaluation-status/",
        {
          start_date: formattedStart,
          end_date: formattedEnd,
          year_semester: newlyset_acadyearsem,
        }
      );

      setEvaluationPeriod();
    } catch (error) {
      console.error("Error setting evaluation period:", error);
    }
  } else {
    console.error("Invalid date range selected:", { start, end });
  }
}
</script>

<template>
  <div class="flex items-center justify-between p-9 pt-10">
    <div :class="cn('grid gap-2', $attrs.class ?? '')">
      <Popover>
        <PopoverTrigger as-child>
          <Button
            id="date"
            :variant="'outline'"
            :class="
              cn(
                'w-[280px] justify-start text-left font-normal',
                !date && 'text-muted-foreground'
              )
            "
          >
            <CalendarIcon class="mr-2 h-4 w-4" />

            <span>
              {{
                date.start
                  ? date.end
                    ? `${format(date.start, "LLL dd, y")} - ${format(
                        date.end,
                        "LLL dd, y"
                      )}`
                    : format(date.start, "LLL dd, y")
                  : "Pick a date"
              }}
            </span>
          </Button>
        </PopoverTrigger>
        <PopoverContent class="w-auto p-0" align="start">
          <Calendar v-model.range="date" :columns="2" />
        </PopoverContent>
      </Popover>
    </div>
    <Button
      class="bg-plpgreen-200 hover:bg-plpgreen-300"
      :disabled="state.isEvaluationPeriodSet"
      @click="onSetEvaluationPeriod"
      >Set Evaluation Period</Button
    >
  </div>
</template>
