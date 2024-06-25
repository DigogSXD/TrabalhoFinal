# TrabalhoFinal
# 29/05
* Para conseguimos visualizar o que precisa ser feito é nescessario saber o que vai ser feito:
  
Temos a situação problema que é a Escola para Jovens Superdotados do Professor Xavier, conhecida por acolher e treinar jovens mutantes, está enfrentando desafios crescentes na administração de suas operações diárias. O aumento do número de alunos e a complexidade das atividades exigem o desenvolvimento de um sistema de gerenciamento eficiente para atender às necessidades específicas da instituição.

A linguagem que eu escolhir foi python, mesmo não apresentando o melhor desempenho em fazer isso, mas é a que estou familiarizado, e conheço uma bliblioteca que se chama pandas, que é uma biblioteca de software para anipulação e análise de dados.

Dei uma revisada em como mexer no GitHub corretamente e reorganizei as pastas para deixar mais claro o que é código e o que não é, e deixar o mais fácil possível para o usuario.

# Pensando na situação problema
Criamos um menu simples onde a pessoa pode fazer 4 opções, que seria Cadastrar Aluno, Buscar Alunos, Registrar Matrícula em Aula e sair, bem simples para ter um norte no que iriamos fazer. Conforme fomos lendo o escopo total do que se pede nos vemos que teremos que arrumar o menu pois vamos ter mais do que 4 opções, pelo que vimos prevemos que serão 10, acrescentando mais 6, Cadastrar Missão, Registrar Participação em Missão, Gerar Relatório de Missões, Criar Equipe, Gerenciar Membros de Equipe, Consultar Equipes e Sair

# 30/05
Com o desenvolvimento do projeto, decidi desistir de usar o Pandas, pois não consegui utilizá-lo corretamente e enfrentei muitos erros durante o processo. Lembrei-me do meu professor do semestre passado, que ensinou programação orientada a objetos (OOP), o que me ajudou a relembrar como criar validações e algumas funções (defs) que eu havia desenvolvido anteriormente.

# 31/05
Não fiz nada

# 1/06
Etapas de Desenvolvimento

Estruturação das Classes

O primeiro passo foi definir as classes principais que compõem o sistema: Aluno, Aula, Missao e Sistema.

        Classe Aluno: Representa um aluno mutante, armazenando informações como nome, idade, habilidades, nível de poder, equipe e status de matrícula. Métodos para validação e matrícula em aulas e missões foram incluídos.
        class Aluno:
          def __init__(self, nome, idade, habilidades, nivel_poder, equipe=None, status_matricula='Ativo'):
            ...
          def validar(self):
            ...
          def matricular_em_aula(self, aula):
            ...
          def participar_missao(self, missao):
            ...
   
        Classe Aula: Representa uma aula, com atributos como nome, instrutor, número de vagas e alunos matriculados.
        class Aula:
            def __init__(self, nome, instrutor, vagas):
                ...
            def registrar_aluno(self, aluno):
                ...
        
        Classe Missao: Representa uma missão, incluindo objetivo, equipe designada, datas de início e término, status e participantes.
        class Missao:
            def __init__(self, objetivo, equipe_designada, data_inicio, data_termino, status='Pendente'):
                ...
            def registrar_participante(self, aluno):
                ...
        Classe Sistema: Gerencia todas as entidades e operações do sistema. Inclui métodos para cadastrar alunos, aulas e missões, além de consultar e gerenciar equipes.
        class Sistema:
            def __init__(self):
                ...
            def cadastrar_aluno(self, aluno):
                ...
            def buscar_alunos(self, nome=None, habilidades=None, equipe=None, status_matricula=None):
                ...
            def cadastrar_aula(self, aula):
                ...
            def consultar_aulas(self):
                ...
            def cadastrar_missao(self, missao):
                ...
            def consultar_missoes(self):
                ...
            def criar_equipe(self, nome, membros, instrutor):
                ...
            def consultar_equipes(self):
                ...
# 1/06 ao 3/06

Implementação das Funcionalidades

Cada funcionalidade foi implementada, testada e corrigida, com base nos métodos definidos nas classes acima

Cadastro de Alunos: Inclui validação dos dados inseridos pelo usuário.

