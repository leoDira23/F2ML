import { useState } from "react";
import { CircleCheck, Pencil, Trash2, X } from "lucide-react";
import "./Table.css";

const initialUsers = [
  {
    id: "T001",
    nome: " João Mendes",
    email: "joao@escola.com",
    disciplinas: ["Matemática"],
    biometria: true,
  },
  {
    id: "T002",
    nome: " Zuliria Domingos",
    email: "zulidomingos@escola.com",
    disciplinas: [ "Bioquímica"],
    biometria: true,
  },
];

export default function Table() {
  const [users, setUsers] = useState(initialUsers);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingUser, setEditingUser] = useState(null);
  const [form, setForm] = useState({
    nome: "",
    email: "",
    disciplinas: "",
  });

  function openNewUser() {
    setEditingUser(null);
    setForm({ nome: "", email: "", disciplinas: "" });
    setModalOpen(true);
  }

  function openEdit(user) {
    setEditingUser(user);
    setForm({
      nome: user.nome,
      email: user.email,
      disciplinas: user.disciplinas.join(", "),
    });
    setModalOpen(true);
  }

  function saveUser() {
    if (editingUser) {
      setUsers(
        users.map((u) =>
          u.id === editingUser.id
            ? {
                ...u,
                nome: form.nome,
                email: form.email,
                disciplinas: form.disciplinas.split(","),
              }
            : u
        )
      );
    } else {
      setUsers([
        ...users,
        {
          id: `T00${users.length + 1}`,
          nome: form.nome,
          email: form.email,
          disciplinas: form.disciplinas.split(","),
          biometria: false,
        },
      ]);
    }

    setModalOpen(false);
  }

  function removeUser(id) {
    if (confirm("Deseja remover este usuário?")) {
      setUsers(users.filter((u) => u.id !== id));
    }
  }

  return (
    <>
      <div className="table-wrapper">
        <div className="table-header">
          <h3>Alunos</h3>
          <button className="btn-primary" onClick={openNewUser}>
            Registar nova presença
          </button>
        </div>

        <table className="admin-table">
          <thead>
            <tr>
              <th>Nome</th>
              <th>ID</th>
              <th>Nº</th>
              <th>Disciplinas</th>
              <th>Biometria</th>
              <th>Ações</th>
            </tr>
          </thead>

          <tbody>
            {users.map((u) => (
              <tr key={u.id}>
                <td>{u.nome}</td>
                <td>{u.id}</td>
                <td>{u.email}</td>
                <td>
                  <div className="tags">
                    {u.disciplinas.map((d, i) => (
                      <span key={i} className="tag">
                        {d}
                      </span>
                    ))}
                  </div>
                </td>
                <td className="center-icon">
                  {u.biometria && <CircleCheck className="ok" />}
                </td>
                <td className="actions">
                  <button onClick={() => openEdit(u)}>
                    <Pencil />
                  </button>
                  <button onClick={() => removeUser(u.id)}>
                    <Trash2 />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {modalOpen && (
        <div className="modal-overlay">
          <div className="modal">
            <header>
              <h4>{editingUser ? "Editar Usuário" : "Novo Usuário"}</h4>
              <button onClick={() => setModalOpen(false)}>
                <X />
              </button>
            </header>

            <input
              placeholder="Nome"
              value={form.nome}
              onChange={(e) => setForm({ ...form, nome: e.target.value })}
            />

            <input
              placeholder="Email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
            />

            <input
              placeholder="Disciplinas (separadas por vírgula)"
              value={form.disciplinas}
              onChange={(e) =>
                setForm({ ...form, disciplinas: e.target.value })
              }
            />

            <button className="btn-primary" onClick={saveUser}>
              Salvar
            </button>
          </div>
        </div>
      )}
    </>
  );
}
