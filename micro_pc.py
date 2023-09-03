# import time
# hora = time.gmtime()[3:6] #Devuelve hora --> [hh,mm,ss]
indicadores = {
    'tiempo_maquina_encendida' : 0,
    'intervalos_tiempo_encendida' : [],
    'tiempo_minimo_encendida': 0,
    'tiempo_maximo_encendida': 0,
    'tiempo_promedio_encendida': 0
}

def pasar_a_minutos(hora):
    return hora[0]*60 + hora[1] + hora[2]/60

def enviar_terminal(indicadores):
    print(indicadores)
    
def indicadores_tiempo(hora_inicia, hora_apaga):
    global indicadores
    rango_tiempo = pasar_a_minutos(hora_apaga) - pasar_a_minutos(hora_inicia)
    indicadores['tiempo_maquina_encendida'] += rango_tiempo
    indicadores['intervalos_tiempo_encendida'].append(rango_tiempo)
    indicadores['tiempo_minimo_encendida'] = min(indicadores['intervalos_tiempo_encendida'])
    indicadores['tiempo_maximo_encendida'] = max(indicadores['intervalos_tiempo_encendida'])
    indicadores['tiempo_promedio_encendida'] = sum(indicadores['intervalos_tiempo_encendida']) / len(indicadores['intervalos_tiempo_encendida'])
    enviar_terminal(indicadores)

#Para enviar info desde la Micro a la PC
"""
from machine import Pin
import _thread
import sys
import time

contador = 0 #esto seria la info...

while True:
    cadena = str(contador)
    sys.stdout.write(cadena+"\r\n")
    contador += 1
"""