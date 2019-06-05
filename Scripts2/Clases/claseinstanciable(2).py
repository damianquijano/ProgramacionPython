#Clases instanciables, llamar al valor de los atributos del espacio de la clase o del obbjeto,  y agregar atributos "al vuelo"(a la clase o al objeto)
class Padre:
    Nombre="Noé" ##--> variables de clase, se llaman mediante nombreclase.atributo o self.atributo u objeto.atributo
    Edad=100
    def idioma(self,lengua):# método con self, por tanto es de objeto llamador solamente, no puede ser utilizada por el nombre de la clase (Padre)
        print(Padre.Nombre + " habla en " + lengua)# usando el  nombre de clase, llama al valor del atributo del espacio de memoria de la clase, o sea, el valor será Noé.
    def idioma2(self,vlengua):
        print (self.Nombre + " habla en " + vlengua)#usando self, usa el nombre del objeto y el valor del atributo del objeto(la copia),no el valor del mismo atributo pero del espacio en memoria de la clase
    def nombrehijo(self,hijo):
        print ("El hijo de " + Padre.Nombre + " es " + hijo)

print(Padre.Nombre)
# Padre.idioma("arameo") # error, el método espera un parámetro de un objeto en  el self, no puedes utilizar la misma clase
# Padre.nombrehijo("Pepe") # error, el método espera un parámetro de un objeto en  el self, no puedes utilizar la misma clase
Padre.Edad=200 #esto ok
print(Padre.Edad) #esto ok

hijo=Padre()
hijo.idioma("griego") # Noé habla en griego ,trabaja ok.
hijo.nombrehijo("Pepe") # El hijo de Noé es Pepe,trabaja ok.

Padre.Edad=400
print(hijo.Edad)#-->400 mantiene el valor inicial mientras no lo modifiques
hijo.Edad=50
print(Padre.Edad)#-->400
print(hijo.Edad)#--> 50

hijo.Nombre="Abel"
print(hijo.Nombre)#-->Abel
hijo.idioma("hebreo")#--> Noé habla en hebreo
hijo.idioma2("hebreo")#--> Abel habla en hebreo

#Si usas self para ver el atributo, verás el valor (clon) del atributo del objeto que llama; en cambio si usas el nombre de la clase, se utiliza el valor del atributo de la clase, como sila clase fuera otro objeto.

#Crear atributos al vuelo, pero será a nivel de objeto
hijo.Apellido="Leo"
nieto=Padre()
print(hijo.Apellido)#-->Leo
#print(nieto.Apellido)#esto dará error, pues no fue definido en nieto
#print(Padre.Apellido)#esto dará error, pues no fue definido en la clase

#Crear atributos al vuelo, pero será a nivel de clase
Padre.Origen="Griego"# definimos un atributo a nivel de clase al vuelo, el cual será reconocido en los objetos creados también
print(Padre.Origen)#-->Griego
print(hijo.Origen)#->Griego
print(nieto.Origen)#-->Griego











