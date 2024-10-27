<script setup lang="ts">
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
</script>

<template>
  <div
    class="w-full bg-white h-16 border-b-[1px] border-black/15 flex items-center z-10 fixed top-0"
  >
    <div class="flex items-center space-x-8 pl-4">
      <div class="flex items-center font-Roboto space-x-2">
        <Avatar class="w-9 h-9">
          <AvatarImage
            src="https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg"
          />
          <AvatarFallback>PLP</AvatarFallback>
        </Avatar>
        <p class="font-medium text-sm text-darks-200/60">
          Pamantasan ng Lungsod ng Pasig
        </p>
      </div>
    </div>
  </div>
</template>
