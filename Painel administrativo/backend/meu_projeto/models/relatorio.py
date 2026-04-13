from database import db
from datetime import datetime

class Relatorio(db.Model):
    __tablename__ = "relatorios"

    id_relatorio = db.Column(db.Integer, primary_key=True, autoincrement=True)

    tipo_relatorio = db.Column(db.String(50), nullable=False)

    periodo_inicio = db.Column(db.Date, nullable=False)
    periodo_fim = db.Column(db.Date, nullable=False)

    gerado_por = db.Column(db.Integer, nullable=True)

    caminho_arquivo = db.Column(db.String(255), nullable=True)

    data_geracao = db.Column(db.DateTime, default=datetime.now)
