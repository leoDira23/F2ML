from flask import Blueprint, request, jsonify
from database import db
from models.usuario import UsuarioSistema
from flask_cors import cross_origin
import datetime
import jwt
from routes.auth import JWT_SECRET, JWT_ALGORITHM
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route("/login", methods=["POST"])
@cross_origin()
def login():
    dados = request.get_json()
    if not dados:
        return jsonify({"status": "error", "mensagem": "Nenhum dado recebido"}), 400

    email = dados.get("email", "").strip().lower()
    senha = dados.get("senha", "").strip()
    print(f"[login] Tentativa de login - Email: '{email}'")

    if not email or not senha:
        return jsonify({"status": "error", "mensagem": "Email e senha obrigatórios"}), 400

    usuario = UsuarioSistema.query.filter_by(email=email).first()
    if not usuario:
        print(f"[login] Usuário não encontrado para email: {email}")
        return jsonify({"status": "error", "mensagem": "Email ou senha inválidos"}), 401

    if not check_password_hash(usuario.senha_hash, senha):
        print(f"[login] Senha incorreta para email: {email}")
        return jsonify({"status": "error", "mensagem": "Email ou senha inválidos"}), 401

    try:
        payload = {
            "id_usuario": usuario.id_usuario,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        print("[login] Token gerado:", token)
    except Exception as e:
        print("[login] Erro ao gerar token:", e)
        return jsonify({"status": "error", "mensagem": "Erro ao gerar token"}), 500

    return jsonify({
        "status": "ok",
        "token": token,
        "usuario": {
            "email": usuario.email,
            "cargo": usuario.cargo,
            "nome": usuario.nome
        }
    }), 200