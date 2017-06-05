# Ejemplo básico de agregar una imagen.Debe tener el archivo logo.gi en la carpeta c:\data, dicho archivo lo puede descargar desde el repositorio https://github.com/damianquijano/PythonCurso3/tree/master/Data

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.
#Es posible que desea conocer más y no logra saber o descurbir al primer momento; no caiga en la tentación de preguntar para ahorrar el esfuerzo de buscar y encontrar. Investigar y ser autónomo es una competencia sumamemente codiciada en el entorno laboral por las empresas y organizaciones. También es posible que no ha leído esta sugerencia, y el profesor le indique que debe leer este comentario.

from tkinter import *


ventana=Tk()
ventana.geometry("800x300+100+100")
ventana.title("Ejemplo de imagen")

miImagen=PhotoImage(file='C:\\data\\logo.gif',master=ventana)
lbImagen=Label(ventana,text="",font=("Agency FB",14),image=miImagen).place(x=10,y=10)

ventana.mainloop()  

# Pag 14 5.9. Images>> http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
# https://tkinter.unpythonic.net/wiki/PhotoImage
# http://mgltools.scripps.edu/api/DejaVu/Tkinter.PhotoImage-class.html