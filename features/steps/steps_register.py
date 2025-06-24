import requests
from urllib.parse import urljoin
from behave import given, when, then

@given('la aplicacion esta en ejecucion')
def step_impl(context):

    response = requests.get(context.base_url)
    assert response.status_code == 200

@when('ingreso nombre "{nombre}" apellido "{apellido}" correo "{correo}" y contraseña "{contrasena}"')
def step_impl(context, nombre, apellido, correo, contrasena):
    url = urljoin(context.base_url, '/registersupervisor')
    data = {
        'nombres': nombre,
        'apellidos': apellido,
        'correo': correo,
        'password': contrasena
    }
    response = requests.post(url, data=data, allow_redirects=True)
    context.response = response

@then('debería ser redirigido a la página de inicio de sesión')
def step_impl(context):
    final_url = context.response.url
    print(">>> Status code:", context.response.status_code)
    print(">>> Final URL:", context.response.url)
    print(">>> Headers:", context.response.headers)
    print(">>> Body:", context.response.text)
    assert 'http://localhost:3000/login' in final_url