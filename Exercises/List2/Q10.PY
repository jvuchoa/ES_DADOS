class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self):
        aumento =  self.salario *1.05
        return aumento

a1= Funcionario("João",800, "Estagiário")
print("Salário Atual: ",a1.aumentar_salario())
            
        