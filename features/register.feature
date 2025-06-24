Feature: Register

Scenario: Se registra existosamente un usuario
    Given la aplicacion esta en ejecucion
    When ingreso nombre "pepito432" apellido "lopez432" correo "pepito432@udec.cl" y contraseña "1234"
    Then debería ser redirigido a la página de inicio de sesión