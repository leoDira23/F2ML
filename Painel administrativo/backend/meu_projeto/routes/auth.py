import os
from functools import wraps
from flask import request, jsonify, Blueprint
from models.usuario import UsuarioSistema
from database import db
import jwt

# 🔹 Chave segura de 32 caracteres ou mais
JWT_SECRET = os.environ.get(
    "JWT_SECRET",
    "Lk9fGh3XvP8s2k1Qz9aRmT6bJ4eY7uW0"  # chave padrão, 32 chars
)
JWT_ALGORITHM = "HS256"

auth_bp = Blueprint("auth", __name__)

# 🔹 Função para pegar usuário logado
def get_usuario_logado():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        usuario = db.session.get(UsuarioSistema, payload["id_usuario"])
        return usuario
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# 🔹 Decorator para proteger rotas
def rota_protegida(cargos_permitidos=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            usuario = get_usuario_logado()
            if not usuario:
                return jsonify({"erro": "Não autenticado"}), 401
            if cargos_permitidos and usuario.cargo.upper() not in [c.upper() for c in cargos_permitidos]:
                return jsonify({"erro": "Sem permissão"}), 403
            return func(usuario, *args, **kwargs)
        return wrapper
    return decorator