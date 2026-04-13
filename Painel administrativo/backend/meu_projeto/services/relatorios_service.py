from database import db
import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from models.professor import Professor
from models.aluno import Aluno
from database import db
from models.presenca import Presenca
from models.presenca_professor import PresencaProfessor
from models.relatorio import Relatorio
from datetime import timedelta
from models.aula import Aula
from models.disciplina import  Disciplina
from datetime import datetime, time
# =====================================================
# FUNÇÃO AUXILIAR PARA GERAR PDF
# =====================================================

def criar_pdf(nome_arquivo, titulo, cabecalho, dados):

    caminho = f"relatorios_pdf/{nome_arquivo}"
    doc = SimpleDocTemplate(caminho, pagesize=A4)

    elementos = []
    estilos = getSampleStyleSheet()

    elementos.append(Paragraph(f"<b>{titulo}</b>", estilos["Title"]))
    elementos.append(Spacer(1, 20))

    tabela_dados = [cabecalho] + dados

    tabela = Table(tabela_dados)
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ]))

    elementos.append(tabela)
    doc.build(elementos)

    return caminho
from datetime import datetime, timedelta
# =====================================================
# RELATÓRIO ALUNOS
# =====================================================
def gerar_relatorio_alunos(data_inicio, data_fim, usuario_id):

    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
    data_fim = datetime.strptime(data_fim, "%Y-%m-%d") + timedelta(days=1)

    presencas = (
        db.session.query(
            Aluno.nome.label("aluno"),
            Disciplina.nome_disciplina.label("disciplina"),
            Presenca.data_registro,
            Presenca.status,
            Presenca.metodo
        )
        .outerjoin(Aluno, Presenca.id_aluno == Aluno.id_aluno)
        .outerjoin(Aula, Presenca.id_aula == Aula.id)
        .outerjoin(Disciplina, Aula.id_disciplina == Disciplina.id_disciplina)
        .filter(Presenca.data_registro.between(data_inicio, data_fim))
        .all()
    )
    print(presencas)


    dados_pdf = []

    if not presencas:
        dados_pdf.append([
            "Sem registros no período", "-", "-", "-", "-"
        ])
    else:
        for p in presencas:
            dados_pdf.append([
               p.aluno or "—",
                p.disciplina or "—",
                p.data_registro.strftime("%d/%m/%Y %H:%M"),
                p.status,
                p.metodo
            ])

    nome_arquivo = f"relatorio_alunos_{datetime.now().timestamp()}.pdf"

    caminho = criar_pdf(
        nome_arquivo,
        "RELATÓRIO DE PRESENÇAS - ALUNOS",
        ["Aluno", "Disciplina", "Data", "Status", "Método"],
        dados_pdf
    )

    novo_relatorio = Relatorio(
        tipo_relatorio="alunos",
        periodo_inicio=data_inicio,
        periodo_fim=data_fim,
        gerado_por=usuario_id,
        caminho_arquivo=caminho,
        data_geracao=datetime.now()
    )

    db.session.add(novo_relatorio)
    db.session.commit()

    return caminho

# =====================================================
# RELATÓRIO PROFESSORES
# =====================================================
def gerar_relatorio_professores(data_inicio, data_fim, usuario_id):
    # --- converter datas do JSON para datetime ---
    try:
        data_inicio_dt = datetime.combine(datetime.strptime(data_inicio, "%Y-%m-%d").date(), time.min)  # 00:00:00
        data_fim_dt = datetime.combine(datetime.strptime(data_fim, "%Y-%m-%d").date(), time.max)      # 23:59:59.999999
    except Exception as e:
        raise ValueError(f"Formato de data inválido: {e}")

    # --- query corrigida ---
    presencas = (
        db.session.query(
            Professor.nome.label("professor"),
            Disciplina.nome_disciplina.label("disciplina"),
            PresencaProfessor.data_registro,
            PresencaProfessor.metodo
        )
        .join(Professor, PresencaProfessor.id_professor == Professor.id_professor)
        .join(Aula, PresencaProfessor.id_aula == Aula.id)  
        .join(Disciplina, Aula.id_disciplina == Disciplina.id_disciplina)
        .filter(PresencaProfessor.data_registro.between(data_inicio_dt, data_fim_dt))
        .all()
    )
    print("PRESENCAS ENCONTRADAS:", presencas)

    # --- preparar dados para PDF ---
    dados_pdf = []

    if not presencas:
        dados_pdf.append(["Sem registros no período", "-", "-", "-"])
    else:
        for p in presencas:
            dados_pdf.append([
                p.professor,
                p.disciplina,
                p.data_registro.strftime("%d/%m/%Y %H:%M"),
                p.metodo
            ])

    # --- gerar arquivo PDF ---
    nome_arquivo = f"relatorio_professores_{datetime.now().timestamp()}.pdf"
    caminho = criar_pdf(
        nome_arquivo,
        "RELATÓRIO DE PRESENÇAS - PROFESSORES",
        ["Professor", "Disciplina", "Data", "Método"],
        dados_pdf
    )

    # --- salvar no banco ---
    novo_relatorio = Relatorio(
        tipo_relatorio="professores",
        periodo_inicio=data_inicio_dt,
        periodo_fim=data_fim_dt,
        gerado_por=usuario_id,
        caminho_arquivo=caminho,
        data_geracao=datetime.now()
    )

    db.session.add(novo_relatorio)
    db.session.commit()

    return caminho