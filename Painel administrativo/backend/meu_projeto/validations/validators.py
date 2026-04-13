
import re
from datetime import datetime



# Lista de cargos válidos no sistema
# O front-end pode consumir isso através de um endpoint
CARGOS_VALIDOS = ["ADMIN", "PROFESSOR", "ALUNO"]

# Tamanho mínimo e máximo da senha
SENHA_MIN = 8
SENHA_MAX = 20



def campo_obrigatorio(valor):
    """
    Verifica se um campo foi informado corretamente.
    Remove espaços antes e depois (trim).
    """
    return valor is not None and str(valor).strip() != ""


def apenas_numeros(valor):
    """
    Verifica se o valor contém apenas números.
    Aceita int ou string numérica.
    """
    if valor is None:
        return False
    return str(valor).isdigit()


def email_valido(email):
    """
    Valida email usando Regex.
    Remove espaços e converte para minúsculas.
    """
    if not email:
        return False

    email = email.strip().lower()

    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None


def nome_completo_valido(nome):
    """
    Valida nome completo:
    - Obrigatório
    - Pelo menos dois nomes
    - Apenas letras e espaços
    """
    if not nome:
        return False

    nome = nome.strip()

    # Deve conter pelo menos nome e sobrenome
    if len(nome.split()) < 2:
        return False

    # Verifica se contém apenas letras e espaços
    for c in nome:
        if not (c.isalpha() or c.isspace()):
            return False

    return True



def valor_em_lista(valor, lista):
    """
    Verifica se o valor existe dentro de uma lista.
    Útil para enums genéricos.
    """
    return valor in lista


def cargo_valido(cargo):
    """
    Valida cargo do usuário.
    Converte para maiúsculas antes de validar.
    """
    if not cargo:
        return False

    return cargo.strip().upper() in ["ADMIN", "COORDENADOR", "PROFESSOR"]


def data_valida(data):
    """
    Valida data no formato YYYY-MM-DD.
    """
    if not data:
        return False

    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False
    



    # 🔹 Validação de senha forte
def senha_valida(senha, min_len=8, max_len=20):
    if not senha:
        return False

    senha = senha.strip()

    if len(senha) < min_len or len(senha) > max_len:
        return False

    # Pelo menos 1 letra e 1 número
    tem_letra = any(c.isalpha() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    return tem_letra and tem_numero

