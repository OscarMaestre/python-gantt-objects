#!/usr/bin/env python3

import datetime

LUNES       =   0
MARTES      =   1
MIERCOLES   =   2
JUEVES      =   3
VIERNES     =   4
SABADO      =   5
DOMINGO     =   6

class Tarea(object):
    def __init__(self, nombre, duracion_en_dias, fecha_inicio=None):
        self.nombre             =   nombre
        self.duracion_en_dias   =   duracion_en_dias
        self.fecha_inicio       =   fecha_inicio
    
    def get_num_dia_inicio(self):
        num_dia=self.fecha_inicio.weekday()
        return num_dia
    
    def get_num_mes_inicio(self):
        num_dia=self.fecha_inicio.month
        return num_dia    
    def get_anio_inicio(self):
        num_anio = self.fecha_inicio.year
        return num_anio
        
    def get_nombre_dia_inicio(self):
        num_dia=self.fecha_inicio.weekday()
        dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        return dias[num_dia]
    
    def get_nombre_mes_inicio(self):
        num_mes = self.get_num_mes_inicio()
        meses = ["Relleno", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                 "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        return meses[num_mes]
    
    def __str__(self):
        cadena = self.nombre + "--->" + str(self.get_num_dia_inicio()) + "-"+self.get_nombre_mes_inicio()+ "-"+str(self.get_anio_inicio())
        return cadena
    
    
        
        
def es_navidad(objeto_fecha):
    numero_de_mes   =   objeto_fecha.month
    numero_de_dia   =   objeto_fecha.day
    #Vacaciones de Navidad
    if ( numero_de_dia > 20 and numero_de_mes==12) and (numero_de_dia<11 and numero_de_mes==1):
        return True
    return False


def hay_clase(objeto_fecha):
    if objeto_fecha.weekday()==DOMINGO:
        return False
    if objeto_fecha.weekday()==SABADO:
        return False
    if es_navidad(objeto_fecha) :
        return False
    
    if objeto_fecha.weekday()==MARTES:
        return True
    if objeto_fecha.weekday()==VIERNES:
        return True
    
    return False

#Dada una fecha y un número de dias de clase nos dice la fecha de la siguiente clase
def siguiente_dia_de_clase(fecha_inicio, numero_de_dias_de_clase):
    contador_dias = 0
    objeto_dia = datetime.timedelta( days = 1)
    
    while contador_dias < numero_de_dias_de_clase +1 :
        fecha_inicio = fecha_inicio + objeto_dia
        if hay_clase(fecha_inicio):
            contador_dias = contador_dias +1
    return fecha_inicio

def ajustar_fechas_inicio_tareas(tareas):
    for pos, tarea in enumerate(tareas):
        nombre          =   tarea.nombre
        fecha_inicio    =   tarea.fecha_inicio
        if fecha_inicio==None:
            tarea_anterior              =   tareas[pos-1]
            fecha_inicio_tarea_anterior =   tarea_anterior.fecha_inicio
            duracion_tarea_anterior     =   tarea_anterior.duracion_en_dias
            #Se ajusta la fecha de inicio de la tarea en funcion de la duracion de la tarea anterior
            tarea.fecha_inicio = siguiente_dia_de_clase(fecha_inicio_tarea_anterior, duracion_tarea_anterior)
    return tareas

tareas=[
    Tarea("Tema 1", 8, datetime.date(2018,9,27) ),
    Tarea("Tema 2", 10),
    Tarea("Tema 3", 1),
]

tareas = ajustar_fechas_inicio_tareas(tareas)

for pos, tarea in enumerate ( tareas ):
    print (tarea)