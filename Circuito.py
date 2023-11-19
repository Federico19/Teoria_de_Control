from machine import Pin
from time import gmtime

class Circuito():
  def __init__(self, maquina):
    self.sensor_prox = Pin(15, Pin.IN)
    self.led_prox = Pin(19, Pin.OUT)
    self.maquina = maquina
    self.control_tiempo = -1
  
  def control_sensor_prox(self):
    if self.sensor_prox.value() == 0:
        self.led_prox.on()
        control_reloj = gmtime()[5]
        if control_reloj > 29:
            self.control_tiempo = control_reloj - 30
        else:
            self.control_tiempo = control_reloj + 30
        self.maquina.prender_maquina()

    control_reloj = gmtime()[5]
    if self.control_tiempo  == control_reloj:
        self.control_tiempo = -1
        self.maquina.apagar_maquina()
    
    self.maquina.control_encoder()