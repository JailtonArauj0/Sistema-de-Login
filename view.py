from controller import *

while True:
    print('Sistema de autenticação \n'
    'Opções:\n'
    '1 - Entrar\n'
    '2 - Cadastrar\n'
    '3 - Sair')
    try:
        escolha = int(input('Qual sua escolha? '))
        if escolha == 1:
            x = LoginController()
            email = input('Digite seu email: ').strip()
            senha = input('Digite sua senha: ').strip()

            login = x.login(email, senha)

            if login == 0:
                print('Login efetuado com sucesso.')
            elif login == 3:
                print('Email não encontrado.')
            elif login == 4:
                print('Senha incorreta.')

        elif escolha == 2:
            x = CadastroController()
            nome = input('Digite seu nome de usuário: ').strip()
            email = input('Digite seu email: ').strip()
            senha = input('Digite sua senha: ').strip()

            cadastro = x.cadastrar(nome, email, senha)
            
            if cadastro == 1:
                print('Usuário cadastrado com sucesso')
            elif cadastro == 2:
                print('Email já cadastrado no sistema')

        elif escolha == 3:
            print('Volte Sempre!')
            break
        else:
            print('Opção incorreta, tente novamente!')
            
    except ValueError as e:
            print('Digite apenas opções de 1 a 3, tente novamente!')
        
