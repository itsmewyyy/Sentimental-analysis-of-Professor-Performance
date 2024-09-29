<template>
    <div v-for="(college, collegeIndex) in colleges" :key="collegeIndex" class="pb-8 pl-8">
      <!-- College Button -->
      <button 
        :id="`multiLevelDropdownButton-${college.name}`"
        :data-dropdown-toggle="`multi-dropdown-${college.name}`"
        class="border border-black/15 college-card rounded-lg pl-5 hover:bg-darks-50" 
        type="button"
      >
        <div class="flex items-center space-x-48 text-darks-700 font-bold text-2xl">
          <p>{{ college.name }}</p>
          <div class="z-10 hover:scale-125">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 20C11.45 20 10.9792 19.8042 10.5875 19.4125C10.1958 19.0208 10 18.55 10 18C10 17.45 10.1958 16.9792 10.5875 16.5875C10.9792 16.1958 11.45 16 12 16C12.55 16 13.0208 16.1958 13.4125 16.5875C13.8042 16.9792 14 17.45 14 18C14 18.55 13.8042 19.0208 13.4125 19.4125C13.0208 19.8042 12.55 20 12 20ZM12 14C11.45 14 10.9792 13.8042 10.5875 13.4125C10.1958 13.0208 10 12.55 10 12C10 11.45 10.1958 10.9792 10.5875 10.5875C10.9792 10.1958 11.45 10 12 10C12.55 10 13.0208 10.1958 13.4125 10.5875C13.8042 10.9792 14 11.45 14 12C14 12.55 13.8042 13.0208 13.4125 13.4125C13.0208 13.8042 12.55 14 12 14ZM12 8C11.45 8 10.9792 7.80417 10.5875 7.4125C10.1958 7.02083 10 6.55 10 6C10 5.45 10.1958 4.97917 10.5875 4.5875C10.9792 4.19583 11.45 4 12 4C12.55 4 13.0208 4.19583 13.4125 4.5875C13.8042 4.97917 14 5.45 14 6C14 6.55 13.8042 7.02083 13.4125 7.4125C13.0208 7.80417 12.55 8 12 8Z" fill="#5F6368"/>
            </svg>
          </div>
        </div>
        <p class="text-left text-darks-300 text-base">{{ college.description }}</p>
      </button>
  
      <!-- Dropdown menu -->
      <div :id="`multi-dropdown-${college.name}`" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-dropdown">
        <ul class="py-2 text-sm text-gray-700" :aria-labelledby="`multiLevelDropdownButton-${college.name}`">
          <li v-if="college.years.length" v-for="(year, yearIndex) in college.years" :key="yearIndex">
            <!-- Year Dropdown Button -->
            <button 
              :id="`yearDropdownButton-${college.name}-${year.year_level_id}`"
              :data-dropdown-toggle="`yearDropdown-${college.name}-${year.year_level_id}`"
              data-dropdown-placement="right-start"
              type="button"
              class="flex items-center justify-center w-full px-4 py-2 hover:bg-gray-100"
            >
              {{ year.year_level_desc }}
            </button>
  
            <!-- Year Dropdown Programs-->
            <div 
              :id="`yearDropdown-${college.name}-${year.year_level_id}`"
              class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700"
            >
              <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="`yearDropdownButton-${college.name}-${year.year_level_id}`">
                <li v-if="year.programs.length" v-for="(program, programIndex) in year.programs" :key="programIndex">
                  <!-- Program Button -->
                  <button 
                    :id="`programDropdownButton-${college.name}-${year.year_level_id}-${program.program_id}`"
                    :data-dropdown-toggle="`programDropdown-${college.name}-${year.year_level_id}-${program.program_id}`"
                    data-dropdown-placement="right-start"
                    type="button"
                    class="flex items-center justify-center w-full px-4 py-2 hover:bg-gray-100"
                  >
                    {{ program.program_desc }}
                  </button>
  
                  <!-- Program Dropdown Sections -->
                  <div 
                    :id="`programDropdown-${college.name}-${year.year_level_id}-${program.program_id}`"
                    class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700"
                  >
                    <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" :aria-labelledby="`programDropdownButton-${college.name}-${year.year_level_id}-${program.program_id}`">
                      <!-- Sections under Program -->
                      <li v-if="program.sections.length" v-for="(section, sectionIndex) in program.sections" :key="sectionIndex">
                        <a 
                          href="#" 
                          class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                          @click.prevent="goToSection(section.section_id)"
                        >
                          {{ section.section_id }}
                        </a>
                      </li>
                    </ul>
                  </div>
                </li>
              </ul>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: "collegeDropdown",
    data() {
      return {
        colleges: [],
      }
    },
    mounted() {
      this.fetchColleges();
    },
    methods: {
      async fetchColleges() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/colleges/'); 
          this.colleges = response.data;
          console.log('API response:', response.data); 
        } catch (error) {
          console.error('Error fetching colleges:', error);
        }
      },
      goToSection(sectionId) {
        this.$router.push({ name: 'SectionStudents', params: { sectionId } });
      }
    }
  };
  </script>
  
  <style scoped>
  .college-card {
    width: 300px;
    height: 88px;
  }
  
  .w-dropdown {
    width: 300px;
  }
  </style>
  