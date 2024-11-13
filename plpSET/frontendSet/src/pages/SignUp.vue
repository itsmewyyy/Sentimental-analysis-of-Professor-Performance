<template>
  <Toaster></Toaster>
  <div class="w-full min-h-screen lg:grid lg:grid-cols-2 relative">
    <div class="flex flex-col justify-center h-full py-12 bg-white">
      <div class="flex items-center justify-center flex-grow">
        <div class="mx-auto grid w-[350px] gap-6">
          <div class="text-center space-y-2">
            <h1 class="text-3xl font-bold">Sign Up</h1>
            <p class="text-muted-foreground">
              Enter your details to
              <span class="text-plpgreen-400 font-bold">evaluate</span> now
            </p>
          </div>

          <form @submit.prevent="register" class="w-full mx-auto">
            <div class="grid gap-4">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <Label for="student-id" class="text-xs">Student Number</Label>
                  <Input
                    type="text"
                    name="student_id"
                    id="student_id"
                    v-model="student_id"
                    default-value="21-00444"
                    class="w-full"
                    placeholder=" "
                    required
                  />
                </div>
                <div>
                  <Label for="birthday" class="text-xs">Birthday</Label>
                  <Popover>
                    <PopoverTrigger as-child>
                      <Button
                        :variant="'outline'"
                        :class="
                          cn(
                            'w-full justify-start text-left font-normal',
                            !dateofbirth && 'text-muted-foreground'
                          )
                        "
                      >
                        <span>{{
                          dateofbirth ? format(dateofbirth, "PPP") : ""
                        }}</span>
                      </Button>
                    </PopoverTrigger>
                    <PopoverContent class="w-auto p-0">
                      <Calendar v-model="dateofbirth" />
                    </PopoverContent>
                  </Popover>
                </div>
              </div>

              <!-- Email, Password & Confirm Password -->
              <div class="grid gap-4">
                <div>
                  <Label for="student_email" class="text-xs">Email</Label>
                  <Input
                    type="text"
                    name="student_email"
                    id="student_email"
                    v-model="student_email"
                    class="w-full"
                    placeholder=""
                    required
                  />
                </div>
                <div>
                  <Label for="password" class="text-xs">Password</Label>
                  <Input
                    v-model="password"
                    type="password"
                    name="password"
                    id="password"
                    class="w-full"
                    placeholder=""
                    required
                  />
                </div>
                <div>
                  <Label for="password_confirmation" class="text-xs"
                    >Confirm Password</Label
                  >
                  <Input
                    v-model="confirm_password"
                    type="password"
                    name="password_confirmation"
                    id="confirm-password"
                    class="w-full"
                    placeholder=""
                    required
                  />
                </div>
              </div>

              <Button
                type="submit"
                class="bg-plpgreen-200 hover:bg-plpgreen-400 mt-4"
                >Register</Button
              >
              <router-link to="/StudentLogin">
                <p class="text-xs text-gray-500">
                  Already have an account?
                  <a
                    href="#"
                    class="text-yellow-500 hover:underline hover:text-plpyellow-200"
                    >Login</a
                  >
                </p>
              </router-link>
            </div>
          </form>
        </div>
      </div>
    </div>

    <div class="bg-yellow-50 flex items-center justify-center h-full p-12">
      <div class="text-left space-y-8">
        <span
          class="text-plpgreen-400 text-7xl tracking-wide font-extrabold block"
        >
          Join the Pamantasan ng Lungsod ng Pasig Community!
        </span>
        <p class="text-gray-500 text-lg tracking-wide leading-normal">
          Join us in our mission to foster academic excellence. Sign up now and
          be part of a dynamic community where your insights shape the
          educational journey. Together, let’s elevate the learning experience
          and make your voice heard in evaluating courses and faculty!
        </p>
      </div>
    </div>

    <div class="absolute bottom-4 right-4">
      <SignInHelper />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { format } from "date-fns";
import SignInHelper from "@/components/SignInHelper.vue";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Popover,
  PopoverTrigger,
  PopoverContent,
} from "@/components/ui/popover";
import { Calendar } from "@/components/ui/v-calendar";
import { Calendar as CalendarIcon } from "lucide-vue-next";
import { cn } from "@/lib/utils";
import { useAuthStore } from "@/store/student";
import { useRouter } from "vue-router";
import { Toaster } from "@/components/ui/toast";
import { useToast } from "@/components/ui/toast/use-toast";

const { toast } = useToast();

const router = useRouter();
const dateofbirth = ref<Date>();

// Define reactive variables
const student_id = ref("");
const password = ref("");
const confirm_password = ref("");
const student_email = ref("");

// Register function
const register = async () => {
  const formattedDateOfBirth = dateofbirth.value
    ? format(dateofbirth.value, "yyyy-MM-dd")
    : "";

  const authStudentRegister = useAuthStore();

  try {
    await authStudentRegister.register(
      student_id.value,
      password.value,
      confirm_password.value,
      formattedDateOfBirth,
      student_email.value
    );

    router.push("/StudentLogin");
  } catch (error) {
    toast({
      variant: "destructive",
      title: "Failed to Register",
      description: error.error,
    });
  }
};
</script>
