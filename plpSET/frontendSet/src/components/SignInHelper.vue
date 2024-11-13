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
        <!-- Heading -->
        <h4 class="text-lg font-semibold text-center">Sign Up Guide</h4>
      </div>

      <!-- Main Content -->
      <div class="p-6 space-y-4 max-h-[400px] overflow-y-auto w-full">
        <!-- First Collapsible: Step-by-Step Instructions -->
        <Collapsible v-model:open="isOpenStepByStep" class="space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4">
            <h4 class="text-sm font-semibold">Step-by-Step Instructions</h4>
            <CollapsibleTrigger as-child>
              <Button variant="ghost" size="sm" class="w-9 p-0">
                <ChevronsUpDown class="h-4 w-4" />
                <span class="sr-only">Toggle</span>
              </Button>
            </CollapsibleTrigger>
          </div>
          <CollapsibleContent class="space-y-2 text-sm text-gray-700">
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              Use a valid email address for important updates
            </div>
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              Choose a strong password with at least 8 characters, including
              uppercase, numbers, and special characters
            </div>
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              Confirm your password to ensure they match.
            </div>
          </CollapsibleContent>
        </Collapsible>

        <!-- Second Collapsible: Error Prevention -->
        <Collapsible v-model:open="isOpenErrorPrevention" class="space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4">
            <h4 class="text-sm font-semibold">Error Prevention</h4>
            <CollapsibleTrigger as-child>
              <Button variant="ghost" size="sm" class="w-9 p-0">
                <ChevronsUpDown class="h-4 w-4" />
                <span class="sr-only">Toggle</span>
              </Button>
            </CollapsibleTrigger>
          </div>
          <CollapsibleContent class="space-y-2 text-sm text-gray-700">
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              Double-check your email for typos
            </div>
          </CollapsibleContent>
        </Collapsible>

        <!-- Third Collapsible: Field Clarifications -->
        <Collapsible v-model:open="isOpenFieldClarifications" class="space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4">
            <h4 class="text-sm font-semibold">Form Field Clarifications</h4>
            <CollapsibleTrigger as-child>
              <Button variant="ghost" size="sm" class="w-9 p-0">
                <ChevronsUpDown class="h-4 w-4" />
                <span class="sr-only">Toggle</span>
              </Button>
            </CollapsibleTrigger>
          </div>
          <CollapsibleContent class="space-y-2 text-sm text-gray-700">
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              Date of Birth: Use the format MM/DD/YYYY
            </div>
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              Student Number: Refer to your student ID card for accuracy
            </div>
          </CollapsibleContent>
        </Collapsible>

        <!-- Fourth Collapsible: Privacy and Security Reminder -->
        <Collapsible v-model:open="isOpenPrivacy" class="space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4">
            <h4 class="text-sm font-semibold">Privacy and Security Reminder</h4>
            <CollapsibleTrigger as-child>
              <Button variant="ghost" size="sm" class="w-9 p-0">
                <ChevronsUpDown class="h-4 w-4" />
                <span class="sr-only">Toggle</span>
              </Button>
            </CollapsibleTrigger>
          </div>
          <CollapsibleContent class="space-y-2 text-sm text-gray-700">
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              Your personal information will be stored securely and used only
              for registration and communication
            </div>
          </CollapsibleContent>
        </Collapsible>
        <!-- Sixth Collapsible: Call-to-Action -->
        <Collapsible v-model:open="isOpenCTA" class="space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4">
            <h4 class="text-sm font-semibold">Call-to-Action</h4>
            <CollapsibleTrigger as-child>
              <Button variant="ghost" size="sm" class="w-9 p-0">
                <ChevronsUpDown class="h-4 w-4" />
                <span class="sr-only">Toggle</span>
              </Button>
            </CollapsibleTrigger>
          </div>
          <CollapsibleContent class="space-y-2 text-sm text-gray-700">
            <div class="rounded-md border px-4 py-3 font-mono text-sm">
              After completing the form, click "Register" to sign up
            </div>
          </CollapsibleContent>
        </Collapsible>
      </div>

      <!-- Fixed Footer Section -->
      <div class="bg-gray-100 p-4 text-sm text-center text-muted-foreground">
        Your data will be stored securely and used for registration purposes
        only.
      </div>
    </HoverCardContent>
  </HoverCard>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Button } from "@/components/ui/button";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card";
import { CircleHelp, ChevronsUpDown } from "lucide-vue-next";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";

const isOpenStepByStep = ref(false);
const isOpenErrorPrevention = ref(false);
const isOpenFieldClarifications = ref(false);
const isOpenPrivacy = ref(false);
const isOpenSupport = ref(false);
const isOpenCTA = ref(false);
</script>
