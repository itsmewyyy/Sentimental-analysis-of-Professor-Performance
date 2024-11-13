<template>
  <div
    class="flex justify-between items-center w-full bg-white h-16 border-b border-black/25 px-4 z-10 top-0 fixed"
  >
    <!-- Left Section: Logo and Text -->
    <RouterLink to="/DeanDashboard">
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

    <!-- Right Section: Calendar Icon with HoverCard and Avatar Dropdown -->
    <div class="flex items-center space-x-1">
      <!-- Calendar Icon with HoverCard -->
      <HoverCard>
        <HoverCardTrigger as-child>
          <Button variant="link">
            <Clock color="#2e5244" stroke-width="2" size="18" />
          </Button>
        </HoverCardTrigger>
        <HoverCardContent class="w-80 mr-20">
          <div class="flex justify-between space-x-4">
            <div class="space-y-1" v-if="evaluationPeriod">
              <div class="flex items-center">
                <CalendarDays class="mr-2 h-4 w-4 opacity-70" />
                <h4 class="text-sm font-semibold">Evaluation Period</h4>
              </div>
              <div class="flex items-center pt-2">
                <span class="text-xs font-medium">
                  {{ evaluationPeriod.start_date }} -
                  {{ evaluationPeriod.end_date }}
                </span>
              </div>
            </div>
          </div>
        </HoverCardContent>
      </HoverCard>

      <DropdownMenu>
        <DropdownMenuTrigger>
          <Avatar class="w-8 h-8 mt-2">
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
        <DropdownMenuContent class="w-50 mr-7">
          <DropdownMenuLabel>
            <div class="flex flex-col space-y-0 line-clamp-2">
              <span class="font-medium">{{ Admin }}</span>
              <span class="text-gray-500 italic text-xs">{{ College }}</span>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator class="bg-plpgreen-100 border-0.5" />
          <RouterLink to="/DeanProfile">
            <DropdownMenuItem>
              <div class="flex items-center space-x-2 cursor-pointer w-full">
                <User size="14" />
                <span class="text-sm">Profile</span>
              </div>
            </DropdownMenuItem>
          </RouterLink>
          <DropdownMenuItem>
            <generateReports></generateReports>
          </DropdownMenuItem>
          <DropdownMenuSeparator class="bg-plpgreen-100" />
          <DropdownMenuItem>
            <div
              class="flex items-center space-x-2 cursor-pointer w-full"
              @click="logout"
            >
              <LogOut size="14" />
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
import { CalendarDays, Clock, LogOut, User, Download } from "lucide-vue-next";
import generateReports from "../reportsGeneration/deanExports/generateReports.vue";
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import axios from "axios";
import { useAuthStore } from "@/store/adminStore";
import { useRouter } from "vue-router";

const Admin = localStorage.getItem("admin_id");
const College = localStorage.getItem("college");

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

const evaluationPeriod = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/latest-evaluation/"
    );
    evaluationPeriod.value = response.data;
  } catch (error) {
    console.error("Error fetching evaluation period:", error);
  }
});
</script>
