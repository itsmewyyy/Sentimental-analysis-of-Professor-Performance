import axios from "axios";

axios.defaults.withCredentials = true;
const axiosInstance = axios.create({
  baseURL: "process.env.VUE_APP_API_BASE_URL",
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
