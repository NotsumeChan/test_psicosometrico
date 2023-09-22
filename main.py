import sys
import os

user = os.getlogin()
sys.path.append(f'C:\Users\{user}\Documents\proyectos personales\python\VISUAL PSICOSOMETRICO')

from audio import audio
from punteo import punteo
from reactimetro import reactimetro
from tijera import tijera
from visual import visual


def main():
    #crea menu con botones con tkinter para ejecutar los test

    pass

if __name__ == '__main__':
    main()