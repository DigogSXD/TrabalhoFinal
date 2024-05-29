def criar_equipe():
    nome_equipe = input("Nome da equipe: ")
    instrutor = input("Nome do instrutor: ")
    
    nova_equipe = pd.DataFrame({
        'Nome da Equipe': [nome_equipe],
        'Membros': [[]],
        'Instrutor': [instrutor]
    })
    
    global equipes_df
    equipes_df = pd.concat([equipes_df, nova_equipe], ignore_index=True)
    print(f"Equipe '{nome_equipe}' criada com sucesso!")

def gerenciar_membros():
    nome_equipe = input("Nome da equipe: ")
    acao = input("Deseja adicionar ou remover um membro? (adicionar/remover): ")
    aluno_nome = input("Nome do aluno: ")
    
    equipe = equipes_df[equipes_df['Nome da Equipe'] == nome_equipe]
    if equipe.empty:
        print("Equipe não encontrada.")
        return
    
    index_equipe = equipes_df[equipes_df['Nome da Equipe'] == nome_equipe].index[0]
    
    if acao == 'adicionar':
        equipes_df.at[index_equipe, 'Membros'].append(aluno_nome)
        print(f"Aluno {aluno_nome} adicionado à equipe {nome_equipe}.")
    elif acao == 'remover':
        if aluno_nome in equipes_df.at[index_equipe, 'Membros']:
            equipes_df.at[index_equipe, 'Membros'].remove(aluno_nome)
            print(f"Aluno {aluno_nome} removido da equipe {nome_equipe}.")
        else:
            print(f"Aluno {aluno_nome} não encontrado na equipe {nome_equipe}.")
    else:
        print("Ação inválida.")


def consultar_equipes():
    nome_equipe = input("Nome da equipe para consulta: ")
    equipe = equipes_df[equipes_df['Nome da Equipe'] == nome_equipe]
    if equipe.empty:
        print("Equipe não encontrada.")
        return
    
    index_equipe = equipes_df[equipes_df['Nome da Equipe'] == nome_equipe].index[0]
    membros = equipes_df.at[index_equipe, 'Membros']
    instrutor = equipes_df.at[index_equipe, 'Instrutor']
    
    print(f"Equipe: {nome_equipe}")
    print(f"Instrutor: {instrutor}")
    print("Membros:")
    for membro in membros:
        print(f" - {membro}")

