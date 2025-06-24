import requests
from urllib.parse import urljoin
from behave import given, when, then

@given('la aplicación está corriendo')
def step_impl(context):
    # podrías incluso verificar que el servidor responda
    response = requests.get(context.base_url)
    assert response.status_code == 200

@when('ingreso usuario "{correo}" y contraseña "{password}"')
def step_impl(context, correo, password):
    url = urljoin(context.base_url, '/login')
    data = {'correo': correo, 'password': password}
    response = requests.post(url, data=data, allow_redirects=True)
    context.response = response

@then('debería ser redirigido al dashboard del usuario')
def step_impl(context):
    final_url = context.response.url
    assert '/dashDocente' in final_url or '/dashEstudiante' in final_url