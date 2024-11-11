<!-- Admin Login -->
<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import { cn } from "@/lib/utils";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store/adminStore";
import axios from "axios";
import type { AxiosError } from "axios";
import { Toaster } from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast/use-toast";

const authStore = useAuthStore();
const router = useRouter();
authStore.restoreSession();
const adminUsername = ref("");
const password = ref("");
const isAuthenticated = computed(() => authStore.isAuthenticated);
const { toast } = useToast();

onMounted(() => {
  if (isAuthenticated.value) {
    const userType = localStorage.getItem("user_type");

    if (userType === "MIS") {
      router.push("/MISDashboard");
    } else if (userType === "Dean") {
      router.push("/DeanDashboard");
    } else if (userType === "Secretary") {
      router.push("/SecretaryDashboard");
    } else {
      router.push("/MISDashboard");
    }
  }
});

const login = async () => {
  const authAdminLogin = useAuthStore();

  try {
    await authAdminLogin.login(adminUsername.value, password.value);

    const yearSemResponse = await axios.get(
      "https://sentiment-professor-feedback-1.onrender.com/api/current-year-sem/",
      { withCredentials: true }
    );

    if (yearSemResponse.status === 200) {
      const currentYearSem = yearSemResponse.data;

      localStorage.setItem("current_year_sem", currentYearSem.year_sem_id);
    }

    // Get user_type from the authenticated user or localStorage
    const userType =
      authAdminLogin.user?.user_type || localStorage.getItem("user_type");

    // Redirect based on user_type
    if (userType === "MIS") {
      router.push("/MISDashboard");
    } else if (userType === "Dean") {
      router.push("/DeanDashboard");
    } else if (userType === "Secretary") {
      router.push("/SecretaryDashboard");
    } else {
      router.push("/MISDashboard");
    }
  } catch (error) {
    toast({
      variant: "destructive",
      title: "Failed to Login", // Access the 'error' key directly
      description: error.error,
    });
  }
};
</script>

<template>
  <Toaster></Toaster>
  <div
    class="min-h-screen flex items-center justify-center"
    v-if="!isAuthenticated"
  >
    <section class="bg-plpyellow-100/15 rounded-lg px-5 font-raleway">
      <div
        class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16"
      >
        <div class="flex flex-col justify-center">
          <h1
            class="mb-4 text-md font-black tracking-tight leading-none text-plpgreen-200 md:text-5xl lg:text-4xl"
          >
            Help Us Improve Education at Pamantasan ng Lungsod ng Pasig!
          </h1>
          <p class="mb-6 text-lg font-normal text-black/50 lg:text-xl">
            Your feedback is invaluable! Participate in the Student Evaluation
            of Teachers (SET) and help us enhance the quality of education at
            Pamantasan ng Lungsod ng Pasig. Share your thoughts and experiences
            to contribute to the continuous improvement of our academic
            environment.
          </p>
        </div>
        <div>
          <div
            class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg border border-black/15"
          >
            <h2 class="text-2xl font-bold text-plpyellow-200">Admin Login</h2>
            <form @submit.prevent="login" class="mt-8 space-y-8">
              <div class="space-y-6">
                <div>
                  <label
                    for="username"
                    class="block mb-2 text-sm font-medium xt-gray-900"
                    >Username</label
                  >
                  <input
                    v-model="adminUsername"
                    type="text"
                    name="username"
                    id="username"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-plpgreen-200 focus:border-plpgreen-200 block w-full p-2.5"
                    placeholder="Enter Username"
                    required
                  />
                </div>
                <div>
                  <label
                    for="password"
                    class="block mb-2 text-sm font-medium text-gray-900"
                    >Your password</label
                  >
                  <input
                    v-model="password"
                    type="password"
                    name="password"
                    id="password"
                    placeholder="••••••••"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-plpgreen-200 focus:border-plpgreen-200 block w-full p-2.5"
                    required
                  />
                </div>
              </div>
              <button
                type="submit"
                class="w-fit px-5 py-3 text-sm font-medium text-center text-white bg-plpgreen-200 rounded-lg hover:bg-plpgreen-400 focus:ring-2 focus:ring-plpgreen-100"
              >
                Login to your account
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
