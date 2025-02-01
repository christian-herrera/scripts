import requests
import logging


def get_ip_from_ipify():
    """
    Obtiene la dirección IP pública usando la API de ipify.

    Se logra haciendo una petición GET a la url de ipify y devolviendo el texto de la respuesta.
    """
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error al obtener la IP: {e}")
        return None