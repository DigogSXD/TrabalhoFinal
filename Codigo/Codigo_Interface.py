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
        
# Interface gráfica usando Tkinter
root = tk.Tk()
root.title("Sistema de Gerenciamento")

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 = ttk.Frame(tabControl)
tab10 = ttk.Frame(tabControl)
tab11 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Cadastrar Aluno')
tabControl.add(tab2, text='Consultar Aluno')
tabControl.add(tab3, text='Cadastrar Aula')
tabControl.add(tab11, text='Excluir Aluno')
tabControl.add(tab4, text='Consultar Aula')
tabControl.add(tab5, text='Matricular em Aula')
tabControl.add(tab6, text='Cadastrar Missão')
tabControl.add(tab7, text='Consultar Missão')
tabControl.add(tab8, text='Registrar em Missão')
tabControl.add(tab9, text='Criar Equipe')
tabControl.add(tab10, text='Consultar Equipe')



tabControl.pack(expand=1, fill="both")

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

# Aba 2: Consultar Aluno
ttk.Label(tab2, text="Nome:").grid(column=0, row=0, padx=10, pady=5)
entry_consultar_nome = ttk.Entry(tab2)
entry_consultar_nome.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab2, text="Habilidades:").grid(column=0, row=1, padx=10, pady=5)
entry_consultar_habilidades = ttk.Entry(tab2)
entry_consultar_habilidades.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(tab2, text="Equipe:").grid(column=0, row=2, padx=10, pady=5)
entry_consultar_equipe = ttk.Entry(tab2)
entry_consultar_equipe.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(tab2, text="Status de Matrícula:").grid(column=0, row=3, padx=10, pady=5)
entry_consultar_status = ttk.Entry(tab2)
entry_consultar_status.grid(column=1, row=3, padx=10, pady=5)

ttk.Button(tab2, text="Consultar Alunos", command=consultar_alunos).grid(column=0, row=4, columnspan=2, pady=10)

# Aba 3: Cadastrar Aula
ttk.Label(tab3, text="Nome da Aula:").grid(column=0, row=0, padx=10, pady=5)
entry_nome_aula = ttk.Entry(tab3)
entry_nome_aula.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab3, text="Instrutor:").grid(column=0, row=1, padx=10, pady=5)
entry_instrutor = ttk.Entry(tab3)
entry_instrutor.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(tab3, text="Número de Vagas:").grid(column=0, row=2, padx=10, pady=5)
entry_vagas = ttk.Entry(tab3)
entry_vagas.grid(column=1, row=2, padx=10, pady=5)

ttk.Button(tab3, text="Cadastrar Aula", command=cadastrar_aula).grid(column=0, row=3, columnspan=2, pady=10)

# Aba 4: Consultar Aula
ttk.Button(tab4, text="Consultar Aulas", command=consultar_aulas).grid(column=0, row=0, columnspan=2, pady=10)

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
ttk.Label(tab9, text="Nome da Equipe:").grid(column=0, row=0, padx=10, pady=5)
entry_nome_equipe = ttk.Entry(tab9)
entry_nome_equipe.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(tab9, text="Nomes dos Membros:").grid(column=0, row=1, padx=10, pady=5)
entry_nomes_membros = ttk.Entry(tab9)
entry_nomes_membros.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(tab9, text="Instrutor:").grid(column=0, row=2, padx=10, pady=5)
entry_instrutor_equipe = ttk.Entry(tab9)
entry_instrutor_equipe.grid(column=1, row=2, padx=10, pady=5)

ttk.Button(tab9, text="Criar Equipe", command=criar_equipe).grid(column=0, row=3, columnspan=2, pady=10)

# Aba 10: Consultar Equipe
ttk.Button(tab10, text="Consultar Equipes", command=consultar_equipes).grid(column=0, row=0, columnspan=2, pady=10)

# Aba 11: Excluir Aluno
ttk.Label(tab11, text="Nome do Aluno:").grid(column=0, row=0, padx=10, pady=5)
entry_excluir_aluno = ttk.Entry(tab11)
entry_excluir_aluno.grid(column=1, row=0, padx=10, pady=5)

ttk.Button(tab11, text="Excluir Aluno", command=excluir_aluno).grid(column=0, row=1, columnspan=2, pady=10)

root.mainloop()



