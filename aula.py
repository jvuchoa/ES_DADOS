import numpy as np

class listasequencial:
   
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
   
    def imprime(self):
        if self.ultima_posicao == -1:
            print("o vetor está vazio")
        else:
            for i in range(self.ultima_posicao+1):
                print(i, "-",self.valores[i])
    
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("capacidade máxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if(valor == self.valores[i]):
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

p1 = listasequencial(5)
p1.insere(4)
p1.insere(3)
p1.insere(5)
p1.insere(7)
p1.insere(8)
p1.imprime()
p1.excluir(3)
print('--------')
p1.imprime()
