class Produto:
    def __init__(self, nome,quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def c_total(self):
        calculo = (self.preco*self.quantidade)
        return calculo
total1=Produto("Seriguela", 3, 6.50)
print("Total",total1.c_total())
