from dotenv import load_dotenv
from utils import get_ip_from_ipify
from cloudflare import get_ip_from_record, update_ip
from telegram import send_ok_update, send_fail_update
import os, logging

load_dotenv(override=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=os.getenv("PATH_LOG_FILE")
)



# ==> Main
def main():
    logging.info("====================> Inicio del proceso <====================")
    # Obtengo todos los valores
    logging.info("Obteniendo datos de Cloudflare y de Ipify...")
    [id_record, ip_record] = get_ip_from_record()
    ip_actual = get_ip_from_ipify()

    # Verifico que no esten vacios los datos
    if id_record is None or ip_record is None:
        logging.error(f"No se pudieron obtener los datos de Cloudflare => ID: {id}, IP: {ip_record}")
        exit(1)
    elif ip_actual is None:
        logging.error(f"No se pudo obtener la IP actual => IP: {ip_actual}")
        exit(1)

    # Comparo las IPs
    logging.info(f"IP en Cloudflare: {ip_record}; IP actual: {ip_actual}")
    if ip_record != ip_actual:
        logging.info("Las IPs no coinciden, intentando actualizar...")
        if update_ip(id_record, ip_actual):
            send_ok_update(ip_actual)
        else:
            send_fail_update(ip_actual)
    else:
        logging.info("La IP de CloudFlare es la correcta...")
    exit(0)

if __name__ == "__main__":
    main()