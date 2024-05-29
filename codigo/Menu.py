def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Aluno")
        print("2. Buscar Alunos")
        print("3. Registrar Matrícula em Aula")
        print("4. Cadastrar Missão")
        print("5. Registrar Participação em Missão")
        print("6. Gerar Relatório de Missões")
        print("7. Criar Equipe")
        print("8. Gerenciar Membros de Equipe")
        print("9. Consultar Equipes")
        print("10. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_aluno()
        elif escolha == '2':
            buscar_alunos()
        elif escolha == '3':
            registrar_matricula()
        elif escolha == '4':
            cadastrar_missao()
        elif escolha == '5':
            registrar_participacao()
        elif escolha == '6':
            gerar_relatorio_missoes()
        elif escolha == '7':
            criar_equipe()
        elif escolha == '8':
            gerenciar_membros()
        elif escolha == '9':
            consultar_equipes()
        elif escolha == '10':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
menu()
