from datetime import datetime, timedelta
import os
from flask import Flask, make_response, render_template
from flask_login import LoginManager
from DBManager import db, init_app
from basedatos.modelos import Supervisor, Estudiante
from logging.config import dictConfig 
from login.login import login_bp
from supervisor.supervisor import supervisor_bp
from estudiante.estudiante import estudiante_bp

from utility import procesar_archivo_csv, calcular_calificacion, verify_supervisor, verify_ayudante, verify_estudiante


dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errores.log',
            'formatter': 'default',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',  # Puedes ajustar este nivel según tus necesidades
            'propagate': True,
        },
    },
})


# inicializar la aplicacion
app = Flask(__name__)
init_app(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login'  # Nombre de la vista para iniciar sesión

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=120)

# Ruta donde se guardan los archivos subidos para los ejercicios
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'md', 'xml', 'csv', 'png', 'jpg', 'jpeg'}

# Encuentra la ruta del directorio del archivo actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define la ruta UPLOAD_FOLDER en relación a ese directorio
UPLOAD_FOLDER = os.path.join(current_directory, "uploads")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Blueprints rutas


@login_manager.user_loader
def load_user(user_id):
    if user_id.startswith("e"):
        user = db.session.get(Estudiante, int(user_id[1:]))
    elif user_id.startswith("s"):
        user = db.session.get(Supervisor, int(user_id[1:]))
    else:
        return None

    return user


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('inicio.html')


app.register_blueprint(supervisor_bp)
app.register_blueprint(estudiante_bp)
app.register_blueprint(login_bp)


# Funcion para ejecutar el script 404
def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    # return redirect(url_for('index')) #te devuelve a esa página


# Ruta para ejecutar el script
if __name__ == '__main__':
    # app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', debug=True, port=3000)
    debug = True
