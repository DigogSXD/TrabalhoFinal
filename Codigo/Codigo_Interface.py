import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import errorcode

# Função para conectar ao banco de dados e criar o banco de dados se não existir.
def criar_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS xman")
        print("Banco de dados criado ou já existe")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Verifique o usuário ou a senha")
        else:
            print(err)

# Função para conectar ao banco de dados xman
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="xman"
    )

def criar_tabelas():
    criar_db()
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

criar_tabelas()











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
    
    def cadastrar_aula(self, aula):
        self.aulas.append(aula)
    
    def consultar_aulas(self):
        return self.aulas

    def cadastrar_missao(self, missao):
        self.missoes.append(missao)
    
    def consultar_missoes(self):
        return self.missoes

    def criar_equipe(self, nome, membros, instrutor):
        equipe = {'nome': nome, 'membros': membros, 'instrutor': instrutor}
        self.equipes.append(equipe)
        for membro in membros:
            membro.equipe = nome
    
    def consultar_equipes(self):
        return self.equipes
    

    #EXCLUIR
    def excluir_aluno(self, nome_aluno):
        # Verifica se o aluno está na lista e o remove
        for aluno in self.alunos:
            if aluno.nome == nome_aluno:
                self.alunos.remove(aluno)
                break
        else:
            print(f"Aluno {nome_aluno} não encontrado na lista.")
            return
        
        # Remove o aluno do banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Aluno WHERE nome = %s", (nome_aluno,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Aluno {nome_aluno} excluído do banco de dados.")



    #UPDATE
    def atualizar_aluno(self, nome_original, nome_novo=None, idade=None, habilidades=None, nivel_poder=None, equipe=None, status_matricula=None):
        aluno_encontrado = None

        for aluno in self.alunos:
            if aluno.nome == nome_original:
                aluno_encontrado = aluno
                break
        else:
            print(f"Aluno {nome_original} não encontrado na lista.")
            return
        
        # Atualizar dados na lista de alunos
        if nome_novo:
            aluno_encontrado.nome = nome_novo
        if idade:
            aluno_encontrado.idade = idade
        if habilidades:
            aluno_encontrado.habilidades = habilidades
        if nivel_poder:
            aluno_encontrado.nivel_poder = nivel_poder
        if equipe:
            aluno_encontrado.equipe = equipe
        if status_matricula:
            aluno_encontrado.status_matricula = status_matricula

        # Atualizar dados no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Aluno SET nome=%s, idade=%s, habilidades=%s, nivel_poder=%s, equipe=%s, status_matricula=%s
            WHERE nome=%s
        """, (nome_novo or aluno_encontrado.nome, idade or aluno_encontrado.idade, ','.join(habilidades) if habilidades else ','.join(aluno_encontrado.habilidades), nivel_poder or aluno_encontrado.nivel_poder, equipe or aluno_encontrado.equipe, status_matricula or aluno_encontrado.status_matricula, nome_original))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Aluno {nome_original} atualizado com sucesso.") 


    def atualizar_aula(self, nome_original, nome_novo=None, instrutor=None, vagas=None):
        aula_encontrada = None

        for aula in self.aulas:
            if aula.nome == nome_original:
                aula_encontrada = aula
                break
        else:
            print(f"Aula {nome_original} não encontrada na lista.")
            return

        # Atualizar dados na lista de aulas
        if nome_novo:
            aula_encontrada.nome = nome_novo
        if instrutor:
            aula_encontrada.instrutor = instrutor
        if vagas:
            aula_encontrada.vagas = vagas

        # Atualizar dados no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Aula SET nome=%s, instrutor=%s, vagas=%s
            WHERE nome=%s
        """, (nome_novo or aula_encontrada.nome, instrutor or aula_encontrada.instrutor, vagas or aula_encontrada.vagas, nome_original))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Aula {nome_original} atualizada com sucesso.")



    # Método para excluir uma aula
    def excluir_aula(self, nome_aula):
        # Verifica se a aula está na lista e a remove
        for aula in self.aulas:
            if aula.nome == nome_aula:
                self.aulas.remove(aula)
                break
        else:
            print(f"Aula {nome_aula} não encontrada na lista.")
            return
        
        # Remove a aula do banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Aula WHERE nome = %s", (nome_aula,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Aula {nome_aula} excluída do banco de dados.")


    # Método para atualizar uma equipe
    def atualizar_equipe(self, nome_equipe, novo_nome=None, novos_membros=None, novo_instrutor=None):
        equipe_encontrada = None

        for equipe in self.equipes:
            if equipe['nome'] == nome_equipe:
                equipe_encontrada = equipe
                break

        if not equipe_encontrada:
            print(f"Equipe {nome_equipe} não encontrada.")
            return

        if novo_nome:
            equipe_encontrada['nome'] = novo_nome
        if novos_membros:
            equipe_encontrada['membros'] = novos_membros
        if novo_instrutor:
            equipe_encontrada['instrutor'] = novo_instrutor

        # Atualiza a equipe no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()

        if novo_nome:
            cursor.execute("UPDATE Equipe SET nome = %s WHERE nome = %s", (novo_nome, nome_equipe))

        if novo_instrutor:
            cursor.execute("UPDATE Equipe SET instrutor = %s WHERE nome = %s", (novo_instrutor, novo_nome or nome_equipe))

        if novos_membros:
            cursor.execute("DELETE FROM Membros_Equipe WHERE equipe_nome = %s", (nome_equipe,))
            for membro in novos_membros:
                cursor.execute("INSERT INTO Membros_Equipe (equipe_nome, membro_nome) VALUES (%s, %s)", (novo_nome or nome_equipe, membro.nome))

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Equipe {nome_equipe} atualizada com sucesso.")


    # Método para excluir uma equipe
    def excluir_equipe(self, nome_equipe):
        # Verifica se a equipe está na lista e a remove
        for equipe in self.equipes:
            if equipe['nome'] == nome_equipe:
                self.equipes.remove(equipe)
                break
        else:
            print(f"Equipe {nome_equipe} não encontrada na lista.")
            return
        
        # Remove a equipe e seus membros do banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Membros_Equipe WHERE equipe_nome = %s", (nome_equipe,))
        cursor.execute("DELETE FROM Equipe WHERE nome = %s", (nome_equipe,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Equipe {nome_equipe} excluída do banco de dados.")






sistema = Sistema()


























# Funções de interface gráfica
def cadastrar_aluno():
    nome = entry_nome.get()
    try:
        idade = int(entry_idade.get())
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número inteiro")
        return
    habilidades = entry_habilidades.get().split(',')
    nivel_poder = entry_nivel_poder.get()
    equipe = entry_equipe.get() or None
    status_matricula = entry_status.get() or 'Ativo'
    aluno = Aluno(nome, idade, habilidades, nivel_poder, equipe, status_matricula)
    if aluno.validar():
        sistema.cadastrar_aluno(aluno)
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
    else:
        messagebox.showerror("Erro", "Dados do aluno inválidos.")

#Excluir
def excluir_aluno():
    nome_aluno = entry_excluir_aluno.get()
    if nome_aluno:
        sistema.excluir_aluno(nome_aluno)
        messagebox.showinfo("Sucesso", f"Aluno {nome_aluno} excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, informe o nome do aluno.")



def consultar_alunos():
    nome = entry_consultar_nome.get() or None
    habilidades = entry_consultar_habilidades.get().split(',') or None
    equipe = entry_consultar_equipe.get() or None
    status_matricula = entry_consultar_status.get() or None
    resultados = sistema.buscar_alunos(nome, habilidades, equipe, status_matricula)
    if resultados:
        result_text = ""
        for aluno in resultados:
            result_text += f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Habilidades: {aluno['habilidades']}, Nível de Poder: {aluno['nivel_poder']}, Equipe: {aluno['equipe']}, Status: {aluno['status_matricula']}\n"
        messagebox.showinfo("Resultados", result_text)
    else:
        messagebox.showinfo("Resultados", "Nenhum aluno encontrado.")

def cadastrar_aula():
    nome = entry_nome_aula.get()
    instrutor = entry_instrutor.get()
    try:
        vagas = int(entry_vagas.get())
    except ValueError:
        messagebox.showerror("Erro", "Número de vagas deve ser um número inteiro")
        return
    aula = Aula(nome, instrutor, vagas)
    sistema.cadastrar_aula(aula)
    messagebox.showinfo("Sucesso", "Aula cadastrada com sucesso!")

def consultar_aulas():
    aulas = sistema.consultar_aulas()
    if aulas:
        result_text = ""
        for aula in aulas:
            result_text += f"Nome: {aula.nome}, Instrutor: {aula.instrutor}, Vagas: {aula.vagas}\n"
        messagebox.showinfo("Resultados", result_text)
    else:
        messagebox.showinfo("Resultados", "Nenhuma aula cadastrada.")

def cadastrar_missao():
    objetivo = entry_objetivo.get()
    equipe_designada = entry_equipe_designada.get()
    data_inicio = entry_data_inicio.get()
    data_termino = entry_data_termino.get()
    missao = Missao(objetivo, equipe_designada, data_inicio, data_termino)
    sistema.cadastrar_missao(missao)
    messagebox.showinfo("Sucesso", "Missão cadastrada com sucesso!")

def consultar_missoes():
    missoes = sistema.consultar_missoes()
    if missoes:
        result_text = ""
        for missao in missoes:
            result_text += f"Objetivo: {missao.objetivo}, Equipe Designada: {missao.equipe_designada}, Data de Início: {missao.data_inicio}, Data de Término: {missao.data_termino}, Status: {missao.status}\n"
        messagebox.showinfo("Resultados", result_text)
    else:
        messagebox.showinfo("Resultados", "Nenhuma missão cadastrada.")

def criar_equipe():
    nome_equipe = entry_nome_equipe.get()
    nomes_membros = entry_nomes_membros.get().split(',')
    instrutor = entry_instrutor_equipe.get()
    membros = [a for a in sistema.alunos if a.nome in nomes_membros]
    if membros:
        sistema.criar_equipe(nome_equipe, membros, instrutor)
        messagebox.showinfo("Sucesso", f"Equipe {nome_equipe} criada com sucesso!")
    else:
        messagebox.showerror("Erro", "Membros não encontrados. Tente novamente.")

def consultar_equipes():
    equipes = sistema.consultar_equipes()
    if equipes:
        result_text = ""
        for equipe in equipes:
            membros_nomes = [membro.nome for membro in equipe['membros']]
            result_text += f"Nome: {equipe['nome']}, Instrutor: {equipe['instrutor']}, Membros: {', '.join(membros_nomes)}\n"
        messagebox.showinfo("Resultados", result_text)
    else:
        messagebox.showinfo("Resultados", "Nenhuma equipe cadastrada.")



# Função para atualizar aluno na interface gráfica
def atualizar_aluno():
    nome_original = entry_nome_original.get()
    nome_novo = entry_nome_novo.get() or None
    idade = entry_idade_nova.get()
    habilidades = entry_habilidades_novas.get().split(',') if entry_habilidades_novas.get() else None
    nivel_poder = entry_nivel_poder_novo.get() or None
    equipe = entry_equipe_nova.get() or None
    status_matricula = entry_status_novo.get()

    if idade:
        try:
            idade = int(idade)
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro")
            return
    
    sistema.atualizar_aluno(nome_original, nome_novo, idade, habilidades, nivel_poder, equipe, status_matricula)
    messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")

def atualizar_aula():
    nome_original = entry_nome_aula_original.get()
    nome_novo = entry_nome_aula_novo.get() or None
    instrutor = entry_instrutor_aula.get() or None
    vagas = entry_vagas_aula.get()
    
    if vagas:
        try:
            vagas = int(vagas)
        except ValueError:
            messagebox.showerror("Erro", "Número de vagas deve ser um número inteiro")
            return
    
    sistema.atualizar_aula(nome_original, nome_novo, instrutor, vagas)
    messagebox.showinfo("Sucesso", "Aula atualizada com sucesso!")

# Função para excluir aula na interface gráfica
def excluir_aula():
    nome_aula = entry_nome_aula_excluir.get()
    if nome_aula:
        sistema.excluir_aula(nome_aula)
        messagebox.showinfo("Sucesso", f"Aula {nome_aula} excluída com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, informe o nome da aula.")

# Função para atualizar equipe na interface gráfica
def atualizar_equipe():
    nome_equipe = entry_nome_equipe.get()
    novo_nome = entry_novo_nome_equipe.get()
    novo_instrutor = entry_novo_instrutor_equipe.get()
    novos_membros_nomes = entry_novos_membros_equipe.get().split(',')

    if nome_equipe:
        novos_membros = [aluno for aluno in sistema.alunos if aluno.nome in novos_membros_nomes]
        sistema.atualizar_equipe(nome_equipe, novo_nome, novos_membros, novo_instrutor)
        messagebox.showinfo("Sucesso", f"Equipe {nome_equipe} atualizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, informe o nome da equipe.")



# Função para excluir equipe na interface gráfica
def excluir_equipe():
    nome_equipe = entry_nome_equipe_excluir.get()
    if nome_equipe:
        sistema.excluir_equipe(nome_equipe)
        messagebox.showinfo("Sucesso", f"Equipe {nome_equipe} excluída com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, informe o nome da equipe.")



















        
# Interface gráfica usando Tkinter
root = tk.Tk()
root.title("Sistema de Gerenciamento")

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl, style='My.TFrame')
tab2 = ttk.Frame(tabControl, style='My.TFrame')
tab3 = ttk.Frame(tabControl, style='My.TFrame')
tab5 = ttk.Frame(tabControl, style='My.TFrame')
tab6 = ttk.Frame(tabControl, style='My.TFrame')
tab7 = ttk.Frame(tabControl, style='My.TFrame')
tab8 = ttk.Frame(tabControl, style='My.TFrame')






tabControl.add(tab1, text='CRUD Aluno')
tabControl.add(tab2, text='CRUD Aula')
tabControl.add(tab3, text='CRUD Equipe')
tabControl.add(tab5, text='Matricular em Aula')
tabControl.add(tab6, text='Cadastrar Missão')
tabControl.add(tab7, text='Consultar Missão')
tabControl.add(tab8, text='Registrar em Missão')






tabControl.pack(expand=1, fill="both")
style = ttk.Style()
style.configure('My.TFrame', background='#1e3c5f')

# Aba 1: Cadastrar Aluno
ttk.Label(tab1, text="Nome:").grid(column=0, row=0, padx=10, pady=5)
entry_nome = ttk.Entry(tab1)
entry_nome.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab1, text="Idade:").grid(column=0, row=1, padx=10, pady=5)
entry_idade = ttk.Entry(tab1)
entry_idade.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(tab1, text="Habilidades:").grid(column=0, row=2, padx=10, pady=5)
entry_habilidades = ttk.Entry(tab1)
entry_habilidades.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(tab1, text="Nível de Poder:").grid(column=0, row=3, padx=10, pady=5)
entry_nivel_poder = ttk.Entry(tab1)
entry_nivel_poder.grid(column=1, row=3, padx=10, pady=5)

