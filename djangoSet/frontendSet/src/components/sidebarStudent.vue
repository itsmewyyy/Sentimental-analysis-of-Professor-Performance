<script setup lang="ts">
import { defineProps } from "vue";
import { GraduationCap, LogOut } from "lucide-vue-next";
import { Card } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";

// Define props for the sidebar component with explicit types
const props = defineProps<{
  isSidebarOpen: boolean;
}>();
</script>

<template>
  <div
    :class="[
      'fixed left-0 top-16 h-full bg-darks-50/50 border-r border-black/15 text-white transition-all duration-300 z-0 overflow-y-auto font-raleway',
      isSidebarOpen ? 'w-72' : 'w-20',
    ]"
  >
    <div class="p-4 flex flex-col h-full justify-between">
      <!-- Top section (Avatar and Info) -->
      <div class="flex items-center space-x-2 mt-8 h-16">
        <Avatar class="w-12 h-12">
          <AvatarImage
            src="https://i.pinimg.com/564x/92/73/47/927347b099b1f06d5b1b49ba31b27de9.jpg"
          />
          <AvatarFallback>OM</AvatarFallback>
        </Avatar>
        <div class="flex-grow text-left tracking-wide leading-relaxed">
          <Card class="bg-transparent shadow-none border-none mt-2">
            <div v-show="isSidebarOpen" class="flex flex-col space-y-1">
              <span class="text-sm font-medium overflow-hidden w-40"
                >21-00444</span
              >
              <span class="text-sm font-semibold overflow-hidden"
                >Catalan, Gian Carlo E.</span
              >
            </div>
          </Card>
        </div>
      </div>

      <!-- Middle section (Home Button, Evaluation Info) -->
      <div class="flex-grow my-32 flex flex-col items-center space-y-16">
        <!-- Home Button -->
        <Button
          class="group w-full max-w-xs border-2 border-darks-100 rounded-full px-4 py-3 bg-transparent hover:bg-transparent text-black transition duration-500 flex items-center justify-center h-12 hover:border-plpgreen-200"
          size="lg"
        >
          <GraduationCap
            class="text-black group-hover:text-plpgreen-200 w-6 h-6"
          />
          <span
            v-show="isSidebarOpen"
            class="ml-2 text-black text-sm transition-transform duration-500 ease-in-out group-hover:text-plpgreen-200"
          >
            Home
          </span>
        </Button>

        <!-- Evaluation Info -->
        <Card
          class="bg-transparent shadow-none border-none w-72 text-center h-full"
        >
          <div v-show="isSidebarOpen">
            <h4
              class="text-xs text-darks-100 font-light mb-2 overflow-hidden text-left-w-40"
            >
              Currently Evaluating
            </h4>
            <span
              class="text-sm font-medium text-muted-foreground overflow-hidden w-38"
            >
              CS104 Algorithms and Complexity
            </span>
            <Separator class="my-2 w-11/12 mx-auto bg-darks-700" />
            <span
              class="text-sm font-medium text-muted-foreground overflow-hidden"
            >
              Ronnie Chu
            </span>
          </div>
        </Card>
      </div>

      <!-- Bottom section (Logout Button) -->
      <div class="flex justify-center mb-16">
        <Button
          class="group w-full max-w-xs rounded-full px-4 py-3 bg-transparent hover:bg-transparent text-black transition duration-500 flex items-center justify-center h-12"
          size="lg"
        >
          <LogOut class="text-black group-hover:text-plpgreen-200 w-6 h-6" />
          <span
            v-show="isSidebarOpen"
            class="ml-2 text-sm group-hover:text-plpgreen-200"
          >
            Logout
          </span>
        </Button>
      </div>
    </div>
  </div>
</template>
