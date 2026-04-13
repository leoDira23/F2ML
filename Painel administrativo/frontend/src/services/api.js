import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor adiciona token automaticamente
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token'); // token salvo no login
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, error => Promise.reject(error));

export default api;