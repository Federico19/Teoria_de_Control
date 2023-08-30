from machine import Pin
import utime

# Variables del sensor y del relay
relay = Pin(17, Pin.OUT)
sensor = Pin(16, Pin.IN)

# Variables del encoder
button_pin = Pin(15, Pin.IN, Pin.PULL_UP)
direction_pin = Pin(12, Pin.IN, Pin.PULL_UP)
step_pin  = Pin(14, Pin.IN, Pin.PULL_UP)
previous_value = True
button_down = False

while True:
"""
# Control del encoder
    #print("dir", direction_pin.value(), "step", step_pin.value(), "button", button_pin.value())

     if previous_value != step_pin.value():
         if step_pin.value() == False:
             if direction_pin.value() == False:
                 print("turned left")
             else:
                 print("turned right")
         previous_value = step_pin.value()   
   
     if button_pin.value() == False and not button_down:
         print("button pushed") 
         button_down = True
     if button_pin.value() == True and button_down:
         button_down = False

     #if button_pin.value() == False:
      #   print("button pressed")
      
#control del sensor en conjunto con el rele
  if sensor.value() == 1:
    print('Arranco)')
    relay.value(1)
  else:
    relay.value(0)
  
  utime.sleep(3)

#control del led RGB
r = Pin(16,Pin.OUT)
g = Pin(17,Pin.OUT)
b = Pin(18,Pin.OUT)

b.on()
r.on()
g.on()
"""
