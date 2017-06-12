# Agregar registro o fila nueva a la base de datos.OK
import fdb
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox



def agregar(id,nom,dialogo):
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
        messagebox.showinfo("Correcto","El registro ha sido agregado OK!",parent=dialogo)
    except:
        con.rollback()
        messagebox.showinfo("Error","El registro no ha sido agregado. ",parent=dialogo)
        
        
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
    
    
    lblCatId=Label(dialogo,text="CatId:",font=("Agency FB",14)).place(x=10,y=50)  
    entradaCatId=StringVar(dialogo)
    txtCatId= Entry(dialogo,textvariable=entradaCatId,font=("Agency FB",14),width=10).place(x=80, y =60)
    
    lblName=Label(dialogo,text="Name:",font=("Agency FB",14)).place(x=10,y=90)  
    entradaName=StringVar(dialogo)
    txtName= Entry(dialogo,textvariable=entradaName,font=("Agency FB",14),width=10).place(x=80, y =100)
    
  
    btAgregar=Button(dialogo,text="Agregar nuevo Registro",relief="solid",fg="blue",height=2,width=20,font=('Helvetica', '8'),bg="yellow",command=lambda:agregar(entradaCatId.get(),entradaName.get(),dialogo)) 
    btAgregar.place (x=10, y=150)
    
