a=input("Introduzca un valor: ")
try:
    a=int(a)
except:
    pass
try:
    if type(a)==int:
        pass
    else:
        a=float(a)
except:
    pass   

if type(a)==str:
    print("Es un texto")

if type(a)==int:
    print("Es un entero")

if type(a)== float:
    print("Es un decimal")

print("Fin")