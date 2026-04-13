from flask import Blueprint, request, jsonify
from config import API_KEY_VALOR
from services.arduino_service import registrar_presenca

arduino_bp = Blueprint("arduino_bp", __name__)

@arduino_bp.route("/api/arduino/presenca", methods=["POST"])
def receber_presenca():

    dados = request.get_json()  # pega os dados enviados como JSON

    api_key = dados.get("api_key")
    id_aluno = dados.get("id_aluno")
    id_aula = dados.get("id_aula")
    hora_entrada = dados.get("hora")
    tipo = dados.get("tipo")

     # ================= DEBUG =================
    print("API KEY RECEBIDA:", api_key)
    print("API KEY ESPERADA:", API_KEY_VALOR)
    # ========================================
    if api_key != API_KEY_VALOR:
        return jsonify({"erro": "Chave API inválida"}), 403

    print("-" * 40)
    print("NOVA PRESENÇA VIA ARDUINO")
    print(f"Aluno: {id_aluno}")
    print(f"Aula: {id_aula}")
    print(f"Hora: {hora_entrada}")
    print("-" * 40)

    sucesso = registrar_presenca(
        id_aluno,
        id_aula,
        hora_entrada,
        tipo
    )

    if sucesso:
        return jsonify({"mensagem": "Presença registrada com sucesso"}), 200
    else:
        return jsonify({"erro": "Erro ao registrar presença"}), 500