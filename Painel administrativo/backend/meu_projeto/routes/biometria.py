from flask import Blueprint, request, jsonify
from services.presenca_service import registar_presenca_com_biometria

biometria_bp = Blueprint("biometria", __name__)

@biometria_bp.route("/biometria/presenca", methods=["POST"])
def biometria_presenca():
    dados = request.get_json()

    dispositivo_id = dados.get("dispositivo_id")
    template = dados.get("template")
    tipo_biometria = dados.get("tipo")

    if not dispositivo_id:
        return {"erro": "Dispositivo não identificado"}, 400

    if not template or not tipo_biometria:
        return {"erro": "Dados biométricos incompletos"}, 400

    resultado = registar_presenca_com_biometria(
        template=template,
        tipo_biometria=tipo_biometria,
        dispositivo_id=dispositivo_id
    )

    return jsonify(resultado), 200 if resultado["sucesso"] else 401

@biometria_bp.route("/biometria/cadastrar-teste", methods=["POST"])
def cadastrar_biometria_teste():

    from models.biometria import Biometria
    from database import db
    import base64

    dados = request.get_json()
    template_base64 = dados.get("template")

    if not template_base64:
        return {"erro": "Template obrigatório"}, 400

    template_bytes = base64.b64decode(template_base64)

    biometria = Biometria(
        pessoa_tipo="ALUNO",
        pessoa_id=1,  # ID de teste
        tipo="DIGITAL",
        template=template_bytes,
        ativo=True
    )

    db.session.add(biometria)
    db.session.commit()

    return {"msg": "Biometria de teste cadastrada com sucesso"}