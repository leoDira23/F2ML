from database import db
from flask import Blueprint, request, send_file
from routes.auth import rota_protegida
from services.relatorios_service import (
    gerar_relatorio_alunos,
    gerar_relatorio_professores
)

relatorios_bp = Blueprint("relatorios", __name__)


@relatorios_bp.route("/relatorios/alunos", methods=["POST"])
@rota_protegida(["ADMIN", "PROFESSOR"])
def relatorio_alunos(usuario_logado):

    dados = request.get_json()
    data_inicio = dados.get("data_inicio")
    data_fim = dados.get("data_fim")

    caminho = gerar_relatorio_alunos(data_inicio, data_fim, usuario_logado.id_usuario)


    return send_file(caminho, as_attachment=True)


@relatorios_bp.route("/relatorios/professores", methods=["POST"])
@rota_protegida(["ADMIN", "COORDENADOR"])
def relatorio_professores(usuario_logado):

    dados = request.get_json()
    data_inicio = dados.get("data_inicio")
    data_fim = dados.get("data_fim")

    caminho = gerar_relatorio_professores(data_inicio, data_fim, usuario_logado.id_usuario)

    return send_file(caminho, as_attachment=True)
