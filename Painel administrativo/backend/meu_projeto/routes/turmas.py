from flask import Blueprint, jsonify, request
from database import db
from models.turma import Turma

turmas_bp = Blueprint('turmas', __name__)

# 🔹 GET - listar turmas
@turmas_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([t.to_dict() for t in turmas])


# 🔹 POST - criar turma
@turmas_bp.route('/turmas', methods=['POST'])
def criar_turma():
    data = request.json

    turma = Turma(
        nome_turma=data.get("nome_turma"),
        ano_letivo=data.get("ano_letivo"),
        turno=data.get("turno"),
        id_curso=data.get("id_curso")
    )

    db.session.add(turma)
    db.session.commit()

    return {
        "mensagem": "Turma criada com sucesso",
        "id_turma": turma.id_turma
    }, 201

# 🔹 PUT - atualizar turma
@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    turma = Turma.query.get(id)

    if not turma:
        return {"mensagem": "Turma não encontrada"}, 404

    data = request.json

    turma.nome_turma = data.get("nome_turma", turma.nome_turma)
    turma.ano_letivo = data.get("ano_letivo", turma.ano_letivo)
    turma.turno = data.get("turno", turma.turno)
    turma.id_curso = data.get("id_curso", turma.id_curso)

    db.session.commit()

    return {"mensagem": "Turma atualizada com sucesso"}, 200



# 🔹 DELETE - apagar turma
@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def apagar_turma(id):
    turma = Turma.query.get(id)

    if not turma:
        return jsonify({"mensagem": "Turma não encontrada"}), 404

    db.session.delete(turma)
    db.session.commit()

    return jsonify({"mensagem": "Turma apagada"}), 200
