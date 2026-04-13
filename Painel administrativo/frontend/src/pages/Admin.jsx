import Header from "../components/Header/Header";
import Text from "../components/Text/Text";
import Card from "../components/Card/Card";
import Button from "../components/Button/Button";
import MiddleNav from "../components/Nav/middleNav";
import {
  alunoService,
  professorService,
} from "../services/services";
import { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar/Sidebar";
import { Users, User, UserCheck, TrendingUp } from "lucide-react";
import { useNavigate } from "react-router-dom";
import "./Admin.css";

export default function Admin() {
  const [SidebarOpen, setSidebarOpen] = useState(false);
  const [activeTab, setActiveTab] = useState(1);

  const navigate = useNavigate();

  const [listarAlunos, setListarAlunos] = useState([]);
  const [listarProfessores, setListarProfessores] = useState([]);

  useEffect(() => {
    async function carregarDados() {
      try {
       
        const token = localStorage.getItem("token");

        if (!token) {
          navigate("/login"); 
          return;
        }


        const dataAlunos = await alunoService.listar();
        setListarAlunos(dataAlunos);

        const dataProfessores = await professorService.listar();
        setListarProfessores(dataProfessores);

      } catch (erro) {
        console.error("Erro ao carregar dados:", erro.response?.data || erro.message);
      }
    }

    carregarDados();
  }, [navigate]);

  return (
    <div className="size-full">
      <Header
        title="Painel Administrativo"
        description="Gestão completa do sistema escolar"
        onMenuClick={() => setSidebarOpen(true)}
      />

      <div className="main">
        <Sidebar open={SidebarOpen} onClose={() => setSidebarOpen(false)} />

        {/* Cards */}
        <Card variant="grid" className="grid-4">
          <div className="grid-child">
            <div className="grid-child-content">
              <p>Coordenadores</p>
              <h2>5</h2>
              <span>2 Presentes</span>
            </div>
            <div className="grid-child-icon">
              <UserCheck />
            </div>
          </div>

          <div className="grid-child">
            <div className="grid-child-content">
              <p>Professores</p>
              <h2>{listarProfessores.length}</h2>
            </div>
            <div className="grid-child-icon">
              <Users />
            </div>
          </div>

          <div className="grid-child">
            <div className="grid-child-content">
              <p>Alunos</p>
              <h2>{listarAlunos.length}</h2>
            </div>
            <div className="grid-child-icon">
              <Users />
            </div>
          </div>

          <div className="grid-child">
            <div className="grid-child-content">
              <p>Taxa de Presença</p>
              <h2>87%</h2>
              <span style={{ color: "green" }}>5%</span>
            </div>
            <div className="grid-child-icon">
              <TrendingUp />
            </div>
          </div>
        </Card>

        {/* Navegação */}
        <MiddleNav variant="grid" className="grid-5">
          {["Usuarios", "Biometria", "Horários", "Presenças", "Relatórios"].map((item, index) => (
            <button
              key={index}
              className={`btn-nav ${activeTab === index + 1 ? "active" : ""}`}
              onClick={() => setActiveTab(index + 1)}
            >
              <Text as="p" size="Xsmall" color="default">
                {item}
              </Text>
            </button>
          ))}
        </MiddleNav>

        {/* Tabela */}
        <Card className={`${activeTab !== 1 ? "hide" : ""}`} variant="default">
          <div className="cardElement">
            <div className="card-text">
              <h4 className="center">
                <Users style={{ color: "rgb(110 106 221)" }} />
                Gestão de Usuários
              </h4>
              <p>Cadastre e gerencie professores e alunos</p>
            </div>

            <Button variant="blue" onClick={() => navigate("/usuarios")}>
              <User /> Novo Usuário
            </Button>
          </div>

          {/* Professores */}
          <h3>Professores</h3>
          <table className="modern-table">
            <thead>
              <tr>
                <th>Nome</th>
                <th>Email</th>
                <th>Disciplina</th>
              </tr>
            </thead>
            <tbody>
              {listarProfessores.length === 0 ? (
                <tr>
                  <td colSpan={3} style={{ textAlign: "center" }}>
                    Nenhum professor encontrado
                  </td>
                </tr>
              ) : (
                listarProfessores.map((prof, idx) => (
                  <tr key={idx}>
                    <td>{prof.nome}</td>
                    <td>{prof.email}</td>
                    <td>{prof.disciplina}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>

          {/* Alunos */}
          <h3>Alunos</h3>
          <table className="modern-table">
            <thead>
              <tr>
                <th>Nome</th>
                <th>Nº Processo</th>
                <th>Turma</th>
              </tr>
            </thead>
            <tbody>
              {listarAlunos.length === 0 ? (
                <tr>
                  <td colSpan={3} style={{ textAlign: "center" }}>
                    Nenhum aluno encontrado
                  </td>
                </tr>
              ) : (
                listarAlunos.map((aluno, idx) => (
                  <tr key={idx}>
                    <td>{aluno.nome}</td>
                    <td>{aluno.numero_processo}</td>
                    <td>{aluno.turma}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </Card>
      </div>
    </div>
  );
}