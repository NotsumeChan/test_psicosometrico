import pygame as p
import sys    as s
import math   as m
import os     as os
from datetime import datetime

p.init()

#definir colores

blanco  = (255,255,255)
verde   = (  0,255,  0)
rojo    = (255,  0,  0)
negro   = (  0,  0,  0)
amarillo= (255,255,  0)
celeste = (  0,170,228)
gris    = (165,165,165)

#variables

size = [600,400] #ancho, altura
Screen = p.display.set_mode(size)
clock = p.time.Clock()

class personaje():
    def __init__(self):
        #caracteristicas
        self.ancho_ruedas : int = 36
        self.largo_ruedas : int = 10
        self.ancho_player : int = 30
        self.largo_player : int = 40 
        self.ancho_player : int = 30
        self.largo_player : int = 40 
        
        #cordenadas
        self.x            : int = 300
        self.y            : int = 300
        
        #velocidad
        self.velocidad    : int = 0
        
        
    def dibujar(self):
        #ruedas
        ancho_ruedas : int = 36
        largo_ruedas : int = 10
        p.draw.rect(Screen,    gris, [self.x-3, self.y+5 , ancho_ruedas  , largo_ruedas  ])
        p.draw.rect(Screen,    gris, [self.x-3, self.y+25, ancho_ruedas  , largo_ruedas  ])
        
        #cuerpo principal
        p.draw.rect(Screen,    rojo, [self.x  , self.y  , self.ancho_player   , self.largo_player  ])
        p.draw.rect(Screen, celeste, [self.x+2, self.y+1, self.ancho_player -4, self.largo_player/4])

class carretera():#predibujar
    def __init__(self) -> None:
        self.grosor     : int = 100
        self.centro     : int = (size[0]/2)
        self.x          : int = self.centro - self.grosor/2
        self.y          : int = 0
        self.limite_izq : int = self.x + 1
        self.limite_der : int = self.x + self.grosor -2
    
    def dibujar(self):
        #calle
        p.draw.rect(Screen, negro, [self.x, self.y, self.grosor, size[1]]) 
        
        #lineas delimitadoras
        p.draw.line(Screen, amarillo, [self.limite_izq,0], [self.limite_izq,400])
        p.draw.line(Screen, amarillo, [self.limite_der,0], [self.limite_der,400])



def main():
    #generar instancias
    player = personaje()
    calle = carretera()
    
    #generar lineas
    lineas_cortas : list = []
    for i in range(int((400-5/40))):
        lineas_cortas.append(i*40)
    
    #variables extras
    reset = True
    errores : int = 0
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
                s.exit()
                
            #tocar el teclado    
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    player.velocidad = -3
                if event.key == p.K_RIGHT:
                    player.velocidad = 3
            #soltar el teclado
            if event.type == p.KEYUP:
                if event.key == p.K_LEFT:
                    player.velocidad = 0
                if event.key == p.K_RIGHT:
                    player.velocidad = 0    
            print(f"errores: {errores}")
        
        #pintar la pantalla verde
        Screen.fill(verde)
        #pintar la carretera
        calle.dibujar()
        
        
        #lineas blancas
        for a in range(len(lineas_cortas)):
            lineas_cortas[a] += 2
            if lineas_cortas[a] > 400:
                lineas_cortas[a] = -35
            p.draw.rect(Screen, blanco, [((size[0])/2)-5, lineas_cortas[a], 8, 20])
        ##

        #movimiento
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
            
        if player.x > calle.limite_izq +4 and player.x < calle.limite_der -33:
            reset = True
                
        #auto
        player.dibujar()
        
        #reset pantalla
        p.display.flip()
        clock.tick(60)

        
if __name__ == '__main__':
    main()
