Feature: Login de estudiantes

   Como estudiante registrado
   Quiero iniciar sesión en la plataforma
   Para acceder a mis cursos y tareas

Scenario: Login exitosa del nombre y correo electrónico
   Given la aplicación está corriendo
   When ingreso usuario "gabriel.perez@example.com" y contraseña "20230101"
   Then debería ser redirigido al dashboard del "estudiante"

Scenario: Login fallido por contraseña incorrecta
    Given la aplicación está corriendo
    When ingreso usuario "estudiante1@plataforma.cl" y contraseña "incorrecta"
    Then debería permanecer en la página de login