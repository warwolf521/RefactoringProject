import requests
from urllib.parse import urljoin
from behave import given, when, then

@given('la aplicacion esta en ejecucion 2')
def step_impl(context):

    response = requests.get(context.base_url)
    assert response.status_code == 200

@when('ingreso nombre "{nombre}" apellido "{apellido}" correo "{correo}" y contraseña "{contrasena}" por error')
def step_impl(context, nombre, apellido, correo, contrasena):
    url = urljoin(context.base_url, '/registersupervisor')
    if nombre == "<vacio>":
        nombre = ""
    data = {
        'nombres': nombre,
        'apellidos': apellido,
        'correo': correo,
        'password': contrasena
    }
    response = requests.post(url, data=data, allow_redirects=True)
    context.response = response

@then('aparece un mensaje de error')
def step_impl(context):
    body = context.response.text
    assert 'Todos los campos son requeridos.' in body