# CodeBending

You need Java JRE > 21 installed and Apache Maven in your computer.

In your favorite virtual env :
`pip install -r requirements.txt`

Then to create the database :
`python .\crear_db.py`

Then to start the project :
`python .\main.py` 

Then you need to connect to http://127.0.0.1:3000/registerSupervisor to create the first supervsor account.

You can encounter an example of exercise for the platform here : https://github.com/GeoffreyHecht/FizzBuzzPasoAPaso

Important: There seems to be a problem with path management under Windows, so I recommend using Linux (or correcting the problem).

## 📋 Escenarios de prueba implementados (Behave)

A continuación se describen los escenarios implementados con Behave para validar el correcto funcionamiento del registro y login de supervisores. Cada escenario está alineado con historias de usuario reales y contempla tanto casos positivos como negativos.

---

### ✅ `features/register.feature`

**Escenario:** Registro exitoso de un supervisor  
**Descripción:**  
Este escenario verifica que un nuevo supervisor pueda registrarse exitosamente cuando se ingresan todos los campos requeridos con un formato correcto.  
**Resultado esperado:**  
El usuario es redirigido a la página de login (`/login`) luego de completar el formulario.  
**Archivo de pasos:** `steps_register.py`

---

### ❌ `features/register_error.feature`

**Escenario:** Registro fallido con datos mal formateados o incompletos  
**Descripción:**  
Se evalúa que el sistema impida el registro si falta algún campo obligatorio (nombre, apellido, correo o contraseña) o si estos no están bien formateados.  
**Resultado esperado:**  
El usuario permanece en la misma página (`/registersupervisor`) y se muestra un mensaje de error como `"Todos los campos son requeridos."`.  
**Archivo de pasos:** `steps_register_error.py`

---

### 🔐 `features/loginSupervisor.feature`

**Escenario:** Inicio de sesión del supervisor  
**Descripción:**  
Este escenario comprueba que el supervisor pueda iniciar sesión con sus credenciales correctas y sea redirigido a su dashboard. También incluye casos negativos (credenciales incorrectas).  
**Resultado esperado:**  
- Éxito: Redirección a `/dashDocente`  
- Fallo: Permanencia en `/login` con mensaje de error  
**Archivo de pasos:** `steps_login.py`

---

### 🌐 Configuración base

**Archivo:** `environment.py`  
Define la URL base donde se ejecuta la aplicación para los tests:
```python
context.base_url = "http://localhost:3000"
