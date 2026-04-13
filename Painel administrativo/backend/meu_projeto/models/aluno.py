from database import db

class Aluno(db.Model):
    __tablename__ = "aluno"

    id_aluno = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero_processo = db.Column(db.String(20), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date)
    id_turma = db.Column(db.Integer, db.ForeignKey("turma.id_turma"))
    id_curso = db.Column(db.Integer, db.ForeignKey("curso.id_curso"))

