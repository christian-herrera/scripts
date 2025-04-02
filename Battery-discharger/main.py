import time, psutil
from telegram import notify_new_data


# ───────────────────────────────────────────────────────────────────
# -----------------------------------------
# Simulando el comportamiento de la batería
# battery = True
# percent = 12
# plugged = False
# -----------------------------------------

try:
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        if battery:
            if plugged:
                print("\n\n[INFO] La batería está cargando nuevamente!")
                print("[INFO] Script finalizado!...")
                break

            if percent < 10:
                print(f"[WARN] Batería crítica => {percent}%")
                notify_new_data(percent)
            else:
                print(f"[INFO] Descarga en progreso: {percent}%")
        else:
            print("[ERROR] No se encontró información sobre la batería.")

        # -----------------------------------------
        # Simulando el comportamiento de la batería
        #percent = percent - 1 # Simulando descarga
        #if percent < 5:
        #    plugged = True
        # -----------------------------------------

        time.sleep(10)
        
except KeyboardInterrupt:
    print("\n\n[INFO] Script interrumpido por el usuario.")
    print("[INFO] Script finalizado!...")
except Exception as e:
    print(f"[ERROR] Ocurrió un error inesperado: {e}")