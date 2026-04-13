from flask import Flask
from flask_cors import CORS
from database import db

# Blueprints
from routes.alunos import alunos_bp
from routes.arduino_routes import arduino_bp
from routes.professores import professores_bp
from routes.turmas import turmas_bp
from routes.cursos import cursos_bp
from routes.presencas import presencas_bp
from routes.aulas import aulas_bp
from routes.disciplinas import disciplinas_bp
from routes.usuarios import usuarios_bp
from routes.relatorios import relatorios_bp
from routes.justificativas import justificativas_bp
from login import login_bp
from routes.auth import auth_bp
from routes.biometria import biometria_bp

app = Flask(__name__)

# =========================
# CORS CORRIGIDO (VITE)
# =========================
CORS(
    app,
    supports_credentials=True,
    resources={r"/*": {"origins": ["http://localhost:5173"]}},
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
)

# =========================
# CONFIG BANCO DE DADOS
# =========================
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/sistema_presenca"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# =========================
# ROTAS
# =========================
@app.route("/")
def home():
    return {"mensagem": "API está a funcionar!"}

app.register_blueprint(arduino_bp)
app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(presencas_bp)
app.register_blueprint(aulas_bp)
app.register_blueprint(disciplinas_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(relatorios_bp)
app.register_blueprint(justificativas_bp)
app.register_blueprint(login_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(biometria_bp)

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)