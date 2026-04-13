from database import db
from datetime import datetime

class Presenca(db.Model):
    __tablename__ = "presenca"

    id_presenca = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_aluno = db.Column(db.Integer,db.ForeignKey("aluno.id_aluno", ondelete="CASCADE"),nullable=False )

    id_aula = db.Column(db.Integer, nullable=True)

    data_registro = db.Column(db.DateTime, default=datetime.utcnow)

    status = db.Column( db.Enum("Presente", "Ausente", "Justificado"),default="Presente"
    )

    metodo = db.Column(db.Enum("Fingerprint", "Manual"), default="Fingerprint")

    hora_entrada = db.Column(db.Time, nullable=True)
    hora_saida = db.Column(db.Time, nullable=True)

    def to_dict(self):
        return {
            "id_presenca": self.id_presenca,
            "id_aluno": self.id_aluno,
            "id_aula": self.id_aula,
            "data_registro": self.data_registro,
            "status": self.status,
            "metodo": self.metodo,
            "hora_entrada": self.hora_entrada,
            "hora_saida": self.hora_saida
        }
