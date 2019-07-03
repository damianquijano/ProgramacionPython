import pymysql
import numpy as np
import pandas as pd
from tkinter import *
import v1f,v2f,v3f

# **************************Funciones ok***************************
def leer(event,i):
    global dat
    arreglo=dat.iloc[i:i+1,:].values 
    entradaId.set(i)
    entradaCatId.set(arreglo[0,0])
    entradaName.set(arreglo[0,1])
    
    
    
def llenar_tags(i):#construye los tags para cada linea y su evento al pulsar sobre la linea.
    T.tag_add("linea"+str(i-2), str(i)+'.0',str(i)+'.end')
    T.tag_bind("linea"+str(i-2), "<Button-1>", lambda e:leer(e,i-2))
    
def refrescar():
    global dat
    
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='udelas', db='ventas')

    cur = conn.cursor()
    cur.execute("SELECT * FROM vendedores")
    resultados=list(cur.fetchall())
    cur.close()
    conn.close()
  
    datos=pd.DataFrame(resultados,columns = ['IdVendedor', 'NombreVendedor'])
    dat=datos
    T.delete(1.0, END)
    T.insert(END, datos)
    
    num_filas=datos.shape[0]
    
    #En Text, las líneas empiezan por 1.0, y en este caso son los headers de columnas
    #por tanto hay que empezar por 2.0 que es nuestra línea 0.Como arranca a partir de 2, hay que sumar a num_filas más 2.
    for i in range(2,num_filas+2):# 
        llenar_tags(i)   
    
    TPrimeros.delete(1.0, END)  
    TPrimeros.insert(END,dat.head(3))
    TUltimos.delete(1.0, END)
    TUltimos.insert(END,dat.tail(3))
    
    # cur.close
    # con.close()
    


# **************************Programa principal***************************
pd.set_option("display.max_rows",None)#para que despliegue todos los rows sin interespacios tipo ...
pd.set_option('expand_frame_repr', False)#para que aparezcan todas las columnas sin "quebrar"


dat=pd.DataFrame()

root = Tk()
root.title("Aplicación de datos.")
root.geometry("1200x750+0+0")  # 1200x750es el tamaño de la ventana, 0+0 es la ubicación.


btRefrescar=Button(root,text="Refrescar",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="magenta",anchor=W, justify=LEFT,command=lambda:refrescar()) 
btRefrescar.place (x=10, y=10)

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


btAgregar=Button(root,text="Agregar nuevo Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",anchor=W, justify=LEFT,command=lambda:v1f.proc_agregar(root)) 
btAgregar.place (x=600, y=20)

btActualizar=Button(root,text="Actualizar Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",anchor=W, justify=LEFT,command=lambda:v2f.proc_actualizar(root,entradaCatId.get())) 
btActualizar.place (x=600, y=80)

btEliminar=Button(root,text="Eliminar Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",anchor=W, justify=LEFT,command=lambda:v3f.proc_eliminar(root,entradaCatId.get(),entradaName.get()) )
btEliminar.place (x=600, y=140)


#--------------------------

refrescar()



mainloop()



