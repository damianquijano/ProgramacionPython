#Calculadora básica con bucle while
opciones=["1","2","3"]
while True:
    print(''' 
    Seleccione una acción(1,2 o 3):
    1.Sumar.
    2.Restar.
    3.Salir.
    ''')
    opcion=input("Introduce opción: ")
    if not(opcion in opciones):
        print("No seleccionó ninguna opción válida")
        input("Pulse para continuar.")
        continue
    if opcion=="1":
        try:
            valor1=float(input("valor1-> "))
            valor2=float(input("valor2-> "))
            suma=valor1 + valor2
            print("La suma es:",round(suma,2))
            input("Pulse para continuar.")
        except:
            print("Alguno de los valores no es correcto")
            input("Pulse para ir al menú.")
            continue
    if opcion=="2":
        try:
            valor1=float(input("valor1-> "))
            valor2=float(input("valor2-> "))
            resta=valor1 - valor2
            print("La resta es:",round(resta,2))
            input("Pulse para continuar.")
        except:
            print("Alguno de los valores no es correcto")
            input("Pulse para ir al menú.")
            continue
    if opcion=="3":break

print("Finalizado")



















