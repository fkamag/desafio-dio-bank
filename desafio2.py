import os

user_list = [{
    'cpf': "admin",
    'name': "Admin",
    'data_nascimento': "26/05/1970",
    'endereco': {
        'logradouro': "Rua Onze",
        'numero': "704",
        'bairro': "Centro",
        'cidade': "Tatuí",
        'estado': "SP"
    },
    'password': "123456"
    }, ]

account_list = [{
    'agencia': '0001',
    'numero_conta': '1',
    'cpf': 'admin',
    'saque_diario': 0,
    'extrato': "",
    'saldo': 0
}, ]


def menu():
    menu = """

[1] Fazer Login
[2] Criar Usuário
[3] Criar Conta
[4] FIM

escolha a opção desejada => """
    return input(menu)


def login():
    print("Faça o login")
    cpf = input("CPF: ")
    return cpf


def get_user(user, user_list):
    result = [usuario for usuario in user_list if usuario["cpf"] == user]
    return result[0] if result else None


def get_account(user, account_list):
    result = [account for account in account_list if account["cpf"] == user]
    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print("Lista de Contas do Usuário")
        for account in result:
            print("Conta nº ", account["numero_conta"])
        option = input("Digite o número da conta que deseja acessar: ")
        selected = [cont for cont in result if cont["numero_conta"] == option]
        return selected[0] if selected else None
    else:
        return None


def valid_password(user):
    password = input("Digite sua senha: ")
    if password == user["password"]:
        return True
    else:
        return False


def create_user(cpf):
    new_user = {}
    name = input("Nome: ")
    date = input("Data de Nascimento: ")
    print("Endereço: ")
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    password = input("Password: ")
    new_user.update({
        "cpf": cpf,
        "name": name,
        "data_nascimento": date,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
        },
        "password": password,
    })
    return new_user


def create_account(user):
    new_account = {}
    number_account = len(account_list) + 1
    new_account.update({
        'agencia': '0001',
        'numero_conta': str(number_account),
        'cpf': user["cpf"],
        'saque_diario': 0,
        'extrato': "",
        'saldo': 0
    })
    return new_account


def menu_user():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

escolha a opção desejada => """
    return input(menu)


def deposit(saldo, extrato, user):
    deposito = float(input("Informe o valor do depósito: "))
    if deposito > 0:
        saldo += deposito
        extrato += f"depósito R$ {deposito:.2f} \n"
        print(f"depósito R$ {deposito:.2f} realizado! \n")
        user["saldo"] = saldo
        user["extrato"] = extrato
    else:
        print("Valor de depósito inválido")


def withdraw(saque_diario, saldo, extrato, user):
    if saque_diario < 3:
        saque = float(input("Informe o valor do saque: "))
        if saque <= saldo:
            if saque > 0:
                saldo -= saque
                extrato += f"saque R$ {saque:.2f} \n"
                print(f"saque R$ {saque:.2f} realizado! \n")
                saque_diario += 1
                user["saldo"] = saldo
                user["extrato"] = extrato
                user["saque_diario"] = saque_diario
            else:
                print("Valor de saque inválido")
        else:
            print("Saldo insuficiente!")
    else:
        print("Ultrapassado limite de 3 saques diários")


def statement(extrato, saldo):
    if extrato:
        print("Extrato de operações" + "\n")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f} \n")
    else:
        print("Não foram realizadas movimentações" + "\n")


def operations_admin():
    while True:
        try:
            option = menu()

            if option == '1':
                result = get_user(login(), user_list)
                if result is None:
                    print("Usuário não encontrado")
                else:
                    valid = valid_password(result)
                    if valid is False:
                        print("senha inválida")
                    else:
                        user = result["cpf"]
                        account = get_account(user, account_list)
                        if account:
                            print("Acessando Conta ", account["numero_conta"])
                            operations(account)
                        else:
                            print("Cliente sem conta cadastrada")

            elif option == '2':
                user = login()
                result = get_user(user, user_list)
                if result:
                    print("CPF já cadastrado")
                else:
                    new_user = create_user(user)
                    user_list.append(new_user)
                    print("Cadastro realizado com sucesso")

            elif option == '3':
                result = get_user(login(), user_list)
                if result is None:
                    print("Usuário não encontrado")
                else:
                    valid = valid_password(result)
                    if valid is False:
                        print("senha inválida")
                    else:
                        new_account = create_account(result)
                        account_list.append(new_account)
                        print("Conta cadastrada com sucesso")
            elif option == '4':
                print("Encerrando sistema")
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Valor inválido, Digite um Número")


def operations(user):
    while True:
        try:
            option = menu_user()
            saldo = user["saldo"]
            extrato = user["extrato"]
            saque_diario = user["saque_diario"]

            if option == 'd':
                deposit(saldo, extrato, user)

            elif option == 's':
                withdraw(saque_diario, saldo, extrato, user)

            elif option == 'e':
                statement(extrato, saldo)

            elif option == 'q':
                print("Obrigado por utilizar nossos serviços!")
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Valor inválido, Digite um Número")


def main():
    os.system('clear')
    operations_admin()


main()
print("FIM")
