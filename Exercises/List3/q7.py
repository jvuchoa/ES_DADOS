class c_imc:
  def __init__(self,peso,altura):
    self.peso=peso
    self.altura=altura

  def calculo(self):
    imc=self.peso/(self.altura ** 2 )
    return round(imc, 3)  # Arredonda o IMC para tres casas decimais

i1=c_imc(72,1.76)
print(i1.calculo())