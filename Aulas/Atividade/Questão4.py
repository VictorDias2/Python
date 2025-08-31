def cadastrar_funcionario(id):
    nome = input('Nome do funcionário: ')
    setor = input('Setor do funcionário: ')
    salario = float(input('Salário do funcionário: R$'))
    dicionario_cadastro = {
    "id": id,
    "nome": nome,
    "setor": setor,
    "salario": salario
    }
    lista_funcionarios.append(dicionario_cadastro) #Copia o dicionario (cadastros) para a lista 'lista_funcionarios'

def consultar_funcionario():
    while True: #Repete até selecionar '4'(retornar ao menu)
        print('''              ------- CONSULTAR FUNCIONÁRIOS -------
            1) Consultar Todos 
            2) Consultar por ID
            3) Consultar por Setor 
            4) Retornar ao Menu  ''')

        opcao = int(input(' >> '))
        while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4: # Barra qualquer valor diferente das opções
            opcao = int(input(' >> '))

        if opcao == 1: #Consultar Todos
            for i in lista_funcionarios:
                print(f'ID: {i['id']}\nNome: {i['nome']}\nSetor: {i['setor']}\nSálario: R${i['salario']}')
                print()
                continue

        elif opcao == 2: #Consultar por ID
            consultar_id = int(input(f'ID: '))
            for i in lista_funcionarios:
                if i['id'] == consultar_id:
                    print(print(f'\nID: {i['id']}\nNome: {i['nome']}\nSetor: {i['setor']}\nSálario: R${i['salario']}'))
                    continue

        elif opcao == 3: #Consultar por Setor
            consultar_setor = input(f'Setor: ')
            for i in lista_funcionarios:
                if i['setor'] == consultar_setor:
                    print(print(f'\nID: {i['id']}\nNome: {i['nome']}\nSetor: {i['setor']}\nSalário: R${i['salario']}'))
                    continue

        elif opcao == 4: #Retorna ao Menu
            break

# Programa Principal:
print(''' ------------------------------------------------------------------
--------- Seja bem vindo a empresa de Victor Ramalho Dias ---------''')
lista_funcionarios = []
while True:
    print('''             ----------    MENU PRINCIPAL   ----------
        1) Cadastrar Funcionário 
        2) Consultar Funcionário
        3) Remover Funcionário 
        4) SAIR  ''')

    opcao = int(input(' >> '))
    if opcao == 1: #Cadastrar funcionário
        ident = int(input('Id do funcionário: '))
        cadastrar_funcionario(ident)

    elif opcao == 2: #Consultar funcionário
        consultar_funcionario()


    elif opcao == 3: #Remover funcionários
        print('             ----------    MENU REMOVER FUNCIONÁRIO   ----------')
        remover_fucionario = int(input('Digite o ID do funcionário para remoção: '))
        for i in lista_funcionarios:
            if i['id'] == remover_fucionario:
                lista_funcionarios.remove(i)
                print('Funcionário removido com sucesso!')
        while i['id'] != remover_fucionario:
            remover_fucionario = int(input('Funcionário não encontrado. Digite o ID corretamente: '))
        for i in lista_funcionarios:
            if i['id'] == remover_fucionario:
                lista_funcionarios.remove(i)
                print('Funcionário removido com sucesso!')


    elif opcao == 4: #SAIR
        break
print('Programa finalizado com sucesso!')
