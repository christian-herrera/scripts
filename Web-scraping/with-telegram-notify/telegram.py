import logging, os, requests
from dotenv import load_dotenv
from datetime import datetime


# Cargar variables de entorno
load_dotenv(override=True)

def notify_new_data():
    """
    Envía un mensaje a través de la API de Telegram.
    """
    fecha_hora = datetime.now().strftime("%H:%M %d/%m/%y")
    message = (
        "<b>🚨 Actualización del Moodle 🌐</b>\n\n"
        f"<b>Curso:</b> <pre>{os.getenv("TITLE_CURSO_MOODLE")}</pre>"
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
    

def notify_error(msg):
    """
    Envía un mensaje a través de la API de Telegram.
    """
    message = (
        "<b>🚨 Error en el Script! 🚨</b>\n\n"
        f"<b>Curso:</b> <pre>{os.getenv("TITLE_CURSO_MOODLE")}</pre>\n\n"
        f"<b>Error:</b> <i>{msg}</i>"
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