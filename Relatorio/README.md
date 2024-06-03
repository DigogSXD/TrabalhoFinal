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

3. Criação do Menu Interativo Definitivo
   
Um menu interativo foi criado para permitir ao usuário interagir com o sistema e acessar todas as funcionalidades.

O menu apresenta opções numeradas, permitindo que o usuário faça suas escolhas. Após cada seleção, ocorre a validação dos dados inseridos para garantir que estejam corretos.

No final o menu ficou com 11 opções.
