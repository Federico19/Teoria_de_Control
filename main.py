import wifi
import socket
import json
import sys
import Circuito
import Maquina
import _thread
import network
from machine import Pin
from time import gmtime, sleep

#Instancia de los objetos 
maquina = Maquina.Maquina()
circuito = Circuito.Circuito(maquina)

#Función ejecutándose en paralelo
def Lectura():
    global circuito
    while True:
        circuito.control_sensor_prox()       
_thread.start_new_thread(Lectura, ())

# Función para manejar las solicitudes
def manejar_peticion(client, circuito):
  # Recibir los datos de la solicitud
  request_data = cl.recv(1024)
  request_str = request_data.decode('utf-8')  # Decodificar los datos

  datos = {
      "sensor_prox" : "No Detecto" if circuito.sensor_prox.value() else "Detecto",
      "velocidad_maquina" : maquina.velocidad_actual,
      "estado_maquina" : "Encendida" if maquina.encendida else "Apagada"
      }
    
  mensaje = json.dumps(datos)

  # Si la solicitud es un GET
  if request_str.startswith('GET'):
      # Enviar la respuesta con el estado actual del LED
      response = f"HTTP/1.1 200 OK\nContent-Type: text/plain\n\n{mensaje}"
      cl.send(response.encode('utf-8'))

  cl.close()  # Cerrar la conexión

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
    manejar_peticion(cl, circuito)
  except OSError as e:
    cl.close()
    print('connection closed')
