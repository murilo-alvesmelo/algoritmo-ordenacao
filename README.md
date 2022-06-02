
# Algoritmos Ordenação - Projeto e Análise de Algoritmos

![image](https://user-images.githubusercontent.com/83835393/171540760-42181cb2-0cc5-4cf6-8da5-b96232ac1dac.png)

Universidade Federal do Tocantins - Ciência da Computação

Pedro Thomas Barros de Oliveira & Murilo Alves Melo


## 1. Introdução

Vimos por meio desse trabalho o estudo e desenvolvimento dos algoritmos de ordenação mais utilizados por desenvolvedores, onde comparamos suas diferentes aplicações e desempenho em determinadas situações de aplicação.
A linguagem escolhida para o desenvolvimento da aplicação foi a Python, e a aplicação foi executada em um computador com a seguinte configuração:

- Processador Intel(R) Core (TM) i7-8565U CPU @ 1.8GHz
- 12GB de memória RAM com frequência de 2666Mhz
- Microsoft Windows 10 Pro 64 Bits
    
## 2. Objetivo
O objetivo do projeto é analisar o desempenho dos algoritmos 
Insertion Sort, Selection Sort,
Bubble Sort, Merge Sort e Quick Sort. 
Que será executada em função do tempo que os algoritmos levam para trabalhar nas situações de vetores aleatórios, crescentes e decrescentes compostos por variáveis de 100 a 5 milhões de elementos, exceto em casos em que o computador não consiga executar algum desses casos.
O software desenvolvido recebe do usuário qual ordenação deverá executar, e após a execução retorna um valor correspondente ao tempo em segundos que a máquina levou para executar a ação. Os valores retornados foram armazenados e serão apresentados nesse projeto através de representação gráfica em função do tempo e número de elementos contidos no vetor.


## 3. Desenvolvimento

Em programação o termo ordenar representa a realocação de um conjunto de dados de forma que fiquem organizados dentro de algum padrão. No caso do algoritmo do projeto, o padrão de ordenação a ser seguido vai ser o numérico ordenado de forma crescente.
Os resultados mostrados no processo podem variar de acordo com o número de objetos a serem ordenados, da forma de organização de cada um deles, além é claro do processo de ordenação selecionado pelo usuário

### 3.1 Insertion Sort

O Insertion Sort é um algoritmo de ordenação muito usado, porém bem simples que consiste na realocação dos dados de forma em que se é construída uma nova lista com os valores ordenados. Em seu melhor caso esse algoritmo percorre todo o vetor e percebe que ele já está ordenado obtendo assim a complexidade de Ω(n). Caso contrário ele possuirá uma complexidade de Θ(n²).

![image](https://user-images.githubusercontent.com/83835393/171542592-c7fd0a79-1ce2-4a27-b817-a794bbfa9a01.png)

![image](https://user-images.githubusercontent.com/83835393/171542756-891bdc95-b532-4629-ae47-1a79eeb80bb4.png)

![image](https://user-images.githubusercontent.com/83835393/171542777-26a83c5a-773a-43fe-9596-13708a3319b8.png)

![image](https://user-images.githubusercontent.com/83835393/171542802-e5285133-4476-46aa-a9e6-fe7edf94f713.png)

Pode-se notar que para um vetor ordenado de forma crescente o algoritmo se comportou de forma superior, o que já era esperada em função de sua complexidade de Ω(n) no melhor dos casos.
Em seu pior caso o algoritmo ordenou o vetor com itens ordenados em forma decrescente provando assim sua complexidade de Θ(n²) a ponto de que vetores de tamanho de 100 mil ou mais elementos não puderam ser executados pela máquina.
No caso do vetor aleatório o comportamento foi parecido ainda assim com o comportamento de Θ(n²), porém com menos processamentos podendo ser executado até 200 mil elementos no vetor. 
Logo é possível notar que Insertion Sort é um algoritmo utilizável apenas para vetores de tamanho pequeno, no caso de vetores grandes com tamanho superior a 10 mil o algoritmo já começa a se tornar lento.

### 3.2  Selection Sort

O Selection Sort percorre o vetor buscando o menor valor e assim que encontrado, ele é alocado na primeira posição, após isso ele busca o segundo menor, então o terceiro, e assim sucessivamente em função de (n-1) até que o maior seja ordenado.

![image](https://user-images.githubusercontent.com/83835393/171542880-db5e05cd-0502-4f95-9303-d8a3f0e9b3ec.png)

![image](https://user-images.githubusercontent.com/83835393/171542919-b722f6b3-d40b-4b6b-b958-6ce05fedf78a.png)

A principal característica do Selection Sort é sua complexidade que sempre é de Θ(n²), o que mantem o gráfico parecido em todos os casos de inserção de valores, ele sofre uma alteração de adaptação em função da quantidade de itens a serem analisados, porém o comportamento se mantem parecido tanto para um vetor de forma crescente que seria o seu melhor caso, quanto para um de forma decrescente. O que torna o Selection Sort assim como o Insection Sort viável apenas para vetores de tamanho pequeno. 

### 3.3  Bubble Sort

O Bubble Sort é um algoritmo de baixa complexidade que percorre o vetor por várias vezes fazendo o elemento de maior vetor ser alocado ao topo.
Seu melhor caso executa essa operação por (N) vezes, levando em consideração que N é o tamanho do vetor. Já seu pior caso tem uma complexidade de O(n²). 
Por ser um algoritmo de complexidade de ordem quadrática ele torna-se não recomendado para vetores com grande quantidade de elementos que busquem uma execução rápida na ordenação.

![image](https://user-images.githubusercontent.com/83835393/171543007-b5f576ba-fd9b-4fe4-998d-41dc27fcb381.png)

![image](https://user-images.githubusercontent.com/83835393/171543061-bb1ed36c-f22c-474e-b44d-2f4d6ba900e8.png)

Esse algoritmo tem um desempenho semelhante com o de um Selection Sort, pelo fato de percorrer o vetor checando seus elementos quando executado em um vetor crescente em uma execução bem rápida.
Ao interagir com um vetor ordenado de forma decrescente o algoritmo precisará percorre-lo o número máximo de vezes e sempre fazendo o máximo de trocas o que reduz seu desempenho consideravelmente sendo assim seu pior caso.
O uso desse algoritmo é recomendado para vetores pequenos e de preferência com ordenação aleatória. Ao interagir com vetores decrescentes a sua execução é consideravelmente aumentada em comparação com outras formas de ordenação.

### 3.4  Merge Sort

O Merge Sort consiste em pegar parte do vetor e criar uma sequência ordenada em função de pares de dados ordenados do vetor original, após isso ele agrupa sequencias de quatro elementos e assim até a ordenação do vetor completo. 

![image](https://user-images.githubusercontent.com/83835393/171543172-afdb8392-05af-4661-93b4-94258c95e41b.png)

![image](https://user-images.githubusercontent.com/83835393/171543190-ab706e3d-ae3c-4dc6-bb30-4c599cbb80e7.png)

O algoritmo possui complexidade Θ (n log n) para todos os casos pelo fato de conseguir dividir o problema em problemas menores. Desde que a complexidade do vetor seja relevante o algoritmo terá o mesmo desempenho para quase todos os casos.

### 3.5  Quick Sort

O Quick Sort é um algoritmo que possui um pior caso de Θ (n²), por mais que possua um pior caso quadrático, esse algoritmo é a melhor opção de ordenação, o tempo médio esperado é de Θ (n log n) que são valores bem pequenos.

![image](https://user-images.githubusercontent.com/83835393/171543238-8bd2e115-3a7c-4792-9884-fdb584dff8d9.png)

![image](https://user-images.githubusercontent.com/83835393/171543250-36c60f14-3186-4dd4-809d-4b40c9287f9a.png)

O algoritmo Quick Sort é de longe o melhor algoritmo de ordenação existente tendo a execução que leva metade do tempo de execução de qualquer outro algoritmo acima nas mesmas condições.

## 4. Conclusão

- Quick Sort se mantém constantes para todos os tamnhos e o Heap é o mais lento.
- Insertion Sort é o mais lento para qualquer tamanho se estão em ordem decrescente.
- Dos algoritimos de complexidade O(n²), o Insertion Sort é o melhor para todos os tamanhos.
