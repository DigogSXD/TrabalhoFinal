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
