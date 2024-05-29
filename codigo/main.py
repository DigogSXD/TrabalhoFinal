def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Aluno")
        print("2. Buscar Alunos")
        print("3. Registrar Matrícula em Aula")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_aluno()
        elif escolha == '2':
            buscar_alunos()
        elif escolha == '3':
            registrar_matricula()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
menu()
