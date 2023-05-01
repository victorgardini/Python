# Sobre o Design Pattern Abstract Factory
O padrão de design Builder é um padrão de criação que permite construir 
objetos complexos passo a passo. Ele fornece uma maneira de separar a 
construção de um objeto complexo de sua representação, de modo que o 
mesmo processo de construção possa criar diferentes representações.

Em termos simples, o padrão Builder é usado quando queremos criar 
um objeto complexo passo a passo e ter controle sobre cada etapa do 
processo de construção.


# Sobre a Implementação Realizada

Temos a classe `Director`, que é responsável por gerenciar o
processo de construção do objeto complexo `Car`. A classe `Builder` define 
os métodos abstratos que são usados para construir o objeto, enquanto 
as classes `JeepBuilder` e `SportsCarBuilder` herdam de `Builder` e implementam 
esses métodos para construir objetos `Car` específicos.

Por fim, temos a classe `Car` que define o objeto complexo a ser construído.

No código principal, criamos uma instância do `JeepBuilder` e um 
`Director`. O `Director` gerencia o processo de construção do objeto 
`Car`, passando o `JeepBuilder` para o método `construct_car`. 
Esse método chama os métodos definidos em `JeepBuilder` para 
construir um objeto `Car` específico. Em seguida, obtemos o 
objeto `Car` criado e imprimimos suas propriedades.

Em seguida, criamos uma instância do `SportsCarBuilder` e outro 
`Director`. O `Director` gerencia o processo de construção do 
objeto `Car`, passando o `SportsCarBuilder` para o método `construct_car`.


Esse padrão nos permite criar objetos complexos passo a passo e ter 
controle sobre cada etapa do processo de construção. Com ele, podemos 
criar diferentes tipos de objetos complexos sem alterar o código do
processo de construção.

Podemos criar diferentes tipos de carros apenas criando um novo 
construtor de carro que herda da classe `Builder` e implementa 
seus métodos abstratos. Dessa forma, podemos reutilizar o 
mesmo processo de construção para criar diferentes tipos de 
carros, mantendo o código organizado e fácil de estender.

O padrão `Builder` é útil quando precisamos construir objetos 
complexos passo a passo e ter controle sobre cada etapa do processo 
de construção. Ele também nos permite criar diferentes tipos de 
objetos complexos sem alterar o código do processo de construção.

No entanto, o padrão Builder pode tornar o código mais complexo,
especialmente se o objeto complexo tiver muitas partes e métodos. 
Além disso, ele pode ser um pouco mais lento do que outras abordagens 
de criação de objetos, pois exige que cada parte seja construída 
individualmente.


# Referências:
- [Builder in Python](https://refactoring.guru/design-patterns/builder/python/example)