ttk.Label(tab1, text="Equipe:").grid(column=0, row=4, padx=10, pady=5)
entry_equipe = ttk.Entry(tab1)
entry_equipe.grid(column=1, row=4, padx=10, pady=5)

ttk.Label(tab1, text="Status de Matrícula:").grid(column=0, row=5, padx=10, pady=5)
entry_status = ttk.Entry(tab1)
entry_status.grid(column=1, row=5, padx=10, pady=5)

ttk.Button(tab1, text="Cadastrar Aluno", command=cadastrar_aluno).grid(column=0, row=6, columnspan=2, pady=10)

#Consultar Aluno
ttk.Label(tab1, text="Nome:").grid(column=3, row=0, padx=10, pady=5)
entry_consultar_nome = ttk.Entry(tab1)
entry_consultar_nome.grid(column=4, row=0, padx=10, pady=5)

ttk.Label(tab1, text="Habilidades:").grid(column=3, row=1, padx=10, pady=5)
entry_consultar_habilidades = ttk.Entry(tab1)
entry_consultar_habilidades.grid(column=4, row=1, padx=10, pady=5)

ttk.Label(tab1, text="Equipe:").grid(column=3, row=2, padx=10, pady=5)
entry_consultar_equipe = ttk.Entry(tab1)
entry_consultar_equipe.grid(column=4, row=2, padx=10, pady=5)

