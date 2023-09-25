import pygame as p

p.init()

def Reactimetro():
    #variables
    screen = p.display.set_mode((800, 600))
    #main loop
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
        screen.fill((255,255,255))
        p.display.flip()
                
Reactimetro()
