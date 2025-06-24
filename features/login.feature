Feature: Login

 Scenario: Login exitosa del nombre y correo electrónico
    Given la aplicación está corriendo
    When ingreso usuario "test2@test.cl" y contraseña "test2"
    Then debería ser redirigido al dashboard del usuario