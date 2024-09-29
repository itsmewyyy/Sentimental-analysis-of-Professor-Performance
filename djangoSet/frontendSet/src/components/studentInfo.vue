<template>

    <div class="w-11/12 h-20 rounded-md border border-black/15 flex items-center align-center pl-10">
        <div class="flex space-x-8" :id = "id" >
            <div class="flex space-x-44 text-base pl-2">
                <p class="w-32">21-00260</p>
                <p class="w-72">Intalan, Ryan Celestino B.</p>
                <p class="w-28">BSCS4A</p>
                <div class="flex space-x-5">
                    <button class="z-40 hover:scale-125"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none">
                        <path d="M5 19H6.425L16.2 9.225L14.775 7.8L5 17.575V19ZM3 21V16.75L16.2 3.575C16.4 3.39167 16.6208 3.25 16.8625 3.15C17.1042 3.05 17.3583 3 17.625 3C17.8917 3 18.15 3.05 18.4 3.15C18.65 3.25 18.8667 3.4 19.05 3.6L20.425 5C20.625 5.18333 20.7708 5.4 20.8625 5.65C20.9542 5.9 21 6.15 21 6.4C21 6.66667 20.9542 6.92083 20.8625 7.1625C20.7708 7.40417 20.625 7.625 20.425 7.825L7.25 21H3ZM15.475 8.525L14.775 7.8L16.2 9.225L15.475 8.525Z" fill="#008000"/>
                    </svg></button>
                    <button class="z-40 hover:scale-125"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none">
                        <path d="M7 21C6.45 21 5.97917 20.8042 5.5875 20.4125C5.19583 20.0208 5 19.55 5 19V6H4V4H9V3H15V4H20V6H19V19C19 19.55 18.8042 20.0208 18.4125 20.4125C18.0208 20.8042 17.55 21 17 21H7ZM17 6H7V19H17V6ZM9 17H11V8H9V17ZM13 17H15V8H13V17Z" fill="#B40D0D"/>
                    </svg></button>
                    
                </div>
            </div>   
        </div>
    </div>

</template>


<script>
export default {
name: "studentInfo",
props: {
student_id: {
  type: String,
  required: true
},
name: {
  type: String,
  required: true
},
section: {
  type: String,
  required: true
},
id: {
    type: String,
    required: true
}


},

};
</script>