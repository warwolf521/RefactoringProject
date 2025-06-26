import requests
from urllib.parse import urljoin
from behave import given, when, then

@given('Se tiene sesion iniciada con las credenciales correo: "{correo}" contrasena "{contrasena}" y se esta dashboard de "{rol}"')
def step_impl(context,correo,contrasena, rol):
    url = urljoin(context.base_url,'/login')
    data = {
        'correo' : correo,
        'password' : contrasena
    }
    response = requests.post(url,data = data,allow_redirects=True)
    context.response = response
    context.rol = rol
    assert response.status_code == 200

@when('Se actualiza la contrasena antigua "{antigua}" y la nueva contrasena "{nueva}" y esta esta se confirma')
def step_impl(context, nueva, antigua):
    if context.rol == 'Docente':
        url = context.response.url + '/cuentaDocente'
    else:
        url = context.response.url + '/cuentaEstudiante'
    response = requests.get(url)
    data = {
        'contraseña_actual': antigua,
        'nueva_contraseña': nueva,
        'confirmar_nueva_contraseña':nueva
    }
    response = requests.post(url,data,allow_redirects=True)

    context.response = response

@then('la contrasena del usuario es actualizada')
def step_impl(context):
    assert context.response.status_code == 200

