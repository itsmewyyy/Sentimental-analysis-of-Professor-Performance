import axios from "axios";

axios.defaults.withCredentials = true;
const axiosInstance = axios.create({
  baseURL: "https://sentiment-professor-feedback-1.onrender.com/",
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
