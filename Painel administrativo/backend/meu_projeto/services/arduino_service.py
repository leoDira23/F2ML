# services/arduino_service.py

from database import db
from datetime import datetime
from sqlalchemy import text  # <- importante para SQL raw

def registrar_presenca(id_aluno, id_aula, hora_entrada, tipo):
    """
    Registra a presença de um aluno ou professor no banco de dados usando SQLAlchemy.
    """
    metodo = "Digital"
    status = "Presente"
    data_registro = datetime.now().date()

    tabela = "presenca_professor" if tipo == "professor" else "presenca"

    try:
        # SQL RAW precisa de text()
        sql = text(f"""
        INSERT INTO {tabela}
        (id_aluno, id_aula, data_registro, status, metodo, hora_entrada, hora_saida)
        VALUES (:id_aluno, :id_aula, :data_registro, :status, :metodo, :hora_entrada, :hora_saida)
        """)

        valores = {
            "id_aluno": id_aluno,
            "id_aula": id_aula,
            "data_registro": data_registro,
            "status": status,
            "metodo": metodo,
            "hora_entrada": hora_entrada,
            "hora_saida": None
        }

        db.session.execute(sql, valores)
        db.session.commit()
        return True

    except Exception as erro:
        print("ERRO AO INSERIR PRESENÇA:", erro)
        db.session.rollback()
        return False