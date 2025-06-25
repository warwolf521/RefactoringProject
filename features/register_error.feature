Feature: Register_error

Scenario: No se ingresa el nombre
    Given la aplicacion esta en ejecucion 2
    When ingreso nombre "<vacio>" apellido "lopez" correo "pepito@udec.cl" y contraseña "1234" por error
    Then aparece un mensaje de error

Scenario: No se ingresa el apellido
    Given la aplicacion esta en ejecucion 2
    When ingreso nombre "pepito" apellido "<vacio>" correo "pepito@udec.cl" y contraseña "1234" por error
    Then aparece un mensaje de error

Scenario: No se ingresa el correo
    Given la aplicacion esta en ejecucion 2
    When ingreso nombre "pepito" apellido "lopez" correo "<vacio>" y contraseña "1234" por error
    Then aparece un mensaje de error

Scenario: No se ingresa la contraseña
    Given la aplicacion esta en ejecucion 2
    When ingreso nombre "pepito" apellido "lopez" correo "pepito@udec.cl" y contraseña "<vacio>" por error
    Then aparece un mensaje de error
