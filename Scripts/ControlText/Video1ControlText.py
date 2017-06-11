
from tkinter import *
import numpy as np
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows",None)



# datos="Veinte mil leguas de viaje submarino es una obra narrada en\nprimera persona por el profesor francés Pierre Aronnax, notable\nbiólogo que es hecho prisionero por el Capitán Nemo y es conducido\npor los océanos a bordo del submarino Nautilus, en compañía de su\ncriado Conseil y el arponero canadiense Ned Land."

datos = \
"""Veinte mil leguas de viaje submarino es una obra narrada en primera persona
por el profesor francés Pierre Aronnax, notable biólogo que es hecho prisionero
por el Capitán Nemo y es conducido por los océanos a bordo del submarino Nautilus,
en compañía de su criado Conseil y el arponero canadiense Ned Land."""



ventana=Tk()
ventana.geometry("800x300+100+100")
ventana.title("Ejemplo del control Text")

#Creamos un control Text
T = Text(ventana, height=10, width=90)
T.pack()

#Agregamos los datos en el control Text. Ejecute el programa para que vea el resultado.
T.insert(END, datos)

print(T.get("1.0","1.end"))
print(T.get("2.0","2.end"))
print(T.get("2.0","2.10"))
print(T.get("3.5","3.end"))


mainloop()