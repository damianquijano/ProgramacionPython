# Ejemplo 2 de control ComboBox.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.
#Es posible que desea conocer más y no logra saber o descurbir al primer momento; no caiga en la tentación de preguntar para ahorrar el esfuerzo de buscar y encontrar. Investigar y ser autónomo es una competencia sumamemente codiciada en el entorno laboral por las empresas y organizaciones. También es posible que no ha leído esta sugerencia, y el profesor le indique que debe leer este comentario.

from tkinter import *
from tkinter import ttk # a diferencia de los controles button,label y entry, el control combobox es un control "extra" que junto con otros que no son del juego de controles que vienen por defecto con Tkinter, se agregan mediante la librería extendida llamada ttk.

def selecciona(Event):
    val = entradaC.get()
    posicion=cities.index(val)
    codigo=lista[1][posicion]
    mensaje=val +" Cod: "+ str(codigo)
    entradaS.set(mensaje)
    
    
ventana=Tk()
ventana.geometry("800x300+100+100")
ventana.title("Ejemplo de control Combo")

# En esta ocasión, cada elemeto de la lista tiene asociado otro valor. Por ejemplo, tenemos una matriz de dos listas:una lista
#contiene nombres de ciudades y la otra contiene los códigos telefónicos asociados a cada ciudad.
lista=[['Toronto', 'Ottawa', 'Montreal', 'Vancouver', 'St. John'],[23, 45, 12, 4, 56]]

# Dado que la varibale lista es una matriz que contiene 2 filas y 5 columnas, podemos extraer la fila de ciudades usando el método
# de lista[0] o lista[1], donde 0 se refiere a la fila 0 (recuerda que empiezan a partir de 0, no de 1) y lista[1] se refiere a la lista de códigos. Al asignar a la variable cities=lista[0], es como hacer cities=['Toronto', 'Ottawa', 'Montreal', 'Vancouver', 'St. John']
cities=lista[0]

#Seguimos con el mismo código del ejemplo anterior
entradaC=StringVar(ventana)
cb3 = ttk.Combobox(ventana, values=cities,textvariable=entradaC, state='readonly')
cb3.bind("<<ComboboxSelected>>",lambda e:selecciona(Event)) # el evento "<<ComboboxSelected>> siempre devuelve un valor llamado Event, y siempre debemos recogerlo en nuestra función que usamos posteriormente, usemos o no dicho parámetro.
cb3.current(0)  # instrucciòn que permite fijar el primer registro (el 0) para que aparezca de primero en el combobox a la hora de visualizarlo en la ventana.
cb3.pack(pady=5, padx=10)


# Lo que deseamos es que al seleccionar un valor del combobox, podaos visualizar todos los valores asociados a dicho valor, en nuestro 
#caso también el códigode la ciudad y que está contenido en la segunda lista de la matriz llamada lista.
entradaS= StringVar(ventana)
val = entradaC.get() # leemos el contenido de la variable entradaC asociada al combobox y que contiene el nombre del valor seleccionado, en este caso Toronto.
posicion=cities.index(val) # si por ejemplo es Toronto, nos devuelve la posición de Toronto en la lista, lo cual sería 0
codigo=lista[1][posicion] # esto nos dice buscar el elemento en la posición 0 de la fila 1 (la segunda) lo cual nos dará el valor
#del código asociado a Toronto, o sea, 23.
mensaje=val +" Cod: "+ str(codigo) #unimos el nombre de Toronto (almacenado en la variable val) y el código (que debes convertir en string para poder concatenar.
entradaS.set(mensaje)
txtSeleccionado=Entry(ventana,textvariable=entradaS,state='readonly',font=("Agency FB",14),width=30).place(x=270,y=80)


ventana.mainloop()  

# Pag 115 31. ttk.Combobox>> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# Una novedad es la instrucciòn bind y la forma de definir el evento o la acción de seleccionar un elemento dentro del combobox mediante la instrucción <<ComboboxSelected>>. La instrucción bind es una forma de asociar el control a un evento, en este caso el evento de seleccionar o pulsar sobre un elemento de la lista del control combobox, esto provoca que se active la función que hemos definido, en este caso llamada selecciona.
# Hay que notar el uso intenso de las variables del tipo StringVar que usamos para almacenar los valores de los controles.