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


query="""SELECT CATEGORY_ID,NAME
          FROM CATEGORY ;"""
resultados=cursor.execute(query).fetchall() # execute ejecuta la acción y con fecthall se pide que se envíen los resultados
#que se guardan en la variable resultados (escriba en la consola resultados y enter para ver el contenido

print("Impresión de Resultados en formato crudo, tal como lo recibimos")
print(resultados)
print("---------------")

data=pd.DataFrame(resultados,columns = ['CATEGORY_ID', 'NAME']) # convertimos los resultados en un formata dataframe de panda para que se vea menjor
print("Impresión de Resultados convertido a formato Dataframe")
print(data) # se manda imprimir

print ("Ok")

cursor.close
con.close