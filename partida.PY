#Archivo con todos los demás archivos optimizados, con el fin de solucionar el problema de hilos en la Raspberry Pi Pico W
from machine import Pin
from time import sleep
import utime
import network
import socket
import _thread
import json

#########################################
class Maquina():
  def __init__(self):
    self.encendida = False
    self.clock_inicial = None
    self.sensor_prox = Pin(15, Pin.IN)
    self.rgb_estado = [Pin(2, Pin.OUT, value = 0), Pin(3, Pin.OUT, value = 0), Pin(4, Pin.OUT, value = 0)]
    self.relay = Pin(16, Pin.OUT, value = 1)
    self.velocidad_actual = 1.0
    self.velocidad_defecto = 1.0
    self.velocidad_leds = [Pin(20,Pin.OUT, value = 0), Pin(19,Pin.OUT, value = 0), Pin(18,Pin.OUT, value = 0)]
    self.encoder = {
                    'button_pin' : Pin(8, Pin.IN, Pin.PULL_UP),
                    'direction_pin' : Pin(6, Pin.IN, Pin.PULL_UP),
                    'step_pin' : Pin(7, Pin.IN, Pin.PULL_UP),
                    'previous_value' : True,
                    'button_down' : False
                    }
    
  def prender_maquina(self):
    self.encendida = True
    self.relay.value(0)
    self.rgb_estado[0].off()
    self.rgb_estado[1].on()
    self.velocidad_leds[0].on()

  def apagar_maquina(self):
    self.encendida = False
    self.relay.value(1)
    self.rgb_estado[0].on()
    self.rgb_estado[1].off()
    self.velocidad_leds[0].off()
    self.velocidad_leds[1].off()
    self.velocidad_leds[2].off()

  def control_encoder(self):
    movimiento = ""
    if self.encoder['previous_value'] != self.encoder['step_pin'].value():
        if self.encoder['step_pin'].value() == False:
            if self.encoder['direction_pin'].value() == False:
                movimiento = 'left'
            else:
                movimiento = 'right'
            self.ajustar_velocidad(movimiento)
        self.encoder['previous_value'] = self.encoder['step_pin'].value()   

    if self.encoder['button_pin'].value() == False and not self.encoder['button_down']:
        self.velocidad_actual = self.velocidad_defecto
        button_down = True
        if movimiento == "":
            self.ajustar_velocidad(False)
        
    if self.encoder['button_pin'].value() == True and self.encoder['button_down']:
        self.encoder['button_down'] = False

  def ajustar_velocidad(self, movimiento):
      if movimiento == 'left':
          if self.velocidad_actual > 1:
              self.velocidad_actual -= 0.1
      else:
          if movimiento == 'right':
              if self.velocidad_actual < 2.9:
                  self.velocidad_actual += 0.1
          else:
              self.velocidad_actual = self.velocidad_defecto
      #print(self.velocidad_actual)
      
      if self.velocidad_actual < 1.7:
          self.velocidad_leds[0].on()
          self.velocidad_leds[1].off()
          self.velocidad_leds[2].off()
      else:
          if self.velocidad_actual < 2.5:
              self.velocidad_leds[0].off()
              self.velocidad_leds[1].on()
              self.velocidad_leds[2].off()
          else:
              self.velocidad_leds[0].off()
              self.velocidad_leds[1].off()
              self.velocidad_leds[2].on()
    
##############################################

def connectWiFi(ssid,password):
  wlan = network.WLAN(network.STA_IF)
  #wlan.config(pm = 0xa11140)
  wlan.active(True)
  wlan.connect(ssid, password)
  # Wait for connect or fail
  max_wait = 10
  while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
      break
    max_wait -= 1
    print('waiting for connection...')
    sleep(1)

  # Handle connection error
  if wlan.status() != 3:
    raise RuntimeError('network connection failed')
  else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
  return status
#################################################
diccionario = [1,1,False]
  
def circuito_integrado():
    import utime
    global diccionario
    maquina = Maquina()
    clock_inicial = utime.ticks_ms()
    
    while True:
        lapso_tiempo = utime.ticks_diff(utime.ticks_ms(), clock_inicial)
        if lapso_tiempo > 250:
            if maquina.sensor_prox.value() == 0:
                maquina.clock_inicial = utime.ticks_ms()
                maquina.prender_maquina()
            clock_inicial = utime.ticks_ms()
        
        lapso_tiempo_maquina = utime.ticks_diff(utime.ticks_ms(), maquina.clock_inicial)
        if lapso_tiempo_maquina > 30000 and maquina.encendida:
            maquina.apagar_maquina()
        if lapso_tiempo_maquina < 30000:
            maquina.control_encoder()
        
        diccionario[0] = maquina.sensor_prox.value()
        diccionario[1] = maquina.velocidad_actual
        diccionario[2] = maquina.encendida

_thread.start_new_thread(circuito_integrado, ())

#Establecer la conexion WiFi
ssid = 'Fibertel WiFi 2.4 GHz'
password = 'Casa41491099'

wifi_connection = connectWiFi(ssid,password)
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)


#Manejar peticiones
clock_inicial = utime.ticks_ms()
contador = 0
while True:
    
  #circuito.control_sensor_prox()
  cl, addr = s.accept()
  print('Solicitud recibida desde:', addr)
  # Recibir los datos de la solicitud
  request_data = cl.recv(1024)
  request_str = request_data.decode('utf-8')  # Decodificar los datos

  mensaje = {
      "sensor_prox" : "No Detecto" if diccionario[0] == 1 else "Detecto",
      "velocidad_maquina" : diccionario[1] * 5,
      "estado_maquina" : "Encendida" if diccionario[2] else "Apagada"
      }
  mensaje2 = json.dumps(mensaje)

  # Si la solicitud es un GET
  if request_str.startswith('GET'):
      # Enviar la respuesta con el estado actual del LED
      response = f"HTTP/1.1 200 OK\nContent-Type: text/plain\n\n{mensaje2}"
      cl.send(response.encode('utf-8'))

  cl.close()  # Cerrar la conexión
