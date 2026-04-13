from database import db

class Curso(db.Model):
    __tablename__ = "curso"

    id_curso = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)

    def to_dict(self):
        return {
            "id_curso": self.id_curso,
            "nome_curso": self.nome_curso,
            "descricao": self.descricao
        }
