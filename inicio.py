import sys
from machine import Pin
from time import gmtime, sleep
import Circuito
import Analizador
import Maquina
import _thread
import network
import socket


maquina = Maquina.Maquina()
circuito = Circuito.Circuito(maquina)
analizador = Analizador.Analizador(maquina)

def Lectura():
    global circuito
    global analizador
    while True:
        circuito.control_sensor_prox()
        analizador.actualizar_informacion()        
_thread.start_new_thread(Lectura, ())


def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html

#######################################################
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = "Fibertel WiFi551 2.4 GHz"
pw = "4149109910"

wlan.connect(ssid, pw)

# Wait for connection with 10 second timeout
timeout = 10
while timeout > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Esperando por la conexión...')
    sleep(1)
    
if wlan.status() != 3:
    raise RuntimeError('Conexión WiFi fallida')
else:
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(wlan.status()):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
    print('Conectado!')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Escuchando en', addr)

######################################################

while True:
    
    try:
        cl, addr = s.accept()
        #print('Cliente conectado desde: ', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
            
        response = get_html('index.html')
        response = response.replace('cadena_1', str(analizador.estado_maquina))
        response = response.replace('cadena_2', str(analizador.tiempo_encendida))
        response = response.replace('cadena_3', str(analizador.tiempo_total_encendida))
        # response = response.replace('cadena_4', str(maquina.velocidad_actual))
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    except OSError as e:
        cl.close()
        print('Connection closed')