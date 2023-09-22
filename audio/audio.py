from pydub import AudioSegment
import numpy as np
import pygame
import tempfile
import os

def audio(duracion_ms, volumen, tono, direccion):
    # Configura las características del pitido
    frecuencia = 440 if tono == "agudo" else 220  # Cambia la frecuencia para agudo o grave
    volumen = volumen / 100.0  # Normaliza el volumen en un rango de 0 a 1
    
    # Genera el pitido usando numpy
    tiempo = np.linspace(0, duracion_ms / 1000, int(duracion_ms * 44.1))
    onda = np.sin(2 * np.pi * frecuencia * tiempo)
    
    # Aplica el volumen
    onda = (onda * volumen).astype(np.int16)
    
    # Crea el segmento de audio con pydub
    pitido = AudioSegment(onda.tobytes(), frame_rate=44100, sample_width=onda.dtype.itemsize, channels=1)

    # Aplica la dirección (izquierda o derecha)
    if direccion == "izquierda":
        pitido = pitido.pan(-1)
    elif direccion == "derecha":
        pitido = pitido.pan(1)
    
    # Guarda el pitido en un archivo temporal
    tmp_filename = tempfile.mktemp(suffix=".wav")
    pitido.export(tmp_filename, format="wav")

    # Inicializa Pygame para reproducir el sonido
    pygame.init()
    pygame.mixer.init()

    try:
        # Carga el sonido y lo reproduce
        sound = pygame.mixer.Sound(tmp_filename)
        sound.play()
        pygame.time.wait(duracion_ms+100)  # Espera hasta que termine el sonido
    finally:
        # Limpia los recursos de Pygame y elimina el archivo temporal
        pygame.mixer.quit()
        pygame.quit()
        os.remove(tmp_filename)

# Ejemplo de uso
duracion_ms = 1000  # Duración en milisegundos
volumen = 100  # Volumen (0-100)
tono = "agudo"  # Tono ("agudo" o "grave")
direccion = "derecha"  # Dirección ("izquierda" o "derecha")

