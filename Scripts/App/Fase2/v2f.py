# Actualizar registro o fila existente.OK
import fdb
import numpy as np
import pandas as pd
from tkinter import *

def actualizar(id,nom):
    con = fdb.connect(
    dsn='localhost:C:/data/FILM.FDB',
    user='SYSDBA', password='udelas')
    cursor = con.cursor()
    #OJO: todo el query debe estar contenido entre doble comillas, y las variables string entre comillas simples.
    try:
        query="UPDATE   CATEGORY  SET   NAME = '"+ nom +"' WHERE CATEGORY_ID ="+ str(id)
        print(query)
        cursor.execute(query)
        con.commit() 
    except:
        con.rollback()
        print("Error")

    cursor.close()
    con.close()

def proc_actualizar(root,id):
    
    dialogo = Toplevel(root)
    dialogo.title("Actualizar datos.")
    dialogo.geometry("1200x750+0+00")
    dialogo.resizable(FALSE,FALSE)
    Button(dialogo,text="Cerrar",bg="green", command=dialogo.destroy,anchor="s").pack(side=BOTTOM, padx=20, pady=20)
    dialogo.grab_set() # esta instrucción igual que la siguiente, obligan que primero se cierre esta ventana para que se pueda cerrar la anterior.
    dialogo.transient(master=root)
    
    
    lblCatId=Label(dialogo,text="CatId:",font=("Agency FB",14)).place(x=10,y=50)  
    entradaCatId=StringVar(dialogo)
    entradaCatId.set(id)
    txtCatId= Entry(dialogo,textvariable=entradaCatId,font=("Agency FB",14),width=10,state='readonly').place(x=80, y =60)
    
    lblName=Label(dialogo,text="Name:",font=("Agency FB",14)).place(x=10,y=90)  
    entradaName=StringVar(dialogo)
    txtName= Entry(dialogo,textvariable=entradaName,font=("Agency FB",14),width=10).place(x=80, y =100)
    
  
    btActualizar=Button(dialogo,text="Actualizar Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",command=lambda:actualizar(entradaCatId.get(),entradaName.get())) 
    btActualizar.place (x=10, y=150)

