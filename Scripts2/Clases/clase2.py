#init, inicializar objetos
class Animal:
    Mision= "Vivir"
    Especie="Animal"
    def __init__ (self, vespecie,vmision):
        self.Especie=vespecie
        self.Mision=vmision
    def caminar(self):
        print("Yo "+ self.Especie+ " estoy caminando")
    def soy(self):
        print("Soy animal del tipo: "+ self.Especie)
    def miMision(self):
        print("Mi misión es: "+ self.Mision)

#Lo siguiente genera un error
#perro=Animal()

perro=Animal("Perro","Ladrar")
perro.soy()
perro.caminar()
perro.miMision()
perro.Mision

# gallina=Animal("Gallina","Cacarea")
# gallina.soy()
# gallina.caminar()
# gallina.miMision()





