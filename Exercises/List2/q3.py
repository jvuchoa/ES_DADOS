class retangulo:
    def __init__(self, base, altura):
          self.base = base
          self.altura = altura  
    def c_area(self):
        calculo = self.base*self.altura
        return calculo
area1 = retangulo(10,8)
print("Área do Retângulo: ",area1.c_area())

       
      


