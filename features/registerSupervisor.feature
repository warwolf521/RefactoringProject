Feature: Register

Scenario: Se registra existosamente un usuario
    Given la aplicacion esta en ejecucion
    When ingreso nombre "pepito4321" apellido "lopez4321" correo "pepito432@udec.cl" y contraseña "1234"
    Then debería ser redirigido a la página de inicio de sesión

Scenario: No se ingresa el nombre
    Given la aplicacion esta en ejecucion
    When ingreso nombre "<vacio>" apellido "lopez" correo "pepito@udec.cl" y contraseña "1234" por error
    Then aparece un mensaje de error

Scenario: No se ingresa el apellido
    Given la aplicacion esta en ejecucion
    When ingreso nombre "pepito" apellido "<vacio>" correo "pepito@udec.cl" y contraseña "1234" por error
    Then aparece un mensaje de error

Scenario: No se ingresa el correo
    Given la aplicacion esta en ejecucion
    When ingreso nombre "pepito" apellido "lopez" correo "<vacio>" y contraseña "1234" por error
    Then aparece un mensaje de error

Scenario: No se ingresa la contraseña
    Given la aplicacion esta en ejecucion
    When ingreso nombre "pepito" apellido "lopez" correo "pepito@udec.cl" y contraseña "<vacio>" por error
    Then aparece un mensaje de error