import fdb
import numpy as np
import pandas as pd
from tkinter import *

def leer(event, tag,i):
    # Los print de abajo es solo para saber lo que recibe la función y podemos ver el valor del print en la consola
    print(event.widget.get('%s.first'%tag, '%s.last'%tag))# devuelve el contenido de la fila entera, donde get('%s.first'%tag, '%s.last'%tag) por ejemplo para fila 1 es igual a get('1.0', '1.end')
    print(tag+" "+str(i))#nombre del tag y el número de la línea que es el asignado al tag también
    arreglo=dat.iloc[i:i+1,:].values # convierto el valor de dat que es dataframe de panda a un arreglo numpy para extraer los valores pero sin los header de columnas
    entradaId.set(i)
    entradaCatId.set(arreglo[0,0])
    entradaName.set(arreglo[0,1])
    
    
    
def llenar_tags(i):#construye los tags para cada linea y su evento al pulsar sobre la linea.
    T.tag_add("linea"+str(i-2), str(i)+'.0',str(i)+'.end')
    T.tag_bind("linea"+str(i-2), "<Button-1>", lambda e:leer(e, "linea"+str(i-2),i-2))
    

con = fdb.connect(
    dsn='localhost:C:/data/FILM.FDB',
    user='SYSDBA', password='udelas'
  )
cursor = con.cursor()

pd.set_option("display.max_rows",None)#para que despliegue todos los rows sin interespacios tipo ...
pd.set_option('expand_frame_repr', False)#para que aparezcan todas las columnas sin "quebrar"


query="""SELECT CATEGORY_ID,NAME
          FROM CATEGORY ;"""
resultados=cursor.execute(query).fetchall() 

dat=pd.DataFrame(resultados,columns = ['CATEGORY_ID', 'NAME']) 


# dat=pd.read_sql("SELECT * from CATEGORY;", con)  # es otra alternativa


root = Tk()
root.title("Aplicación de datos.")
root.geometry("1200x750+0+0")  # 1200x750es el tamaño de la ventana, 0+0 es la ubicación.


btActualizar=Button(root,text="Refrescar",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="magenta",anchor=W, justify=LEFT) 
btActualizar.place (x=10, y=10)

T = Text(root, height=20, width=30)
T.place(x=10,y=50)

TPrimeros = Text(root, height=5, width=30)
TPrimeros.place(x=280,y=150)

TUltimos = Text(root, height=5, width=30)
TUltimos.place(x=280,y=250)

lblId=Label(root,text="Id:",font=("Agency FB",14)).place(x=300,y=10)
entradaId= StringVar(root)
txtId=Entry(root,textvariable=entradaId,font=("Agency FB",14),width=10).place(x=370,y=20)

lblCatId=Label(root,text="CatId:",font=("Agency FB",14)).place(x=300,y=50)  
entradaCatId=StringVar(root)
txtCatId= Entry(root,textvariable=entradaCatId,font=("Agency FB",14),width=10).place(x=370, y =60)

lblName=Label(root,text="Name:",font=("Agency FB",14)).place(x=300,y=90)  
entradaName=StringVar(root)
txtName= Entry(root,textvariable=entradaName,font=("Agency FB",14),width=10).place(x=370, y =100)


btAgregar=Button(root,text="Agregar nuevo Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",anchor=W, justify=LEFT) 
btAgregar.place (x=600, y=20)

btActualizar=Button(root,text="Actualizar Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",anchor=W, justify=LEFT) 
btActualizar.place (x=600, y=80)

btEliminar=Button(root,text="Eliminar Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",anchor=W, justify=LEFT) 
btEliminar.place (x=600, y=140)


#--------------------------
T.insert(END, dat)

num_filas=dat.shape[0]

#En Text, las líneas empiezan por 1.0, y en este caso son los headers de columnas
#por tanto hay que empezar por 2.0 que es nuestra línea 0.Como arranca a partir de 2, hay que sumar a num_filas más 2.
for i in range(2,num_filas+2):# 
    llenar_tags(i)   
    
TPrimeros.insert(END,dat.head(3))
TUltimos.insert(END,dat.tail(3))


con.close()
mainloop()