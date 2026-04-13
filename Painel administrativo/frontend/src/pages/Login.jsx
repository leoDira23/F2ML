import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { FaEnvelope, FaLock, FaEye, FaEyeSlash } from "react-icons/fa";
import "./Login.css";
import logo from "../assets/imagens/logo-fingger.jpeg";
import illustration from "../assets/imagens/fingerprint-illustration.jpeg";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

const handleLogin = async (e) => {
  e.preventDefault();

  // BLOQUEIO IMEDIATO
  if (loading) return;

  setLoading(true);
  setErrorMessage("");

  try {
    const response = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, senha: password }),
    });

    const data = await response.json();

    if (!response.ok || data.status === "error") {
      setErrorMessage(data.mensagem || "Erro no login");
      return;
    }

    localStorage.setItem("token", data.token);
    localStorage.setItem("user", JSON.stringify(data.usuario));
    localStorage.setItem("role", data.usuario.cargo);

    const cargo = data.usuario.cargo.trim().toLowerCase();

    switch (cargo) {
      case "admin":
        navigate("/");
        break;
      case "professor":
        navigate("/professor");
        break;
      case "coordenador":
        navigate("/coordenador");
        break;
      default:
        setErrorMessage("Perfil inválido");
    }

  } catch (error) {
    setErrorMessage("Falha na conexão com o servidor");
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="page-bg">
      <div className="center-wrap">
        <div className="card-root">
          <div className="card-left">
            <div className="left-inner">
              <div className="logo-row">
                <img src={logo} alt="Logo" className="logo-img" />
                <span className="brand">Fingerprint</span>
              </div>

              <h1 className="title">Login</h1>
              <p className="subtitle">Por favor, insira suas credenciais</p>

              <form className="form-area" onSubmit={handleLogin}>
                <div className="input-row">
                  <FaEnvelope className="icon" />
                  <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    disabled={loading}
                  />
                </div>

                <div className="input-row password-row">
                  <FaLock className="icon" />
                  <input
                    type={showPassword ? "text" : "password"}
                    placeholder="Senha"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    disabled={loading}
                  />
                  <span
                    className="show-password"
                    onClick={() => setShowPassword(!showPassword)}
                  >
                    {showPassword ? <FaEyeSlash /> : <FaEye />}
                  </span>
                </div>

                {errorMessage && <div className="error-box">{errorMessage}</div>}

                <Link to="/recuperar-senha" className="forgot">
                  Esqueceu a senha?
                </Link>

                <button className="btn-primary" type="submit" disabled={loading}>
                  {loading ? "Entrando..." : "Entrar"}
                </button>
              </form>
            </div>
          </div>

          <div className="card-right">
            <img src={illustration} alt="Ilustração" className="illustration" />
          </div>
        </div>
      </div>
    </div>
  );
}