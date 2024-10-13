import random
from pyfiglet import Figlet

figlet = Figlet()

fuentes_disponibles = figlet.getFonts()

fuente_seleccionada = input("Introduce el nombre de la fuente (presiona Enter para elegir una aleatoria): ")

if not fuente_seleccionada:
    fuente_seleccionada = random.choice(fuentes_disponibles)

if fuente_seleccionada not in fuentes_disponibles:
    print("Fuente no válida. Se seleccionará una fuente aleatoria.")
    fuente_seleccionada = random.choice(fuentes_disponibles)

figlet.setFont(font=fuente_seleccionada)

texto_imprimir = input("Introduce el texto que desees: ")

print(figlet.renderText(texto_imprimir))
