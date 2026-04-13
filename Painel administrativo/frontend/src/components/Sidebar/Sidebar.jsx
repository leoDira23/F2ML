import { X, UserCheck, BookOpen, Users } from "lucide-react";
import { useNavigate } from "react-router-dom";
import "./Sidebar.css";

export default function Sidebar({ open, onClose }) {
  const navigate = useNavigate();

  if (!open) return null;

  return (
    <>
      <div className="sidebar-overlay" onClick={onClose}></div>

      <aside className="sidebar">
        <button className="close-btn" onClick={onClose}>
          <X />
        </button>

        <nav>
          <button onClick={() => { navigate("/admin"); onClose(); }}>
            <UserCheck />
            Admin
          </button>

          <button onClick={() => { navigate("/coordenador"); onClose(); }}>
            <Users />
            Coordenador
          </button>

          <button onClick={() => { navigate("/professor"); onClose(); }}>
            <BookOpen />
            Professor
          </button>
        </nav>
      </aside>
    </>
  );
}
