import pandas as pd

# DataFrame para armazenar os dados dos alunos
alunos_df = pd.DataFrame(columns=['Nome', 'Idade', 'Habilidades', 'Nível de Poder', 'Equipe', 'Status de Matrícula'])

def cadastrar_aluno():
    nome = input("Nome: ")
    idade = input("Idade: ")
    habilidades = input("Habilidades (separadas por vírgula): ")
    nivel_poder = input("Nível de Poder: ")
    equipe = input("Equipe (se aplicável): ")
    status_matricula = input("Status de Matrícula: ")
    
    # Validação dos dados
    if not nome or not idade or not habilidades or not nivel_poder or not status_matricula:
        print("Todos os campos obrigatórios devem ser preenchidos!")
        return
    
    try:
        idade = int(idade)
        if idade <= 0:
            print("Idade deve ser um número positivo.")
            return
    except ValueError:
        print("Idade deve ser um número.")
        return
    
    # Adicionar aluno ao DataFrame
    novo_aluno = pd.DataFrame({
        'Nome': [nome],
        'Idade': [idade],
        'Habilidades': [habilidades.split(',')],
        'Nível de Poder': [nivel_poder],
        'Equipe': [equipe],
        'Status de Matrícula': [status_matricula]
    })
    
    global alunos_df
    alunos_df = pd.concat([alunos_df, novo_aluno], ignore_index=True)
    print(f"Aluno {nome} cadastrado com sucesso!")

