from particula import Particula

class Particulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula) 

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
    def __str__(self):
        return "".join(
            str(Particula) + '\n' for Particula in self.__particulas
        )


