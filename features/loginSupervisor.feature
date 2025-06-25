Feature: Login de supervisores

   Como supervisor autorizado
   Quiero iniciar sesión en el sistema
   Para monitorear el progreso de los estudiantes

Scenario: Login exitoso del supervisor
   Given la aplicación está corriendo
   When ingreso usuario "supervisor1@plataforma.cl" y contraseña "supervisor123"
   Then debería ser redirigido al dashboard del "supervisor"

Scenario: Login fallido por contraseña incorrecta
    Given la aplicación está corriendo
    When ingreso usuario "supervisor1@plataforma.cl" y contraseña "incorrecta"
    Then debería permanecer en la página de login