import pygame as p
import sys
import os
sys.path.append(f"{os.getcwd()}/reactimetro")

p.init()

def reactimetro():
    #variables
    screen = p.display.set_mode((800, 600))
    #main loop
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
        screen.fill((255,255,255))
        p.display.flip()