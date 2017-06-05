# Ejemplos de creación y configuración de la ventana principal que será el contenedor de otros controles para que en conjunto funciones todo como una aplicación.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.

from tkinter import *

ventana= Tk()

ventana.config(background="red",borderwidth=20, relief="groove")
ventana.config(highlightbackground="green", highlightcolor="green", highlightthickness=1)
ventana.attributes("-alpha", 0.5) # te permite que sea transparente, si pones 0.1 es casi invisible, si pones 0.9 es opaca.
ventana.resizable(FALSE,FALSE) # si permites esta instrucción, la ventana no puede ser aumentada o disminuida (estirada) durante la ejecucion del programa.Si pones (TRUE,FALSE) permite estirar solamente horizontalmente, si pones (FALSE,TRUE) permite estiral solamente verticalmente. Por defaul, si no escribes esta instrucción, está (TRUE,TRUE)
ventana.title("Ventana Hola Mundo")
ventana.geometry("500x300+700+300")  # 500x300 es el tamaño de la ventana, donde 500 es el ancho en x horizontal ,y  300 es alto de la vetnana en y vertical . Tenemos luego +700+300 ,señala la posición de la ventana en la pantalla del monitor y se refiere a las coordenadas de la esquina superior izquierda de la ventana. Por tanto la ventana está a 700px hacia la derecha en eje x  y 300 hacia abajo en eje y. El eje horizontal x inicia en 0, y parte de izquierda hacia la derecha, y el eje y inicia en 0 y parte de arriba hacia abajo.

ventana.mainloop()

# La variable llamada ventana (pudo llamarse de otra manera como: main, vent1, o lo que sea) recibe el objeto Tk()
# EL objeto Tk() crea una ventana dentro de la cual agregaremos otros controles que permitirán construir una aplicación gráfica.
# Cambie los valores de ventana.geometry("500x300+100+100")  de tal modo que cambie el tamaño de la pantalla y su posición.
# Cambie el resto de los valores y pruebe los resultados.
# Consulte el archivo http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf para estudiar las diversas opciones en la creación de una ventana principal.

# w.keys()
# w.config()
# relief -->("flat", "raised", "sunken", "ridge", "solid", "groove")