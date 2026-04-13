from flask import Blueprint, request, jsonify
from database import db
from models.justificativa import Justificativa

justificativas_bp = Blueprint('justificativas', __name__)

@justificativas_bp.route('/justificativas', methods=['POST'])
def criar_justificativa():
    data = request.json

    j = Justificativa(
        id_presenca=data.get("id_presenca"),
        motivo=data.get("motivo"),
        documento=data.get("documento")
    )

    db.session.add(j)
    db.session.commit()

    return jsonify({"message": "Justificativa enviada", "id": j.id_justificativa}), 201


@justificativas_bp.route('/justificativas', methods=['GET'])
def listar_justificativas():
    js = Justificativa.query.all()

    lista = []
    for j in js:
        lista.append({
            "id": j.id_justificativa,
            "motivo": j.motivo,
            "status": j.status_aprovacao
        })

    return jsonify(lista), 200
