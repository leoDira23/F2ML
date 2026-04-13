// services.js
import api from './api.js';

export const authService = {
  login: async (email, senha) => {
    const { data } = await api.post('/login', { email, senha });
    localStorage.setItem('token', data.token); // salva token
    return data;
  },
};

export const alunoService = {
  listar: async () => {
    const { data } = await api.get('/alunos'); // token já vai no header
    return data;
  },
};

export const professorService = {
  listar: async () => {
    const { data } = await api.get('/professores'); // token já vai no header
    return data;
  },
};