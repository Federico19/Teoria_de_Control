import pygame, sys, serial

def enviar_decicison_micro(decision):
    print(decision)
    sys.stdout.write(decision+"\r\n")

pygame.init()

Rpi= serial.Serial(port = "COM8", baudrate=115200)
try:
    Rpi.Open()
    print("Conectado")
except:
 #   Rpi.close()
    if(Rpi.isOpen()):
        print("Conectado")
    else:
        print("No conectado")

blanco = (255,255,255)
negro = (0,0,0)
ROJO = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Ventana
ventana = pygame.display.set_mode((800, 500))
fuente = pygame.font.SysFont("Consolas", 18)

#Boton
#boton = pygame.Rect(20,110,200,40)

while True:
  if (Rpi.isOpen()):
    # Envio de Informacion
    # Esto se recibe en bytes.
    estado_maquina_by = Rpi.readline() 
    tiempo_encendida_by = Rpi.readline()
    tiempo_total_encendida_by = Rpi.readline()
    #velocidad_by = Rpi.readline()

    # Conversión de Byte a String
    estado_maquina = estado_maquina_by.decode('UTF-8')[:-2]
    tiempo_encendida = tiempo_encendida_by.decode('UTF-8')[:-2]
    tiempo_t_encendida = tiempo_total_encendida_by.decode('UTF-8')[:-2]
    #velocidad = velocidad_by.decode('UTF-8')[:-2]

    cadena_estado_maquina = 'Estado de la máquina: ' + estado_maquina
    cadena_t_encendida = 'Tiempo que la máquina lleva encendida: ' + tiempo_encendida
    cadena_t_t_encendida = 'Tiempo total que la máquina lleva encendida: ' + tiempo_t_encendida
    #cadena_velocidad = 'Velocidad de la máquina: ' + velocidad
    
    info_estado = fuente.render(cadena_estado_maquina, True, blanco)
    info_t_encendida = fuente.render(cadena_t_encendida, True, blanco)
    info_t_t_encendida = fuente.render(cadena_t_t_encendida, True, blanco)
    #info_velocidad = fuente.render(cadena_velocidad, True, blanco)
   
    # Pintamos sobre la ventana la info.
    ventana.fill(negro)
    ventana.blit(info_estado, (20, 20))
    ventana.blit(info_t_encendida, (20, 40))
    ventana.blit(info_t_t_encendida, (20, 60))
    #ventana.blit(info_velocidad, (20, 80))

    # Boton
    """
    opcion = ''
    if estado_maquina == 'Apagada':
      opcion = 'Encender'
    else:
       opcion = 'Apagar'

    if boton.collidepoint(pygame.mouse.get_pos()):
      pygame.draw.rect(ventana, verde, boton, 0)
    else:      
      pygame.draw.rect(ventana, azul, boton, 0)
    mensaje = fuente.render(opcion + ' Máquina' , True, blanco)
    ancho = boton.x + (boton.width - mensaje.get_width())/2 
    alto = boton.y + (boton.height - mensaje.get_height())/2 
    ventana.blit(mensaje, (ancho, alto))
    """

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #  enviar_decicison_micro(opcion)

    # Actualizamos
    pygame.display.update()
