import sys
import os
import tkinter as tk
from tkinter import ttk

sys.path.append(os.getcwd())

from audio import audio
from punteo import punteo
from reactimetro import reactimetro
from tijera import tijera
from visual import visual


def ejecutar(x):
    #ejecuta test segun boton seleccionado
    if x == 0:
        audio()
    elif x == 1:
        punteo()
    elif x == 2:
        reactimetro()
    elif x == 3:
        tijera()
    elif x == 4:
        visual()
    pass

def main():
    #crea menu con botones con tkinter para ejecutar los test
    root = tk.Tk()
    root.title('TEST PSICOSOMETRICO')
    root.geometry('300x300')
    root.configure(bg='white')
    root.resizable(0,0)
    #crear lista de botones
    botones = ['Audio', 'Punteo', 'Reactimetro', 'Tijera', 'Visual']
    #mostrar botones
    for i in range(len(botones)):
        ttk.Button(root, text=botones[i], command=lambda x=i: ejecutar(x)).pack(pady=10)
    pass

if __name__ == '__main__':
    main()