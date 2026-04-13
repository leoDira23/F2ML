export const GlobalStore = {
  alunos: [],
  user: null,
  
  // Função para atualizar e notificar (se necessário)
  setAlunos(novosAlunos) {
    this.alunos = novosAlunos;
    console.log("Estado Global Atualizado:", this.alunos);
  }
};