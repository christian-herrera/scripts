from dotenv import load_dotenv
import requests, os, logging, json

load_dotenv(override=True)


def get_ip_from_record(): 
    """
    Permite obtener del registro de CloudFlare la IP que tiene almacenada.
    """
    try:
            
        response = requests.get(
            f"https://api.cloudflare.com/client/v4/zones/{os.getenv('CLOUDFLARE_ZONE_ID')}/dns_records",
            headers = {
                "Authorization": f"Bearer {os.getenv('CLOUDFLARE_API_TOKEN')}",
                "Content-Type": "application/json"
            }
        )

        response.raise_for_status() 
        data = response.json()
        #print(json.dumps(data, indent=4))
        ip, id = None, None
        for record in data["result"]:
            if record["name"] == os.getenv("CLOUDFLARE_DNS_NAME"):
                ip = record["content"]
                id = record["id"]
                break
        return(id, ip)
    
    except requests.RequestException as e:
        print(f"Error al obtener la IP del registro: {e}")
        return None, None
    


def update_ip(id, new_ip):
    """
    Permite actualizar la IP del registro correspondiente a la `id` y al `os.getenv("CLOUDFLARE_DNS_NAME")` configurado.
    """
    logging.debug(f"Actualizando IP del id: {id} con la nueva IP: {new_ip}")
    try:
        response = requests.put(
            f"https://api.cloudflare.com/client/v4/zones/{os.getenv('CLOUDFLARE_ZONE_ID')}/dns_records/{id}",
            headers = {
                "Authorization": f"Bearer {os.getenv('CLOUDFLARE_API_TOKEN')}",
                "Content-Type": "application/json"
            },
            json = {
                "name": os.getenv("CLOUDFLARE_DNS_NAME"),
                "type": "A",
                "content": f"{new_ip}",
                "proxiable": True,
                "proxied": False,
                "ttl": 1,
                "comment": os.getenv("CLOUDFLARE_DNS_COMMENT")
            }
        )
        response.raise_for_status()
        
        if response.json()["success"] == True:
            logging.info("IP actualizada correctamente")
            return True
        else:
            logging.error(f"Error al actualizar la IP => {response.json()}")
            return False
    except requests.RequestException as e:
        logging.error(f"Error al actualizar la IP: {e}")
        return False