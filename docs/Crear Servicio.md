# Crear Servicio en Linux

## Entorno Virtual de Python3

En primer lugar se debe crear el entorno virtual, para eso usar:
```bash
python3 -m venv .venv
```

Luego, con `pip`, instalar las dependencias correspondientes al script.
```bash
source .venv/bin/activate
pip install <modulo1> <modulo2> ...
deactivate
```
Una vez terminado, se debe usar el path absoluto al ejecutable de python del entorno virtual. Si la ruta donde se creó la carpeta `.venv` es `/home/user1/Scripts`, entonces se usará `/home/user1/Scripts/.venv/bin/python3`

<br>

## Crear el Servicio
Para crear el servicio, se debe crear el un archivo por ejemplo: `mi-script.service` en la ruta: `/etc/systemd/system/`. Allí colocar lo siguiente:
```
[Unit]
Description=Mi Primer Script
After=network.target

[Service]
User=user1
Group=user1
WorkingDirectory=/home/user1/Scripts
ExecStart=/home/user1/Scripts/.venv/bin/python3 /home/user1/Scripts/main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
Notar que la directiva `ExecStart` requiere del comando `python3` obtenido del entorno virtual, y del archivo `main.py` que es el script de python3.

Finalmente, guardar este archivo y reiniciar el *daemon* con:
```bash
sudo systemctl daemon-reload
```
Si todo es correcto, se podrá hacer uso de los comandos:
```bash
sudo systemctl enable   mi-script.service
sudo systemctl disable  mi-script.service
sudo systemctl start    mi-script.service
sudo systemctl stop     mi-script.service
sudo systemctl restart  mi-script.service
sudo systemctl status   mi-script.service
```

<br>

## Plus: Dar permisos al usuario
Para permitir que el `user1` ejecute los comandos listados anteriormente se debe editar el archivo `/etc/sudoers`. La forma correcta de hacerlo es usando:
```bash
sudo visudo
```
Alli, se debe configurar al usuario de la siguiente forma:
```
user1 ALL=(root) NOPASSWD: /usr/bin/systemctl * mi-script.service
```

<br>