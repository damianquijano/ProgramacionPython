# Agregar registro o fila nueva a la base de datos.
import fdb
import numpy as np
import pandas as pd
from tkinter import *

def agregar(id,nom):
    con = fdb.connect(
    dsn='localhost:C:/data/FILM.FDB',
    user='SYSDBA', password='udelas')
    cursor = con.cursor()
    #OJO: todo el query debe estar contenido entre doble comillas, y las variables string entre comillas simples.
    # Ejemplo: query="INSERT INTO CATEGORY (CATEGORY_ID, NAME) VALUES (17,'bbb')"
  
    try:
        query="INSERT INTO CATEGORY (CATEGORY_ID, NAME) VALUES("+ str(id)+",'"+ nom + "')"
        print(query)
        cursor.execute(query)
        con.commit() 
       
    except:
        con.rollback()
        print("Error")
        
        
    cursor.close() 
    con.close()

def proc_agregar(root):
    
    dialogo = Toplevel(root)
    dialogo.title("Agregar datos.")
    dialogo.geometry("1200x750+0+00")
    dialogo.resizable(FALSE,FALSE)
    Button(dialogo,text="Cerrar",bg="green", command=dialogo.destroy,anchor="s").pack(side=BOTTOM, padx=20, pady=20)
    dialogo.grab_set() # esta instrucción igual que la siguiente, obligan que primero se cierre esta ventana para que se pueda cerrar la anterior.
    dialogo.transient(master=root)
    
    lblId=Label(dialogo,text="Id:",font=("Agency FB",14)).place(x=10,y=10)
    entradaId= StringVar(dialogo)
    txtId=Entry(dialogo,textvariable=entradaId,font=("Agency FB",14),width=10).place(x=80,y=20)
    
    lblCatId=Label(dialogo,text="CatId:",font=("Agency FB",14)).place(x=10,y=50)  
    entradaCatId=StringVar(dialogo)
    txtCatId= Entry(dialogo,textvariable=entradaCatId,font=("Agency FB",14),width=10).place(x=80, y =60)
    
    lblName=Label(dialogo,text="Name:",font=("Agency FB",14)).place(x=10,y=90)  
    entradaName=StringVar(dialogo)
    txtName= Entry(dialogo,textvariable=entradaName,font=("Agency FB",14),width=10).place(x=80, y =100)
    
  
    btAgregar=Button(dialogo,text="Agregar nuevo Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",command=lambda:agregar(entradaCatId.get(),entradaName.get())) 
    btAgregar.place (x=10, y=150)
    
