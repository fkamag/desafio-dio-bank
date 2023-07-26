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
    'password': "123456",
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


def buscar_usuario(user, user_list):
    result = [usuario for usuario in user_list if usuario["cpf"] == user]
    return result[0] if result else None


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
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "password": password,
        "saque_diario": 0,
        "extrato": "",
        "saldo": 0})
    return new_user


def menu_user():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

escolha a opção desejada => """
    return input(menu)


def operations_admin():
    while True:
        try:
            option = menu()

            if option == '1':
                result = buscar_usuario(login(), user_list)
                if result is None:
                    print("Usuário não encontrado")
                else:
                    valid = valid_password(result)
                    if valid is False:
                        print("senha inválida")
                    else:
                        operations(result)

            elif option == '2':
                user = login()
                result = buscar_usuario(user, user_list)
                if result:
                    print("CPF já cadastrado")
                else:
                    new_user = create_user(user)
                    user_list.append(new_user)
                    print("Cadastro realizado")

            elif option == '3':
                print("Sistema de Criar Conta em Manutenção")
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
                deposito = float(input("Informe o valor do depósito: "))
                if deposito > 0:
                    saldo += deposito
                    extrato += f"depósito R$ {deposito:.2f} \n"
                    print(f"depósito R$ {deposito:.2f} realizado! \n")
                    user["saldo"] = saldo
                    user["extrato"] = extrato
                else:
                    print("Valor de depósito inválido")

            elif option == 's':
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
        except ValueError:
            print("Valor inválido, Digite um Número")


def main():
    operations_admin()


main()
print("FIM")
