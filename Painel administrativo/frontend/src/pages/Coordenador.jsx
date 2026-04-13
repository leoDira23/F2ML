import Header from "../components/Header/Header";
import MiddleNav from "../components/Nav/middleNav";
import ContentCard from "../components/Card/ContentCard";
import Text from "../components/Text/Text";
import Button from "../components/Button/Button";
import Sidebar from "../components/Sidebar/Sidebar";  
import Card from "../components/Card/Card";
import "./Coordenador.css";
import {
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
import { useState } from "react";

export default function Coordenador() {

    const [activeTab,setActiveTab] = useState(1);

  return (
    <div className="size-full">
      <Header
        title="Painel do Coordenador Pedagogico"
        description="Monitoramento de professores e turmas"
      />
    <div className="main">
      
      
      <Card variant="grid" className={'grid-4'}>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Total de Professores</p>
            <h2>{4}</h2>
            <span>1 em aula agora</span>
          </div>
          <div className="grid-child-icon">
            <Users/>
          </div>
        </div>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Turmas Ativas</p>
            <h2>{4}</h2>
          </div>
          <div className="grid-child-icon">
            <BookOpenIcon></BookOpenIcon>
          </div>
        </div>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Total de Alunos</p>
            <h2>{20}</h2>
          </div>
          <div className="grid-child-icon">
            <Users />
          </div>
        </div>
        <div className="grid-child">
          <div className="grid-child-content">
            <p>Taxa de Presença</p>
            <h2>{"87%"}</h2>
            <span style={{ color: "green" }}>{"5%"}</span>
          </div>
          <div className="grid-child-icon">
            <TrendingUp />
          </div>
        </div>
      </Card>

        <MiddleNav variant="grid" className={`grid-4`}>
            <button className={`btn-nav ${activeTab == 1 ? "active" : ""}`} key={1}
            onClick={() => setActiveTab(1)}><Text as="p" size="Xsmall" color="default">Professores</Text></button>
            <button className={`btn-nav ${activeTab == 2 ? "active" : ""}`} key={2}
            onClick={() => setActiveTab(2)}><Text as="p" size="Xsmall" color="default">Turmas</Text></button>
            <button className={`btn-nav ${activeTab == 3 ? "active" : ""}`} key={3}
            onClick={() => setActiveTab(3)}><Text as="p" size="Xsmall" color="default">Justificativas</Text></button>
            <button className={`btn-nav ${activeTab == 4 ? "active" : ""}`} key={4}
            onClick={() => setActiveTab(4)}><Text as="p" size="Xsmall" color="default">Relatorios</Text></button>
        </MiddleNav>

      <Card className={`${activeTab !== 1 ? "hide" : ""}`} variant="default">
        <div className="cardElement">
          <div className="card-text">
            <h4
              style={{ margin: "0", marginBottom: "10px" }}
              className="center"
            >
              <Users />
              Controle de professores
            </h4>
            <p>Monitore a atividade, presença e assiduidade dos professores</p>
          </div>
        </div>



        <div className="cardElement">
  <table className="modern-table">
    <thead>
      <tr>
        <th>Nome</th>
        <th>Email</th>
        <th>Função</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Michael Mateus</td>
        <td>michael@email.com</td>
        <td>Administrador</td>
        <td><span className="status active">Ativo</span></td>
      </tr>
      <tr>
        <td>Ana Silva</td>
        <td>ana@email.com</td>
        <td>Usuário</td>
        <td><span className="status inactive">Inativo</span></td>
      </tr>
            <tr>
        <td>Ana Silva</td>
        <td>ana@email.com</td>
        <td>Usuário</td>
        <td><span className="status inactive">Inativo</span></td>
      </tr>
            <tr>
        <td>Ana Silva</td>
        <td>ana@email.com</td>
        <td>Usuário</td>
        <td><span className="status inactive">Inativo</span></td>
      </tr>
            <tr>
        <td>Ana Silva</td>
        <td>ana@email.com</td>
        <td>Usuário</td>
        <td><span className="status inactive">Inativo</span></td>
      </tr>
    </tbody>
  </table>
        </div>
      </Card>


        <Card className={`${activeTab !== 2 ? "hide" : ""}`} variant="default">
                    <div className="cardElement">
                      <div className="card-text">
                        <h4
                          style={{ margin: "0", marginBottom: "10px" }}
                          className="center"
                        > 
                          Relatorios de Assiduidade do Docente</h4>
                        <p>Gere Relatorios Semanais, ou mensais dos Professores</p>
                      </div>
                    </div>
      
                    <Card variant="grid">
      
      
                      <Card variant="default">
                        <p
                          style={{ margin: "0", marginBottom: "10px" }}
                          className="center"
                        > <Users></Users>
                          Presença dos Professores</p>
      
                        <Text as="span" size="small" color="default">
                          Relatorio completo de Presenças e Faltas
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
                        > <Clock></Clock>
                          Horas Letivas</p>
      
                        <Text as="span" size="small" color="default">
                          Horas Trabalhadas vs. Previstas
                        </Text>
      
                        <Button variant="white">
                          <Download></Download>
                          <p>Gerar Relatório</p>
                        </Button>
                      </Card>

                       <Card variant="default">
                        <p
                          style={{ margin: "0", marginBottom: "10px" }}
                          className="center"
                        > <Settings></Settings>
                          Substituições</p>
      
                        <Text as="span" size="small" color="default">
                          Historico de Substituições e Ausencias
                        </Text>
      
                        <Button variant="white">
                          <Download></Download>
                          <p>Gerar Relatório</p>
                        </Button>
                      </Card>
      
                      <Card variant="default">
                        <p
                          style={{ margin: "0", marginBottom: "10px" }}
                          className="center"
                        > <ChartColumn/>
                          Estatisticas Gerais</p>
      
                        <Text as="span" size="small" color="default">
                          Resumo Completo do Periodo
                        </Text>
      
                        <Button variant="white">
                          <NotepadText></NotepadText>
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
