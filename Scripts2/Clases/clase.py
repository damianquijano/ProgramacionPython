class Animal:#Mayúscula
    Mision= "Vivir"
    def caminar(self):# self toma el valor del nombre de la variable instanciada u objeto.
        print("Caminando")
    def soy(self,clase):
        print("Soy animal del tipo: "+ clase)
    def MiMision(self,vmision):
        print("Mi misión es: "+ self.Mision+ " y " + vmision)
    
#Uso del punto para acceder a los atributos y métodos.
print(Animal.Mision)


#Instancias, perro y gallina son instancias u objetos.
perro=Animal()
perro.caminar()
print(perro.Mision)
perro.soy("Perro")
perro.Mision="Ladrar"
print(perro.Mision)


# gallina=Animal()
# # print(gallina.Mision)
# # gallina.soy("Gallina")
# perro.Mision="Ladrar"
# gallina.Mision="Poner huevos"
# 
# print(perro.Mision)
# print(gallina.Mision)




#Uso del self en la clase al referirse a Mision.
# perro.MiMision("Ladrar")

#Demostración que ambos objetos contienen valores diferentes
# perro.Mision="Vivir y ladrar"
# gallina.Mision="Vivir y poner huevos"
# print(perro.Mision) #con las variables no usas paréntesis al final, sólo con los métodos.
# print(gallina.Mision)




#No se puede:
#cerdo=perro()
#Si se puede:
#cerdo=perro #no es una instancia


#Lo siguiente sale error, a menos que  quites el self, pero entonces no puede instanciar.Volver más tarde sobre este asunto.
#Animal.soy("Pescado")




#Polimorfismo
# perro=Mamifero("Perro")
# quecome(perro,"carne")
# perro.caminar()