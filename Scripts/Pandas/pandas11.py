import fdb
import numpy as np
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)


con = fdb.connect(
    dsn='localhost:C:/data/FILM.FDB',
    user='SYSDBA', password='udelas'
  )


cursor = con.cursor()


query="""UPDATE   CATEGORY  SET   NAME = 'Romanas' WHERE CATEGORY_ID = 17   """
cursor.execute(query) #los querys como insert, delete o update, son de acción, no devuelven ningún grupo de registros o resultados
# por eso no asignamos el resultado de la acción a ninguna variable como es el caso de un query del tipo select
con.commit() #para que sea efectiva la acción de arriba, se confirma con la instrucción commit desde el objeto conexión.

# Ahora vamos a visualizar los datos con un selec para verificar la inserción
query="""SELECT CATEGORY_ID,NAME
          FROM CATEGORY ;"""
resultados=cursor.execute(query).fetchall() 

data=pd.DataFrame(resultados,columns = ['CATEGORY_ID', 'NAME']) 
print(data) 



print ("Ok")

cursor.close
con.close