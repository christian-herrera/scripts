import os, requests
from dotenv import load_dotenv


# Cargar variables de entorno
load_dotenv(override=True)


def notify_new_data(value):
    """
    Envía un mensaje a través de la API de Telegram.
    Pasa el valor de la batería como argumento.
    """
    message = (
        "<b>🪫Batería Critica!🪫</b>\n\n"
        f"<b>Valor:</b> <pre>{value}%</pre>"
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
        return True
    except requests.RequestException as e:
        print(f"[ERROR] No se logró enviar el mensaje: {e}")
        return False