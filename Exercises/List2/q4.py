class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):  
      
        self.saldo += valor
        print(f'Depósito de R${valor}. Saldo atual: R${self.saldo}')
        
    def sacar(self, valor):
        
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor}. Saldo atual: R${self.saldo}')
        else:
            print('Saldo insuficiente.')
        

if __name__ == "__main__":
    conta = ContaBancaria("João", 1000)  # Cria uma conta com saldo inicial de R$ 1000
    conta.depositar(500)  # Deposita R$ 500 na conta
    conta.sacar(200)      # Saca R$ 200 da conta
