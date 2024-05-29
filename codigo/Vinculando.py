aulas_df = pd.DataFrame(columns=['Nome', 'Instrutor', 'Vagas', 'Alunos Matriculados'])

# Exemplo de aulas disponíveis
aulas_df = pd.DataFrame({
    'Nome': ['Treinamento de Combate', 'Controle de Poderes'],
    'Instrutor': ['Wolverine', 'Tempestade'],
    'Vagas': [5, 3],
    'Alunos Matriculados': [[], []]
})

def registrar_matricula():
    aluno_nome = input("Nome do aluno: ")
    aula_nome = input("Nome da aula: ")
    
    aluno = alunos_df[alunos_df['Nome'] == aluno_nome]
    if aluno.empty:
        print("Aluno não encontrado.")
        return
    
    aula = aulas_df[aulas_df['Nome'] == aula_nome]
    if aula.empty:
        print("Aula não encontrada.")
        return
    
    index_aula = aulas_df[aulas_df['Nome'] == aula_nome].index[0]
    
    if len(aulas_df.at[index_aula, 'Alunos Matriculados']) >= aulas_df.at[index_aula, 'Vagas']:
        print("Não há vagas disponíveis nesta aula.")
        return
    
    aulas_df.at[index_aula, 'Alunos Matriculados'].append(aluno_nome)
    print(f"Aluno {aluno_nome} matriculado na aula {aula_nome} com sucesso!")
