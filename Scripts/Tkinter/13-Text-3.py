# Ejemplo del control Text. Vamos aumentar más las posibilidades,queremos que cada línea del texto tenga un tag, de tal modo que al pulsar sobre una línes cualquiera se active una función que lea los datos de dicha línea.

# Pero si la cantidad de filas son por ejemplo 100 líneas: ¿hay que crear a mano un tag para cada línea? ¿hay  que escribir 100 funciones ..una para cada línea?
#Lo de arriba es lo que tenemos que  resolver con este ejemplo.


# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.
#Es posible que desea conocer más y no logra saber o descurbir al primer momento; no caiga en la tentación de preguntar para ahorrar el esfuerzo de buscar y encontrar. Investigar y ser autónomo es una competencia sumamemente codiciada en el entorno laboral por las empresas y organizaciones. También es posible que no ha leído esta sugerencia, y el profesor le indique que debe leer este comentario.

from tkinter import *
import numpy as np
import pandas as pd


def leer(event,nombreTag,numlinea):
    entradaS.set(T.get(str(numlinea)+'.0',str(numlinea)+'.end'))
    
    
def llenar_tags(i):#construye los tags para cada linea y su evento al pulsar sobre la linea.
    T.tag_add("linea"+str(i-2), str(i)+'.0',str(i)+'.end')
    T.tag_bind("linea"+str(i-2), "<Button-1>", lambda e:leer(e, "linea"+str(i-2),i)) 
     

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)


#Empezaremos con un ejemplo usando datos  creados en una lista, como vemos abajo.
datos = [["Pedro Luna",25, "8-345-23",1200.00],["María Pérez",35, "7-345-23",1000.00]
,["Camilo Cela",55, "3-345-03",2200.00],["Viviana Belen",28, "8-125-13",800.00]
,["Carlos Berto",45, "2-145-13",1500.00],["Miriam Pela",34, "8-441-23",1600.00]

]

# Convertimos la lista en formato Dataframe con Pandas
data=pd.DataFrame(datos,columns = ['Nombre', 'Edad','Cedula','Salario'])

ventana=Tk()
ventana.geometry("800x300+100+100")
ventana.title("Ejemplo del control Text")

#Creamos un control Text
T = Text(ventana, height=10, width=70)
T.pack()

#Agregamos los datos en el control Text. 
T.insert(END, data)


num_filas=data.shape[0] # cuando estudió el temario de manejo de datos con Panda, debe recordar que esta es una de varias formas de conocer el total de registros.

#En Text, las líneas empiezan por 1.0, y en este caso son los headers de columnas
#por tanto hay que empezar por 2.0 que es nuestra línea 0.Como arranca a partir de 2, hay que sumar a num_filas más 2.
for i in range(2,num_filas+2):# 
    llenar_tags(i)  

#Creamos un control Entry para ver los valores de la línea seleccionada.
entradaS= StringVar(ventana)
txtSeleccionado=Entry(ventana,textvariable=entradaS,state='readonly',font=("Agency FB",14),width=50).place(x=270,y=180)

# Ejecute el programa y pulse sobre la fila de los nombres de las coolumnas y también sobre la tercera fila. 


mainloop()