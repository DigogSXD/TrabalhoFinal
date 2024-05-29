missoes_df = pd.DataFrame(columns=['Objetivo', 'Equipe Designada', 'Data Início', 'Data Término', 'Status', 'Participantes'])
equipes_df = pd.DataFrame(columns=['Nome da Equipe', 'Membros', 'Instrutor'])

def cadastrar_missao():
    objetivo = input("Objetivo da missão: ")
    equipe_designada = input("Equipe designada: ")
    data_inicio = input("Data de início (DD/MM/AAAA): ")
    data_termino = input("Data de término (DD/MM/AAAA): ")
    status = input("Status da missão: ")
    
    if not objetivo or not equipe_designada or not data_inicio or not data_termino or not status:
        print("Todos os campos obrigatórios devem ser preenchidos!")
        return
    
    nova_missao = pd.DataFrame({
        'Objetivo': [objetivo],
        'Equipe Designada': [equipe_designada],
        'Data Início': [data_inicio],
        'Data Término': [data_termino],
        'Status': [status],
        'Participantes': [[]]
    })
    
    global missoes_df
    missoes_df = pd.concat([missoes_df, nova_missao], ignore_index=True)
    print(f"Missão '{objetivo}' cadastrada com sucesso!")
