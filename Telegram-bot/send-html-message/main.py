from utils import get_ip_from_ipify
from telegram import send_ip
import logging, os

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=os.getenv("PATH_LOG_FILE")
)

def main():
    try:
        # Obtengo la IP Publica actual de Ipify
        ip = get_ip_from_ipify()
        if ip is None:
            raise ValueError("Error al obtener la IP")

        # Intento enviar el mensaje con la IP leida
        if send_ip(ip):
            logging.info("Proceso completado exitosamente.")

    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()