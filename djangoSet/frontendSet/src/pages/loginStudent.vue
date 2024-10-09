<!-- Student Login -->
<template>
  <div class="min-h-screen flex items-center justify-center font-raleway">
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
            class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-md"
          >
            <h2 class="text-2xl font-bold text-plpyellow-200">Student Login</h2>
            <form @submit.prevent="login" class="mt-8 space-y-6">
              <div class="space-y-2">
                <div class="space-y-6">
                  <div class="relative w-full mb-4">
                    <div
                      class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"
                    >
                      <svg
                        class="w-4 h-4 text-gray-500 dark:text-gray-400"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 20"
                      >
                        <path
                          d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
                        />
                      </svg>
                    </div>
                    <input
                      v-model="dateofbirth"
                      id="datepicker-autohide"
                      datepicker
                      datepicker-autohide
                      type="text"
                      class="py-3 px-0 bg-gray-50 border-2 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-plpgreen-200 focus:border-plpgreen-200 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 cursor-pointer caret-transparent"
                      placeholder="Date of Birth"
                      required
                    />
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

<script>
import { useAuthStore } from "@/store/student";

export default {
  data() {
    return {
      student_acc_number: "",
      password: "",
      dateofbirth: "",
      formatted_date: "",
    };
  },
  mounted() {
    this.initializeDatepicker();
  },
  methods: {
    initializeDatepicker() {
      const datepickerElement = document.getElementById("datepicker-autohide");
      if (datepickerElement) {
        const datepicker = new Datepicker(datepickerElement, {
          autohide: true,
          format: "mm/dd/yyyy",
        });

        datepickerElement.addEventListener("changeDate", (event) => {
          this.dateofbirth = event.target.value;
          this.formatDate();
        });
      }
    },
    formatDate() {
      if (this.dateofbirth) {
        const [month, day, year] = this.dateofbirth.split("/");
        this.formatted_date = `${year}-${month.padStart(2, "0")}-${day.padStart(
          2,
          "0"
        )}`;
        console.log("Formatted Date:", this.formatted_date);
      }
    },

    async login() {
      const authStudentLogin = useAuthStore();

      if (this.dateofbirth) {
        this.formatDate();
      }

      try {
        await authStudentLogin.login(
          this.student_acc_number,
          this.password,
          this.formatted_date
        );
        this.$router.push("/StudentDashboard");
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