ttk.Label(tab1, text="Status de Matrícula:").grid(column=3, row=3, padx=10, pady=5)
entry_consultar_status = ttk.Entry(tab1)
entry_consultar_status.grid(column=4, row=3, padx=10, pady=5)

ttk.Button(tab1, text="Consultar Alunos", command=consultar_alunos).grid(column=3, row=4, columnspan=2, pady=10)

#Atualizar Aluno
ttk.Label(tab1, text="Nome Original:").grid(column=5, row=0, padx=10, pady=5)
entry_nome_original = ttk.Entry(tab1)
entry_nome_original.grid(column=6, row=0, padx=10, pady=5)

ttk.Label(tab1, text="Novo Nome:").grid(column=5, row=1, padx=10, pady=5)
entry_nome_novo = ttk.Entry(tab1)
entry_nome_novo.grid(column=6, row=1, padx=10, pady=5)

ttk.Label(tab1, text="Nova Idade:").grid(column=5, row=2, padx=10, pady=5)
entry_idade_nova = ttk.Entry(tab1)  
entry_idade_nova.grid(column=6, row=2, padx=10, pady=5)

ttk.Label(tab1, text="Novas Habilidades:").grid(column=5, row=3, padx=10, pady=5)
entry_habilidades_novas = ttk.Entry(tab1)
entry_habilidades_novas.grid(column=6, row=3, padx=10, pady=5)

