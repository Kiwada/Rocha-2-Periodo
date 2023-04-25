def menu_principal():
    num_conta = 0
    while True:
        print("\n############ MENU PRINCIPAL ############")
        print("1. Criar Conta      2. Mostrar Saldo")
        print("3. Depósito         4. Saque")
        print("5. Transferência    6. Relatório Geral")
        print("0. Sair")
        print("---------------------------------------")
        op = int(input("Digite sua opção -> "))
        if op == 0:
            break
        elif op == 1:
            print("#### CRIANDO UMA CONTA ####")
            num_conta += 1
            nome = input("Nome do cliente: ")
            valor = float(input("Saldo inicial: "))
            #conta.append(criar(num_conta, nome, valor, 500.00))
        elif op == 2:
            print("##### SALDO EM CONTA #####")
            numero = int(input("Número da conta: "))
            #mostrar_saldo(conta, numero)
        elif op == 3:
            print("#### DEPÓSITO EM CONTA ####")
            numero = int(input("Número da conta: "))
            valor = float(input("Valor a depositar: "))
            #creditar(conta, numero, valor)
        elif op == 4:
            print("##### SAQUE EM CONTA #####")
            numero = int(input("Número da conta: "))
            valor = float(input("Valor a sacar: "))
            #debitar(conta, numero, valor)
        elif op == 5:
            print("### TRANSFERÊNCIA ENTRE CONTAS ###")
            num1 = int(input("Número da conta de origem: "))
            num2 = int(input("Número da conta de destino: "))
            valor = float(input("Valor a transferir: R$ "))
            #transferir(conta, num1, num2, valor)
        elif op == 6:
            print("## RELATÓRIO DE CONTAS ##")
            #emitir_relatorio(conta)
        else:
            print("\n##### OPÇÃO INVÁLIDA #####\n")


if __name__ == "__main__":
    menu_principal()