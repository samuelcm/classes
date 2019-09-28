#Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado():
    def __init__ (self, lado = None):
        self.lado = lado
    def alterar_lado(self):
        lado = float(input("Lado: "))
        self.lado = lado
    def mostrar_lado(self):
        print(self.lado)
    def area(self):
        print(self.lado*2)