ttk.Label(tab1, text="Novo Nível de Poder:").grid(column=5, row=4, padx=10, pady=5)
entry_nivel_poder_novo = ttk.Entry(tab1)
entry_nivel_poder_novo.grid(column=6, row=4, padx=10, pady=5)

ttk.Label(tab1, text="Nova Equipe:").grid(column=5, row=5, padx=10, pady=5)
entry_equipe_nova = ttk.Entry(tab1)
entry_equipe_nova.grid(column=6, row=5, padx=10, pady=5)

ttk.Label(tab1, text="Novo Status de Matrícula:").grid(column=5, row=6, padx=10, pady=5)
entry_status_novo = ttk.Entry(tab1)
entry_status_novo.grid(column=6, row=6, padx=10, pady=5)

ttk.Button(tab1, text="Atualizar Aluno", command=atualizar_aluno).grid(column=5, row=7, columnspan=2, pady=10)

#Excluir Aluno
ttk.Label(tab1, text="Nome do Aluno:").grid(column=7, row=0, padx=10, pady=5)
entry_excluir_aluno = ttk.Entry(tab1)
entry_excluir_aluno.grid(column=8, row=0, padx=10, pady=5)

ttk.Button(tab1, text="Excluir Aluno", command=excluir_aluno).grid(column=7, row=1, columnspan=2, pady=10)





















