# Web Scraping (Moodle)

El script permite en base a una URL de uno de los cursos de la página de Asignaturas de la facultad de ingeniería, saber si los docentes cargaron algún nuevo material. En funcion del resultado, enviará una notificacion usando los bots de Telegram. La idea es ejecutarlo varias veces al dia para mantener un registro del mismo.

<br><br>

# Contenido de `.env`
## Credenciales del Moodle
- `MOODLE_USER`: Usuario.
- `MOODLE_PASS`: Clave.

## URL y demás datos que se utilizaran
- `URL_LOGIN_MOODLE`: Es la url donde esta el formulario de inicio de sesión.
- `URL_CURSO_MOODLE`: Es la url del curso en especifico que se quiere verificar.
- `TITLE_CURSO_MOODLE`: Es el titulo del curso, se utiliza para enviar en el mensaje usando Telegram.

## Variables para Telegram
- `TELEGRAM_TOKEN`: Es el Token que devuelve el bot `@BotFather` al momento de la creación del bot.
- `TELEGRAM_CHAT_ID`: Es el ID asociado al chat, se puede obtener haciendo consultas a la url: *[getUpdates](https://api.telegram.org/bot<TELEGRAM_TOKEN>/getUpdates)*.

## Demás Variables
Las siguientes variables son para el uso general del script:

- `PATH_LOG_FILE`: Es el path completo del archivo *log*, por ejemplo: `debug.log`. Queda en la misma carpeta del `main.py`.
- `PATH_DATA_EXTRACTED`: Archivo que mantiene los datos extraídos de la ultima ejecución. Queda en la misma carpeta del `main.py`.

<br><br>

# Crear Task en Windows
Se debera crear un archivo `wscript.vbs` para ocultar la ventana del cmd de windows cuando se ejecuta la tarea. En la misma carpeta, crear un archivo con el nombre mencionado y colocar:

```
Set objShell = CreateObject("WScript.Shell")
objShell.Run "<PATH>\.venv\Scripts\python.exe <PATH>\main.py", 0, False
```
En lugar de `<PATH>`, colocar la ruta completa de donde está ubicada la carpeta de este script. Finalmente, crear la tarea en el Programador de Tareas de Windows y usar el desencadenador deseado (en función de las veces por dia que se quiere ejecutar), en el campo acción, simplemente buscar este archivo creado.