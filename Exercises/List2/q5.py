class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        return f"Nome do individuo: {self.nome} Idade: {self.idade}"
info1=Pessoa("Gabriel", 19)
print(info1.falar())
