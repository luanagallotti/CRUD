

def menu():

    print('1 para cadastro de produtos: ')
    print('2- para cadastro de clientes: ')
    print('0 para sair do programa')

    opcao = int(input(''))

    if opcao == 1:
        cadProd()
    elif opcao == 2:
        cadCliente()
    elif opcao == 0:
        exit()
    else:
        print("Opção Inválida!")
