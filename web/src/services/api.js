import axios from "axios";

const BASE_URL = 'http://localhost:3000/';

const api = axios.create({
  baseURL: BASE_URL,
});

api.defaults.headers.post['Content-Type'] = 'application/json';

export default api;