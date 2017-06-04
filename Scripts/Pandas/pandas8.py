import fdb
import numpy as np
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)


con = fdb.connect(
    dsn='localhost:C:/data/FILM.FDB',
    user='SYSDBA', password='udelas'
  )

print("Version de Firebird: ",con.firebird_version)
print("-------------")
print("Versión (corta): ", con.version)
print("-------------")
print("Nombre de la computadora en la que instaló firebird: ",con.site_name)
print("-------------")
print("Nombre de la base de datos y su ubicación: ", con.database_name)
print("-------------")
print("Ods: ",con.ods_version)
print("-------------")
print("Nombres de los usuarios conectados y cantidad de conexiones: ",con.db_info(fdb.isc_info_user_names))  
print("-------------")
# 

# No olvide cerrar la conexión antes de terminar el programa
con.close



