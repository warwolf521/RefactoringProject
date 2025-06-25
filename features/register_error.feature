Feature: Register_error

Scenario: No se ingresa el nombre
    Given la aplicacion esta en ejecucion 2
    When ingreso nombre "<vacio>" apellido "lopez432" correo "pepito@udec.cl" y contraseña "1234" por error
    Then aparece un mensaje de error