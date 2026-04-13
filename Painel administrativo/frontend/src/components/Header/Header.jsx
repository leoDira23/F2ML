import Button from "../Button/Button";
import Text from "../Text/Text";
import { Menu, LogOut, Bell } from "lucide-react";
import { useNavigate } from "react-router-dom";
import "./Header.css";
import "../Text/text.css";
import "../Notification/Notification.css";
import { useNotification } from "../Notification/useNotification";

export default function Header({ title, onMenuClick }) {
  const navigate = useNavigate();
  const { texto, show, hide } = useNotification();

  // Função de logout
  const handleLogout = () => {
    localStorage.removeItem("token"); // remove o JWT
    navigate("/login");               // redireciona para a tela de login
  };

  return (
    <header className="header">
      <div className="perfil">
        <div className="hamburger">
          <Button variant="white" onClick={onMenuClick}>
            <Menu />
          </Button>
        </div>

        <div className="fotodeperfil"></div>
        <div>
          <Text as="h1" size="big" color="default">{title}</Text>
        </div>
      </div>

      {texto && (
        <div className="overlay" onClick={hide}>
          <div className="toast">{texto}</div>
        </div>
      )}

      <div className="sideButtons">
        {/* Notificações */}
        <Button
          className="notification"
          variant="white"
          onClick={() => show("Sem notificações no momento.")}
        >
          <Bell />
        </Button>

        {/* Botão de logout */}
        <Button className="logout" variant="white" onClick={handleLogout}>
          <LogOut />
          Sair
        </Button>
      </div>
    </header>
  );
}

// Componente vazio opcional
function Header2() {
  return <header className="header"></header>;
}