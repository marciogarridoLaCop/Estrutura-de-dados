# Universidade de Vassouras


[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)
# Conheca o Curso de Engenharia de Software 
[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2021/12/Simbolo_Engenharia_de_Software.jpg)](https://universidadedevassouras.edu.br/graduacao-marica/engenharia-de-software/)

## Estrutura-de-dados-avançados
# Exercício 00

O problema que usaremos é bem conhecido e bastante simples. Queremos resolver uma equação de segundo grau, ou seja, dada a equação : 𝒂𝒙𝟐 + 𝒃𝒙 + 𝒄, queremos saber quais são as suas raízes reais, se elas existirem. Desta forma, resolva a função 2𝑥ˆ2 + 2𝑥 − 6.

# Exercício 01

Um engenheiro de automação capturou durante um período de 30 dias [Dados Climáticos](https://github.com/marciogarridoLaCop/Estrutura-de-dados/blob/EDA/dadosclimaticos.txt), diversos valores de temperatura, umidade e pressão de um ambiente específico. Sabendo que o acumulado de 24 horas foi a resultante de aporte de n ciclos de 10 minutos, calcule:

1) Para todas as grandezas climáticas, os valores mínimos, máximos, médios em 24 horas de um do vigésimo dia;
2) A quantidade de ciclos por período de coleta neste dia.


# Exercícios 02
Enunciado: Árvore Genealógica

Imagine que você recebeu a tarefa de criar uma árvore genealógica para uma família. A árvore deve ser capaz de armazenar informações sobre várias gerações de uma família e suas relações.

Requisitos:

Modelo de Dados:

Cada membro da família deve ser representado como um dicionário contendo: nome, idade, sexo e uma lista de filhos.
A lista de filhos de cada membro da família deve conter dicionários representando cada filho.
Funções a serem implementadas:

adicionar_membro(nome, idade, sexo, pai=None): Adiciona um membro à árvore genealógica. Se o pai for especificado, o membro é adicionado como filho desse pai.
buscar_membro(nome): Retorna o dicionário representando o membro da família com o nome especificado.
descendentes(nome): Retorna uma lista de todos os descendentes do membro com o nome especificado. Esta função deve ser implementada de forma recursiva.
Exemplo de Uso:

Adicione um membro chamado "João" com 70 anos.
Adicione um filho para "João" chamado "Carlos" com 50 anos.
Adicione um filho para "Carlos" chamado "Pedro" com 30 anos.
Adicione um filho para "Pedro" chamado "Lucas" com 10 anos.
Ao chamar a função descendentes("João"), ela deve retornar uma lista contendo "Carlos", "Pedro" e "Lucas".
Desafio Extra:

Implemente uma função antepassados(nome) que, dado o nome de um membro, retorna uma lista de todos os seus antepassados diretos (pai, avô, bisavô, etc.). Esta função também deve ser implementada de forma recursiva.
Este enunciado exige que o aluno utilize listas para armazenar os filhos de cada membro, dicionários para armazenar informações sobre cada membro e recursividade para buscar descendentes e antepassados.
