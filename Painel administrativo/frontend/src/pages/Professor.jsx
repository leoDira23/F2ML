import Header from "../components/Header/Header";
import ContentCard from "../components/Card/ContentCard";
import Button from "../components/Button/Button";
import Sidebar from "../components/Sidebar/Sidebar";
import  Card  from "../components/Card/Card";
import Text from "../components/Text/Text";
import Table from "../components/Table/Table";
import MiddleNav from "../components/Nav/middleNav";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import "./Professor.css"

import {
  PlayCircle,
  Users,
  Calendar,
  Calendar1,
  Check,
  CircleCheck,
  BookOpenIcon,
  AlertCircle,
  Clock,
  ChartColumn,
  Settings,
  TrendingUp,
  UserCheck,
  Eye,
  NotepadText,
  BookOpen,
  User,
  FingerprintIcon,
  Download
} from "lucide-react";

export default function Professor() {
  
  const [activeTab,setActiveTab] = useState(1);
  const navigate = useNavigate();
  return (
  <div className="size-full">
    <Header
        title="Painel do Professor"
        description="Prof. João Mendes - ID T035"
      />
    <div className="main">
      
      <Card variant="default">
        <div><p><strong>Minhas turmas e Horarios</strong></p>
        <p>Selecione a turma para gerenciar a aula</p></div>
        
        <div className="cardElement-grid">
          <Button variant={`white`} navigate onClick={() => navigate("/turmaA11")}>
            <p>Turma A - 11º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma B - 11º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma C - 11º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma A - 12º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma B - 12º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma C - 12º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma A - 13º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma B - 13º Ano</p>
          </Button>
          <Button variant={`white`}>
            <p>Turma C - 13º Ano</p>
          </Button>
        </div>

      </Card>

      <Card variant="grid" className={'grid-4'}>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Total De Alunos</p>
            <h2>5</h2>
          </div>
          <div className="grid-child-icon">
            <UserCheck />
          </div>
        </div>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Presentes</p>
            <h2>0</h2>
          </div>
          <div className="grid-child-icon">
            <Users />
          </div>
        </div>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Ausentes</p>
            <h2>5</h2>
          </div>
          <div className="grid-child-icon">
            <AlertCircle />
          </div>
        </div>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Tempo de Aula</p>
            <h2>-:-</h2>
          </div>
          <div className="grid-child-icon">
            <Clock />
          </div>
        </div>
      </Card>

      <Card variant="default">
        <div className="card-text">
          <h4 style={{ margin: "0" }} className="center">
            <Calendar />
            
            Controle da Aula - {"Turma A - 11º Ano"}
          </h4>
          <p>TREI - Seg/Qua 08:00-09:30</p>
        </div>
        <Button variant={"blue"} > <PlayCircle></PlayCircle> Iniciar Aula</Button>
      </Card>

      <MiddleNav className={`grid-3`}>
        <button className={`btn-nav ${activeTab == 1 ? "active" : ""}`} key={1}
            onClick={() => setActiveTab(1)}><Text as="p" size="Xsmall" color="default">Lista de Presença</Text></button>
        <button className={`btn-nav ${activeTab == 2 ? "active" : ""}`} key={2}
            onClick={() => setActiveTab(2)}><Text as="p" size="Xsmall" color="default">Meu Historico</Text></button>
        <button className={`btn-nav ${activeTab == 3 ? "active" : ""}`} key={3 }
            onClick={() => setActiveTab(3)}><Text as="p" size="Xsmall" color="default">Justificativa</Text></button>
      </MiddleNav>

      <Card className={`${activeTab !== 1 ? "hide" : ""}`} variant="default" data-conteudo="listaDePresenca">
        <div>
          <p><Text as="span" size="medium" color="default">Lista de Presença</Text></p>
          <p><Text as="span" size="small" color="muted">Acompanhe e marque presença dos alunos em tempo real</Text></p> 
        </div>
          <div className="cardElement">
            <Table></Table>
          </div>
        
      </Card>

      <Card className={`${activeTab !== 2 ? "hide" : ""}`} variant="default" data-conteudo="listaDePresenca">
        <div>
          <p><Text as="span" size="medium" color="default">Meu Historico de Presença</Text></p>
          <p><Text as="span" size="small" color="muted">Visualize Suas presenças e aulas Ministradas</Text></p> 
        </div>

        <Card style={{background:"#3d6bec5d"}}>
            
                          <div className="div-grid">
            
                            <Card>
                              <Text as="p" size="Xsmall" color="default">Aulas este Mês</Text>
                              <Text as="h4" size="medium" color="default">15</Text>
                            </Card>
                            <Card>
                              <Text as="p" size="Xsmall" color="default">Horarios Totais</Text>
                              <Text as="h4" size="medium" color="default">97h</Text>
                            </Card>
                            <Card>
                              <Text as="p" size="Xsmall" color="default">Taxas de Presença</Text>
                              <Text as="h4" size="medium" color="default">92%</Text>
                            </Card>
                          </div>
            
                          </Card>
          <div className="cardElement">
            
          </div>
        
      </Card>

      <Card className={`${activeTab !== 3 ? "hide" : ""}`} variant="default" data-conteudo="relatorio">
                          <div className="cardElement">
                            <div className="card-text">
                              <h4
                                style={{ margin: "0", marginBottom: "10px" }}
                                className="center"
                              > 
                                Relatórios e Estatísticas</h4>
                              <p>Gere Relatorios Semanais, ou mensais dos Professores</p>
                            </div>
                          </div>
            
                          <Card variant="grid" className={"grid-2"}>
            
            
                            <Card variant="default">
                              <p
                                style={{ margin: "0", marginBottom: "10px" }}
                                className="center"
                              > <NotepadText></NotepadText>
                                Relatório Mensal</p>
            
                              <Text as="span" size="small" color="default">
                                Suas presenças e aulas do mês atual
                              </Text>
            
                              <Button variant="blue">
                                <Download></Download>
                                <p>Gerar Relatorio</p>
                              </Button>
                            </Card>
      
                             <Card variant="default">
                              <p
                                style={{ margin: "0", marginBottom: "10px" }}
                                className="center"
                              > <NotepadText></NotepadText>
                                Presenças dos Alunos</p>
            
                              <Text as="span" size="small" color="default">
                                Relatorio de presença por turma
                              </Text>
            
                              <Button variant="white">
                                <Download></Download>
                                <p>Gerar Relatório</p>
                              </Button>
                            </Card>
            
                          </Card>
            
                          <Card style={{background:"#3d6bec5d"}}>
                            <div className="cardElement">
                            <div className="card-text">
                              <h4
                                style={{ margin: "0", marginBottom: "10px" }}
                                className="center"
                              ><TrendingUp></TrendingUp>
                                Resumo Estátistico do Mês</h4>
                            </div>
                          </div>
            
                          <div className="div-grid">
            
                            <Card>
                              <Text as="p" size="Xsmall" color="default">Total de Aulas</Text>
                              <Text as="h4" size="medium" color="default">156</Text>
                            </Card>
                            <Card>
                              <Text as="p" size="Xsmall" color="default">Taxa Presença</Text>
                              <Text as="h4" size="medium" color="default">97%</Text>
                            </Card>
                            <Card>
                              <Text as="p" size="Xsmall" color="default">Faltas Totais</Text>
                              <Text as="h4" size="medium" color="default">92</Text>
                            </Card>
                            <Card>
                              <Text as="p" size="Xsmall" color="default">Horas Trabalhadas</Text>
                              <Text as="h4" size="medium" color="default">234h</Text>
                            </Card>
            
                          </div>
            
                          </Card>
                         
            
              </Card>
    </div>
    </div>
  );
}
