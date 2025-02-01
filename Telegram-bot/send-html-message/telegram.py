import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import logging


# Cargar variables de entorno
load_dotenv(override=True)

def send_ip(ip):
    """
    Envía un mensaje a través de la API de Telegram.
    """
    fecha_hora = datetime.now().strftime("%H:%M %d/%m/%y")
    message = (
        "<b>🚨 Actualización de IP 🌐</b>\n\n"
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