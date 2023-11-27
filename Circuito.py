from machine import Pin
import utime

class Circuito():
  def __init__(self, maquina):
    self.sensor_prox = Pin(15, Pin.IN, value = 1)
    self.led_prox = Pin("LED", Pin.OUT)
    self.maquina = maquina
  
  def control_sensor_prox(self):
    if self.sensor_prox.value() == 0:
        self.led_prox.on()
        self.maquina.prender_maquina()
        self.maquina.clock_inicial = utime.ticks_ms()
    else:
        self.led_prox.off()
    
    lapso_tiempo = utime.ticks_diff(utime.ticks_ms(), self.maquina.clock_inicial)

    if self.maquina.encendida:
      if lapso_tiempo > 30000:
         self.maquina.apagar_maquina()
      self.maquina.control_encoder()
