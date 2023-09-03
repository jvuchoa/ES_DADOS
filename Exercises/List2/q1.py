class A_Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def Calcular_area(self):
        areaC = 3.14 * self.raio**2
        return areaC
p1=A_Circulo(8)
print("Área do círculo: ", p1.Calcular_area() )
      

     
    
    