from flask import Blueprint, jsonify, request
from database import db
from models.curso import Curso

cursos_bp = Blueprint('cursos', __name__)
@cursos_bp.route("/cursos", methods=["GET"])
def listar_cursos():
    cursos = Curso.query.all()
    return jsonify([c.to_dict() for c in cursos])



@cursos_bp.route("/cursos", methods=["POST"])
def criar_curso():
    dados = request.json

    curso = Curso(
        nome_curso=dados["nome_curso"],
        descricao=dados.get("descricao")
    )

    db.session.add(curso)
    db.session.commit()

    return jsonify({"mensagem": "Curso criado com sucesso", "curso": curso.to_dict()})



@cursos_bp.route("/cursos/<int:id_curso>", methods=["GET"])
def obter_curso(id_curso):
    curso = Curso.query.get_or_404(id_curso)
    return jsonify(curso.to_dict())



@cursos_bp.route("/cursos/<int:id_curso>", methods=["PUT"])
def atualizar_curso(id_curso):
    curso = Curso.query.get_or_404(id_curso)
    dados = request.json

    curso.nome_curso = dados.get("nome_curso", curso.nome_curso)
    curso.descricao = dados.get("descricao", curso.descricao)

    db.session.commit()

    return jsonify({"mensagem": "Curso atualizado com sucesso", "curso": curso.to_dict()})



@cursos_bp.route("/cursos/<int:id_curso>", methods=["DELETE"])
def deletar_curso(id_curso):
    curso = Curso.query.get_or_404(id_curso)
    db.session.delete(curso)
    db.session.commit()
    return jsonify({"mensagem": "Curso removido com sucesso"})
