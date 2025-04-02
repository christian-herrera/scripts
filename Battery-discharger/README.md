# Battery Discharge

El script permite tener un bucle que verifica la descarga de la batería. La idea es usarlo algunas veces en el año para lograr la descarga completa de la batería del servidor. Cuando llega al valor limite (10%), automáticamente envía cada 10 segundos un mensaje a traves de Telegram.

<br><br>

# Contenido de `.env`
## Variables para Telegram
- `TELEGRAM_TOKEN`: Es el Token que devuelve el bot `@BotFather` al momento de la creación del bot.
- `TELEGRAM_CHAT_ID`: Es el ID asociado al chat, se puede obtener haciendo consultas a la url: *[getUpdates](https://api.telegram.org/bot<TELEGRAM_TOKEN>/getUpdates)*.


<br><br>