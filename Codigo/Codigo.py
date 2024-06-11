import mysql.connector
from mysql.connector import errorcode

# Função para conectar ao banco de dados e criar o banco de dados se não existir.
def criar_db():
    try:
        # Veja se a senha está correta caso não consegui conectar
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ceub123456"
        )
        cursor = conn.cursor()
        
        # Criar o banco de dados se não existir
        cursor.execute("CREATE DATABASE IF NOT EXISTS xman")
        print("Deu certo ele criou ou já existe")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Veja se o usuario ou a senha está errada")
        else:
            print(err)

# Função para conectar ao banco de dados xman
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ceub123456",
        database="xman"
    )

def criar_tabelas():
    # Primeiro, criar o banco de dados se não existir
    criar_db()
    
    # Conectar ao banco de dados recém-criado
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Aluno (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT,
        habilidades TEXT,
        nivel_poder VARCHAR(255),
        equipe VARCHAR(255),
        status_matricula VARCHAR(255)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Aula (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        instrutor VARCHAR(255),
        vagas INT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Missao (
        id INT AUTO_INCREMENT PRIMARY KEY,
        objetivo VARCHAR(255),
        equipe_designada VARCHAR(255),
        data_inicio DATE,
        data_termino DATE,
        status VARCHAR(255)
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabelas criadas com sucesso.")

# Chamar a função para criar as tabelas
criar_tabelas()

# Aqui pra baixo é POO
class Aluno:
    def __init__(self, nome, idade, habilidades, nivel_poder, equipe=None, status_matricula='Ativo'):
        self.nome = nome
        self.idade = idade
        self.habilidades = habilidades
        self.nivel_poder = nivel_poder
        self.equipe = equipe
        self.status_matricula = status_matricula
        self.aulas = []
        self.missoes = []
    
    def validar(self):
        if not self.nome or not isinstance(self.idade, int) or self.idade <= 0 or not self.habilidades or not self.nivel_poder:
            return False
        return True
    
    def salvar_bd(self):
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Aluno (nome, idade, habilidades, nivel_poder, equipe, status_matricula)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.nome, self.idade, ','.join(self.habilidades), self.nivel_poder, self.equipe, self.status_matricula))
        conn.commit()
        cursor.close()
        conn.close()
    
    @staticmethod
    def buscar_bd(nome=None, habilidades=None, equipe=None, status_matricula=None):
        conn = conectar_bd()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM Aluno WHERE 1=1"
        params = []
        
        if nome:
            query += " AND nome LIKE %s"
            params.append(f"%{nome}%")
        
        if habilidades:
            query += " AND (" + " OR ".join("habilidades LIKE %s" for _ in habilidades) + ")"
            params.extend(f"%{hab}%" for hab in habilidades)
        
        if equipe:
            query += " AND equipe = %s"
            params.append(equipe)
        
        if status_matricula:
            query += " AND status_matricula = %s"
            params.append(status_matricula)
        
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
    
    def matricular_em_aula(self, aula):
        if aula.vagas > 0:
            self.aulas.append(aula)
            aula.registrar_aluno(self)
            aula.vagas -= 1
            # Atualizar banco de dados aqui se necessário
    
    def participar_missao(self, missao):
        self.missoes.append(missao)
        missao.registrar_participante(self)
        # Atualizar banco de dados aqui se necessário

class Aula:
    def __init__(self, nome, instrutor, vagas):
        self.nome = nome
        self.instrutor = instrutor
        self.vagas = vagas
        self.alunos = []
    
    def registrar_aluno(self, aluno):
        self.alunos.append(aluno)

class Missao:
    def __init__(self, objetivo, equipe_designada, data_inicio, data_termino, status='Pendente'):
        self.objetivo = objetivo
        self.equipe_designada = equipe_designada
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.status = status
        self.participantes = []
    
    def registrar_participante(self, aluno):
        self.participantes.append(aluno)

class Sistema:
    def __init__(self):
        self.alunos = []
        self.aulas = []
        self.missoes = []
        self.equipes = []
    
    def cadastrar_aluno(self, aluno):
        if aluno.validar():
            aluno.salvar_bd()
            self.alunos.append(aluno)
        else:
            print("Dados do aluno inválidos.")
    
    def buscar_alunos(self, nome=None, habilidades=None, equipe=None, status_matricula=None):
        return Aluno.buscar_bd(nome, habilidades, equipe, status_matricula)
    
    # Funções para cadastrar e consultar aulas
    def cadastrar_aula(self, aula):
        self.aulas.append(aula)
    
    def consultar_aulas(self):
        return self.aulas

    # Funções para cadastrar e consultar missões
    def cadastrar_missao(self, missao):
        self.missoes.append(missao)
    
    def consultar_missoes(self):
        return self.missoes

    # Funções para criar e consultar equipes
    def criar_equipe(self, nome, membros, instrutor):
        equipe = {'nome': nome, 'membros': membros, 'instrutor': instrutor}
        self.equipes.append(equipe)
        for membro in membros:
            membro.equipe = nome
    
    def consultar_equipes(self):
        return self.equipes


def menu():
    sistema = Sistema()
    
    while True:
        print("\n--- Sistema de Gerenciamento de Alunos Mutantes ---")
        print("1. Cadastrar novo aluno")
        print("2. Consultar alunos")
        print("3. Cadastrar nova aula")
        print("4. Consultar aulas")
        print("5. Matricular aluno em aula")
        print("6. Cadastrar nova missão")
        print("7. Consultar missões")
        print("8. Registrar participação em missão")
        print("9. Criar nova equipe")
        print("10. Consultar equipes")
        print("11. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            while True:
                nome = input("Nome: ")
                try:
                    idade = int(input("Idade: "))
                    if idade <= 0:
                        raise ValueError
                except ValueError:
                    print("Idade inválida. Deve ser um número positivo.")
                    continue
                habilidades = input("Habilidades (separadas por vírgula): ").split(',')
                nivel_poder = input("Nível de Poder: ")
                equipe = input("Equipe (opcional): ") or None
                status_matricula = input("Status de Matrícula (Ativo/Inativo): ") or 'Ativo'
                aluno = Aluno(nome, idade, habilidades, nivel_poder, equipe, status_matricula)
                if aluno.validar():
                    sistema.cadastrar_aluno(aluno)
                    print("Aluno cadastrado com sucesso!")
                    break
                else:
                    print("Dados do aluno inválidos. Tente novamente.")
        
        elif opcao == '2':
            nome = input("Nome (opcional): ") or None
            habilidades = input("Habilidades (opcional, separadas por vírgula): ").split(',') or None
            equipe = input("Equipe (opcional): ") or None
            status_matricula = input("Status de Matrícula (opcional): ") or None
            resultados = sistema.buscar_alunos(nome, habilidades, equipe, status_matricula)
            if resultados:
                for aluno in resultados:
                    print(f"\nNome: {aluno['nome']}, Idade: {aluno['idade']}, Habilidades: {aluno['habilidades']}, Nível de Poder: {aluno['nivel_poder']}, Equipe: {aluno['equipe']}, Status: {aluno['status_matricula']}")
            else:
                print("Nenhum aluno encontrado.")
        
        elif opcao == '3':
            while True:
                nome = input("Nome da Aula: ")
                instrutor = input("Instrutor: ")
                try:
                    vagas = int(input("Número de Vagas: "))
                    if vagas <= 0:
                        raise ValueError
                except ValueError:
                    print("Número de vagas inválido. Deve ser um número positivo.")
                    continue
                aula = Aula(nome, instrutor, vagas)
                sistema.cadastrar_aula(aula)
                print("Aula cadastrada com sucesso!")
                break
        
        elif opcao == '4':
            aulas = sistema.consultar_aulas()
            if aulas:
                for aula in aulas:
                    print(f"\nNome: {aula.nome}, Instrutor: {aula.instrutor}, Vagas: {aula.vagas}")
            else:
                print("Nenhuma aula cadastrada.")
        
        elif opcao == '5':
            nome_aluno = input("Nome do Aluno: ")
            nome_aula = input("Nome da Aula: ")
            aluno = next((a for a in sistema.alunos if a.nome == nome_aluno), None)
            aula = next((a for a in sistema.aulas if a.nome == nome_aula), None)
            if aluno and aula:
                aluno.matricular_em_aula(aula)
                print(f"Aluno {nome_aluno} matriculado na aula {nome_aula} com sucesso!")
            else:
                print("Aluno ou Aula não encontrados. Tente novamente.")
        
        elif opcao == '6':
            while True:
                objetivo = input("Objetivo da Missão: ")
                equipe_designada = input("Equipe Designada: ")
                data_inicio = input("Data de Início (AAAA-MM-DD): ")
                data_termino = input("Data de Término (AAAA-MM-DD): ")
                missao = Missao(objetivo, equipe_designada, data_inicio, data_termino)
                sistema.cadastrar_missao(missao)
                print("Missão cadastrada com sucesso!")
                break
        
        elif opcao == '7':
            missoes = sistema.consultar_missoes()
            if missoes:
                for missao in missoes:
                    print(f"\nObjetivo: {missao.objetivo}, Equipe Designada: {missao.equipe_designada}, Data de Início: {missao.data_inicio}, Data de Término: {missao.data_termino}, Status: {missao.status}")
            else:
                print("Nenhuma missão cadastrada.")
        
        elif opcao == '8':
            nome_aluno = input("Nome do Aluno: ")
            objetivo_missao = input("Objetivo da Missão: ")
            aluno = next((a for a in sistema.alunos if a.nome == nome_aluno), None)
            missao = next((m for m in sistema.missoes if m.objetivo == objetivo_missao), None)
            if aluno and missao:
                aluno.participar_missao(missao)
                print(f"Aluno {nome_aluno} registrado na missão {objetivo_missao} com sucesso!")
            else:
                print("Aluno ou Missão não encontrados. Tente novamente.")
        
        elif opcao == '9':
            while True:
                nome_equipe = input("Nome da Equipe: ")
                nomes_membros = input("Nomes dos Membros (separados por vírgula): ").split(',')
                instrutor = input("Instrutor: ")
                membros = [a for a in sistema.alunos if a.nome in nomes_membros]
                if membros:
                    sistema.criar_equipe(nome_equipe, membros, instrutor)
                    print(f"Equipe {nome_equipe} criada com sucesso!")
                    break
                else:
                    print("Membros não encontrados. Tente novamente.")
        
        elif opcao == '10':
            equipes = sistema.consultar_equipes()
            if equipes:
                for equipe in equipes:
                    membros_nomes = [membro.nome for membro in equipe['membros']]
                    print(f"\nNome: {equipe['nome']}, Instrutor: {equipe['instrutor']}, Membros: {', '.join(membros_nomes)}")
            else:
                print("Nenhuma equipe cadastrada.")
        
        elif opcao == '11':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha novamente.")
# Chamar a função de menu
menu()
