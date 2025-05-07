from datetime import datetime, timedelta
import os, shutil
from sqlite3 import IntegrityError
from click import DateTime
from flask import Flask, make_response, render_template, request, url_for, redirect, jsonify, session, flash, current_app
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from wtforms import FileField, SubmitField, PasswordField, StringField, DateField, BooleanField, validators, FileField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired, Length, ValidationError
from funciones_archivo.manejoArchivosJava import eliminarPackages, agregarPackage
from funciones_archivo.manejoCarpetas import agregarCarpetaSerieEstudiante,crearCarpetaSerie, crearCarpetaEjercicio, crearArchivadorEstudiante, agregarCarpetaEjercicioEstudiante
from funciones_archivo.manejoMaven import ejecutarTestUnitario
from werkzeug.security import check_password_hash, generate_password_hash, check_password_hash
from DBManager import db, init_app
from basedatos.modelos import Supervisor, Grupo, Serie, Estudiante, Ejercicio, Ejercicio_asignado, Curso, serie_asignada, inscripciones, estudiantes_grupos, supervisores_grupos
from pathlib import Path
import markdown
import csv
import logging
from logging.config import dictConfig
from ansi2html import Ansi2HTMLConverter
import json
from login.login import login_bp
from supervisor.supervisor import supervisor_bp

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


#inicializar la aplicacion
app = Flask(__name__)
init_app(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.l'  # Nombre de la vista para iniciar sesión

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=120)

UPLOAD_FOLDER = 'uploads' #Ruta donde se guardan los archivos subidos para los ejercicios
ALLOWED_EXTENSIONS = {'md','xml','csv','png','jpg', 'jpeg'}

# Encuentra la ruta del directorio del archivo actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define la ruta UPLOAD_FOLDER en relación a ese directorio
UPLOAD_FOLDER = os.path.join(current_directory, "uploads")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Blueprints rutas

app.register_blueprint(login_bp)
app.register_blueprint(supervisor_bp)

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



#Funcion para ejecutar el script 404
def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    #return redirect(url_for('index')) #te devuelve a esa página

#Ruta para ejecutar el script
if __name__ == '__main__':
    #app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0',debug=True, port=3000)
    debug=True
