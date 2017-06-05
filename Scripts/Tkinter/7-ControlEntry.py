# Ejemplos de Control Entry y las variables Tkinter que permiten leer y asignar valores a controles.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.

from tkinter import *
def saludar():
    saludo="Hola "+entradaN.get()+" "+entradaA.get()  # el método get permite leer el contenido de la variable.
    entradaS.set(saludo) # el método set permite modificar el contenido.
    ventana.focus_set() #deja el foco en la ventana principal, en ningún control, elimine esta instrucción para que vea donde queda el foco del cursor.

def limpiar():
    entradaS.set("") # el método set permite modificar el contenido.
    entradaN.set("")
    entradaA.set("")
    ventana.focus_set()


ventana=Tk()
ventana.geometry("800x300+100+100")
ventana.title("Ejemplo de control Entry")

lblUsuario=Label(ventana,text="Nombre:",font=("Agency FB",14)).place(x=300,y=10)

entradaN= StringVar(ventana)
txtNombre=Entry(ventana,textvariable=entradaN,font=("Agency FB",14),width=10).place(x=370,y=20)

lblNombre=Label(ventana,text="Apellido:",font=("Agency FB",14)).place(x=300,y=50)  

entradaA=StringVar(ventana)
txtApellido= Entry(ventana,textvariable=entradaA,font=("Agency FB",14),width=10).place(x=370, y =60)

btnSaludar=Button(ventana,text="Saludar", font=("Agency FB",14),width=10,command=lambda:saludar()).place(x=500, y =10)   
btnLimpiar=Button(ventana,text="Limpiar", font=("Agency FB",14),width=10,command=lambda:limpiar()).place(x=500, y =60)

entradaS=StringVar(ventana)
txtSaludo=Entry(ventana,textvariable=entradaS,font=("Agency FB",14),width=30,state='readonly').place(x=370,y=120)

ventana.mainloop()  


# Las variables tkinter permiten que se puedan ver y modificar los valores internos de los controles, esto posibilita que un control modifique contenidos a otro.

# Pag 41 10. The Entry widget >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# Pag 153 52. Control variables: the values behind the widgets >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# v = DoubleVar() # Holds a float; default value 0.0
# v = IntVar() # Holds an int; default value 0
# v = StringVar() # Holds a string; default value ''

