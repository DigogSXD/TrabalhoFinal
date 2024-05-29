def gerar_relatorio_missoes():
    missao_objetivo = input("Objetivo da missão para gerar relatório: ")
    missao = missoes_df[missoes_df['Objetivo'] == missao_objetivo]
    if missao.empty:
        print("Missão não encontrada.")
        return
    
    index_missao = missoes_df[missoes_df['Objetivo'] == missao_objetivo].index[0]
    participantes = missoes_df.at[index_missao, 'Participantes']
    
    print(f"Relatório da Missão: {missao_objetivo}")
    print(f"Equipe Designada: {missoes_df.at[index_missao, 'Equipe Designada']}")
    print(f"Data de Início: {missoes_df.at[index_missao, 'Data Início']}")
    print(f"Data de Término: {missoes_df.at[index_missao, 'Data Término']}")
    print(f"Status: {missoes_df.at[index_missao, 'Status']}")
    print("Participantes:")
    for participante in participantes:
        print(f" - {participante}")
