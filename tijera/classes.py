import pygame as p
from variables import *

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

    def movimiento(self, event):
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                self.velocidad = -3
            if event.key == p.K_RIGHT:
                self.velocidad = 3
        #soltar el teclado
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                self.velocidad = 0
            if event.key == p.K_RIGHT:
                self.velocidad = 0   

class carretera():#predibujar
    def __init__(self) -> None:
        self.grosor     : int = 100
        self.centro     : int = (size[0]/2)
        self.x          : int = self.centro - self.grosor/2
        self.y          : int = 0
        self.limite_izq : int = self.x + 1
        self.limite_der : int = self.x + self.grosor -2
        self.lineas_cortas : list = carretera.generarLineasCortas()
    
    def dibujarCalle(self):
        #calle
        p.draw.rect(Screen, negro, [self.x, self.y, self.grosor, size[1]]) 
        
        #lineas delimitadoras
        p.draw.line(Screen, amarillo, [self.limite_izq,0], [self.limite_izq,400])
        p.draw.line(Screen, amarillo, [self.limite_der,0], [self.limite_der,400])

    def generarLineasCortas():
        lineas_cortas : list = []
        for i in range(int((400-5/40))):
            lineas_cortas.append(i*40)
        return lineas_cortas
    
    def animacionLineasCortas(self):
        for a in range(len(self.lineas_cortas)):
            self.lineas_cortas[a] += 2
            if self.lineas_cortas[a] > 400:
                self.lineas_cortas[a] = -35
            p.draw.rect(Screen, blanco, [((size[0])/2)-5, self.lineas_cortas[a], 8, 20])