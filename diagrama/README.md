<div align="center">
  <h1>Diagrama de todas as classes </h1>
</div> 
<h2>Classe Sistema: </h2>


Mantém listas de alunos, aulas, missões e equipes.
Fornece métodos para cadastrar e consultar cada entidade.
Classe Aluno:

Representa um aluno com atributos como nome, idade, habilidades, nível de poder, equipe e status de matrícula.
Inclui métodos para validar dados, matricular em aula e participar de missão.
Classe Aula:

Representa uma aula com atributos como nome, instrutor, número de vagas e lista de alunos matriculados.
Inclui um método para registrar alunos na aula.
Classe Missao:

Representa uma missão com atributos como objetivo, equipe designada, datas de início e término, status e participantes.
Inclui um método para registrar participantes.
Classe Equipe:

Representa uma equipe com atributos como nome, instrutor e lista de membros.
Inclui métodos para adicionar e remover membros, bem como consultar equipes.



















    +---------------------+
    |       Sistema       |
    +---------------------+
    | - alunos: list      |
    | - aulas: list       |
    | - missoes: list     |
    | - equipes: list     |
    +---------------------+
    | + cadastrar_aluno() |
    | + buscar_alunos()   |
    | + cadastrar_aula()  |
    | + consultar_aulas() |
    | + cadastrar_missao()|
    | + consultar_missoes()|
    | + criar_equipe()    |
    | + consultar_equipes()|
    +---------------------+
                 |
                 | contains
                 |
    +------------+------------+
    |                          |
    |                          |
    V                          V
    +-----------------+     +----------------+
    |      Aluno      |     |      Aula      |
    +-----------------+     +----------------+
    | - nome: str     |     | - nome: str    |
    | - idade: int    |     | - instrutor: str|
    | - habilidades: list | | - vagas: int   |
    | - nivel_poder: str   | | - alunos: list |
    | - equipe: str   |     +----------------+
    | - status_matricula: str| | + registrar_aluno()|
    +-----------------+     +----------------+
    | + validar()     |
    | + matricular_em_aula() |
    | + participar_missao() |
    +-----------------+
                 |
                 | participates
                 |
    +------------+------------+
    |                          |
    |                          |
    V                          V
    +------------------+   +----------------+
    |     Missao       |   |     Equipe     |
    +------------------+   +----------------+
    | - objetivo: str  |   | - nome: str    |
    | - equipe_designada: str | - instrutor: str|
    | - data_inicio: str|   | - membros: list |
    | - data_termino: str| +----------------+
    | - status: str    |   | + adicionar_membro()|
    | - participantes: list | | + remover_membro()|
    +------------------+   | + consultar_equipes()|
    | + registrar_participante() |
    +------------------+ 