# Aba 2: Cadastrar Aula
ttk.Label(tab2, text="Nome da Aula:").grid(column=0, row=0, padx=10, pady=5)
entry_nome_aula = ttk.Entry(tab2)
entry_nome_aula.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab2, text="Instrutor:").grid(column=0, row=1, padx=10, pady=5)
entry_instrutor = ttk.Entry(tab2)
entry_instrutor.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(tab2, text="Número de Vagas:").grid(column=0, row=2, padx=10, pady=5)
entry_vagas = ttk.Entry(tab2)
entry_vagas.grid(column=1, row=2, padx=10, pady=5)

ttk.Button(tab2, text="Cadastrar Aula", command=cadastrar_aula).grid(column=0, row=3, columnspan=2, pady=10)

#Consultar Aula
ttk.Button(tab2, text="Consultar Aulas", command=consultar_aulas).grid(column=3, row=0, columnspan=1, pady=10)

#Atualizar Aula
ttk.Label(tab2, text="Nome Original da Aula:").grid(column=4, row=0, padx=10, pady=5)
entry_nome_aula_original = ttk.Entry(tab2)
entry_nome_aula_original.grid(column=5, row=0, padx=10, pady=5)

ttk.Label(tab2, text="Novo Nome da Aula:").grid(column=4, row=1, padx=10, pady=5)
entry_nome_aula_novo = ttk.Entry(tab2)
entry_nome_aula_novo.grid(column=5, row=1, padx=10, pady=5)

