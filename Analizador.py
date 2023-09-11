from time import gmtime
import sys

class Analizador():
    def __init__(self, maquina):
        self.maquina = maquina
        self.estado_maquina = 'Apagada'
        self.hora_encendio = 0
        self.hora_apago = 0
        self.tiempo_encendida = 0
        self.tiempo_total_encendida = 0
        self.rangos_tiempo_encendido = [0]
        self.veces_encendida = 0
        self.promedio_tiempos_encendida = 0
        self.minimo_tiempo_encendida = 0
        self.maximo_tiempo_encendida = 0
        self.tiempo_cero = gmtime()[5]
  
    def paso_un_segundo(self):
        if self.tiempo_cero != gmtime()[5]:
            self.tiempo_cero = gmtime()[5]
            return True
        else:
            return False

    def pasar_a_segundos(self,hora):
        return hora[0]*3600 + hora[1]*60 + hora[2]

    def actualizar_informacion(self):
        if self.paso_un_segundo():
            if self.maquina.encendida:
                self.estado_maquina = 'Encendida'
                self.tiempo_encendida += 1
                self.tiempo_total_encendida += 1
            else:
                if self.estado_maquina != 'Apagada':
                    self.rangos_tiempo_encendido.append(self.tiempo_encendida)
                self.tiempo_encendida = 0
                self.estado_maquina = 'Apagada'
            
            #self.enviar_info_serial()
            #self.enviar_informacion()
    
    def enviar_info_serial(self):
        sys.stdout.write(self.estado_maquina+'\n')
        sys.stdout.write(str(self.tiempo_encendida)+'\n')
        sys.stdout.write(str(self.tiempo_total_encendida)+'\n')
        #sys.stdout.write(str(self.maquina.velocidad_actual)+'\n')
        
    def enviar_info_wifi(self):
        pass
        
    def enviar_informacion(self):
        print('Estado maquina: ', self.estado_maquina)
        print('Tiempo encendida: ', self.tiempo_encendida)
        print('Tiempo total encendida: ', self.tiempo_total_encendida)