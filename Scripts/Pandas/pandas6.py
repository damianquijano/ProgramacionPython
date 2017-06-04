import numpy as np
import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)

#Utilizaremos el siguiente Dataframe para la práctica escribiendo el siguiente programa:
data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks','Dragoons', 'Dragoons', 'Dragoons', 'Dragoons','Scouts',                          'Scouts', 'Scouts', 'Scouts'],'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# A continuación convertimos el diccionario data en un dataframe:        
df = pd.DataFrame(data)   
#Por tanto nuestro Dataframe es la variable df . 












