import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import logging
import json

last_message_id = 0
cmd_enabled = ["sensors", "ip"]


# Cargar variables de entorno
load_dotenv(override=True)

def send_ip(new_ip):
    """
    Envía un mensaje a través de la API de Telegram.
    """
    # Creo el mensaje a enviar
    fecha_hora = datetime.now().strftime("%H:%M %d/%m/%y")
    message = (
        "<b>🚀 Actualización de IP 🌐</b>\n\n"
        f"<b>Fecha y Hora:</b> <pre>{fecha_hora}</pre>\n\n"
        f"<b>Nueva IP:</b> <pre>{new_ip}</pre>"
    )

    try:
        # Envío el mensaje
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
    

def send_sensors():
    """
    Envía el mensaje con los valores de Temperatura de la maquina.
    """

    # Obtengo la temperatura directo de los sensores de la pc
    temp = 0
    try:
        temp = int(open("/sys/class/thermal/thermal_zone1/temp").read()) / 1000
    except Exception as e:
        logging.error(f"Error al leer la temperatura del sistema: {e}")
        return False

    # Creo el mensaje a enviar
    fecha_hora = datetime.now().strftime("%H:%M %d/%m/%y")
    message = (
        "<b>🚨 Sensores 🌡️</b>\n\n"
        f"<b>Fecha y Hora:</b> <pre>{fecha_hora}</pre>\n\n"
        f"<b>Temperatura:</b> <pre>{temp} °C</pre>"
    )

    try:
        # Envío el mensaje
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





def check_command():
    """
    Verifica si el comando recibido es válido y lo devuelve en caso de serlo.
    """
    global last_message_id, cmd_enabled
    try:
        response = requests.post(
            url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates",
            data={
                "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
            },
        )
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        #print(json.dumps(response.json(), indent=4))  
        raw_message_id = response.json()["result"][-1]["update_id"]
        text = response.json()["result"][-1]["message"]["text"]

        # Para la primera ejecucion, omite el primer mensaje
        if last_message_id == 0:
            last_message_id = raw_message_id

        # Capta cada comando nuevo
        if last_message_id != raw_message_id:
            last_message_id = raw_message_id
            if text in [f"/{cmd}" for cmd in cmd_enabled]:
                logging.info(f"Comando recibido: '{text}'")
                return text
            else:
                logging.warning(f"Comando no válido -> '{text}'")

        return None
    except requests.RequestException as e:
        logging.error(f"Error en el checkeo del comando: {e}")
        return None