Consulta de Alunos: Permite buscar alunos por critérios específicos.

Cadastro e Consulta de Aulas: Gestão de aulas com verificação de vagas.

Cadastro e Consulta de Missões: Gerenciamento de missões e registro de participação.

Criação e Consulta de Equipes: Formação de equipes e gestão dos membros.

# 3/06

Criação do Menu Interativo Definitivo
   
Um menu interativo foi criado para permitir ao usuário interagir com o sistema e acessar todas as funcionalidades.

O menu apresenta opções numeradas, permitindo que o usuário faça suas escolhas. Após cada seleção, ocorre a validação dos dados inseridos para garantir que estejam corretos.

No final o menu ficou com 11 opções.

# 5/06 até 18/06

Fiz a conexão com o banco de dados, configurei a conexão com o banco de dados no codigo e Implementei métodos para salvar e buscar dados no banco de dados.

mysql.connector: Utilizada para a conexão e execução de comandos no banco de dados MySQL.

Conexão com o Banco de Dados

Para conectar-se ao banco de dados MySQL, a função conectar_bd foi definida

Criação do Banco de Dados

A função criar_db cria o banco de dados xman caso ele ainda não exista:

A função criar_tabelas é responsável por criar todas as tabelas necessárias dentro do banco de dados xman:

Aluno: Armazena informações sobre os alunos, incluindo nome, idade, habilidades, nível de poder, equipe e status de matrícula.

Aula: Contém detalhes sobre as aulas oferecidas, como nome, instrutor e número de vagas.

Missao: Registra informações sobre as missões, como objetivo, equipe designada, datas de início e término, e status.

Matricula: Relaciona alunos e aulas, representando as matrículas dos alunos nas aulas.

HistoricoParticipacao: Registra a participação dos alunos nas aulas ao longo do tempo.

Equipe: Guarda informações sobre as equipes, incluindo nome e instrutor.

Membros_Equipe: Relaciona alunos às equipes, registrando a participação dos alunos nas equipes.

# 19/06 até 20/06
A classe Aluno foi desenvolvida para representar e gerenciar informações sobre os alunos da escola de mutantes. Esta classe permite a criação de instâncias de alunos, validação de dados, armazenamento no banco de dados e busca de registros de alunos. Abaixo, detalharemos a estrutura, métodos e funcionalidades desta classe.

Atributos
A classe Aluno possui os seguintes atributos:

nome: Nome do aluno (string).

idade: Idade do aluno (inteiro).

habilidades: Lista de habilidades do aluno (lista de strings).

nivel_poder: Nível de poder do aluno (string).

equipe: Equipe à qual o aluno pertence (string, opcional).

status_matricula: Status de matrícula do aluno (string, padrão 'Ativo').

__init__(self, nome, idade, habilidades, nivel_poder, equipe=None, status_matricula='Ativo')
Este é o método construtor da classe, responsável por inicializar uma nova instância de Aluno com os atributos fornecidos.

validar(self)
Este método verifica se os dados do aluno são válidos. Ele retorna True se todos os dados necessários estão presentes e válidos, caso contrário, retorna False.

salvar_bd(self)
Este método salva os dados do aluno no banco de dados. Ele se conecta ao banco de dados, insere os dados do aluno na tabela Aluno e, em seguida, fecha a conexão.

buscar_bd(nome=None, habilidades=None, equipe=None, status_matricula=None)
Este método estático permite buscar alunos no banco de dados com base em critérios fornecidos (nome, habilidades, equipe e status de matrícula). Ele constrói dinamicamente a consulta SQL de acordo com os parâmetros fornecidos, executa a consulta e retorna os resultados.

Para criar um aluno, uma instância da classe Aluno é inicializada com os dados do aluno.

#21/06 até 22/06
Atributos
A classe Aula possui os seguintes atributos:

nome: Nome da aula (string).

instrutor: Nome do instrutor da aula (string).

vagas: Número de vagas disponíveis para a aula (inteiro).

__init__(self, nome, instrutor, vagas)
Este é o método construtor da classe, responsável por inicializar uma nova instância de Aula com os atributos fornecidos.

