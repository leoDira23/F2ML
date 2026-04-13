// src/App.jsx
import { Routes, Route } from "react-router-dom";
import Admin from "./pages/Admin";
import Coordenador from "./pages/Coordenador";
import Professor from "./pages/Professor";
import Login from "./pages/Login";
import { AuthProvider } from "./AuthContext";
import PrivateRoute from "./PrivateRoute";

export default function App() {
  return (
    <AuthProvider>
      <Routes>
        

        <Route path="/login" element={<Login />} />

        {/* Rotas protegidas */}
        <Route
          path="/"
          element={
            <PrivateRoute>
              <Admin />
            </PrivateRoute>
          }
        />
        <Route
          path="/coordenador"
          element={
            <PrivateRoute>
              <Coordenador />
            </PrivateRoute>
          }
        />
        <Route
          path="/professor"
          element={
            <PrivateRoute>
              <Professor />
            </PrivateRoute>
          }
        />
      </Routes>
    </AuthProvider>
  );
}