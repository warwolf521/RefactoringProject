Feature: Subida de archivos Java para ejercicios

  Scenario: Estudiante sube un archivo .java exitosamente
    Given el estudiante ha iniciado sesión y está en la página del ejercicio
    When selecciona el archivo "FizzBuzz.java"
    And presiona el botón "Subir"
    Then el sistema guarda el archivo en la carpeta correspondiente
    And muestra un mensaje indicando que todos los tests fueron aprobados

  Scenario: Estudiante sube un archivo no válido
    Given el estudiante está en la página del ejercicio
    When selecciona un archivo que no termina en ".java"
    And presiona el botón "Subir"
    Then el sistema muestra un mensaje de error indicando que el formato no es válido
