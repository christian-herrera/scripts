# Check-And-Update

El script permite leer el registro de Cloudflare, leer la IP Publica actual y luego, en caso de diferir, actualizar el registro correspondiente en CloudFLare.

La API de CloudFlare se detalla en la documentación oficial ([Link](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/list/)).


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


## Demás Variables
Las siguientes variables son para el uso general del script:

- `PATH_LOG_FILE`: Es el path completo del archivo *log*, por ejemplo: `/home/user/Scripts/debug.log`.