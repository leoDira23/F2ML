from flask import Blueprint, jsonify, request
from database import db
from models.presenca import Presenca
from datetime import datetime
from routes.auth import rota_protegida

presencas_bp = Blueprint('presencas', __name__)



@presencas_bp.route("/presencas", methods=["GET"])
@rota_protegida(["ADMIN", "PROFESSOR"])
def listar_presencas():
    presencas = Presenca.query.all()
    return jsonify([p.to_dict() for p in presencas])



@presencas_bp.route("/presencas", methods=["POST"])
@rota_protegida(["ADMIN", "PROFESSOR"])
def criar_presenca(usuario_logado):
    dados = request.json

    nova = Presenca(
        aluno_id=dados["aluno_id"],
        data_registro=date.today(),
        status=dados.get("status", "presente")
    )

    db.session.add(nova)
    db.session.commit()

    return jsonify({
        "mensagem": "Presença registada com sucesso",
        "presenca": nova.to_dict()
    }), 201


@presencas_bp.route("/presencas/<int:id_presenca>", methods=["GET"])
def obter_presenca(id_presenca):
    p = Presenca.query.get_or_404(id_presenca)
    return jsonify(p.to_dict())


@presencas_bp.route("/presencas/<int:id_presenca>", methods=["PUT"])
def atualizar_presenca(id_presenca):
    p = Presenca.query.get_or_404(id_presenca)
    dados = request.json

    p.status = dados.get("status", p.status)
    p.metodo = dados.get("metodo", p.metodo)

    db.session.commit()

    return jsonify({
        "mensagem": "Presença atualizada",
        "presenca": p.to_dict()
    })



@presencas_bp.route("/presencas/<int:id_presenca>", methods=["DELETE"])
def deletar_presenca(id_presenca):
    p = Presenca.query.get_or_404(id_presenca)
    db.session.delete(p)
    db.session.commit()

    return jsonify({"mensagem": "Presença removida com sucesso"})
