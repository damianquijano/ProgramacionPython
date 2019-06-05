#Calculadora simple
def pedirvalores():
    valores=[]
    while True:
        try:
           
            valor1 = float(input("Escriba el primer valor: "))
            valor2 = float(input("Escriba el segundo valor: "))
            valores.append(valor1)
            valores.append(valor2)   
                                     
            break
           
        except:
            print("Usted ha escrito un valor no numérico.")
            input("Pulse cualquier tecla para escribir nuevamente los valores.")
    
    return valores

opcion = "0"
opciones=["1","2","3"]
while opcion != "3":
    print('''
    Seleccione una acción(1,2 o 3):
    1. Sumar.
    2. Restar.
    3. Salir.
    ''')
    opcion = input("-->")
    if opcion == "3":
        break
    if not(opcion in opciones):
        print("No ha seleccionado una operación válida.")
        input("Pulse cualquier tecla para regresar al menú.")
        continue
      
    lista_de_valores = pedirvalores()
    valor1 = lista_de_valores[0]
    valor2 = lista_de_valores[1]
    if opcion == "1":
            print("La suma es: ",valor1 + valor2)
    if opcion == "2":
        print("La resta es: ",valor1 - valor2)
    opcion = input("Escriba cualquier tecla para continuar.\nPara Salir directamente escriba 3\n-->")


print("Hasta la vista beby")        
        
              

    
    
    
      
 
    
