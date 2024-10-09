<script setup lang="ts">
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
  DropdownMenuLabel,
} from "@/components/ui/dropdown-menu";
</script>
<template>
  <div
    class="flex items-center justify-between text-base h-14 border-t border-black/25 w-11/12 font-normal text-darks-900 pl-12"
  >
    <div class="w-6/12">
      <DropdownMenu>
        <DropdownMenuTrigger
          ><button class="hover:bg-darks-100/40 w-full h-12 p-1.5 rounded">
            GE101: Algorithms and Complexity
          </button></DropdownMenuTrigger
        >
        <DropdownMenuContent class="w-full">
          <DropdownMenuItem>Profile</DropdownMenuItem>
          <DropdownMenuItem>Billing</DropdownMenuItem>
          <DropdownMenuItem>Team</DropdownMenuItem>
          <DropdownMenuItem>Subscription</DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>

    <div class="w-6/12">
      <DropdownMenu>
        <DropdownMenuTrigger class="flex items-center space-x-2 rounded">
          <p class="h-8 p-1.5 px-4 rounded bg-darks-100/30">BSCS1A</p>
          <p class="h-8 p-1.5 px-4 rounded bg-darks-100/30">
            BSIT1C
          </p></DropdownMenuTrigger
        >
        <DropdownMenuContent class="w-full">
          <DropdownMenuLabel>My Account</DropdownMenuLabel>
          <DropdownMenuItem>Profile</DropdownMenuItem>
          <DropdownMenuItem>Billing</DropdownMenuItem>
          <DropdownMenuItem>Team</DropdownMenuItem>
          <DropdownMenuItem>Subscription</DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  </div>
</template>
