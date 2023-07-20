menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
saque_diário = 0

while True:
    option = input(menu)

    if option == 'd':
        deposito = float(input("Informe o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"depósito R$ {deposito:.2f} \n"
            print(f"depósito R$ {deposito:.2f} realizado! \n")
        else:
            print("Valor de depósito inválido")

    elif option == 's':
        if saque_diário < 3:
            saque = float(input("Informe o valor do saque: "))
            if saque < saldo:
                if saque > 0:
                    saldo -= saque
                    extrato += f"saque R$ {saque:.2f} \n"
                    print(f"saque R$ {saque:.2f} realizado! \n")
                    saque_diário += 1
                else:
                    print("Valor de saque inválido")
            else:
                print("Saldo insuficiente!")
        else:
            print("Ultrapassado limite de 3 saques diários")
    elif option == 'e':
        if extrato:
            print("Extrato de operações" + "\n")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f} \n")
        else:
            print("Não foram realizadas movimentações" + "\n")
    elif option == 'q':
        print("Obrigado por utilizar nossos serviços!")
        break
    else:
        print("Opção inválida")

print("FIM")
