from flask import Blueprint, request, jsonify
from datetime import datetime
from database import db

arduino_bp = Blueprint("arduino_bp", __name__)

API_KEY_VALOR = "tPmAT5Ab3j7F9"


@arduino_bp.route("/api/arduino/presenca", methods=["POST"])
def receber_dados():

    api_key = request.form.get("api_key")
    if api_key != API_KEY_VALOR:
        return jsonify({"erro": "Chave API inválida"}), 403

    # ==============================
    # DADOS RECEBIDOS DO ARDUINO / ESP32
    # ==============================
    id_aluno = request.form.get("id_aluno")
    id_aula = request.form.get("id_aula")
    hora_entrada = request.form.get("hora")
    tipo = request.form.get("tipo")  # aluno | professor

    metodo = "Digital"
    status = "Presente"
    data_registro = datetime.now().date()

    tabela = "presenca_professor" if tipo == "professor" else "presenca"

    # ==============================
    # LOG
    # ==============================
    print("-" * 40)
    print("NOVA PRESENÇA VIA ARDUINO")
    print(f"Tabela: {tabela}")
    print(f"ID: {id_aluno}")
    print(f"Aula: {id_aula}")
    print(f"Hora: {hora_entrada}")
    print("-" * 40)

    # ==============================
    # INSERÇÃO NO BANCO
    # ==============================
    try:
        cursor = db.cursor()

        sql = f"""
        INSERT INTO {tabela}
        (id_aluno, id_aula, data_registro, status, metodo, hora_entrada, hora_saida)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            id_aluno,
            id_aula,
            data_registro,
            status,
            metodo,
            hora_entrada,
            None
        )

        cursor.execute(sql, valores)
        db.commit()

        return jsonify({"mensagem": "Presença registrada com sucesso"}), 200

    except Exception as erro:
        print("ERRO:", erro)
        return jsonify({"erro": "Erro ao registrar presença"}), 500