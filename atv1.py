class usuarioIMC:
    def __init__(self, peso, altura):
         self.peso = peso
         self.altura = altura
    
    def  IMC(self):
        calculo= self.peso/(self.altura*self.altura)
        return calculo

p1 = usuarioIMC(73, 1.76)
print("INDICE DE MASSA CORPORAL: ", p1.IMC())