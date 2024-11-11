<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useAuthStore } from "@/store/student";
import { format } from "date-fns";
import { Calendar as CalendarIcon } from "lucide-vue-next";
import { Calendar } from "@/components/ui/v-calendar";
import { Button } from "@/components/ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { cn } from "@/lib/utils";
import { useRouter } from "vue-router";
import { Toaster } from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast/use-toast";

const { toast } = useToast();
const router = useRouter();
const authStore = useAuthStore();
authStore.restoreSession();

const student_acc_number = ref("");
const password = ref("");
const dateofbirth = ref<Date>();

// Check if the user is authenticated
const isAuthenticated = computed(() => authStore.isAuthenticated);

// Redirect to the dashboard if already logged in
onMounted(() => {
  if (isAuthenticated.value) {
    router.push("/StudentDashboard");
  }
});

const login = async () => {
  const formattedDateOfBirth = dateofbirth.value
    ? format(dateofbirth.value, "yyyy-MM-dd")
    : "";

  try {
    await authStore.login(
      student_acc_number.value,
      password.value,
      formattedDateOfBirth
    );
    router.push("/StudentDashboard");
  } catch (error) {
    toast({
      variant: "destructive",
      title: "Failed to Login",
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
    <section class="bg-plpyellow-100/15 rounded-xl px-5">
      <div
        class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16"
      >
        <div class="flex flex-col justify-center">
          <h1
            class="mb-4 text-md font-black tracking-tight leading-none text-plpgreen-200 md:text-5xl lg:text-4xl"
          >
            Help Us Improve Education at Pamantasan ng Lungsod ng Pasig!
          </h1>
          <p class="mb-6 text-lg font-normal text-darks-900/50 lg:text-xl">
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
            <h2 class="text-2xl font-bold text-plpyellow-200">Student Login</h2>
            <form @submit.prevent="login" class="mt-8 space-y-6">
              <div class="space-y-2">
                <div class="space-y-6">
                  <div class="text-darks-200">
                    <Popover>
                      <PopoverTrigger as-child>
                        <Button
                          :variant="'outline'"
                          class="bg-gray-50"
                          :class="
                            cn(
                              'w-full justify-start text-left font-normal',
                              !dateofbirth && 'text-muted-foreground'
                            )
                          "
                        >
                          <CalendarIcon class="mr-2 h-4 w-4" />
                          <span>{{
                            dateofbirth
                              ? format(dateofbirth, "PPP")
                              : "Date of Birth"
                          }}</span>
                        </Button>
                      </PopoverTrigger>
                      <PopoverContent class="w-auto p-0">
                        <Calendar v-model="dateofbirth" />
                      </PopoverContent>
                    </Popover>
                  </div>

                  <div>
                    <label
                      for="stud_accnumber"
                      class="block mb-2 text-sm font-medium text-gray-900"
                      >Student Number</label
                    >
                    <input
                      v-model="student_acc_number"
                      type="text"
                      name="stud_accnumber"
                      id="stud_accnumber"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-plpgreen-200 focus:border-plpgreen-200 block w-full p-2.5"
                      placeholder="Enter Student Number"
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
                <div
                  class="flex justify-between items-center text-sm font-medium text-gray-900"
                >
                  <div></div>
                  <a
                    href="#"
                    class="text-blue-600 hover:underline dark:text-blue-500 text-xs"
                    >Forgot Password?</a
                  >
                </div>
              </div>
              <div class="space-y-2">
                <button
                  type="submit"
                  class="w-full px-5 py-3 text-sm font-medium text-center text-white bg-plpgreen-200 rounded-lg hover:bg-plpgreen-400 sm:w-auto focus:ring-2 focus:ring-plpgreen-100"
                >
                  Login to your account
                </button>

                <div class="text-xs font-medium text-gray-900">
                  Create your student account
                  <router-link
                    to="/StudentRegister"
                    class="text-blue-600 hover:underline dark:text-blue-500"
                  >
                    here
                  </router-link>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
