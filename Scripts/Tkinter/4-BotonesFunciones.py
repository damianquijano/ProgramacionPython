# En el programa , vemos la segunda parte del uso de la instrucción command que permite llamar a una función al momento de pulsar el control botón. También vemos ejemplo de la ventana emergente o de diálogo.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.


from tkinter import *
from tkinter import messagebox  # habilita el uso de ventanas pequeñas del tipo : alerta, error, advertencias, información, elección. 

def despedir(despedida):
    messagebox.showinfo("Despedida",despedida,parent=ventana)
def sumar(n1,n2):
    valores=str(n1)+" + "+str(n2)+ " es: "
    suma=n1+n2
    messagebox.showinfo("La suma de: " ,valores+ str(suma),parent=ventana)

ventana = Tk()
ventana.title("Ventana Hola Mundo") 
ventana.geometry("500x300+700+300")
b1=Button(ventana,text="Mi primer boton",command=lambda:despedir("Adiós mundo cruel")) 
b1.place (x=160, y=120)
b1=Button(ventana,text="Mi segundo boton",command=lambda:sumar(2,4)) 
b1.place (x=160, y=180)

ventana.mainloop()