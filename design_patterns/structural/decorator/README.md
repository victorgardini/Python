# Sobre o Design Pattern Decorator
O padrão Decorator é um padrão de design estrutural que permite adicionar
comportamentos a um objeto existente de forma dinâmica, sem alterar sua 
estrutura subjacente. Isso é feito criando uma classe decoradora que 
envolve a classe base original e adiciona funcionalidades adicionais.

# Sobre a Implementação Realizada
Temos a classe abstrata `Component`, que define a interface para a classe 
base original e as classes decoradoras. A classe `ConcreteComponent` é a
classe base original e implementa a interface `Component`.

A classe abstrata `Decorator` define a interface para as classes decoradoras
e tem um objeto do tipo `Component` como atributo. As classes 
`ConcreteDecoratorA` e `ConcreteDecoratorB` são as classes decoradoras
e implementam a interface `Decorator`.

Cada classe decoradora tem uma instância do tipo `Component` como 
atributo e adiciona um comportamento adicional ao resultado do 
método operation da classe base original.

No código principal, criamos uma instância da classe base original 
`ConcreteComponent`. Em seguida, criamos uma instância da classe
decoradora `ConcreteDecoratorA`, passando a instância de `ConcreteComponent` 
como argumento. Em seguida, criamos uma instância da classe decoradora 
`ConcreteDecoratorB`, passando a instância de `ConcreteDecoratorA` como argumento.

Finalmente, chamamos o método `operation` da instância de `ConcreteDecoratorB`
e imprimimos o resultado.

O resultado final é a concatenação dos resultados dos métodos `operation` 
das classes `ConcreteDecoratorA`, `ConcreteComponent` e `ConcreteDecoratorB`.

O padrão Decorator é útil quando você precisa adicionar comportamentos 
adicionais a uma classe sem modificar sua estrutura subjacente. Isso
torna o código mais flexível e extensível, permitindo que você adicione 
e remova comportamentos dinamicamente em tempo de execução.


# Referências:
- [Decorator in Python](https://refactoring.guru/design-patterns/decorator/python/example)