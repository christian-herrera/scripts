# Check-Update-Notify

El script permite leer el registro de Cloudflare, leer la IP Publica actual y luego, en caso de diferir, actualizar el registro correspondiente en CloudFLare. Adicionalmente, se utiliza lo desarrollado en [Send-HTML-Message](../../Telegram-bot/send-html-message/README.md) para enviar la notificación al Bot de Telegram.

<br>

# APIs

- El detalle de todas las llamadas disponibles a la API se encuentra en la documentación oficial ([Link](https://core.telegram.org/bots/api))
- La API de CloudFlare se detalla en la documentación oficial ([Link](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/list/)).



<br><br>

# Contenido de `.env`
## Credenciales de Cloudflare
En el archivo `.env` se deberán dejar las siguientes variables:

- `CLOUDFLARE_EMAIL`: Email de la cuenta.
- `CLOUDFLARE_API_TOKEN`: Token generado, deberá tener los permisos: `DNS: Write`.
- `CLOUDFLARE_ZONE_ID`: Es el ID de la zona, se encuentra 
- `CLOUDFLARE_DNS_RECORD_ID`: Es el ID del registro que se pretende actualizar.
- `CLOUDFLARE_DNS_NAME`: Es el nombre del registro, por ejemplo: *miIp.dominio.com*.
- `CLOUDFLARE_DNS_COMMENT`: Es el comentario que mantiene el registro.


## Credenciales de Telegram
- `TELEGRAM_TOKEN`: Es el Token que devuelve el bot `@BotFather` al momento de la creación del bot.
- `TELEGRAM_CHAT_ID`: Es el ID asociado al chat, se puede obtener haciendo consultas a la url: *[getUpdates](https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates)*.


## Demás Variables
Las siguientes variables son para el uso general del script:

- `PATH_LOG_FILE`: Es el path completo del archivo *log*, por ejemplo: `/home/user/Scripts/debug.log`.