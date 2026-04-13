from database import db

class Aula(db.Model):
    __tablename__ = "aula"

    id = db.Column("id_aula", db.Integer, primary_key=True)
    id_turma = db.Column("id_turma", db.Integer, nullable=False)
    id_disciplina = db.Column("id_disciplina", db.Integer, nullable=False)
    data = db.Column("data_aula", db.Date, nullable=False)
    hora_inicio = db.Column("hora_inicio", db.Time, nullable=False)
    hora_fim = db.Column("hora_fim", db.Time, nullable=False)

    def to_dict(self):
        return {
            "id_aula": self.id,
            "id_turma": self.id_turma,
            "id_disciplina": self.id_disciplina,
            "data_aula": str(self.data),
            "hora_inicio": str(self.hora_inicio),
            "hora_fim": str(self.hora_fim)
        }
