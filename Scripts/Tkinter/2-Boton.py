# Ejemplo de creación y configuración del control botón que es agregado a la ventana principal.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.

from tkinter import *
ventana = Tk()
ventana.title("Ventana Hola Mundo")
ventana.geometry("500x300+700+300")
b1=Button(ventana,text="Mi primer boton",relief="solid",fg="blue",height=5,width=20,font=('Helvetica', '10'),bg="yellow",anchor=W, justify=LEFT) 
b1.place (x=160, y=120)
ventana.mainloop()

#Pag 18 The Button widget >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf

#Pag 12 5.5. Anchors >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# tk.NE, tk.SE, tk.SW, tk.NW: Align a corner of the stipple pattern with the corresponding corner
# of the containing object. For example, tk.NE means that the top left corner of the stipple pattern coincides
# with the top left corner of the area to be stippled.
# • tk.N, tk.E, tk.S, tk.W: Align the stipple pattern with the center of one side of the containing object.
# For example, tk.E means the center of the stipple pattern will coincide with the center of the right
# side of the area to be stippled.
# • tk.CENTER: Align the center of the stipple pattern with the center of the containing object.


# Pag 12 5.6. Relief styles >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# Pag 10 5.3. Colors >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# Pag 10 5.4. Type fonts >> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf

# Pruebe con diferentes valores para conocer las diferentes posibilidades en la configuración de un botón.

# Los métodos de ubicación de un control dentro de una ventana son tres: pack, grid y place.
# Nosotros usaremos place: http://effbot.org/tkinterbook/place.htm  , utiliza los ejes de coordenadas de la pantalla y tamaños de pixels.
# http://python-para-impacientes.blogspot.com/2015/12/tkinter-disenando-ventanas-graficas.html
