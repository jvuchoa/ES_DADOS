class P_Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
p1=P_Triangulo(6,7,8)
print("Perímetro do triângulo: ",p1.calcular_perimetro())
