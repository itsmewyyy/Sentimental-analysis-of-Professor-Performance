<template>
  <HoverCard>
    <HoverCardTrigger as-child>
      <Button variant="link" class="relative">
        <CircleHelp
          stroke-width="1.5"
          class="text-[#000000] hover:text-plpgreen-400 transition-colors duration-200"
        />
      </Button>
    </HoverCardTrigger>

    <!-- Hover Card Content with Fixed Footer -->
    <HoverCardContent class="w-[400px] p-0 mr-12">
      <!-- Dark Background Section -->
      <div class="bg-plpgreen-300 text-white p-6 rounded-t-md">
        <h4 class="text-lg font-semibold text-center">How to Evaluate</h4>
      </div>

      <!-- Main Content with max height and scrolling -->
      <div class="p-6 space-y-4 max-h-[400px] overflow-y-auto w-full">
        <!-- First Collapsible -->
        <Collapsible v-model:open="isOpenFirst" class="space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4">
            <h4 class="text-sm font-semibold">
              What does the Acronym stand for?
            </h4>
            <CollapsibleTrigger as-child>
              <Button variant="ghost" size="sm" class="w-9 p-0">
                <ChevronsUpDown class="h-4 w-4" />
                <span class="sr-only">Toggle</span>
              </Button>
            </CollapsibleTrigger>
          </div>
          <div class="rounded-md border px-4 py-3 font-mono text-sm">
            SA - Strongly Agree
          </div>
          <CollapsibleContent class="space-y-2">
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              A - Agree
            </div>
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              N - Neutral
            </div>
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              D - Disagree
            </div>
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              SD - Strongly Disagree
            </div>
          </CollapsibleContent>
        </Collapsible>

        <!-- Second Collapsible -->
        <Collapsible v-model:open="isOpenSecond" class="space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4">
            <h4 class="text-sm font-semibold">
              Is it okay to put N/A in open-ended questions?
            </h4>
            <CollapsibleTrigger as-child>
              <Button variant="ghost" size="sm" class="w-9 p-0">
                <ChevronsUpDown class="h-4 w-4" />
                <span class="sr-only">Toggle</span>
              </Button>
            </CollapsibleTrigger>
          </div>
          <div class="rounded-md border px-4 py-3 font-mono text-sm">
            It’s allowed, but not encouraged.
          </div>
          <CollapsibleContent class="space-y-2">
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              The Student Evaluation for Teachers (SET) is designed to gather
              detailed feedback and provide meaningful responses that help
              improve the quality of education in PLP.
            </div>
          </CollapsibleContent>
        </Collapsible>
      </div>

      <!-- Fixed Footer Section -->
      <div
        class="bg-gray-100 p-4 text-sm text-center text-muted-foreground flex items-center justify-center space-x-2"
      >
        <CircleAlert class="h-5 w-5 text-muted-foreground" />
        <span>Remember to answer truthfully at all times</span>
      </div>
    </HoverCardContent>
  </HoverCard>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card";
import { CircleHelp, CircleAlert, ChevronsUpDown } from "lucide-vue-next";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { ref } from "vue";

// Separate states for each collapsible
const isOpenFirst = ref(false);
const isOpenSecond = ref(false);
</script>
