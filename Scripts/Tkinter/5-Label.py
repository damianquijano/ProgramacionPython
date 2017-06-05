# En el programa , vemos ejemplo de la creación y configuración del control label.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.


from tkinter import *


def despedir(despedida):
    messagebox.showinfo("Despedida",despedida,parent=ventana)

ventana = Tk()
ventana.title("Ventana Hola Mundo") 
ventana.geometry("500x300+700+300")
lb=Label(ventana,text="Pulse el botón para ver el mensaje.",fg="blue",height=3,width=33,font=('Helvetica', '10'),bg="yellow",relief="solid")
lb.place (x=160, y=120)
b1=Button(ventana,text="Pulse aquí",command=lambda:despedir("Adiós mundo cruel")) 
b1.place (x=240, y=190)

ventana.mainloop()

# Pag 48 12. The Label widget >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# El label es un control utilizado para contener información que no se puede variar, como títulos o referencias o explicaciones.