<script setup lang="ts">
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { AlignLeft } from "lucide-vue-next";

// Props destructuring (optional)
const { toggleSidebar } = defineProps<{
  toggleSidebar: () => void;
}>();
</script>

<template>
  <div
    class="grid-cols-5 grid-rows-2 gap-4 w-full bg-white h-16 border-b-[1px] border-black/20 flex items-center z-10 fixed top-0"
  >
    <div class="flex items-center col-span-5 space-x-8 pl-4">
      <!-- Sidebar toggle button with hover effect -->
      <Button
        @click="toggleSidebar"
        size="icon"
        class="hover:bg-transparent bg-transparent"
      >
        <AlignLeft
          color="black"
          :size="36"
          class="rounded-full bg-white p-2 stroke-width-3 hover:shadow-lg hover:outline hover:outline-2 hover:outline-gray-500 transition-all duration-100"
        />
      </Button>

      <!-- Avatar and text for Pamantasan -->
      <div class="flex items-center font-Raleway">
        <Avatar class="mr-4">
          <AvatarImage
            src="https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg"
          />
          <AvatarFallback>PLP</AvatarFallback>
        </Avatar>
        <p class="font-regular text-base text-darks-700">
          Pamantasan ng Lungsod ng Pasig
        </p>
      </div>
    </div>
  </div>
</template>
