import base64
from models.biometria import Biometria


def validar_biometria(template_recebido, tipo_biometria):
    """
    template_recebido -> base64 string vinda do dispositivo
    tipo_biometria -> 'DIGITAL' ou 'FACE'
    """

    try:
        # Converte Base64 para bytes
        template_bytes = base64.b64decode(template_recebido)
    except Exception:
        return {"valido": False, "erro": "Template inválido"}

    biometrias = Biometria.query.filter_by(
        tipo=tipo_biometria,
        ativo=True
    ).all()

    for bio in biometrias:
        # Comparação direta (simulada)
        if bio.template == template_bytes:
            return {
                "valido": True,
                "pessoa_tipo": bio.pessoa_tipo,
                "pessoa_id": bio.pessoa_id
            }

    return {"valido": False}