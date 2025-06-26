Feature: Registro masivo de estudiantes mediante archivo CSV

  Scenario: Supervisor sube un archivo CSV válido
    Given el supervisor ha iniciado sesión y accede a la página de registro de estudiantes
    When selecciona el archivo "lista_estudiantes.csv"
    And presiona el botón "Registrar Estudiantes"
    Then el sistema procesa el archivo
    And registra los estudiantes en la base de datos

  Scenario: Supervisor sube un archivo CSV con formato incorrecto
    Given el supervisor ha iniciado sesión y accede a la página de registro de estudiantes
    When selecciona el archivo "lista_estudiantes_mal.csv"
    And presiona el botón "Registrar Estudiantes"
    Then el sistema ignora las filas inválidas
    And muestra un mensaje de advertencia indicando los errores detectados