ttk.Label(tab2, text="Instrutor:").grid(column=4, row=2, padx=10, pady=5)
entry_instrutor_aula = ttk.Entry(tab2)
entry_instrutor_aula.grid(column=5, row=2, padx=10, pady=5)

ttk.Label(tab2, text="Número de Vagas:").grid(column=4, row=3, padx=10, pady=5)
entry_vagas_aula = ttk.Entry(tab2)
entry_vagas_aula.grid(column=5, row=3, padx=10, pady=5)
ttk.Button(tab2, text="Atualizar Aula", command=atualizar_aula).grid(column=4, row=4, columnspan=2, pady=10)

# Excluir Aula
ttk.Label(tab2, text="Nome da Aula para Excluir:").grid(column=7, row=0, padx=10, pady=5)
entry_nome_aula_excluir = ttk.Entry(tab2)
entry_nome_aula_excluir.grid(column=8, row=0, padx=10, pady=5)

ttk.Button(tab2, text="Excluir Aula", command=excluir_aula).grid(column=6, row=1, columnspan=2, pady=10)





















# Aba 5: Matricular em Aula
ttk.Label(tab5, text="Nome do Aluno:").grid(column=0, row=0, padx=10, pady=5)
entry_nome_aluno_aula = ttk.Entry(tab5)
entry_nome_aluno_aula.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab5, text="Nome da Aula:").grid(column=0, row=1, padx=10, pady=5)
entry_nome_aula_aluno = ttk.Entry(tab5)
entry_nome_aula_aluno.grid(column=1, row=1, padx=10, pady=5)

ttk.Button(tab5, text="Matricular em Aula").grid(column=0, row=2, columnspan=2, pady=10)













# Aba 6: Cadastrar Missão
ttk.Label(tab6, text="Objetivo:").grid(column=0, row=0, padx=10, pady=5)
entry_objetivo = ttk.Entry(tab6)
entry_objetivo.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab6, text="Equipe Designada:").grid(column=0, row=1, padx=10, pady=5)
entry_equipe_designada = ttk.Entry(tab6)
entry_equipe_designada.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(tab6, text="Data de Início (AAAA-MM-DD):").grid(column=0, row=2, padx=10, pady=5)
entry_data_inicio = ttk.Entry(tab6)
entry_data_inicio.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(tab6, text="Data de Término (AAAA-MM-DD):").grid(column=0, row=3, padx=10, pady=5)
entry_data_termino = ttk.Entry(tab6)
entry_data_termino.grid(column=1, row=3, padx=10, pady=5)

