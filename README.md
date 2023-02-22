# Universidade de Vassouras


[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)
# Conheca o Curso de Engenharia de Software 
[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2021/12/Simbolo_Engenharia_de_Software.jpg)](https://universidadedevassouras.edu.br/graduacao-marica/engenharia-de-software/)

## Estrutura-de-dados



### Exemplo de complexidade de algoritimos utilizando a sequência de Fibonacci



### Exemplo de somatório de padrão



## Existindo um padrão 2D de um Array6x6, arr:

        1 1 1 0 0 0
        0 1 0 0 0 0
        1 1 1 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0


Definimos uma ampulheta 'A' para ser um subconjunto de valores com índices
caindo neste padrão na representação gráfica 'arr':

          a b c
            d
          e f g

Ou seja, em formato de ampulheta      

Desta forma, para uma matriz 6X6 existem 16 ampulhetas. Uma soma de ampulheta é a soma dos valores existentes nesse conjunto. 

Considerando a seguinte matriz:

      1 1 1 0 0 0
      0 1 0 0 0 0
      1 1 1 0 0 0
      0 0 2 4 4 0
      0 0 0 2 0 0
      0 0 1 2 4 0

As combinações possíveis são

![Screenshot](/ampulhetamaior.png) 

Calcule a soma da ampulheta para cada ampulheta em e imprima a soma máxima da ampulheta. A matriz será sempre

        ModelagemProduto.py



Para rodar o programa de modelagem da tabela Estabelecimento e precos rode o arquivo:

        ModelagemEstabelecimento.py

Ao final, serão gerados 3 arquivos na pasta temporaria tmp

![Screenshot](/venv/img/estabelecimentos.png) 



"""







Function Description
It should return an integer, the maximum hourglass sum in the array.
arr: an array of integers
Input Format
Each of the 6 lines of inputs 'arr' contains 6 space-separated integers arr[i][j].
Constraints
-9 <= arr[i][j] <= 9
0 <= i,j <= 5
Output Format
Print the largest (maximum) hourglass sum found in 'arr'.
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19
"""
