import { useState, useEffect, useRef } from "react";

const CHAVE = "aula_inicio";
const DURACAO = 45 * 60 * 1000;

export default function useAulaTimer() {
  const [tempoRestante, setTempoRestante] = useState(DURACAO);
  const [ativo, setAtivo] = useState(false);

  const intervalRef = useRef(null);

  // ▶️ iniciar
  const iniciar = () => {
    if (intervalRef.current) return;
    const inicio = Date.now();
    localStorage.setItem(CHAVE, inicio);
    setAtivo(true);

    intervalRef.current = setInterval(() => {
      const inicio = localStorage.getItem(CHAVE);

      if (!inicio) {
        parar();
        return;
      }

      const restante = DURACAO - (Date.now() - Number(inicio));

      if (restante <= 0) {
        parar();
      } else {
        setTempoRestante(restante);
      }
    }, 1000);
  };

  //  parar
  const parar = () => {
    localStorage.removeItem(CHAVE);

    setAtivo(false);
    setTempoRestante(DURACAO);

    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
  };

  // NÃO inicia automaticamente
  useEffect(() => {
    const inicio = localStorage.getItem(CHAVE);

    if (inicio) {
      setAtivo(true);
      setTempoRestante(DURACAO - (Date.now() - Number(inicio)));
    }
  }, []);

  // formatar tempo
  const formatarTempo = (ms) => {
    const min = Math.floor(ms / 60000);
    const seg = Math.floor((ms % 60000) / 1000);
    return `${min}:${seg.toString().padStart(2, "0")}`;
  };

  return {
    tempoRestante,
    ativo,
    iniciar,
    parar,
    formatarTempo,
  };
}