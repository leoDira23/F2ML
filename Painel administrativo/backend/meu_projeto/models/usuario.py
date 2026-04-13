from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioSistema(db.Model):
    __tablename__ = "usuarios_sistema"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(512), nullable=False)
    cargo = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default="ativo")

    def set_senha(self, senha):
        print("SET_SENHA FOI CHAMADO")
        hash_gerado = generate_password_hash(senha.strip())
        print("HASH GERADO:", hash_gerado)
        self.senha_hash = hash_gerado

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha.strip())

