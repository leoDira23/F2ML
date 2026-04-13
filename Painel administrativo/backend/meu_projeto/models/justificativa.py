from database import db
from datetime import datetime

class Justificativa(db.Model):
    __tablename__ = "justificativas"

    id_justificativa = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_presenca = db.Column(
        db.Integer,
        db.ForeignKey("presenca.id_presenca", ondelete="CASCADE"),
        nullable=False
    )

    motivo = db.Column(db.Text, nullable=False)
    documento = db.Column(db.String(255), nullable=True)

    status_aprovacao = db.Column(
        db.Enum("pendente", "aceito", "rejeitado"),
        default="pendente",
        nullable=False
    )

    data_envio = db.Column(db.DateTime, default=datetime.now)

    presenca = db.relationship(
        "Presenca",
        backref=db.backref("justificativas", lazy=True)
    )
