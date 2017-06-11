# Eliminar registro o fila existente.
import fdb
import numpy as np
import pandas as pd
from tkinter import *

def eliminar(id,nom):
    con = fdb.connect(
    dsn='localhost:C:/data/FILM.FDB',
    user='SYSDBA', password='udelas')
    cursor = con.cursor()
    #OJO: todo el query debe estar contenido entre doble comillas, y las variables string entre comillas simples.
    try:
        query="DELETE FROM   CATEGORY  WHERE    CATEGORY_ID ="+str(id)
        print(query)
        cursor.execute(query)
        con.commit() 
    except:
        con.rollback()
        print("Error")
    cursor.close()
    con.close()




root = Tk()
root.title("Eliminar datos.")
root.geometry("1200x750+0+0")  

lblId=Label(root,text="Id:",font=("Agency FB",14)).place(x=10,y=10)
entradaId= StringVar(root)
txtId=Entry(root,textvariable=entradaId,font=("Agency FB",14),width=10).place(x=80,y=20)

lblCatId=Label(root,text="CatId:",font=("Agency FB",14)).place(x=10,y=50)  
entradaCatId=StringVar(root)
txtCatId= Entry(root,textvariable=entradaCatId,font=("Agency FB",14),width=10).place(x=80, y =60)

lblName=Label(root,text="Name:",font=("Agency FB",14)).place(x=10,y=90)  
entradaName=StringVar(root)
txtName= Entry(root,textvariable=entradaName,font=("Agency FB",14),width=10).place(x=80, y =100)


btEliminar=Button(root,text="Eliminar Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",anchor=W, justify=LEFT,command=lambda:eliminar(entradaCatId.get(),entradaName.get())) 
btEliminar.place (x=10, y=150)


mainloop()