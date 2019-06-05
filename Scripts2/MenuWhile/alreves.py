#Librerías
import sys

#Variables
alreves=""
contador=0

#Programa
palabra=input("Introduzca una palabra: ")
long=len(palabra)
if long==0:
    print("Usted no ha introducido ninguna palabra")
    sys.exit()

while contador < long:
    alreves=palabra[contador]+alreves  
    contador=contador +1
print(alreves)

alreves=""
for i in range(0,long):
   alreves=palabra[i] + alreves
print(alreves)    

    