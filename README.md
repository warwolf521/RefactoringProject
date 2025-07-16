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

# Escenarios de prueba implementados (Behave)

A continuación se describen los features implementadas con Behave para validar su correcto funcionamiento. Cada escenario está alineado con historias de usuario reales y contempla tanto casos positivos como negativos.

---
###  `feature 1: login`

**Escenario:** Inicio de sesión del supervisor y estudiante.  
**Descripción:** Este escenario comprueba que el supervisor y estudiante pueda iniciar sesión con sus credenciales correctas y sea redirigido a su dashboard correspondiente. También incluye casos negativos (credenciales incorrectas).  
**Resultado esperado:**  
- Éxito: Redirección a `/dashDocente` o `/dashEstudiante`  
- Fallo: Permanencia en `/login` 
**Archivo de pasos:** `steps_login.py`

---

### `feature 2: Subida de archivos `

**Escenario:** Subida de ejercicios java por el estudiante y csv .
**Descripción:**  
Este escenario verifica que el estudiante pueda subir archivos java y estos sean verificados correctamente, ademas, verifica la subida de archivos csv por el supervisor, y que el registro de los estudiantes respectivos sea exitosa.  
**Resultado esperado:**  
El archivo correspondiente es subido a la plataforma y retorna un estado 200.
**Archivo de pasos:** `steps_file_uploads.py`

---

### `feature 3: Registro de supervisores`

**Escenario:** Registro de un nuevo supervisor  
**Descripción:**  
Este escenario verifica que un nuevo supervisor pueda registrarse correctamente cuando se ingresan todos los campos requeridos con un formato valido, incluye pruebas invalidas.  
**Resultado esperado:**  
- Éxito: El usuario es registrado en la base de datos y es redirigido a la página de login (`/login`) luego de completar el formulario.  
- Fallo: El usuario no se registra y se notifica al usuario mediante un pop-up que el valor ingresado es invalido 
**Archivo de pasos:** `steps_register.py`

---

###  `feature 4: Edicion de contraseña`

**Escenario:** Cambio de contraseña por el supervisor o estudiante 
**Descripción:**  
Se evalua que el sistema permita la modificacion de la contraseña de la cuenta, y si estan bien formateadas, dando un resultado exitoso o fallido.
**Resultado esperado:**  
El usuario permanece en la misma página (`/cuentaDocente` o `/cuentaEstudiante`) y se actualiza la contraseña en la base de datos.  
**Archivo de pasos:** `steps_modify.py`

---


### Configuración base

**Archivo:** `environment.py`  
Define la URL base donde se ejecuta la aplicación para los tests:
```python
context.base_url = "http://localhost:3000"
```

---

### Ejecucion con Docker

Para compilar y ejecutar la aplicación utilizando Docker, sigue estos pasos:

1. Asegúrate de tener Docker instalado en tu máquina. Puedes descargarlo desde [aquí](https://www.docker.com/get-started).

2. Abre una terminal y navega hasta el directorio del proyecto.

3. Compila la imagen de Docker utilizando el siguiente comando:
   ```
   docker build -t nombre_de_la_imagen .
   ```
   Reemplaza `nombre_de_la_imagen` con el nombre que desees para tu imagen.

4. Una vez que la imagen se haya construido correctamente, ejecuta un contenedor a partir de la imagen con el siguiente comando:
   ```
   docker run -p 3000:3000 nombre_de_la_imagen
   ```
   Esto mapeará el puerto 3000 del contenedor al puerto 3000 de tu máquina local.

5. Accede a la aplicación en tu navegador en la siguiente URL:
   ```
   http://localhost:3000
   ```