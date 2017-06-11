import fdb
import numpy as np
import pandas as pd
from tkinter import *

def leer(event, tag,i):
    
    # print(tag+" "+str(i))#nombre del tag y el número de la línea que es el asignado al tag también
    print("*****************************")
    i=i-2
    print(dat.iloc[i:i+1,:])
    print("--------")
    print(dat.iloc[i:i+1,:].values)
    arreglo=dat.iloc[i:i+1,:].values # convierto el valor de dat que es dataframe de panda a un arreglo numpy para extraer los valores pero sin los header de columnas
    entradaId.set(i)# fila de la data original(no del control Text).Si es 15 de la data, es 17 de Text.
    entradaCountry.set(arreglo[0,0])
    entradaCurrency.set(arreglo[0,1])
    
    
    
def llenar_tags(i):#construye los tags para cada linea y su evento al pulsar sobre la linea.
    T.tag_add("linea"+str(i-2), str(i)+'.0',str(i)+'.end')
    ini=str(i)+'.0'
    T.tag_bind("linea"+str(i-2), "<Button-1>", lambda e:leer(e, T.tag_names(ini),i))
    

con = fdb.connect(
    dsn='localhost:C:/data/EMPLOYEE.FDB',
    user='SYSDBA', password='udelas'
  )
cursor = con.cursor()
pd.set_option("display.max_rows",None)#para que despliegue todos los rows sin interespacios tipo ...
pd.set_option('expand_frame_repr', False)#para que aparezcan todas las columnas sin "quebrar"


query="""SELECT *
          FROM COUNTRY ;"""
resultados=cursor.execute(query).fetchall() 

dat=pd.DataFrame(resultados,columns=['Country','Currency']) 

# dat=pd.read_sql("SELECT * from COUNTRY;", con)  otra alternativa


root = Tk()
root.geometry("800x300+100+100")  


T = Text(root, height=20, width=30)
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

for i in range(2,num_filas+2):# 
    llenar_tags(i)   
    
con.close()
mainloop()