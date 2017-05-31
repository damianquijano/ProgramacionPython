import numpy as np
import pandas as pd ## importamos o añadimos el módulo pandas al programa y le asignamos
# el alias pd 

# A continuación tenemos una colección de datos llamada diccionario, la cual inicia y
# termina con llaves, y dentro tenemos filas conformadas cada una por dos partes, el 
# nombre de la fila a la izquierda de dos puntos y el valor de la fila a la derecha de 
# los dos puntos y que es una lista con elementos dentro de ella.

data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 
                         'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons','Scouts', 
                         'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
 
# A continuación convertimos el diccionario data en un dataframe:        
df = pd.DataFrame(data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])   

# Ahora tenemos que ejecutar el script para que las variables se carguen en memoria y podamos usar la consola.

# Escribamos en la consola : data , vea los resultados.
# Ahora escribamos en la consola: df  , y vean la diferencia.




