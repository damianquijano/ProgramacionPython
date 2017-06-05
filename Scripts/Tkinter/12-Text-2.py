# Ejemplo del control Text, que usaremos para que contengan los valores de las tablas de datos.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.
#Es posible que desea conocer más y no logra saber o descurbir al primer momento; no caiga en la tentación de preguntar para ahorrar el esfuerzo de buscar y encontrar. Investigar y ser autónomo es una competencia sumamemente codiciada en el entorno laboral por las empresas y organizaciones. También es posible que no ha leído esta sugerencia, y el profesor le indique que debe leer este comentario.

from tkinter import *
import numpy as np
import pandas as pd


def leer1(event):
    entradaS.set(T.get('1.0','1.end'))# aunque es más correcto event.widget.get('1.0','1.end')
    
    
def leer3(event):
    entradaS.set(T.get('3.0','3.end'))   
     

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

T.tag_add("MiTag1", '1.0','1.end')
T.tag_bind("MiTag1", "<Button-1>", lambda e:leer1(e))

T.tag_add("MiTag3", '3.0','3.end')
T.tag_bind("MiTag3", "<Button-1>", lambda e:leer3(e))

#Creamos un control Entry para ver los valores de la línea seleccionada.
entradaS= StringVar(ventana)
txtSeleccionado=Entry(ventana,textvariable=entradaS,state='readonly',font=("Agency FB",14),width=50).place(x=270,y=180)

# Ejecute el programa y pulse sobre la fila de los nombres de las coolumnas y también sobre la tercera fila. 


mainloop()


# En este ejemplo buscamos la forma de que al pulsar sobre una línea podamos extraer los datos de dicha línea.
# El control text utiliza unas instrucciones llamadas tag que marcan una porción del texto y permite que se genere un evento al pulsar sobre dicha porción.
# La instrucción se aplica en dos pasos: uno en el que crea un tag con un nombre y le asigna la porción del texto que debe cubrir, y el otro paso es asignar
# a dicho tag la posibilidad de que haga algo si se pulsa (evento botón).
# El primer paso se hace mediante tag_add : T.tag_add("MiTag1", '1.0','1.end') estamos creando un tag llamada MiTag1 que cubre todo el contenido de la lìnea 1 del control. Por tanto, si pulsamos encima de cualquier parte o palabra de la línea , pasará algo.
# El segundo paso se usa tag_bind : T.tag_bind("MiTag1", "<Button-1>", lambda e:leer1(e))  de este modo mediante bind se asocia el tag MiTag1 al evento de pulsar
#  sobre cualquier parte de la línea 1, y cuando esto pase, se activa la función llamada leer1(e). Recuerda que cuando usamos bind y eventos, siempre se recibe
# un valor que es Event,no se puede obviar, lo cual no quita que podamos agregar más parámetros, como veremos más adelante.
# 
# En el ejemplo, hemos creados dos tag, uno para la fila 1 y otro para la fila 3. Ejecuta el programa y haz la prueba:intenta pulsar también en otras filas que
# no tienen ningún tag asociado.
# 
# 
















