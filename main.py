import pygame as p
import sys    as s
import os     as os
from datetime import datetime
from classes import *
from variables import *

p.init()

def main():
    #generar instancias
    player = personaje()
    calle = carretera()
    
    #generar lineas cetrales de la calle
    lineas_cortas : list = []
    for i in range(int((400-5/40))):
        lineas_cortas.append(i*40)
    
    #variables extras
    reset = True
    errores : int = 0
    erroresAux : int = 0
    timmer : int = 0
    fps : int = 60
    inicio = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    while True:
        #buscador de eventos
        for event in p.event.get():
            #cerrar el programa
            if event.type == p.QUIT:
                #guardar datos archivo externo
                with open(f"{os.getcwd()}/erroes.txt", "a") as file:#cambiar la ruta
                    fin = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    file.write(f"\n=========================\nhora inicio:  {inicio}\nhora termino: {fin}\nerrores totales:{errores}\n=========================")
                #cerrar el programa
                s.exit()
                
            #movimiento jugador
            player.movimiento(event)
 
            
        
        #pintar la pantalla verde
        Screen.fill(verde)
        #pintar la carretera
        calle.dibujar()
        
        
        #pintar lineas blancas
        for a in range(len(lineas_cortas)):
            lineas_cortas[a] += 2
            if lineas_cortas[a] > 400:
                lineas_cortas[a] = -35
            p.draw.rect(Screen, blanco, [((size[0])/2)-5, lineas_cortas[a], 8, 20])
        ##


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

        
if __name__ == '__main__':
    main()
