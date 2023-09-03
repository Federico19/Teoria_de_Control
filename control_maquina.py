from machine import Pin
import time
from fechas import indicadores_tiempo

dic ={
    'inicio_dia' : True,
    'time_count': 0,
    'sensor_count': 0,
    'veces_apago_maquina' : 0,
    'veces_encendio_maquina' : 0 ,
    'maquina_encendida' : False,
    'sensor_proximidad' : Pin(16, Pin.IN),
    'relay' : Pin(17, Pin.OUT),
    'red' : Pin(20, Pin.OUT),
    'green' : Pin(19, Pin.OUT),
    'blue' : Pin(18, Pin.OUT),
    'led' : Pin(15, Pin.OUT),
    'hora_inicia' : None,
    'hora_apaga' : None
}


def prender_maquina(dic):
    if dic['sensor_count'] > 0:
        #Enciendo la maquina
        dic['hora_inicia'] = time.gmtime()[3:6]
        dic['relay'].value(1)
        dic['maquina_encendida'] = True
        dic['veces_encendio_maquina'] += 1
        dic['red'].off()
        dic['green'].on()
        dic['time_count'] , dic['sensor_count'] = 0,0


def apagar_maquina(dic):
    if dic['time_count'] >=30:
        print('=========Tiempo==========')
        if dic['sensor_count'] < 5:
            #Apago la maquina
            dic['hora_apaga'] = time.gmtime()[3:6]
            indicadores_tiempo(dic['hora_inicia'], dic['hora_apaga'])
            
            dic['relay'].value(0)
            dic['maquina_encendida'] = False
            dic['veces_apago_maquina'] += 1
            dic['red'].on()
            dic['green'].off()

        dic['time_count'] , dic['sensor_count'] = 0,0


def control_estado_maquina(dic):
    if dic['maquina_encendida']:
        apagar_maquina(dic)
    else:
        prender_maquina(dic)


while True:
    if dic['inicio_dia']:
        dic['inicio_dia'] = False
        dic['sensor_count'] += 1
        prender_maquina(dic)
        
    if dic['sensor_proximidad'].value() == 0:
        dic['sensor_count'] += 1
        dic['led'].on()

    control_estado_maquina(dic)

    time.sleep(0.2)
    dic['time_count'] += 0.2
        
    if int(dic['time_count']) == 10 or int(dic['time_count']) == 20 or  int(dic['time_count'])== 30:
        print(dic['time_count'])
    dic['led'].off()