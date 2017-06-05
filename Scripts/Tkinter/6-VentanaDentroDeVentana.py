# En el programa , vemos ejemplo de la creación y configuración de una ventana TopLevel o ventanas hijas de la ventana principal.

# Intente entender el funcionamiento del programa. Primero debe ajecutarlo para darse cuenta lo que hace, y luego entender cómo lo hace.
# Experimente modificando, quitando, agregando instrucciones y valores con el fin de observar sus efectos y comprender la utilidad de instrucciones y porciones del código.
# Lea en los documentos abajo sugeridos, concretamente lo que se refiere al tema principal de este programa, para que pueda ampliar los conocimientos. No necesariamente comprenderá todo lo que aparece en la lectura, pero partes de ella ayudarán a su aprendizaje y permitirá que usted realice preguntas al profesor.En el caso de controles(Widgets) experimente con las diferentes opciones,  atributos y métodos.
# Recuerde que puede ampliar sus conocimientos buscando en internet , por ejemplo mediante Goolge. Por ejemplo si escribe: control boton Tkinter python, aparecerán muchos links en español con ejemplos, manuales y tutoriales, y si selecciona la opción videos, también podrá acceder a ejemplos claros en vivo.

from tkinter import *

def  saludar():
    dialogo = Toplevel(main)
    dialogo.title("Saludos")
    dialogo.geometry("120x120+250+120")# 120x120 es el tamaño de la ventana, 250+120 es la ubicación.
    dialogo.resizable(FALSE,FALSE)
    Button(dialogo,text="Cerrar",bg="green", command=dialogo.destroy,anchor="s").pack(side=BOTTOM, padx=20, pady=20)
    Label(dialogo, text='Hola mundo!!',font=("Agency FB",14)).pack(side=TOP,padx=10, pady=10)
    dialogo.grab_set() # esta instrucción igual que la siguiente, obligan que primero se cierre esta ventana para que se pueda cerrar la anterior.
    dialogo.transient(master=main)



main= Tk()
main.config(bg="blue")
main.title("Ventana Hola Mundo")
main.geometry("500x300+100+100") 
btnSaludar=Button(main,text="Hola Mundo",font=("Agency FB",14),width=10,command=lambda:saludar()).place(x=200,y=20)

main.mainloop()

# La instrucción command=dialogo.destroy escrita en el boton dentro de la función saludar, hace cerrar la ventana desde donde se pulsa el botón para cerrarla. Ejecute y entienda lo que tratamos de explicar.

# La función saludar() crea otra ventana pero del tipo TopLevel, o sea, estará dentro de la ventana principal llamada main, es la hija de main. Desde dicha función, agregamos nuevos controles del tipo botones y labels  que pertenecen a la nueva ventana hija llamada dialogo.

# Al crear el boton y label de la ventana llamada dialogo, hemos usado pack en vez de place, pero realmente da igual. Hay tres modos de ubicar o posición un control dentro de una ventana, mediante: grid, pack o place.


# https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Gesti%C3%B3n_de_ventanas
# http://python-para-impacientes.blogspot.com/2016/01/tkinter-tipos-de-ventanas.html
# https://ic1800a2011.wordpress.com/2013/06/21/027-ejemplo-de-una-ventana-modal-en-tkinter-python-3-x/
# http://www.w3ii.com/es/python/tk_toplevel.html

