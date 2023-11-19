import wifi
import socket
import json
import sys
import Circuito
import Analizador
import Maquina
import _thread
import network
from machine import Pin
from time import gmtime, sleep

#Instancia de los objetos 
maquina = Maquina.Maquina()
circuito = Circuito.Circuito(maquina)
analizador = Analizador.Analizador(maquina)

#Función ejecutándose en paralelo
def Lectura():
    global circuito
    global analizador
    while True:
        circuito.control_sensor_prox()
        analizador.actualizar_informacion()        
_thread.start_new_thread(Lectura, ())

# Función para manejar las solicitudes
def handle_request(client, analizador, circuito):
    #Cargar Datos del circuito en diccionario
    response = {
    'estado_maquina' : analizador.estado_maquina ,
    'tiempo_encendida' : analizador.tiempo_encendida ,
    'tiempo_total_encendida' : analizador.tiempo_total_encendida ,
    'led_maquina_apagada' : analizador.maquina.rgb_estado[0] ,
    'led_maquina_encendida' : analizador.maquina.rgb_estado[1] ,
    'velocidad_maquina' : analizador.maquina.velocidad_actual ,
    'led_velocidad_baja' : analizador.maquina.velocidad_leds[0] ,
    'led_velocidad_media' : analizador.maquina.velocidad_leds[1] ,
    'led_velocidad_alta' : analizador.maquina.velocidad_leds[2] ,
    'sensor_proximidad' : 1 if circuito.sensor_prox.value() == 0 else 0
    }
    
    # Convertir el diccionario a JSON
    json_data = json.dumps(response)
    
    # Enviar el contenido JSON
    client.send(json_data)

    # Cerrar la conexión
    client.close()

###########################################################
    
country = 'AR'
ssid = 'ssid_red_wifi'
password = 'password'
wifi_connection = wifi.connectWiFi(ssid,password,country)

#Establecer Conexión WiFi
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
###########################################################

#Bucle para tratar las peticiones
while True:
  try:
    cl, addr = s.accept()
    handle_request(cl, analizador, circuito)
  except OSError as e:
    cl.close()
    print('connection closed')