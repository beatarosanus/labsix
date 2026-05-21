class Conta:
    def __init__(self):
        self.saldo = 0
    def saca(self):
        self.retirada = int(input("Informe quanto você quer retirar: "))
        self.saldo -= self.retirada
    def deposita(self):
        self.entrada = int(input("Quanto você quer adicionar? "))
        self.saldo += self.entrada
    def calcula_Rendimento(self):
        self.rendimento = self.saldo * 0.1
    def imprimir_dados(self):
        print("Seu saldo é: ", self.saldo)
    def imprimir_rendimento(self):
        print("Seu rendimento é igual a: ", self.rendimento)
      
