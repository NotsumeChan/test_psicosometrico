import sys
import os
import flet as ft
from flet_core.control_event import ControlEvent

sys.path.append(os.getcwd())

from audio import audio
from punteo import punteo
from reactimetro import reactimetro
from tijera import tijera
from visual import visual

def main(page : ft.Page)  -> None:
    page.title = "Test Psicosométrico"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"
    

    page.add(
        ft.Container(
            ft.Column(

                [ft.TextButton("Audio", on_click=audio.audio()),
                ft.TextButton("Punteo", on_click=punteo.punteo()),
                ft.TextButton("Reactimetro", on_click=reactimetro.reactimetro()),
                ft.TextButton("Tijera", on_click=tijera()),
                ft.TextButton("Visual", on_click=visual.visual())],
                alignment=ft.MainAxisAlignment.START

            )
        )
    )
    
if __name__ == '__main__':
    ft.app(target=main)