ttk.Button(tab6, text="Cadastrar Missão", command=cadastrar_missao).grid(column=0, row=4, columnspan=2, pady=10)

# Aba 7: Consultar Missão
ttk.Button(tab7, text="Consultar Missões", command=consultar_missoes).grid(column=0, row=0, columnspan=2, pady=10)

# Aba 8: Registrar em Missão
ttk.Label(tab8, text="Nome do Aluno:").grid(column=0, row=0, padx=10, pady=5)
entry_nome_aluno_missao = ttk.Entry(tab8)
entry_nome_aluno_missao.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab8, text="Objetivo da Missão:").grid(column=0, row=1, padx=10, pady=5)
entry_objetivo_missao = ttk.Entry(tab8)
entry_objetivo_missao.grid(column=1, row=1, padx=10, pady=5)

ttk.Button(tab8, text="Registrar em Missão").grid(column=0, row=2, columnspan=2, pady=10)































# Aba 9: Criar Equipe
ttk.Label(tab3, text="Nome da Equipe:").grid(column=0, row=0, padx=10, pady=5)
entry_nome_equipe = ttk.Entry(tab3)
entry_nome_equipe.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab3, text="Nomes dos Membros:").grid(column=0, row=1, padx=10, pady=5)
entry_nomes_membros = ttk.Entry(tab3)
entry_nomes_membros.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(tab3, text="Instrutor:").grid(column=0, row=2, padx=10, pady=5)
entry_instrutor_equipe = ttk.Entry(tab3)
entry_instrutor_equipe.grid(column=1, row=2, padx=10, pady=5)

ttk.Button(tab3, text="Criar Equipe", command=criar_equipe).grid(column=0, row=3, columnspan=2, pady=10)

# Aba 10: Consultar Equipe
ttk.Button(tab3, text="Consultar Equipes", command=consultar_equipes).grid(column=2, row=0, columnspan=2, pady=10)



# Atualizar Equipe
ttk.Label(tab3, text="Nome da Equipe:").grid(column=4, row=0, padx=10, pady=5)
entry_nome_equipe = ttk.Entry(tab3)
entry_nome_equipe.grid(column=5, row=0, padx=10, pady=5)

ttk.Label(tab3, text="Novo Nome da Equipe:").grid(column=4, row=1, padx=10, pady=5)
entry_novo_nome_equipe = ttk.Entry(tab3)
entry_novo_nome_equipe.grid(column=5, row=1, padx=10, pady=5)

ttk.Label(tab3, text="Novo Instrutor da Equipe:").grid(column=4, row=2, padx=10, pady=5)
entry_novo_instrutor_equipe = ttk.Entry(tab3)
entry_novo_instrutor_equipe.grid(column=5, row=2, padx=10, pady=5)

ttk.Label(tab3, text="Novos Membros da Equipe (nomes separados por vírgula):").grid(column=4, row=3, padx=10, pady=5)
entry_novos_membros_equipe = ttk.Entry(tab3)
entry_novos_membros_equipe.grid(column=5, row=3, padx=10, pady=5)

ttk.Button(tab3, text="Atualizar Equipe", command=atualizar_equipe).grid(column=5, row=4, columnspan=1, pady=10)


# Excluir Equipe
ttk.Label(tab3, text="Nome da Equipe para Excluir:").grid(column=6, row=0, padx=10, pady=5)
entry_nome_equipe_excluir = ttk.Entry(tab3)
entry_nome_equipe_excluir.grid(column=7, row=0, padx=10, pady=5)

ttk.Button(tab3, text="Excluir Equipe", command=excluir_equipe).grid(column=6, row=1, columnspan=2, pady=10)






root.mainloop()
