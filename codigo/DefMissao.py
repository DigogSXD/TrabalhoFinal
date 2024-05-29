def registrar_participacao():
    missao_objetivo = input("Objetivo da missão: ")
    aluno_nome = input("Nome do aluno: ")
    
    missao = missoes_df[missoes_df['Objetivo'] == missao_objetivo]
    if missao.empty:
        print("Missão não encontrada.")
        return
    
    aluno = alunos_df[alunos_df['Nome'] == aluno_nome]
    if aluno.empty:
        print("Aluno não encontrado.")
        return
    
    index_missao = missoes_df[missoes_df['Objetivo'] == missao_objetivo].index[0]
    missoes_df.at[index_missao, 'Participantes'].append(aluno_nome)
    print(f"Aluno {aluno_nome} registrado na missão '{missao_objetivo}' com sucesso!")
