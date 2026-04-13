from database import db
from datetime import datetime

class Biometria(db.Model):
    __tablename__ = 'biometria'

    id = db.Column(db.Integer, primary_key=True)

    # Identifica se é aluno ou professor
    pessoa_tipo = db.Column(
        db.Enum('ALUNO', 'PROFESSOR'),
        nullable=False
    )

    # ID do aluno ou do professor
    pessoa_id = db.Column(db.Integer, nullable=False)

    # Tipo de biometria
    tipo = db.Column(
        db.Enum('DIGITAL', 'FACE'),
        nullable=False
    )

    # Template biométrico (vem do dispositivo)
    template = db.Column(db.LargeBinary, nullable=False)

    dispositivo_id = db.Column(db.Integer, nullable=True)

    ativo = db.Column(db.Boolean, default=True)

    cadastrado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
