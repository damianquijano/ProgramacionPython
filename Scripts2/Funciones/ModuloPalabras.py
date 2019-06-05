#Módulo de Palabras
import math

def ultimaLetra(palabra):
    mensaje="La última letra es: " + palabra[-1]
    return (mensaje)

def verificarVocal(palabra):
    mensaje="No hay ninguna vocal."
    if "a" in palabra:
        mensaje="Existe al menos una vocal"
    if "e" in palabra:
        mensaje="Existe al menos una vocal"
    if "i" in palabra:
        mensaje="Existe al menos una vocal"
    if "o" in palabra:
        mensaje="Existe al menos una vocal"
    if "u" in palabra:
        mensaje="Existe al menos una vocal"
    return (mensaje)