# __Configurar__
#
# 📌 python -m venv .venv
# 📌 .\.venv\Scripts\activate
# 📌 pip install -r requirements.txt
#
# __Ejecutar__
# <C:\Users\xxxx\web-scraping>\.venv\Scripts\python <C:\Users\xxxx\web-scraping>\main.py



import logging, os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Configuraciones y Credenciales
load_dotenv(override=True)

# Estructuro los paths que usaré
script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, os.getenv("PATH_LOG_FILE"))
data_extract_path = os.path.join(script_dir, os.getenv("PATH_DATA_EXTRACTED"))


# Loggin en el archivo debug.log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=log_path,
    encoding='utf-8'
)

# Payload que se envia en el login
payload = {
    "username": os.getenv("MOODLE_USER"),   # Credencial: Usuario
    "password": os.getenv("MOODLE_PASS"),   # Credencial: Contraseña
    "logintoken": "",                       # El token obtenido del formulario
    "rememberusername": "1"                 # Si quieres recordar el nombre de usuario
}




# ───────────────────────────────────────────────────────────────────
# 📌 Función: getToken(session)
# 📌 Descripción: Obtiene el Token del login. Luego llama a la
#                 funciøn tryLogin para intentar el inicio de sesion
# ───────────────────────────────────────────────────────────────────
def getToken(session):
    """
    Obtiene el Token que usa el form del Login. Si se logra, llama
    a la funcion para intentar el inicio de sesion con las credenciales.
    """
    # Hago la peticion GET
    resp = session.get(os.getenv("URL_LOGIN_MOODLE"))

    if resp.status_code == 200:
        logging.info("Formulario de login recibido correctamente.")

        # Obtengo el token actual y lo agrego al payload
        soup = BeautifulSoup(resp.text, "html.parser")
        payload["logintoken"] = soup.find("input", {"name": "logintoken"})["value"]
        logging.info(f"Token obtenido: {payload["logintoken"]}")
        tryLogin(session)
    else:
        logging.error(f"No se identifico el token: {resp.status_code}")




# ───────────────────────────────────────────────────────────────────
# 📌 Función: tryLogin(session)
# 📌 Descripción:   Intenta hacer el login con el payload cargado de las
#                   credenciales y con el Token. El exito se logra si se
#                   obtuvo el string "Estimado Docente" que es el que
#                   aparece en la web post-login.
# ───────────────────────────────────────────────────────────────────
def tryLogin(session):
    """
    Intenta hacer el login con el payload actualizado. Si se logra,
    llama a la funcion downloadData() para tomar los datos de la url.
    """
    # Intento el login (metodo POST)
    resp = session.post(os.getenv("URL_LOGIN_MOODLE"), data=payload)

    if resp.status_code == 200 and "Estimado Docente" in resp.text:
        logging.info("Login exitoso!")
        downloadData(session)
    else:
        logging.error("Login fallido.")



# ───────────────────────────────────────────────────────────────────
# 📌 Función: downloadData(session)
# 📌 Descripción:   Descarga el html de la web "curso_url". Si
#                   credenciales y con el Token. El exito se logra si el
#                   HTML contiene un div con el atributo: "role='main'".
# ───────────────────────────────────────────────────────────────────
def downloadData(session):
    """
    Descarga el HTML completo de la url cargada en la variable "curso_url".
    Si se logra, entonces llama a la funcion checkIfNewData().
    """
    # Peticion GET
    resp = session.get(os.getenv("URL_CURSO_MOODLE"))
    if resp.status_code == 200:
        # Busco el div que contiene los datos
        soup = BeautifulSoup(resp.text, "html.parser")
        main_div = soup.find("div", {"role": "main"})
        title = soup.find("title")
        logging.info(f"Curso identificado: {title.text}")
        

        if main_div:
            content = main_div.text                 # Solo texto (sin HTML)
            # content = main_div.prettify()         # HTML nativo
            logging.info("Div encontrado!")
            checkIfNewData(content)
        else:
            logging.error("No se encontró el div con role='main'.")
    else:
        logging.error(f"Error al realizar la solicitud: {resp.status_code}")



# ───────────────────────────────────────────────────────────────────
# 📌 Función: downloadData(data)
# 📌 Descripción:   Descarga el contenido de la url en un archivo de
#                   de texto definido por la variable de entorno:
#                   "PATH_DATA_EXTRACTED". Si existe, entonces primero
#                   compara para detectar cambios.
# ───────────────────────────────────────────────────────────────────
def checkIfNewData(data):
    """
    Descarga el contenido de la url en un archivo de texto. Si el
    archivo ya existe, entonces previamente verifica si difiere
    de los datos descargados. Finalmente, sobrescribe en el archivo.
    """
    # Leo el archivo de la ultima comprobacion
    if os.path.exists(data_extract_path):
        with open(data_extract_path, "r") as file:
            saved_content = file.read()
    else:
        saved_content = ""

    # Comparo el contenido
    if data != saved_content:
        logging.info("Hay nueva informacion en el curso!")
        # logging.info("[ ==== INICIO: NUEVA DATA ================================ >")
        # logging.info(f"\n{data}")
        # logging.info("====================================== FIN: NUEVA DATA ====]")
        with open(data_extract_path, "w") as file:
            file.write(data)
    else:
        logging.info("El sitio no se há modificado!")



# ───────────────────────────────────────────────────────────────────
#                      ==> MAIN PRINCIPAL <==
#
# 📌 Descripción:   Se genera una nueva session y se llama a la
#                   primer funcion. Esta desencadena las demas!
# ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    logging.info("=====================================> NUEVA EJECUCIÓN!")
    session = requests.Session()   #Nueva Sesión
    getToken(session)
