import pygame as p
import sys    as s
import os     as os
from datetime import datetime

s.path.append(f"{os.getcwd()}")


from classes import *
from variables import *

p.init()
clock = p.time.Clock()

def tijera():
    #generar instancias
    player = personaje()
    calle = carretera()
    
    #variables extras
    reset      : bool = True #NO repetir errores ya cometidos
    errores    : int = 0     #contador de errores
    erroresAux : int = 0     #comparador para mostrar por consola
    timmer     : int = 0     #timmer para mostrar mensaje de error cometido
    fps        : int = 60    #limitador de fps
    inicio           = datetime.now().strftime('%d/%m/%Y %H:%M:%S')#formato fecha/hora
    
    name : str = input("ingrese nombre alumno: ")

    while True:
        #buscador de eventos
        for event in p.event.get():
            #cclick boton cerrar ventana
            if event.type == p.QUIT:
                #guardar datos archivo externo
                with open(f"{os.getcwd()}/tijera/HistorialTijera.txt", "a") as file:#ruta dinamica del archivo de registro
                    fin = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    file.write(f"\n============{name}============\nhora inicio:  {inicio}\nhora termino: {fin}\nerrores totales:{errores}\n=========================")
                #cerrar el programa
                s.exit()
                
            #movimiento jugador
            player.movimiento(event)
 
            
        
        #pintar la pantalla verde
        Screen.fill(verde)
        #pintar la carretera
        calle.dibujarCalle()
        #pintar lineas blancas
        calle.animacionLineasCortas()

        #colision jugador
        #tratar de ver como agregarlo a una funcion para que sea mas facil de leer
        if player.x >= calle.limite_izq and player.x <= calle.limite_der:
            player.x += player.velocidad
            
        if player.x < calle.limite_izq+2:
            player.x = calle.limite_izq+2
            
        if player.x > calle.limite_der-31:
            player.x = calle.limite_der-31
            
        #contador errores
        if reset:
            if player.x <= calle.limite_izq +3:
                errores += 1
                reset = False
                
            if player.x >= calle.limite_der -32:
                errores += 1
                reset = False

        #reset contador errores    
        if player.x > calle.limite_izq +4 and player.x < calle.limite_der -33:
            reset = True
                
        #pintar auto
        player.dibujar()
        
        #update pantalla
        
        os.system('cls')
        
        if erroresAux != errores :
            timmer = 120

        if timmer > 0:
            print("ups te saliste")
            erroresAux = errores

        timmer -= 1
        if timmer < 0: timmer = 0
        print(f"errores totales: {errores}")


        p.display.flip()
        clock.tick(fps)


tijera()