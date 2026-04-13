from flask import Blueprint, request, jsonify
from database import db
from models.usuario import UsuarioSistema
from sqlalchemy.exc import IntegrityError
from validations.validators import senha_valida
from routes.auth import rota_protegida
from werkzeug.security import generate_password_hash  # <<< IMPORTAR

# Validators centralizados
from validations.validators import (
    email_valido,
    nome_completo_valido,
    campo_obrigatorio,
    senha_valida,
    cargo_valido
    
)

usuarios_bp = Blueprint("usuarios", __name__)

# ============================================================
# LISTAR USUÁRIOS DO SISTEMA (SÓ ADMIN)
# ============================================================

@usuarios_bp.route("/usuarios", methods=["GET"])
@rota_protegida(["ADMIN"])
def listar_usuarios(usuario_logado):
    usuarios = UsuarioSistema.query.all()
    return jsonify([
        {
            "nome":  u.nome,
            "email": u.email,
            "cargo": u.cargo,
            "status": u.status
        }
        for u in usuarios
    ]), 200

# ============================================================
# POST - criar usuário (SÓ ADMIN)
# ============================================================

@usuarios_bp.route("/usuarios", methods=["POST"])
@rota_protegida(["ADMIN"])
def criar_usuario(usuario_logado):
    dados = request.get_json()

    # Campos obrigatórios
    for campo in ["nome", "email", "senha", "cargo"]:
        if not campo_obrigatorio(dados.get(campo)):
            return {"erro": f"O campo '{campo}' é obrigatório."}, 400

    # Valida dados
    if not nome_completo_valido(dados["nome"]):
        return {"erro": "Informe o nome completo."}, 400
    if not email_valido(dados["email"]):
        return {"erro": "Email inválido."}, 400
    if not senha_valida(dados["senha"]):
        return {"erro": "Senha inválida. Deve conter entre 8 e 20 caracteres e ter letras e números."}, 400
    if not cargo_valido(dados["cargo"]):
        return {"erro": "Cargo inválido."}, 400

    status_inicial = "ATIVO" if dados["cargo"].strip().upper() == "ADMIN" else "INATIVO"

    usuario = UsuarioSistema(
        nome=dados["nome"].strip(),
        email=dados["email"].strip().lower(),
        cargo=dados["cargo"].strip().upper(),
        status=status_inicial
    )

    # 🔒 Hash pelo model
    usuario.set_senha(dados["senha"])

    try:
        db.session.add(usuario)
        db.session.commit()
        return {"mensagem": "Usuário criado com sucesso", "id": usuario.id_usuario}, 201
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Email já cadastrado."}, 400

# ============================================================
# PUT - atualizar usuário (SÓ ADMIN)
# ============================================================

@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
@rota_protegida(["ADMIN"])
def atualizar_usuario(usuario_logado, id):
    usuario = UsuarioSistema.query.get_or_404(id)
    dados = request.get_json()

    if "nome" in dados:
        if not nome_completo_valido(dados["nome"]):
            return {"erro": "Nome inválido."}, 400
        usuario.nome = dados["nome"].strip()

    if "email" in dados:
        if not email_valido(dados["email"]):
            return {"erro": "Email inválido."}, 400
        usuario.email = dados["email"].strip().lower()

    if "cargo" in dados:
        if not cargo_valido(dados["cargo"]):
            return {"erro": "Cargo inválido."}, 400
        usuario.cargo = dados["cargo"].strip().upper()

    if "status" in dados:
        if dados["status"].upper() not in ["ATIVO", "INATIVO"]:
            return {"erro": "Status inválido."}, 400
        usuario.status = dados["status"].upper()

    try:
        db.session.commit()
        return {"mensagem": "Usuário atualizado com sucesso"}
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Email já cadastrado."}, 400

# ============================================================
# DELETE - apagar usuário (SÓ ADMIN)
# ============================================================

@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
@rota_protegida(["ADMIN"])
def apagar_usuario(usuario_logado, id):
    usuario = UsuarioSistema.query.get_or_404(id)

    try:
        db.session.delete(usuario)
        db.session.commit()
        return {"mensagem": "Usuário removido com sucesso"}
    except IntegrityError:
        db.session.rollback()
        return {"erro": "Não é possível apagar este usuário."}, 400

# ============================================================
# PUT - alterar status (SÓ ADMIN)
# ============================================================

@usuarios_bp.route("/usuarios/<int:id>/status", methods=["PUT"])
@rota_protegida(["ADMIN"])
def alterar_status(usuario_logado, id):
    dados = request.get_json()
    usuario = UsuarioSistema.query.get_or_404(id)

    if dados.get("status") not in ["ATIVO", "INATIVO"]:
        return {"erro": "Status inválido"}, 400

    usuario.status = dados["status"]
    db.session.commit()

    return {
        "mensagem": "Status alterado com sucesso",
        "alterado_por": usuario_logado.nome
    }, 200