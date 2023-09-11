from machine import Pin
from time import gmtime

class Maquina():
  def __init__(self):
    self.encendida = False
    self.rgb_estado = [Pin(2, Pin.OUT, value = 0), Pin(3, Pin.OUT, value = 0), Pin(4, Pin.OUT, value = 0)]
    self.relay = Pin(16, Pin.OUT, value = 00)
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
    self.relay.value(1)
    self.rgb_estado[0].off()
    self.rgb_estado[1].on()

  def apagar_maquina(self):
    self.encendida = False
    self.relay.value(0)
    self.rgb_estado[0].on()
    self.rgb_estado[1].off()

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
      print(self.velocidad_actual)
    
      self.velocidad_leds[0].off()
      self.velocidad_leds[1].off()
      self.velocidad_leds[2].off()
      
      if self.velocidad_actual < 1.7:
          self.velocidad_leds[0].on()
      else:
          if self.velocidad_actual < 2.5:
              self.velocidad_leds[1].on()
          else:
              self.velocidad_leds[2].on()