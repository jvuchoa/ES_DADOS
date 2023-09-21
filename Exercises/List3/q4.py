class somaDigitos:

  def __init__(self,num):
    self.num=num

  def cont(self):
    somador=0
    numStr=str(self.num)
    for i in numStr:
      somador+=int(i)
    return somador
try:
    numero = int(input("Digite um número inteiro: "))
    calculadora = somaDigitos(numero)
    resultado = calculadora.cont()
    print(f"A soma dos dígitos de {numero} é {resultado}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")