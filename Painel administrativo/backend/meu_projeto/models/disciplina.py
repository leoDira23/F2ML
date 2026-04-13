from database import db

class Disciplina(db.Model):
    __tablename__ = "disciplina"

    id_disciplina = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_disciplina = db.Column(db.String(100), nullable=False)
    carga_horaria = db.Column(db.Integer)

    id_professor = db.Column(
        db.Integer,
        db.ForeignKey("professor.id_professor"),
        nullable=True
    )

    id_curso = db.Column(
        db.Integer,
        db.ForeignKey("curso.id_curso"),
        nullable=True
    )

    def to_dict(self):
        return {
            "id_disciplina": self.id_disciplina,
            "nome_disciplina": self.nome_disciplina,
            "carga_horaria": self.carga_horaria,
            "id_professor": self.id_professor,
            "id_curso": self.id_curso
        }
