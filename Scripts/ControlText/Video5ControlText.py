from tkinter import *
import numpy as np
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)

def leer(event, fila):
    ini=str(fila)+'.0'
    fin=str(fila)+'.end'
    print(T.get(ini,fin))
    print(T.tag_names(ini)," Fila: "+ str(fila))
    print("------------------")

def llenar_tags(i):#construye los tags para cada linea y su evento al pulsar sobre la linea.
    T.tag_add("MiTag"+str(i-2), str(i)+'.0',str(i)+'.end')
    T.tag_bind("MiTag"+str(i-2), "<Button-1>", lambda e:leer(e, i)) 
    
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

#Agregar un evento que detecte la fila seleccionada al pulsar con el mouse.
num_filas=data.shape[0] # Debe ser 6. cuando estudió el temario de manejo de datos con Panda, debe recordar que esta es una de varias formas de conocer el total de registros.

#En Text, las líneas empiezan por 1.0, y en este caso son los headers de columnas
#por tanto hay que empezar en la línea 2.0.
#For desde 2 a 8, pero recuerda que el último número no se incluye, entonces realmente llega a 7.
for i in range(2,num_filas+2):
    llenar_tags(i)  

mainloop()