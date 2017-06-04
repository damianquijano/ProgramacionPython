import fdb
import numpy as np
import pandas as pd


pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)

con = fdb.connect(
    dsn='localhost:C:/data/EMPLOYEE.FDB',
    user='SYSDBA', password='udelas'
  )
  
cursor = con.cursor()
# acceder a la SQL del archivo

cursor.execute('SELECT * from COUNTRY')
rows = cursor.fetchall()

#print row
for row in rows :
        print (row[0])

print ("registros: ", len(rows))

cursor.close
con.close