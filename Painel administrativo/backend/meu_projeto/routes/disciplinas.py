from flask import Blueprint, request, jsonify
from database import db
from models.disciplina import Disciplina

disciplinas_bp = Blueprint("disciplinas", __name__)


@disciplinas_bp.route("/disciplinas", methods=["GET"])
def listar_disciplinas():
    disciplinas = Disciplina.query.all()
    return jsonify([d.to_dict() for d in disciplinas])


@disciplinas_bp.route("/disciplinas", methods=["POST"])
def criar_disciplina():
    dados = request.json

    nova = Disciplina(
        nome_disciplina=dados.get("nome_disciplina"),
        carga_horaria=dados.get("carga_horaria"),
        id_professor=dados.get("id_professor"),
        id_curso=dados.get("id_curso")
    )

    db.session.add(nova)
    db.session.commit()

    return jsonify({"mensagem": "Disciplina criada com sucesso!"}), 201


@disciplinas_bp.route("/disciplinas/<int:id_disciplina>", methods=["GET"])
def obter_disciplina(id_disciplina):
    d = Disciplina.query.get_or_404(id_disciplina)
    return jsonify(d.to_dict())



@disciplinas_bp.route("/disciplinas/<int:id_disciplina>", methods=["PUT"])
def atualizar_disciplina(id_disciplina):
    d = Disciplina.query.get_or_404(id_disciplina)
    dados = request.json

    d.nome_disciplina = dados.get("nome_disciplina", d.nome_disciplina)
    d.carga_horaria = dados.get("carga_horaria", d.carga_horaria)
    d.id_professor = dados.get("id_professor", d.id_professor)
    d.id_curso = dados.get("id_curso", d.id_curso)

    db.session.commit()

    return jsonify({"mensagem": "Disciplina atualizada com sucesso!"})


@disciplinas_bp.route("/disciplinas/<int:id_disciplina>", methods=["DELETE"])
def deletar_disciplina(id_disciplina):
    d = Disciplina.query.get_or_404(id_disciplina)

    db.session.delete(d)
    db.session.commit()

    return jsonify({"mensagem": "Disciplina removida!"})
