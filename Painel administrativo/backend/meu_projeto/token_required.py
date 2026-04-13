from functools import wraps
from flask import request, jsonify
import jwt
from routes.auth import JWT_SECRET, JWT_ALGORITHM

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"mensagem": "Token não fornecido"}), 401

        try:
            token = auth_header.split(" ")[1]
            dados = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            request.id_usuario = dados["id_usuario"]
        except jwt.ExpiredSignatureError:
            return jsonify({"mensagem": "Token expirado"}), 401
        except:
            return jsonify({"mensagem": "Token inválido"}), 401

        return f(*args, **kwargs)

    return decorated