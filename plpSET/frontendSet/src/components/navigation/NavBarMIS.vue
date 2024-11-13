<template>
  <div
    class="flex justify-between items-center w-full bg-white h-16 border-b border-black/25 px-4 z-10 top-0 fixed"
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
          <Avatar class="mt-2 w-8 h-8">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="36"
              height="36"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#595959"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="lucide lucide-circle-user-round"
            >
              <path d="M18 20a6 6 0 0 0-12 0" />
              <circle cx="12" cy="10" r="4" />
              <circle cx="12" cy="12" r="10" />
            </svg>
            <!-- <AvatarImage
            src="https://plpasig.edu.ph/wp-content/uploads/2023/01/cropped-logo120.png"
          />
          <AvatarFallback>PLP</AvatarFallback> -->
          </Avatar>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-48 mr-8 z-10">
          <DropdownMenuLabel>
            <div class="flex flex-col space-y-0 line-clamp-2">
              <span class="font-medium">MIS</span>
              <span class="text-gray-500 italic text-xs">Admin</span>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator class="bg-plpgreen-100 border-0.5" />
          <RouterLink to="/MISDashboardAnalytics">
            <DropdownMenuItem>
              <div class="flex items-center space-x-3 cursor-pointer w-full">
                <ChartNoAxesCombined size="16" />
                <span class="text-sm">Analytics </span>
              </div>
            </DropdownMenuItem>
          </RouterLink>
          <RouterLink to="/DatabaseManagement">
            <DropdownMenuItem>
              <div class="flex items-center space-x-3 cursor-pointer w-full">
                <Box size="16" />
                <span class="text-sm">Databases</span>
              </div>
            </DropdownMenuItem>
          </RouterLink>
          <RouterLink to="/StudentDatabase">
            <DropdownMenuItem>
              <div class="flex items-center space-x-3 cursor-pointer w-full">
                <GraduationCap size="16" />
                <span class="text-sm">Students</span>
              </div>
            </DropdownMenuItem>
          </RouterLink>
          <DropdownMenuItem>
            <generateReports></generateReports>
          </DropdownMenuItem>
          <DropdownMenuSeparator class="bg-plpgreen-100" />
          <DropdownMenuItem>
            <div
              class="flex items-center space-x-2 w-full cursor-pointer"
              @click="logout"
            >
              <LogOut size="16" />
              <span class="text-sm">Logout</span>
            </div>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  </div>
</template>

<script setup lang>
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
import axios from "axios";
import { useAuthStore } from "@/store/adminStore";
import { useRouter } from "vue-router";
import generateReports from "../reportsGeneration/MISExports/generateReports.vue";

const router = useRouter();

const logout = async () => {
  const authAdminLogin = useAuthStore();

  try {
    await authAdminLogin.logout();
    router.push("/");
  } catch (error) {
    console.error("Logout failed:", error);
  }
};
</script>
