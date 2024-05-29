#Instalar a bliblioteca plantuml
pip install plantuml

from plantuml import PlantUML

uml_code = """
@startuml
class Aluno {
    - nome
    - idade
    - habilidades
    - nivel_poder
    - equipe
    - status_matricula
    + cadastrar()
    + buscar()
}

class Missao {
    - objetivo
    - equipe_designada
    - data_inicio
    - data_termino
    - status
    - participantes
    + cadastrar()
    + registrar_participacao()
    + gerar_relatorio()
}

class Equipe {
    - nome
    - membros
    - instrutor
    + criar()
    + gerenciar_membros()
    + consultar()
}

class Aula {
    - nome
    - instrutor
    - vagas
    - alunos_matriculados
    + registrar_matricula()
}

Aluno --> Aula : registrar_matricula
Aluno --> Missao : registrar_participacao
Equipe --> Missao : equipe_designada
Aluno --> Equipe : pertence_a
@enduml
"""

# Save the UML code to a file
with open('diagrama_classes.puml', 'w') as f:
    f.write(uml_code)

# Generate the diagram using PlantUML
server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
server.processes_file('diagrama_classes.puml')
