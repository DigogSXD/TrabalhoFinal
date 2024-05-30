
<div align="center">
  <h2>Bem-vindo ao nosso repositório! </h2>
</div> 
<div align="center">
  <h2>🎯 Objetivo </h2>
</div> 
* Manual do Usuário para o Sistema de Gerenciamento de Alunos, Missões e Equipes
Este manual oferece instruções detalhadas para usar o sistema de gerenciamento de alunos, missões e equipes. O sistema permite o cadastro e gerenciamento de alunos (mutantes), missões, equipes e matrículas em aulas e treinamentos.

Índice
Introdução
Instalação
Iniciando o Sistema
Funcionalidades do Sistema
Cadastro de Alunos
Consulta de Alunos
Matrícula em Aulas e Treinamentos
Cadastro de Missões
Acompanhamento de Participação em Missões
Relatórios de Missões
Gerenciamento de Equipes
Navegação no Menu
Introdução
Este sistema foi desenvolvido para gerenciar o cadastro de alunos (mutantes), suas matrículas em aulas e treinamentos, bem como o gerenciamento de missões e equipes. O sistema oferece uma interface interativa no terminal para facilitar o uso.

Instalação
Para usar o sistema, você precisará do Python instalado em sua máquina. Siga os passos abaixo para instalar e iniciar o sistema:

Instale o Python: Se você ainda não tem o Python instalado, baixe e instale a versão mais recente do site oficial do Python.

Baixe o Código do Sistema: Certifique-se de que o código do sistema está disponível localmente em seu computador.

Instale as Dependências: Execute o comando abaixo para instalar as dependências necessárias.

sh
Copiar código
pip install pandas
Execute o Sistema: Navegue até o diretório onde o código do sistema está armazenado e execute o arquivo principal.

sh
Copiar código
python sistema_gerenciamento.py
Iniciando o Sistema
Ao iniciar o sistema, você verá um menu de opções no terminal. Use as opções do menu para navegar pelas funcionalidades do sistema.

Funcionalidades do Sistema
Cadastro de Alunos
Para cadastrar um novo aluno, siga os passos abaixo:

No menu principal, escolha a opção "1. Cadastrar Aluno".
Insira os dados solicitados:
Nome
Idade
Habilidades (separadas por vírgula)
Nível de Poder
Equipe (se aplicável)
Status de Matrícula
O sistema validará os dados e informará se o cadastro foi realizado com sucesso.
Consulta de Alunos
Para buscar alunos por diferentes critérios, siga os passos abaixo:

No menu principal, escolha a opção "2. Buscar Alunos".
Insira o critério de busca (nome, habilidades, equipe, status) e o valor correspondente.
O sistema exibirá os alunos que correspondem ao critério de busca.
Matrícula em Aulas e Treinamentos
Para matricular alunos em aulas ou treinamentos, siga os passos abaixo:

No menu principal, escolha a opção "3. Registrar Matrícula em Aula".
Insira o nome do aluno e o nome da aula.
O sistema verificará a disponibilidade de vagas e, se houver, registrará a matrícula do aluno.
Cadastro de Missões
Para cadastrar uma nova missão, siga os passos abaixo:

No menu principal, escolha a opção "4. Cadastrar Missão".
Insira os detalhes da missão:
Objetivo
Equipe Designada
Data de Início (DD/MM/AAAA)
Data de Término (DD/MM/AAAA)
Status
O sistema registrará a missão com os dados fornecidos.
Acompanhamento de Participação em Missões
Para registrar a participação de alunos em missões, siga os passos abaixo:

No menu principal, escolha a opção "5. Registrar Participação em Missão".
Insira o objetivo da missão e o nome do aluno.
O sistema adicionará o aluno à lista de participantes da missão.
Relatórios de Missões
Para gerar relatórios de missões, siga os passos abaixo:

No menu principal, escolha a opção "6. Gerar Relatório de Missões".
Insira o objetivo da missão para a qual deseja gerar o relatório.
O sistema exibirá um relatório detalhado da missão, incluindo os participantes e os detalhes da missão.
Gerenciamento de Equipes
Criação de Equipes
Para criar uma nova equipe, siga os passos abaixo:

No menu principal, escolha a opção "7. Criar Equipe".
Insira o nome da equipe e o nome do instrutor.
O sistema registrará a nova equipe com os dados fornecidos.
Gerenciamento de Membros
Para adicionar ou remover membros de uma equipe, siga os passos abaixo:

No menu principal, escolha a opção "8. Gerenciar Membros de Equipe".
Insira o nome da equipe e escolha se deseja adicionar ou remover um membro.
Insira o nome do aluno a ser adicionado ou removido.
O sistema atualizará a lista de membros da equipe conforme solicitado.
Consulta de Equipes
Para consultar informações sobre uma equipe, siga os passos abaixo:

No menu principal, escolha a opção "9. Consultar Equipes".
Insira o nome da equipe para consulta.
O sistema exibirá os detalhes da equipe, incluindo membros e instrutor.
Navegação no Menu
Para navegar no menu, simplesmente insira o número correspondente à opção desejada e pressione Enter. Siga as instruções exibidas para cada funcionalidade.

Menu Principal
plaintext
Copiar código
Menu:
1. Cadastrar Aluno
2. Buscar Alunos
3. Registrar Matrícula em Aula
4. Cadastrar Missão
5. Registrar Participação em Missão
6. Gerar Relatório de Missões
7. Criar Equipe
8. Gerenciar Membros de Equipe
9. Consultar Equipes
10. Sair
Para sair do sistema, escolha a opção "10. Sair".

