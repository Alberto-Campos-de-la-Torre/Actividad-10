from algoritmos import distanciaeuclidiana
class Particula:
    def __init__(self,idd=0, origenx=0, origeny=0, destinox=0, destinoY=0, velocidad=0,rojo=0, verde=0, azul=0, distancia=0.0):
        self.__idd =idd           
        self.__origenx =origenx
        self.__origeny =origeny
        self.__destinox =destinox
        self.__destinoy =destinoY      
        self.__velocidad =velocidad
        self.__rojo =rojo
        self.__verde =verde
        self.__azul =azul
        self.distancia = distanciaeuclidiana(origenx,destinox,origeny,destinoY)

    def __str__(self):
        return (
            'ID:' + str(self.__idd) + '\n' +
            'Origen X:' + str(self.__origenx) + '\n' +
            'Origen Y:' + str(self.__origeny) + '\n' +
            'Destino X:' + str(self.__destinox) + '\n' +
            'Destino Y:' + str(self.__destinoy) + '\n' +
            'Velocidad:' + str(self.__velocidad) + '\n' +
            'Color:'     +
            'Rojo:' + str(self.__rojo) + '\n' +
            'Verde:' + str(self.__verde) + '\n' +
            'Azul:' + str(self.__azul) + '\n' +
            'Distancia = ' + str(self.distancia) + '\n'
        )             

#l01 = Particula("220203","56","102","89","76","100","78","0","98")
#print(l01)
#l02 = Particula("220204","58","105","99","86","105","88","1","100")
#print(l02)
