# Sobre o Design Pattern Template Method
O padrão de design Visitor é utilizado para separar a lógica de um objeto
de sua estrutura. Ele permite que você defina novas operações sem alterar
as classes dos elementos sobre os quais as operações são realizadas.

Em geral, o Visitor usa uma interface Visitor para definir uma operação
a ser realizada sobre elementos de uma estrutura de objetos. Em seguida,
para cada classe de objeto na estrutura, ela implementa o método 
accept() - que aceita um objeto Visitor - e chama o método do objeto 
Visitor apropriado.


# Sobre a Implementação Realizada
No código, a classe Component é uma classe abstrata que define a interface 
de um componente. Ela declara um método abstrato `accept()`, que deve ser
implementado por cada componente concreto para receber um `Visitor`.

Existem dois tipos de `ConcreteComponents` - `ConcreteComponentA` e 
`ConcreteComponentB` - que implementam a interface `Component` e definem
seus próprios métodos exclusivos.

A classe `Visitor` define a interface do visitante. É uma classe abstrata
que define um método abstrato para cada ConcreteComponent que pode ser 
visitado. Cada método `visit()` é nomeado de forma diferente para refletir
o `ConcreteComponent` que ele visita.

As classes `ConcreteVisitor1` e `ConcreteVisitor2` implementam a interface
`Visitor` e fornecem uma implementação concreta para cada método `visit()`.

A função `client_code()` é o ponto de entrada para o padrão `Visitor`.
Ele toma uma lista de `Component` e um `Visitor` e chama `accept()` para 
cada componente, que redireciona a chamada de volta para o `Visitor`, que 
executa o comportamento específico do `ConcreteComponent`.

O Visitor é especialmente útil quando se trabalha com uma estrutura de 
objetos complexa, como uma árvore de objetos, e se deseja executar uma 
operação em todos os elementos dessa estrutura. Em vez de adicionar um
método na classe base para realizar a operação, pode-se adicionar um
Visitor que realiza a operação nos diferentes tipos de elementos.

Além disso, o padrão de Visitor é útil quando há um grande número de classes 
de elementos e cada uma delas tem um comportamento diferente a ser executado
por um algoritmo. Neste caso, é possível criar diferentes visitantes para 
executar esses comportamentos.


# Referências:
- [Visitor in Python](https://refactoring.guru/design-patterns/visitor/python/example)
