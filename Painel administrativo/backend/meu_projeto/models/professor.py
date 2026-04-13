from database import db

class Professor(db.Model):
    __tablename__ = "professor"

    id_professor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    senha_hash = db.Column(db.String(255))
    disciplina_principal = db.Column(db.String(100))
    tipo_usuario = db.Column(db.Enum('professor', 'coordenador', 'admin'), default='professor')
    id_usuario = db.Column(db.Integer)
