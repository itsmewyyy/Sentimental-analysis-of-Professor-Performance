<template>
  <div
    class="flex justify-between items-center w-full bg-white h-16 border-b border-black/25 px-4 z-10 top-0 fixed"
    v-if="profProfile"
  >
    <!-- Left Section: Logo and Text -->
    <RouterLink to="/ProfessorDashboard">
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

    <div class="flex items-center space-x-1">
      <DropdownMenu>
        <DropdownMenuTrigger>
          <Avatar class="w-8 h-8 mt-2">
            <AvatarImage
              src="https://plus.unsplash.com/premium_photo-1661942126259-fb08e7cce1e2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            />
            <AvatarFallback>PLP</AvatarFallback>
          </Avatar>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-50 mr-7">
          <DropdownMenuLabel>
            <div class="flex flex-col space-y-0 line-clamp-2">
              <span class="font-medium"
                >{{ profProfile.first_name }} {{ profProfile.surname }}
              </span>
              <span class="text-gray-500 italic text-xs">{{ College }}</span>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator class="bg-plpgreen-100 border-0.5" />
          <RouterLink to="/ProfProfile">
            <DropdownMenuItem>
              <div class="flex items-center space-x-2 cursor-pointer w-full">
                <User size="14" />
                <span class="text-sm">Profile</span>
              </div>
            </DropdownMenuItem>
          </RouterLink>
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

const Professor = localStorage.getItem("professor");
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

const profProfile = ref(null);

onMounted(async () => {
  const profID = localStorage.getItem("professor");
  if (profID) {
    try {
      const response = await axios.get(
        "https://sentiment-professor-feedback-1.onrender.com/api/professor-list/",
        { withCredentials: true }
      );

      const professor = response.data.find(
        (prof) => prof.professor_id === profID
      );
      if (professor) {
        profProfile.value = professor;
      } else {
        errorMessage.value = "Professor not found. Please contact support.";
      }
    } catch (error) {
      console.error("Error fetching professor profile:", error);
    }
  } else {
    console.error("Professor ID not found in localStorage.");
  }
});
</script>
