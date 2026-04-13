from database import db
from datetime import datetime

class PresencaProfessor(db.Model):
    __tablename__ = "presenca_professor"

    id_presenca_prof = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_professor = db.Column(db.Integer, nullable=False)
    id_aula = db.Column(db.Integer, nullable=False)

    data_registro = db.Column(db.DateTime, default=datetime.utcnow)

    metodo = db.Column(
        db.Enum("Fingerprint", "Manual"),
        default="Fingerprint"
    )

    def to_dict(self):
        return {
            "id_presenca_prof": self.id_presenca_prof,
            "id_professor": self.id_professor,
            "id_aula": self.id_aula,
            "data_registro": self.data_registro,
            "metodo": self.metodo
        }
