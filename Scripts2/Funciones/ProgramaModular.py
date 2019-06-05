import sys
import ModuloPalabras
import ModuloMatematicas

#Programa principal

print("\t\n")
print("Seleccione una opción del menú(un número entero).\t\n")
print("Imprimir la última letra de una palabra: seleccione 1.\t\n")
print("Verificar si existe al menos una vocal en una palabra: seleccione 2.\t\n")
print("Calcular perímetro de un pentágono: seleccione 3.\t\n")
print("Calcular el volumen de un  cilindro: seleccione 4.\t\n")
print("\t\n")

try:
    opcion=int(input("Escoja una opción: 1 / 2 /3 / 4-> "))
except:
    print("Usted no ha introducido un valor numérico entero al seleccionar una opción.\t\nEl programa terminó")
    sys.exit(0)
if opcion < 1 or opcion > 4:
    print("Usted no ha introducido un valor entre 1(incluido)  y 4(incluido) para seleccionar una opción.\t\nEl programa terminó")
    sys.exit(0)
    
    
if opcion==1:
    palabra= input("Introduzca una palabra: ")
    if len(palabra)>0:
        ultima=ModuloPalabras.ultimaLetra(palabra)
        print(ultima)
    else:
        print("Usted no ha introducido ninguna palabra")

if opcion==2:
    palabra= input("Introduzca una palabra: ")
    resultado= ModuloPalabras.verificarVocal(palabra)
    print( resultado)

if opcion==3:
    try:
        lado=float(input("Introduzca el valor del lado del pentágono, debe ser mayor a 0: "))
    
    except:
        print("\t\nUsted no ha introducido un valor númerico en algún valor usado para la ecuación.\t\nEL programa se detendrá.")
        sys.exit(0)         
    
    if lado<=0:
        print("\t\nUsted ha introducido un valor númerico igual o menor a cero.\t\nEL programa se detendrá.")
        sys.exit(0)  
    
    resultado= ModuloMatematicas.perimetro(lado)
    print("El perímetro del pentágono es: ",resultado) 

if opcion==4:
    try:
        radio=float(input("Introduzca el valor del radio del cilindro, debe ser mayor a 0: "))
        altura=float(input("Introduzca el valor de la altura del cilindro, debe ser mayor a 0: "))
    
    except:
        print("\t\nUsted no ha introducido un valor númerico en algún valor usado para la ecuación.\t\nEL programa se detendrá.")
        sys.exit(0)         
    
    if radio<=0 or altura<=0:
        print("\t\nUsted ha introducido un valor númerico igual o menor a cero.\t\nEL programa se detendrá.")
        sys.exit(0)  
    
    resultado= ModuloMatematicas.volumen(radio,altura)
    print("El volumen del cilindro es: ",resultado)    

print("\t\nFin del programa.")