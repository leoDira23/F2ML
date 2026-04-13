from database import db

class Turma(db.Model):
    __tablename__ = 'turma'

    id_turma = db.Column(db.Integer, primary_key=True)
    nome_turma = db.Column(db.String(100), nullable=False)
    ano_letivo = db.Column(db.String(20), nullable=False)
    turno = db.Column(db.String(20), nullable=False)
    id_curso = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id_turma": self.id_turma,
            "nome_turma": self.nome_turma,
            "ano_letivo": self.ano_letivo,
            "turno": self.turno,
            "id_curso": self.id_curso
        }
