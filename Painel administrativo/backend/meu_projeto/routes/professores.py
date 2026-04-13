from flask import Blueprint, request, jsonify
from database import db
from models.professor import Professor
from sqlalchemy.exc import IntegrityError
from routes.auth import rota_protegida
from werkzeug.security import generate_password_hash

# Validators centralizados
from validations.validators import email_valido, nome_completo_valido, cargo_valido, campo_obrigatorio

professores_bp = Blueprint("professores", __name__)

# ============================================================
# LISTAR PROFESSORES
# ============================================================
@professores_bp.route("/professores", methods=["GET"])
@rota_protegida(["ADMIN", "PROFESSOR", "COORDENADOR"])
def listar_professores(usuario_logado):
    professores = Professor.query.all()
    return jsonify([
        {
            "nome": p.nome,
            "email": p.email,
            "disciplina": p.disciplina_principal
        } for p in professores
    ]), 200

# ============================================================
# CRIAR PROFESSOR
# ============================================================
@professores_bp.route("/professores", methods=["POST"])
@rota_protegida(["ADMIN", "PROFESSOR", "COORDENADOR"])
def criar_professor(usuario_logado):
    dados = request.get_json()

    # Campos obrigatórios
    for campo in ["nome", "email", "senha", "disciplina_principal"]:
        if not campo_obrigatorio(dados.get(campo)):
            return {"erro": f"O campo '{campo}' é obrigatório."}, 400

    if not nome_completo_valido(dados["nome"]):
        return {"erro": "Nome inválido."}, 400
    if not email_valido(dados["email"]):
        return {"erro": "Email inválido."}, 400

    senha_hash = generate_password_hash(dados["senha"])
    professor = Professor(
        nome=dados["nome"].strip(),
        email=dados["email"].strip().lower(),
        senha_hash=senha_hash,
        disciplina_principal=dados["disciplina_principal"].strip(),
        tipo_usuario=dados.get("tipo_usuario", "PROFESSOR").strip().upper()
    )

    try:
        db.session.add(professor)
        db.session.commit()
        return {"mensagem": "Professor criado com sucesso", "id_professor": professor.id_professor}, 201
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Email já cadastrado."}, 400

# ============================================================
# ATUALIZAR PROFESSOR
# ============================================================
@professores_bp.route("/professores/<int:id>", methods=["PUT"])
@rota_protegida(["ADMIN", "PROFESSOR", "COORDENADOR"])
def atualizar_professor(usuario_logado, id):
    professor = Professor.query.get_or_404(id)
    dados = request.get_json()

    if "nome" in dados:
        if not nome_completo_valido(dados["nome"]):
            return {"erro": "Nome inválido."}, 400
        professor.nome = dados["nome"].strip()

    if "email" in dados:
        if not email_valido(dados["email"]):
            return {"erro": "Email inválido."}, 400
        professor.email = dados["email"].strip().lower()

    if "tipo_usuario" in dados:
        if not cargo_valido(dados["tipo_usuario"]):
            return {"erro": "Tipo de usuário inválido."}, 400
        professor.tipo_usuario = dados["tipo_usuario"].strip().upper()

    if "disciplina_principal" in dados:
        professor.disciplina_principal = dados["disciplina_principal"].strip()

    try:
        db.session.commit()
        return {"mensagem": "Professor atualizado com sucesso", "id": professor.id_professor}
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Email já cadastrado."}, 400

# ============================================================
# DELETAR PROFESSOR
# ============================================================
@professores_bp.route("/professores/<int:id>", methods=["DELETE"])
@rota_protegida(["ADMIN", "COORDENADOR"])
def apagar_professor(usuario_logado, id):
    professor = Professor.query.get_or_404(id)

    try:
        db.session.delete(professor)
        db.session.commit()
        return {"mensagem": "Professor removido com sucesso"}
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Não é possível apagar este professor: existem vínculos."}, 400