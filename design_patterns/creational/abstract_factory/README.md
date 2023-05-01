# Sobre o Design Pattern Abstract Factory
O padrão de design Abstract Factory é um padrão de criação que fornece uma 
interface para criar famílias de objetos relacionados ou dependentes sem 
especificar suas classes concretas. Ele permite que você crie objetos 
relacionados sem se preocupar com as classes específicas desses objetos.

Em termos simples, o Abstract Factory é um padrão de criação que encapsula
a criação de objetos relacionados, sem expor sua lógica de criação.


# Sobre a Implementação Realizada
Neste exemplo, temos as classes abstratas `Pizza` e `Beverage` que definem 
os métodos abstratos `prepare` e `serve`, respectivamente. As classes 
concretas `Margherita`, `Pepperoni`, `Coke` e `Pepsi` implementam esses métodos
de acordo com suas características.

Em seguida, temos a classe abstrata `Restaurant` que define os métodos 
abstratos `get_pizza` e `get_beverage`. As classes concretas `ItalianRestaurant` 
e `AmericanRestaurant` herdam de `Restaurant` e implementam esses métodos para 
criar instâncias de `Margherita` e `Coke`, e `Pepperoni` e `Pepsi`, respectivamente.

Por fim, no código principal, criamos instâncias das fábricas 
`ItalianRestaurant` e `AmericanRestaurant` e chamamos seus métodos 
`get_pizza` e `get_beverage` para obter instâncias concretas de `Pizza` 
e `Beverage`. Em seguida, chamamos os métodos `prepare` e serve desses 
objetos para obter os resultados esperados.


No exemplo deste código, podemos criar uma nova fábrica que produz diferentes
tipos de Pizza e Beverage, desde que implemente a interface `Restaurant`.
Isso torna a implementação flexível e fácil de estender.

O padrão Abstract Factory pode ser útil quando você precisa criar 
objetos que pertencem a uma família específica e precisam ser 
consistentes entre si. Ele também permite que você adicione novos 
tipos de produtos sem modificar o código existente.

No entanto, esse padrão pode aumentar a complexidade do código, 
especialmente se houver muitas famílias de produtos a serem criadas.
Além disso, ele pode ser difícil de aplicar em situações em que os 
produtos não são facilmente categorizados em famílias.

Em resumo, o padrão Abstract Factory é útil quando você precisa
criar objetos relacionados que devem ser consistentes entre si, 
enquanto mantém uma implementação flexível e fácil de estender.


# Referências:
- [Abstract Factory in Python](https://refactoring.guru/design-patterns/abstract-factory/python/example)