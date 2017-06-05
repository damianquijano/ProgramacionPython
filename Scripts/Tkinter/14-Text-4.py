#Aplicación simple de visualización de una tabla de base de datos, que permite seleccionar una fila y
#ver sus valores en controles por separado tipo entry.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.
#Es posible que desea conocer más y no logra saber o descurbir al primer momento; no caiga en la tentación de preguntar para ahorrar el esfuerzo de buscar y encontrar. Investigar y ser autónomo es una competencia sumamemente codiciada en el entorno laboral por las empresas y organizaciones. También es posible que no ha leído esta sugerencia, y el profesor le indique que debe leer este comentario.

import fdb
import numpy as np
import pandas as pd
from tkinter import *

def leer(event, tag,i):
    print(event.widget.get('%s.first'%tag, '%s.last'%tag))# devuelve el nombre de la palabra tageada, esto es para saber los datos que está recibiendo la función
    print(tag+" "+str(i))#nombre del tag y el número de la línea que es el asignado al tag también
    arreglo=dat.iloc[i:i+1,:].values # convierto a arreglo numpy para extraer el valor sin el header de columna
    entradaId.set(i)
    entradaCountry.set(arreglo[0,0])
    entradaCurrency.set(arreglo[0,1])
    
    
    
def llenar_tags(i):#construye los tags para cada linea y su evento al pulsar sobre la linea.
    T.tag_add("linea"+str(i-2), str(i)+'.0',str(i)+'.end')
    T.tag_bind("linea"+str(i-2), "<Button-1>", lambda e:leer(e, "linea"+str(i-2),i-2))
    

con = fdb.connect(
    dsn='localhost:C:/data/EMPLOYEE.FDB',
    user='SYSDBA', password='udelas'
  )

pd.set_option("display.max_rows",None)#para que despliegue todos los rows sin interespacios tipo ...
pd.set_option('expand_frame_repr', False)#para que aparezcan todas las columnas sin "quebrar"
dat=pd.read_sql("SELECT * from COUNTRY;", con)


root = Tk()
root.geometry("800x300+100+100")  


T = Text(root, height=10, width=30)
T.pack(side=LEFT)

lblId=Label(root,text="Id:",font=("Agency FB",14)).place(x=300,y=10)
entradaId= StringVar(root)
txtId=Entry(root,textvariable=entradaId,font=("Agency FB",14),width=10).place(x=370,y=20)

lblCountry=Label(root,text="Country:",font=("Agency FB",14)).place(x=300,y=50)  
entradaCountry=StringVar(root)
txtCountry= Entry(root,textvariable=entradaCountry,font=("Agency FB",14),width=10).place(x=370, y =60)

lblCurrency=Label(root,text="Currency:",font=("Agency FB",14)).place(x=300,y=90)  
entradaCurrency=StringVar(root)
txtCurrency= Entry(root,textvariable=entradaCurrency,font=("Agency FB",14),width=10).place(x=370, y =100)


#--------------------------
T.insert(END, dat)

num_filas=dat.shape[0]

#En Text, las líneas empiezan por 1.0, y en este caso son los headers de columnas
#por tanto hay que empezar por 2.0 que es nuestra línea 0.Como arranca a partir de 2, hay que sumar a num_filas más 2.
for i in range(2,num_filas+2):# 
    llenar_tags(i)   
    

con.close()
mainloop()