salvar_bd(self)
Este método salva os dados da aula no banco de dados. Ele se conecta ao banco de dados, insere os dados da aula na tabela Aula e, em seguida, fecha a conexão.

Criação de uma Aula
Para criar uma aula, uma instância da classe Aula é inicializada com os dados da aula.

Atributos
A classe Missao possui os seguintes atributos:

objetivo: Objetivo da missão (string).

equipe_designada: Equipe designada para a missão (string).

data_inicio: Data de início da missão (data).

data_termino: Data de término da missão (data).

status: Status da missão (string, padrão 'Pendente').

Atributos
A classe Equipe possui os seguintes atributos:

nome: Nome da equipe (string).

instrutor: Nome do instrutor da equipe (string).

membros: Lista de membros da equipe (lista de dicionários, onde cada dicionário representa um membro com um ID e um nome).

__init__(self, nome, instrutor, membros=[])
Este é o método construtor da classe, responsável por inicializar uma nova instância de Equipe com os atributos fornecidos.

salvar_bd(self)
Este método salva os dados da equipe no banco de dados. Ele se conecta ao banco de dados, insere os dados da equipe na tabela Equipe, recupera o ID da equipe inserida, insere os membros da equipe na tabela Membros_Equipe e, em seguida, fecha a conexão.

carregar_bd()
Este método estático carrega todas as equipes do banco de dados, incluindo seus membros. Ele se conecta ao banco de dados, recupera os dados das equipes da tabela Equipe, para cada equipe, recupera seus membros da tabela Membros_Equipe e, em seguida, fecha a conexão.

#23/06 sofrendo muitos updates class sistema

Resumo das Funcionalidades Principais:

Inicialização e Carregamento de Dados:

No método __init__, ao criar uma instância de Sistema, os dados são carregados automaticamente chamando o método carregar_dados().
carregar_dados() chama métodos específicos para carregar alunos, aulas, missões e equipes do banco de dados.
Gerenciamento de Alunos:

cadastrar_aluno(aluno): Valida e cadastra um aluno no banco de dados e na lista interna self.alunos.
buscar_alunos(nome=None, habilidades=None, equipe=None, status_matricula=None): Chama um método estático Aluno.buscar_bd() para buscar alunos com critérios específicos.
Gerenciamento de Aulas:

cadastrar_aula(aula): Salva uma nova aula no banco de dados e na lista interna self.aulas.
consultar_aulas(): Retorna a lista de aulas carregadas.
Gerenciamento de Missões:

cadastrar_missao(missao): Salva uma nova missão no banco de dados e na lista interna self.missoes.
consultar_missoes(): Retorna a lista de missões carregadas.
atualizar_missao(id_missao, ...) e excluir_missao(id_missao): Atualiza e exclui missões no banco de dados e na lista interna.
Gerenciamento de Equipes:

criar_equipe(nome, membros, instrutor): Cria uma nova equipe com membros e um instrutor, salvando-a no banco de dados e na lista interna self.equipes.
consultar_equipes(): Retorna a lista de equipes carregadas.
Métodos para atualizar e excluir equipes.
Matrícula em Aula:

matricular_em_aula(nome_aluno, nome_aula): Matricula um aluno em uma aula específica, atualizando o banco de dados e a lista interna de vagas da aula.

Análise dos Métodos
Persistência de Dados: Todos os métodos de cadastro (cadastrar_aluno, cadastrar_aula, cadastrar_missao, criar_equipe) utilizam o método salvar_bd() das respectivas classes (Aluno, Aula, Missao, Equipe) para persistir os dados no banco de dados após validação.

Atualização e Exclusão: Métodos como atualizar_aluno, atualizar_aula, atualizar_missao, atualizar_equipe e equivalentes de exclusão utilizam comandos SQL diretamente para atualizar ou excluir registros do banco de dados, garantindo consistência entre a lista interna e o banco.

Consulta e Carregamento: Métodos como buscar_alunos, consultar_aulas, consultar_missoes, consultar_equipes usam consultas SQL para carregar dados específicos do banco de dados e retorná-los como listas de dicionários.

# 29/06

Criação da interface usando a bliblioteca tkinter arrumando os erros até hoje
