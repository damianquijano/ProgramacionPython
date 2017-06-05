# Ejemplo de crear un control ComboBox. Ejecute el programa para que sepa sobre su naturaleza y funcionamiento.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.
#Es posible que desea conocer más y no logra saber o descurbir al primer momento; no caiga en la tentación de preguntar para ahorrar el esfuerzo de buscar y encontrar. Investigar y ser autónomo es una competencia sumamemente codiciada en el entorno laboral por las empresas y organizaciones. También es posible que no ha leído esta sugerencia, y el profesor le indique que debe leer este comentario.

from tkinter import *
from tkinter import ttk # a diferencia de los controles button,label y entry, el control combobox es un control "extra" que junto con otros que no son del juego de controles que vienen por defecto con Tkinter, se agregan mediante la librería extendida llamada ttk.

def selecciona(Event):
    val = entradaC.get()
    entradaS.set(val)
    
    
ventana=Tk()
ventana.geometry("800x300+100+100")
ventana.title("Ejemplo de control Combo")

cities = ('Toronto', 'Ottawa', 'Montreal', 'Vancouver', 'St. John')

entradaC=StringVar(ventana)
cb3 = ttk.Combobox(ventana, values=cities,textvariable=entradaC, state='readonly')
cb3.bind("<<ComboboxSelected>>",lambda e:selecciona(Event)) # el evento "<<ComboboxSelected>> siempre devuelve un valor llamado Event, y siempre debemos recogerlo en nuestra función que usamos posteriormente, usemos o no dicho parámetro.
cb3.current(0)  # instrucciòn que permite fijar el primer registro (el 0) para que aparezca de primero en el combobox a la hora de visualizarlo en la ventana.
cb3.pack(pady=5, padx=10)

entradaS= StringVar(ventana)
entradaS.set(entradaC.get())# leemos el contenido de la variable entradaC asociada al combobox y que contiene el nombre del valor seleccionado, en este caso Toronto.
txtSeleccionado=Entry(ventana,textvariable=entradaS,state='readonly',font=("Agency FB",14),width=30).place(x=270,y=80)


ventana.mainloop()  

# Pag 115 31. ttk.Combobox>> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# Una novedad es la instrucciòn bind y la forma de definir el evento o la acción de seleccionar un elemento dentro del combobox mediante la instrucción <<ComboboxSelected>>. La instrucción bind es una forma de asociar el control a un evento, en este caso el evento de seleccionar o pulsar sobre un elemento de la lista del control combobox, esto provoca que se active la función que hemos definido, en este caso llamada selecciona.
# Hay que notar el uso intenso de las variables del tipo StringVar que usamos para almacenar los valores de los controles.
