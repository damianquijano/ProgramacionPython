# En el programa vemos un ejemplo del uso de la instrucción command que permite llamar a una función al momento de pulsar el control botón. También vemos ejemplo de la ventana emergente o de diálogo.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.

from tkinter import *
from tkinter import messagebox  # habilita el uso de ventanas pequeñas del tipo : alerta, error, advertencias, información, elección. 

def despedir(despedida):
    messagebox.showinfo("Despedida",despedida,parent=ventana)

ventana = Tk()
ventana.title("Ventana Hola Mundo")
ventana.geometry("500x300+700+300")
b1=Button(ventana,text="Mi primer boton",command=lambda:despedir("Adioz mundoz krueloz")) 
b1.place (x=160, y=120)
ventana.mainloop()


# Pag 155 55. Pop-up dialogs  >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf  lea los diferentes tipos de ventanas de mensajes.

# Una opicón interesante es el uso de la instrucción command dentro del botón, lo cual permite llamar una función que haga algo al momento de 
# hacer clik sobre el botón, y además permite enviar parámetros a la función. Se debe usar una función lambda o en línea para llamar la función 
# externa. Simplemente esriba lambda : y la función con los parámetros.

