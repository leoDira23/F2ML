from flask import Blueprint, jsonify, request
from database import db
from models.aula import Aula

aulas_bp = Blueprint('aulas', __name__)


@aulas_bp.route('/aulas', methods=['GET'])
def listar_aulas():
    aulas = Aula.query.all()
    return jsonify([a.to_dict() for a in aulas])



@aulas_bp.route('/aulas', methods=['POST'])
def criar_aula():
    dados = request.json

    nova_aula = Aula(
        id_turma=dados["id_turma"],
        id_disciplina=dados["id_disciplina"],
        data=dados["data_aula"],
        hora_inicio=dados["hora_inicio"],
        hora_fim=dados["hora_fim"]
    )

    db.session.add(nova_aula)
    db.session.commit()

    return jsonify({"mensagem": "Aula criada com sucesso", "aula": nova_aula.to_dict()})



@aulas_bp.route('/aulas/<int:id_aula>', methods=['GET'])
def obter_aula(id_aula):
    aula = Aula.query.get_or_404(id_aula)
    return jsonify(aula.to_dict())


@aulas_bp.route('/aulas/<int:id_aula>', methods=['PUT'])
def atualizar_aula(id_aula):
    aula = Aula.query.get_or_404(id_aula)
    dados = request.json

    aula.id_turma = dados.get("id_turma", aula.id_turma)
    aula.id_disciplina = dados.get("id_disciplina", aula.id_disciplina)
    aula.data = dados.get("data_aula", aula.data)
    aula.hora_inicio = dados.get("hora_inicio", aula.hora_inicio)
    aula.hora_fim = dados.get("hora_fim", aula.hora_fim)

    db.session.commit()

    return jsonify({"mensagem": "Aula atualizada com sucesso", "aula": aula.to_dict()})


@aulas_bp.route('/aulas/<int:id_aula>', methods=['DELETE'])
def deletar_aula(id_aula):
    aula = Aula.query.get_or_404(id_aula)
    db.session.delete(aula)
    db.session.commit()
    return jsonify({"mensagem": "Aula removida com sucesso"})
