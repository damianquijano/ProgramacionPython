#Calculadora simple
opcion = "0"
opciones=["1","2","3"]
while True:
    print('''
    Seleccione una acción(1,2 o 3):
    1. Sumar.
    2. Restar.
    3. Salir.
    ''')
    opcion = input(">")
    if opcion == "3":
        break
    if not(opcion in opciones):
        print("No ha seleccionado una operación válida.")
        input("Pulse cualquier tecla para regresar al menú.")
        continue
      
    try:
       
        valor1 = float(input("Escriba el primer valor: "))
        valor2 = float(input("Escriba el segundo valor: "))
        if opcion == "1":
            print("La suma es: ",valor1 + valor2)
        if opcion == "2":
            print("La resta es: ",valor1 - valor2)
       
    except:
        print("Usted ha escrito un valor no numérico.")
        input("Pulse cualquier tecla para regresar al menú.")

print("Hasta la vista beby")        
        
              

    
    
    
      
 
    
