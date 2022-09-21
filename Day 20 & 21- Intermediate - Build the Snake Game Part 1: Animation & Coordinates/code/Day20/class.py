# Heranca

class Animal:
    def __init__(self):
        self.nro_olhos = 2

    def dormir(self):
        print("Dormindo")

    def se_mover(self):
        print("Caminhando")



class Peixe(Animal):
    def __init__(self):
        super().__init__()  # importandoos atributos e metodos da supeclasse Animal

    def dormir(self):
        super().dormir() # Usando um metodo da superclasse
        print("So que na agua")

    def se_mover(self):  # Sobrecrevendo a classe se mover
        print("nadando")


jaguar = Animal()
nemo = Peixe()

jaguar.se_mover()
nemo.se_mover()

print(nemo.nro_olhos)

nemo.dormir()