from utils import get_ip_from_ipify
from telegram import check_command, send_sensors, send_ip
from time import time
from dotenv import load_dotenv
import logging, os


load_dotenv(override=True)
SEG_BT_CHECK = float(os.getenv("SEG_BT_CHECK"))
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=os.getenv("PATH_LOG_FILE")
)


def main():
    try:
        last = 0
        while True:
            if time() - last >= SEG_BT_CHECK:
                last = time()
                cmd = check_command()

                if cmd is None:
                    continue

                # Envío el valor de temperatura
                if cmd == "/sensors":
                    send_sensors()
                
                # Envío la IP Actual
                if cmd == "/ip":
                    ip = get_ip_from_ipify()
                    if ip is None:
                        raise ValueError("Error al obtener la IP")
                    
                    send_ip(ip)

    except KeyboardInterrupt:
        logging.info("Finalizando el Script . . .")
    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()