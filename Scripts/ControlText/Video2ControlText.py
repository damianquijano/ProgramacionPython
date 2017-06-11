
from tkinter import *
import numpy as np
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)



datos = [["Pedro Luna",25, "8-345-23",1200.00],["María Pérez",35, "7-345-23",1000.00]
,["Camilo Cela",55, "3-345-03",2200.00],["Viviana Belen",28, "8-125-13",800.00]
,["Carlos Berto",45, "2-145-13",1500.00],["Miriam Pela",34, "8-441-23",1600.00] ]

# Convertimos la lista en formato Dataframe con Pandas
data=pd.DataFrame(datos,columns = ['Nombre', 'Edad','Cedula','Salario'])

ventana=Tk()
ventana.geometry("800x300+100+100")
ventana.title("Ejemplo del control Text")

#Creamos un control Text
T = Text(ventana, height=10, width=90)
T.pack()

#Agregamos los datos en el control Text. Ejecute el programa para que vea el resultado.
T.insert(END, data)

print(T.get("1.0","1.end"))
print(T.get("2.0","2.end"))
print(T.get("2.0","2.10"))
print(T.get("3.5","3.end"))


mainloop()







