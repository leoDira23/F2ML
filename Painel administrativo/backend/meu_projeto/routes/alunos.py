from flask import Blueprint, request, jsonify
from database import db
from models.aluno import Aluno
from sqlalchemy.exc import IntegrityError
from routes.auth import rota_protegida
from validations.validators import campo_obrigatorio, nome_completo_valido, apenas_numeros, data_valida

alunos_bp = Blueprint("alunos", __name__)

# ============================
# LISTAR ALUNOS
# ============================
@alunos_bp.route("/alunos", methods=["GET"])
@rota_protegida(["ADMIN", "COORDENADOR", "PROFESSOR"])
def listar_alunos(usuario_logado):
    alunos = Aluno.query.all()
    return jsonify([
        {
            "id": a.id_aluno,
            "nome": a.nome,
            "numero_processo": a.numero_processo,
            "turma": a.nome_turma,
            "presente": getattr(a, "presente", False)
        } for a in alunos
    ]), 200

# ============================
# CRIAR ALUNO
# ============================
@alunos_bp.route("/alunos", methods=["POST"])
@rota_protegida(["ADMIN", "PROFESSOR", "COORDENADOR"])
def criar_aluno(usuario_logado):
    dados = request.get_json()

  
    for campo in ["nome", "numero_processo", "id_turma"]:
        if not campo_obrigatorio(dados.get(campo)):
            return {"erro": f"O campo '{campo}' é obrigatório."}, 400

    if not nome_completo_valido(dados["nome"]):
        return {"erro": "Nome inválido."}, 400
    if not apenas_numeros(dados["numero_processo"]):
        return {"erro": "Número de processo deve conter apenas números."}, 400
    if not isinstance(dados["nome_turma"], int):
        return {"erro": "ID da turma inválido."}, 400

    aluno = Aluno(
        nome=dados["nome"].strip(),
        numero_processo=dados["numero_processo"].strip(),
        nome_turma=dados["nome_turma"]
    )

    try:
        db.session.add(aluno)
        db.session.commit()
        return {"mensagem": "Aluno criado com sucesso", "id": aluno.id_aluno}, 201
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Erro ao criar aluno (possível duplicidade)."}, 400

# ============================
# ATUALIZAR ALUNO
# ============================
@alunos_bp.route("/alunos/<int:id>", methods=["PUT"])
@rota_protegida(["ADMIN", "PRODESSOR", "COORDENADOR"])
def atualizar_aluno(usuario_logado, id):
    aluno = Aluno.query.get_or_404(id)
    dados = request.get_json()

    if "nome" in dados:
        if not nome_completo_valido(dados["nome"]):
            return {"erro": "Nome inválido."}, 400
        aluno.nome = dados["nome"].strip()
    if "numero_processo" in dados:
        if not apenas_numeros(dados["numero_processo"]):
            return {"erro": "Número de processo inválido."}, 400
        aluno.numero_processo = dados["numero_processo"].strip()
    if "nome_turma" in dados:
        if not isinstance(dados["nome_turma"], int):
            return {"erro": "ID da turma inválido."}, 400
        aluno.nome_turma = dados["nome_turma"]

    db.session.commit()
    return {"mensagem": "Aluno atualizado com sucesso"}

# ============================
# DELETAR ALUNO
# ============================
@alunos_bp.route("/alunos/<int:id>", methods=["DELETE"])
@rota_protegida(["ADMIN"])
def apagar_aluno(usuario_logado, id):
    aluno = Aluno.query.get_or_404(id)
    try:
        db.session.delete(aluno)
        db.session.commit()
        return {"mensagem": "Aluno removido com sucesso"}
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Não foi possível apagar este aluno."}, 400