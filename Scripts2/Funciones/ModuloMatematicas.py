#Módulo de Matemáticas

import math

def perimetro(lado):
    perimetro= lado *5
    return (round(perimetro,2))
    
def volumen(radio, altura):
    volumen= math.pi * (math.pow(radio,2)) * altura
    return ( round(volumen,2))