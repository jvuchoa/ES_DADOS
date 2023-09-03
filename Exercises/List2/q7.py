class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def Detalhes(self):
        return f" Veículo: {self.marca}, {self.modelo}, {self.ano}"
info1= Carro("Lamborghini", "URUS", "2021/2022")
print(info1.Detalhes()) 