#### Classe Pessoa: Crie uma classe que modele uma pessoa:
#### Atributos: nome, idade, peso e altura
#### Métodos: Envelhercer, engordar, emagrecer, crescer.
#### Obs: Por padrão, a cada ano que nossa pessoa envelhece,
#### sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa():
    def __init__ (self, nome = None, idade = None, peso = None, altura = None):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        nova_idade = int(input('Quantos anos está a pessoa agora?'))
        envelheceu = nova_idade - self.idade
        print(f'Sua pessoa envelheceu {envelheceu} anos')
    def engordar_emagrecer(self):
        kg_atual = float(input("Quilos atuais: "))
        if kg_atual > self.peso:
            print("A pessoa engordou", kg_atual-self.peso, 'quilos.')
        elif self.peso > kg_atual:
            print("A pessoa emagreceu", self.peso-kg_atual, 'quilos.')
    def crescer(self):
        idade_atual = float(input('Idade atual: '))

        if idade_atual < self.idade:
            print("Voce digitou uma idade atual menor do que a idade passada")
        elif idade_atual > self.idade and idade_atual<21:
            crescimento = (21-idade_atual)*0.5
            print(f"A pessoa crescerá ainda {crescimento} centimetros.")
        else:
            crescimento =0
            print("Ela não crescerá mais.")

    def print_all (self):
        print ('Nome:', self.nome, ' Idade:', self.idade,' Peso:', self.peso,' Altura:', self.altura)
