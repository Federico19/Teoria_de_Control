import network
import socket
import time
import secrets  # Librería con las credenciales de tu red Wi-Fi

from machine import Pin

led = Pin("LED", Pin.OUT)

class WifiConnect():
    def connect():
        wlan = network.WLAN(network.STA_IF)
        try:
            wlan.active(True)
            wlan.connect(secrets.SSID, secrets.PASSWORD)
            while wlan.isconnected() == False:
                print('[WLAN] Esperando la conexión...')
                time.sleep(1)
            ip = wlan.ifconfig()[0]
            print(f'[WLAN] Conectado en = {ip}')
        except:
            print('No se que pasa que no funka')

try:
    WifiConnect.connect()
except KeyboardInterrupt:
    machine.reset()
