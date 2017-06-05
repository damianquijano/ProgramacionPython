# Ejemplo del control Text, que usaremos para que contengan los valores de las tablas de datos.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.
#Es posible que desea conocer más y no logra saber o descurbir al primer momento; no caiga en la tentación de preguntar para ahorrar el esfuerzo de buscar y encontrar. Investigar y ser autónomo es una competencia sumamemente codiciada en el entorno laboral por las empresas y organizaciones. También es posible que no ha leído esta sugerencia, y el profesor le indique que debe leer este comentario.

from tkinter import *
import numpy as np
import pandas as pd

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

#Agregamos los datos en el control Text. Ejecute el programa para que vea el resultado.
T.insert(END, data)

print(T.get("1.0","1.end"))
print(T.get("2.0","2.end"))
print(T.get("2.0","2.10"))
print(T.get("3.5","3.end"))


mainloop()

# Breve explicación:
# El control Text tiene muchos métodos, pero tenemos que tener en cuenta que funciona como una Notepad , no como Excell. Todo lo que esté contenido
# dentro del control, lo interpreta como letras , no como registros o columnas a pesar que se vea de ese modo gracias a Pandas.
# La instrucción insert permite agregar contenido dentro del control Text, y se hace mediante la acciòn: T.insert(END, data)
# esto se traduce : agregue todo el contenido que tiene la variable data al final del contenido del control texto llamado T.
# Dado que al inicio-almomento de ser creado-  el control texto está vacío, entonces en el control texto solamente aparecerá elcontenido de la variable data.
# La palabra END indica al final del documento o del control text.


# A continuación se hacen unas pruebas para entender las instrucciones que permiten extraer información del contenido del control text.
# print(T.get("1.0","1.end"))  esto nos muestra la primera fila del contenido, y a diferencia de las listas de python o dataframe de pandas o de las tablas de las bases de datos, la primera fila no empieza desde 0, empieza desde 1. La instrucción get() permite leer el contenido. La instrucción "1.0" significa que leemos el valor ubicado en la línea 1 y la columna 0 (en cambio las columnas son a partir de 0). La instrucción "1.end" significa que es la posición en la fila 1 y al final de dicha fila. Al escribir los dos valores de la siguiente forma:("1.0","1.end") esto significa que se refiere a un intervalo de caracteres que inicia a partir de la fila 1 y la columna 0 hasta el final de la fila 1, por tanto,nos mostrará todo el contenido en la fila 1 del control text. 
# Es importante entender la nomenclatura  "fila.columna" para visualizar un elemento dentro del control text.
# El resultado es: '       Nombre  Edad    Cedula  Salario' , resulta que es la fila en la que aparecen los títulos de las columnas, vemos un gran espacio a la izquierda de la columna Nombre, es porque la columna índice, que agrega Pandas de forma automática, no tiene nombre la columna.

# Veamos otros ejemplos:
# print(T.get("2.0","2.end")) --> '0  Pedro Luna    25  8-345-23   1200.0'
# print(T.get("2.0","2.10"))  ---> '0  Pedro L'
# print(T.get("3.5","3.end"))  -->'dro Luna    25  8-345-23   1200.0'
# 

#Bibliografía:
# Pag 82 24. The Text widget>> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf


# http://effbot.org/tkinterbook/text.htm
# http://www.python-course.eu/tkinter_text_widget.php
# http://www.tkdocs.com/tutorial/text.html
# https://www.tutorialspoint.com/python/tk_text.htm
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/text.html
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/text-methods.html
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/text-index.html


# http://books.gigatux.nl/mirror/pythonprogramming/0596000855_python2-CHP-8-SECT-4.html


