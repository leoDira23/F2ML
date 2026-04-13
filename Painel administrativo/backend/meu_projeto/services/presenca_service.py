from datetime import datetime
from database import db
from models.presenca import Presenca
from models.presenca_professor import PresencaProfessor
from services.biometria_service import validar_biometria


def registar_presenca_com_biometria(template, tipo_biometria, dispositivo_id=None):
    """
    template -> base64
    tipo_biometria -> DIGITAL ou FACE
    dispositivo_id -> id do dispositivo biométrico
    """

    resultado_validacao = validar_biometria(
        template_recebido=template,
        tipo_biometria=tipo_biometria
    )

    if not resultado_validacao["valido"]:
        return {
            "sucesso": False,
            "erro": "Biometria não reconhecida"
        }

    # Aqui depois entra o registro de presença
    return {
        "sucesso": True,
        "pessoa_id": resultado_validacao["pessoa_id"],
        "pessoa_tipo": resultado_validacao["pessoa_tipo"],
        "dispositivo_id": dispositivo_id
    }

    # =========================
    # ALUNO
    # =========================
    if pessoa_tipo == "ALUNO":

        nova_presenca = Presenca(
            id_aluno=pessoa_id,
            data_registro=agora,
            hora_entrada=hora_atual,
            status="Presente",
            metodo="Fingerprint"
        )

        db.session.add(nova_presenca)
        db.session.commit()

        return {
            "sucesso": True,
            "tipo": "ALUNO",
            "mensagem": "Presença do aluno registada com sucesso"
        }

    # =========================
    # PROFESSOR
    # =========================
    if pessoa_tipo == "PROFESSOR":

        nova_presenca = PresencaProfessor(
            professor_id=pessoa_id,
            data_registro=agora,
            hora_entrada=hora_atual,
            status="Presente",
            metodo="Fingerprint"
        )

        db.session.add(nova_presenca)
        db.session.commit()

        return {
            "sucesso": True,
            "tipo": "PROFESSOR",
            "mensagem": "Presença do professor registada com sucesso"
        }

    return {
        "sucesso": False,
        "mensagem": "Tipo inválido"
    }
