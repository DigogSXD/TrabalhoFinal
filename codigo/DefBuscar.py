def buscar_alunos():
    criterio = input("Buscar por (nome, habilidades, equipe, status): ")
    valor = input(f"Valor para {criterio}: ")
    
    if criterio == 'habilidades':
        resultado = alunos_df[alunos_df['Habilidades'].apply(lambda habilidades: valor in habilidades)]
    else:
        resultado = alunos_df[alunos_df[criterio] == valor]
    
    if resultado.empty:
        print("Nenhum aluno encontrado.")
    else:
        print(resultado)
