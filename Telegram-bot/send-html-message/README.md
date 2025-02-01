# Send-HTML-Message

Este Script permite enviar un mensaje HTML a traves de una petición GET. Primero se debe crear el bot con `@BotFather` y asi obtener el `TOKEN`.

Luego, se requiere enviar un mensaje al bot creado para ejecutar la siguiente consulta:

```
https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates
```
Allí, se ubica el valor de la clave: `result -> message -> chat -> id` y se utiliza en la variable de entorno `TELEGRAM_CHAT_ID`.

## API
El detalle de todas las llamadas disponibles a la API se encuentra en la documentación oficial [Link](https://core.telegram.org/bots/api)


<br><br>

# Contenido de `.env`
## Credenciales de Telegram
- `TELEGRAM_TOKEN`: Es el Token que devuelve el bot `@BotFather` al momento de la creación del bot.
- `TELEGRAM_CHAT_ID`: Es el ID asociado al chat, se puede obtener haciendo consultas a la url: *[getUpdates](https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates)*.


## Demás Variables
Las siguientes variables son para el uso general del script:

- `PATH_LOG_FILE`: Es el path completo del archivo *log*, por ejemplo: `/home/user/Scripts/debug.log`.