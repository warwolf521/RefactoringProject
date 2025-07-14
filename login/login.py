from flask import Blueprint, request,flash,redirect,url_for,render_template
from flask_login import login_user, logout_user,login_required
from basedatos.modelos import Supervisor, Estudiante
from werkzeug.security import check_password_hash
login_bp = Blueprint('login',__name__)

@login_bp.route('/login', methods=['GET', 'POST'])
# funcion login
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        # Primero verifica si las credenciales son de un estudiante o un supervisor.
        estudiante = Estudiante.query.filter_by(correo=correo).first()

        # Si es estudiante y las credenciales son correctas.
        if estudiante and check_password_hash(estudiante.password, password):
            login_user(estudiante)
            flash('Has iniciado sesión exitosamente', 'success')
            return redirect(url_for('estudiante.dashEstudiante', estudiante_id=estudiante.id))

        # Si no, verifica si las credenciales son de un supervisor.
        supervisor = Supervisor.query.filter_by(correo=correo).first()

        # Si es supervisor y las credenciales son correctas.
        if supervisor and check_password_hash(supervisor.password, password):
            login_user(supervisor)
            flash('Has iniciado sesión exitosamente', 'success')
            return redirect(url_for('supervisor.dashDocente', supervisor_id=supervisor.id))

        # Si las credenciales no coinciden con ningún usuario.
        flash('Credenciales inválidas', 'danger')

    return render_template('inicio.html')


@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))