<template>
  <NavBarProfessor></NavBarProfessor>
  <ScrollArea class="h-svh w-full">
    <div class="max-w-3xl mx-auto p-4 space-y-6" v-if="profProfile">
      <h1 class="text-xl font-semibold mt-4 text-gray-900">My Profile</h1>
      <!-- Profile Header -->
      <Card>
        <CardContent class="p-6">
          <div class="flex justify-between items-start">
            <div class="flex gap-4 items-center">
              <Avatar class="h-16 w-16">
                <AvatarImage
                  src="https://plus.unsplash.com/premium_photo-1661942126259-fb08e7cce1e2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                  alt=""
                />
                <AvatarFallback>RC</AvatarFallback>
              </Avatar>
              <div>
                <h2 class="text-lg font-semibold">
                  {{ profProfile.first_name }}
                  {{ profProfile.middle_name }}
                  {{ profProfile.surname }}
                  {{ profProfile.extension_name }}
                </h2>
                <p class="text-gray-500 italic text-xs">
                  {{ profProfile.department_desc }}
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
            <p class="text-sm text-gray-500">Last Name</p>
            <p class="text-gray-900">
              {{ profProfile.surname }}
            </p>
          </div>
          <div>
            <p class="text-sm text-gray-500">First Name</p>
            <p class="text-gray-900">{{ profProfile.first_name }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Middle Name</p>
            <p class="text-gray-900">{{ profProfile.middle_name }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Extension Name</p>
            <p class="text-gray-900">{{ profProfile.extension_name }}</p>
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
            <p class="text-sm text-gray-500">Professor ID</p>
            <p class="text-gray-900">{{ profProfile.professor_id }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Department</p>
            <p class="text-gray-900">{{ profProfile.department_desc }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-500">Status</p>
            <p class="text-gray-900">{{ profProfile.status }}</p>
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
                <div class="grid flex-1 gap-2">
                  <Label for="link" class="">Password</Label>
                  <Input
                    id="link"
                    default-value="23454"
                    read-only
                    type="password"
                  />
                </div>
                <div class="grid flex-1 gap-2">
                  <Label for="link" class="">Confirm Password</Label>
                  <Input
                    id="link"
                    default-value="23454"
                    read-only
                    type="password"
                  />
                </div>
              </div>
              <DialogFooter class="sm:justify-start">
                <DialogClose as-child>
                  <Button
                    type="submit"
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
              <p class="text-gray-900">@plpasig</p>
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
import NavBarProfessor from "@/components/navigation/NavBarProfessor.vue";
import ScrollArea from "@/components/ui/scroll-area/ScrollArea.vue";
import { ref, onMounted } from "vue";
import axios from "axios";

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
