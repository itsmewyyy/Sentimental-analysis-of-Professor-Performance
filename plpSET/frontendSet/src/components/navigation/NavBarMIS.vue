<template>
  <div
    class="flex justify-between items-center w-full bg-white h-16 border-b border-black/25 px-4 z-10 top-0 sticky"
  >
    <!-- Left Section: Logo and Text -->
    <RouterLink to="/MISDashboard">
      <div class="flex items-center space-x-2 cursor-pointer">
        <Avatar class="w-9 h-9">
          <AvatarImage
            src="https://plpasig.edu.ph/wp-content/uploads/2023/01/cropped-logo120.png"
          />
          <AvatarFallback>PLP</AvatarFallback>
        </Avatar>
        <p
          class="font-medium text-darks-200/80 transition-colors hover:text-darks-900 cursor-pointer text-sm"
        >
          Pamantasan ng Lungsod ng Pasig
        </p>
      </div>
    </RouterLink>

    <div class="flex items-center space-x-4">
      <DropdownMenu>
        <DropdownMenuTrigger>
          <Avatar class="mt-2 w-9 h-9">
            <AvatarImage
              src="https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg"
            />
            <AvatarFallback>PLP</AvatarFallback>
          </Avatar>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-48 mr-7 z-10">
          <DropdownMenuLabel>
            <div class="flex flex-col space-y-0 line-clamp-2">
              <span class="font-medium">Catalan, Gian Carlo E.</span>
              <span class="text-gray-500 italic text-xs">21-00444</span>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator class="bg-plpgreen-100 border-0.5" />
          <DropdownMenuItem>
            <div class="flex items-center space-x-3">
              <User size="16" />
              <span class="text-sm">Profile</span>
            </div>
          </DropdownMenuItem>

          <DropdownMenuItem>
            <RouterLink to="/MISDashboardAnalytics">
              <div class="flex items-center space-x-3">
                <ChartNoAxesCombined size="16" />
                <span class="text-sm">Analytics </span>
              </div>
            </RouterLink>
          </DropdownMenuItem>
          <DropdownMenuItem>
            <RouterLink to="/DatabaseManagement">
              <div class="flex items-center space-x-3">
                <Box size="16" />
                <span class="text-sm">Databases</span>
              </div>
            </RouterLink>
          </DropdownMenuItem>
          <DropdownMenuItem>
            <RouterLink to="/StudentDatabase">
              <div class="flex items-center space-x-3">
                <GraduationCap size="16" />
                <span class="text-sm">Students</span>
              </div>
            </RouterLink>
          </DropdownMenuItem>
          <DropdownMenuItem>
            <div class="flex items-center space-x-3">
              <Download size="16" />
              <span class="text-sm">Download Results</span>
            </div>
          </DropdownMenuItem>
          <DropdownMenuSeparator class="bg-plpgreen-100" />
          <DropdownMenuItem>
            <div class="flex items-center space-x-2">
              <LogOut size="16" />
              <span class="text-sm">Logout</span>
            </div>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  </div>
</template>

<script setup>
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  CalendarDays,
  Clock,
  LogOut,
  Download,
  User,
  ChartNoAxesCombined,
  Box,
  GraduationCap,
} from "lucide-vue-next";
import { RouterLink } from "vue-router";
</script>

<style scoped>
/* Add custom styles if needed */
</style>
