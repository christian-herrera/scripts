import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import logging


# Cargar variables de entorno
load_dotenv(override=True)

def send_ok_update(ip):
    """
    Envia el mensaje de confirmacion de actualizacion de la IP...
    """
    fecha_hora = datetime.now().strftime("%H:%M %d/%m/%y")
    message = (
        "<b>🚨 Actualización de IP (Script Automatico) 🌐</b>\n\n"
        f"<b>Fecha y Hora:</b> <pre>{fecha_hora}</pre>\n\n"
        f"<b>Nueva IP:</b> <pre>{ip}</pre>"
    )

    try:
        response = requests.post(
            url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
            data={
                "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
                "text": message,
                "parse_mode": "HTML",
                "disable_notification": False
            },
        )
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        logging.info("Mensaje enviado exitosamente.")        
        return True
    except requests.RequestException as e:
        logging.error(f"Error al enviar el mensaje: {e}")
        return False
    

def send_fail_update(ip):
    """
    Envia el mensaje de que no se logro actualizar la IP en CloudFlare...
    """
    fecha_hora = datetime.now().strftime("%H:%M %d/%m/%y")
    message = (
        "<b>🚨 Actualización de IP (Script Automatico) 🌐</b>\n\n"
        "🚧🚧 <b><i>Falló la actualizacion de ClouFlare!</i></b> 🚧🚧\n\n"
        f"<b>Fecha y Hora:</b> <pre>{fecha_hora}</pre>\n\n"
        f"<b>Nueva IP:</b> <pre>{ip}</pre>"
    )

    try:
        response = requests.post(
            url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
            data={
                "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
                "text": message,
                "parse_mode": "HTML",
                "disable_notification": False
            },
        )
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        logging.info("Mensaje enviado exitosamente.")        
        return True
    except requests.RequestException as e:
        logging.error(f"Error al enviar el mensaje: {e}")
        return False