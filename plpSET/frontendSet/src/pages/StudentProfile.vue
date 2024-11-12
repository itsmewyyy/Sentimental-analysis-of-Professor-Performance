<template>
  <NavBarStudent></NavBarStudent>
  <ScrollArea class="h-svh w-full">
    <div class="max-w-3xl mx-auto p-4 space-y-6 pt-28" v-if="studentProfile">
      <h1 class="text-xl font-semibold mt-4 text-gray-900">My Profile</h1>

      <!-- Profile Header -->
      <Card>
        <CardContent class="p-6">
          <div class="flex justify-between items-start">
            <div class="flex gap-4 items-center">
              <Avatar class="h-16 w-16">
                <AvatarImage
                  src="https://scontent.fcrk3-2.fna.fbcdn.net/v/t39.30808-1/464624148_1812122635988644_8047543269600036803_n.jpg?stp=dst-jpg_s160x160&_nc_cat=103&ccb=1-7&_nc_sid=6738e8&_nc_ohc=0C3RvHUHEjcQ7kNvgF_do2n&_nc_zt=24&_nc_ht=scontent.fcrk3-2.fna&_nc_gid=AH7tbo_NHnbk6TXxaOG0bRA&oh=00_AYAN1CwDuYbpljVoCcywiXOgEh6Jb89ShPvrhRMoOFwmPA&oe=67281993"
                  alt=""
                />
                <AvatarFallback>JA</AvatarFallback>
              </Avatar>
              <div>
                <h2 class="text-lg font-semibold">
                  {{ studentProfile.info.first_name }}
                  {{ studentProfile.info.middle_name }}
                  {{ studentProfile.info.surname }}
                  {{ studentProfile.info.extension_name }}
                </h2>
                <p class="text-gray-500 italic text-xs">
                  {{ studentProfile.account.student_acc_number }}
                </p>
              </div>
            </div>
            <Button variant="ghost" size="sm" class="text-blue-600">
              <Pencil class="h-4 w-4 mr-1" />
              Edit
            </Button>
          </div>
        </CardContent>
      </Card>

      <!-- Personal Information -->
      <Card>
        <CardHeader>
          <CardTitle>Personal Information</CardTitle>
        </CardHeader>
        <CardContent class="grid sm:grid-cols-4 gap-2">
          <div>
            <p class="text-sm text-gray-500">Surname</p>
            <p class="text-gray-900">{{ studentProfile.info.surname }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-500">First Name</p>
            <p class="text-gray-900">{{ studentProfile.info.first_name }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Middle Name</p>
            <p class="text-gray-900">{{ studentProfile.info.middle_name }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Extension Name</p>
            <p class="text-gray-900">
              {{ studentProfile.info.extension_name }}
            </p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Birthday</p>
            <p class="text-gray-900">
              {{ studentProfile.account.date_of_birth }}
            </p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Status</p>
            <p class="text-gray-900">{{ studentProfile.info.status }}</p>
          </div>
        </CardContent>
      </Card>

      <!-- Academic Details -->
      <Card>
        <CardHeader>
          <CardTitle>Academic Details</CardTitle>
        </CardHeader>
        <CardContent class="grid sm:grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-gray-500">Student ID</p>
            <p class="text-gray-900">
              {{ studentProfile.account.student_acc_number }}
            </p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Section</p>
            <p class="text-gray-900">{{ studentProfile.info.section }}</p>
          </div>
        </CardContent>
      </Card>

      <!-- Account Information -->
      <Card>
        <CardHeader class="flex flex-row items-center justify-between">
          <CardTitle>Account Information</CardTitle>
          <Dialog>
            <DialogTrigger as-child>
              <Button variant="ghost" size="sm" class="text-blue-600">
                <Pencil class="h-4 w-4 mr-1" />
                Edit
              </Button>
            </DialogTrigger>
            <DialogContent class="sm:max-w-md">
              <DialogHeader>
                <DialogTitle>Change Password</DialogTitle>
                <DialogDescription
                  >Make sure to remember your new password</DialogDescription
                >
              </DialogHeader>
              <div class="flex items-center space-x-2">
                <div class="grid gap-2">
                  <Label html-for="password" class="text-xs">Password</Label>
                  <Input id="password" type="password" v-model="password" />
                </div>
                <div class="grid gap-2">
                  <Label html-for="cpassword" class="text-xs"
                    >Confirm Password</Label
                  >
                  <Input
                    id="cpassword"
                    type="password"
                    v-model="confirmPassword"
                  />
                </div>
              </div>
              <DialogFooter class="sm:justify-start">
                <DialogClose as-child>
                  <Button
                    type="submit"
                    @click="changePassword"
                    class="bg-transparent hover:bg-transparent bg-plpgreen-300 hover:bg-plpgreen-400"
                    >New Password</Button
                  >
                </DialogClose>
              </DialogFooter>
            </DialogContent>
          </Dialog>
        </CardHeader>
        <CardContent class="grid gap-4">
          <div class="grid sm:grid-cols-2 gap-4">
            <div>
              <p class="text-sm text-gray-500">Email</p>
              <p class="text-gray-900">
                {{ studentProfile.account.plp_email }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500">Password</p>
              <p class="text-gray-900">******</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  </ScrollArea>
</template>

<script setup>
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogClose,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Pencil } from "lucide-vue-next";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import NavBarStudent from "@/components/navigation/NavBarStudent.vue";
import { ref, onMounted } from "vue";
import axios from "axios";
import { useAuthStore } from "@/store/student";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
import { useToast } from "@/components/ui/toast/use-toast";
import { Toaster } from "@/components/ui/toast";

const authStore = useAuthStore();
authStore.restoreSession();
const { toast } = useToast();
const studentProfile = ref(null);
const password = ref("");
const confirmPassword = ref("");

// Method to handle password change
const changePassword = async () => {
  if (password.value !== confirmPassword.value) {
    toast({
      variant: "destructive",
      title: "Error updating password",
      description: "Passwords do not match",
    });
    return;
  }

  try {
    const studentId = localStorage.getItem("student_id");
    await axios.put(
      `https://sentiment-professor-feedback-1.onrender.com/api/student-acc/${studentId}/`,
      {
        password: password.value,
        confirm_password: confirmPassword.value,
      }
    );
    toast({
      title: "Success",
      description: "Password updated succesfully",
    });
  } catch (error) {
    toast({
      variant: "destructive",
      title: "Error updating password",
      description: error.error,
    });
  }
};

onMounted(async () => {
  const studentId = localStorage.getItem("student_id");
  if (studentId) {
    try {
      const response = await axios.get(
        `https://sentiment-professor-feedback-1.onrender.com/api/student-profile?student_id=${studentId}`
      );
      studentProfile.value = response.data;
    } catch (error) {
      console.error("Error fetching student profile:", error);
    }
  } else {
    console.error("Student ID not found in localStorage.");
  }
});
</script>
