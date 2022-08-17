from controller import *

while True:
    print('Sistema de autenticação \n'
    'Opções:\n'
    '1 - Entrar\n'
    '2 - Cadastrar\n'
    '3 - Deletar conta\n'
    '4 - Sair')
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
                print('Email ou senha incorretos')

        elif escolha == 2:
            x = CadastroController()
            nome = input('Digite seu nome de usuário: ').strip()
            email = input('Digite seu email: ').strip()
            senha = input('Digite sua senha: ').strip()

            cadastro = x.cadastrar(nome, email, senha)
            
            if cadastro == 0:
                print('Usuário cadastrado com sucesso')
            elif cadastro == 1:
                print('Email já cadastrado no sistema')

        elif escolha == 3:
            deletarUsuario = DeletarController()
            email = input('Digite seu email: ').strip()
            senha = input('Digite sua senha: ').strip()

            deletar = deletarUsuario.deletar(email, senha)

            if deletar == 0:
                print('Cadastro removido com sucesso.')
            elif deletar == 3:
                print('Email ou senha incorretos')

        elif escolha == 4:
            print('Volte Sempre!')
            break
        
        else:
            print('Opção incorreta, tente novamente!')
            
    except ValueError as e:
            print('Digite apenas opções de 1 a 3, tente novamente!')
        
