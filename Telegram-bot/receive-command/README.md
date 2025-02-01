# Receive-Command

Este Script permite verificar cada 10 segundos la existencia de un nuevo comando. Se utiliza un bucle para mantener el script vivo, en cada verificación, si existe un comando nuevo, deberá ser uno que esté habilitado (cargado en la variable `cmd_enabled` ubicado en el modulo `telegram.py`).

Si esta habilitado, se le pasa el comando que llega al `main.py`y allí se ejecuta la acción correspondiente.


<br><br>

# Contenido de `.env`
## Credenciales de Telegram
- `TELEGRAM_TOKEN`: Es el Token que devuelve el bot `@BotFather` al momento de la creación del bot.
- `TELEGRAM_CHAT_ID`: Es el ID asociado al chat, se puede obtener haciendo consultas a la url: *[getUpdates](https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates)*.


## Demás Variables
Las siguientes variables son para el uso general del script:

- `PATH_LOG_FILE`: Es el path completo del archivo *log*, por ejemplo: `/home/user/Scripts/debug.log`.
- `SEG_BT_CHECK`: Son los segundos que deben transcurrir entre cada consulta a la url de Telegram.