Feature: Modficacion del perfil de usuario

Scenario: Se actualiza el nombre del usuario Supervisor
    Given Se tiene sesion iniciada con las credenciales correo: "hola@udec.cl" contrasena "hola" y se esta dashboard de "Docente"
    When Se actualiza la contrasena antigua "hola" y la nueva contrasena "4321" y esta esta se confirma
    Then la contrasena del usuario es actualizada

Scenario: Se actualiza el nombre del usuario Estudiante
    Given Se tiene sesion iniciada con las credenciales correo: "hola@udec.cl" contrasena "hola" y se esta dashboard de "Estudiante"
    When Se actualiza la contrasena antigua "hola" y la nueva contrasena "4321" y esta esta se confirma
    Then la contrasena del usuario es actualizada