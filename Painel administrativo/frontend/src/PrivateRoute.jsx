import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

export default function PrivateRoute({ children }) {
  const { user, loading } = useAuth();

  const token = localStorage.getItem("token");

  if (loading) {
    return <div>Carregando...</div>;
  }

  // 🔥 agora valida token também
  if (!user && !token) {
    return <Navigate to="/login" replace />;
  }

  return children;
}