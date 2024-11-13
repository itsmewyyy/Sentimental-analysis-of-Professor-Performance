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
        <h4 class="text-lg font-semibold text-center">How to Register</h4>
      </div>

      <!-- Main Content -->
      <div class="p-6 space-y-4">
        <ul class="list-decimal pl-2 space-y-4 text-sm">
          <li>Enter your <strong>Student Number</strong> as shown on your school ID.</li>
          <li>Use your <strong>PLP email address</strong> to receive confirmation emails.</li>
          <li>Choose a <strong>strong password</strong> with at least 8 characters.</li>
          <li>Confirm your password by entering it again.</li>
        </ul>
      </div>

      <!-- Fixed Footer Section -->
      <div class="bg-gray-100 p-4 text-sm text-center text-muted-foreground">
        Your data will be stored securely and used for registration purposes only.
      </div>
    </HoverCardContent>
  </HoverCard>
</template>

<script setup lang="ts">
import { Button } from '@/components/ui/button'
import { HoverCard, HoverCardContent, HoverCardTrigger } from '@/components/ui/hover-card'
import { CircleHelp } from 'lucide-vue-next'
</script>
