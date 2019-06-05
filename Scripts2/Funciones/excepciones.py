import sys

error="Ninguno"
try:
    a=float(input("Introduce valor numérico: "))
except:
    print("Usted no ha introducido un valor numérico, el programa terminó")
    sys.exit(0)

print("El  valor introducido fue: ",round(a,2))


    