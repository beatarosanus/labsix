from CONTA import Conta
obj = Conta()
print("Nubank Beatriz")
print()
print("Opção 1: Depósito")
print("Opção 2: Saque")
print("Opção 3: Olhar rendimento")
print()
while True:
    opcao = int(input("Qual opção ? "))
    if opcao == 1:
        obj.deposito()
    elif opcao == 2:
        obj.saque()
    elif opcao == 3:
        obj.calcula_rendimento()
    else:
        print("Isso não é válido.")
        break
