from machine import Pin
import sys

led = Pin("LED", Pin.OUT)

#Comunicación serial USB, PC --> Microcontrolador
contador = 0
while True:
    cadena = str(contador)
    sys.stdout.write(cadena+"\r\n")
    contador += 1

    x=str(sys.stdin.readline())
    try:
        if x[0] == '1':
            led.on()
            sys.stdout.write("Led prendido \r\n")
            
        else:
            if x[0] == '2':
                led.off()
                sys.stdout.write("Led apagado \r\n")
    except:
        print("Seee rompio")