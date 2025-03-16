# Web Scraping (Moodle)

El script permite en base a una URL de uno de los cursos de la página de Asignaturas de la facultad de ingeniería, saber si los docentes cargaron algún nuevo material. La idea es ejecutarlo varias veces al dia para mantener un registro del mismo.

🚀 Para futuras versiones, se debería implementar la funcionalidad de enviar por Telegram una notificación.

<br><br>

# Contenido de `.env`
## Credenciales del Moodle
- `MOODLE_USER`: Usuario.
- `MOODLE_PASS`: Clave.

## URL que se utilizaran
- `URL_LOGIN_MOODLE`: Es la url donde esta el formulario de inicio de sesión.
- `URL_CURSO_MOODLE`: Es la url del curso en especifico que se quiere verificar.


## Demás Variables
Las siguientes variables son para el uso general del script:

- `PATH_LOG_FILE`: Es el path completo del archivo *log*, por ejemplo: `debug.log`. Queda en la misma carpeta del `main.py`.
- `PATH_DATA_EXTRACTED`: Archivo que mantiene los datos extraídos de la ultima ejecución. Queda en la misma carpeta del `main.py`.