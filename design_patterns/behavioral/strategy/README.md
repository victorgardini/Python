# Sobre o Design Pattern Strategy
O padrão Strategy permite que um objeto altere seu comportamento em 
tempo de execução, encapsulando uma família de algoritmos e 
tornando-os intercambiáveis. Isso permite que o cliente escolha o 
algoritmo que melhor se adapta às suas necessidades sem afetar o 
código do objeto.


# Sobre a Implementação Realizada
No código, a classe `Context` define a interface de interesse para os 
clientes e mantém uma referência a um objeto de uma classe que implementa
essa interface, que pode ser mudado em tempo de execução. A classe 
`Strategy` é uma classe abstrata que define a interface comum para todos os
algoritmos suportados, e as classes concretas `ConcreteStrategyA` e
`ConcreteStrategyB` implementam essa interface de maneiras diferentes.

O método `do_some_business_logic()` da classe `Context` é o método que 
usa o algoritmo atual. Ele delega o trabalho para o objeto 
`Strategy` em vez de implementar várias versões do algoritmo em
seu próprio código.

O código do cliente escolhe qual estratégia será utilizada e a passa 
para a instância do `Context`. Depois disso, o cliente pode chamar
o método `do_some_business_logic()` do `Context` sem se preocupar
com qual algoritmo está sendo usado internamente.

O exemplo implementa dois algoritmos de ordenação de lista:
`ConcreteStrategyA` ordena a lista em ordem crescente e `ConcreteStrategyB`
ordena a lista em ordem decrescente. O cliente escolhe qual estratégia
utilizar para ordenar a lista e passa essa estratégia para a instância do
`Context` por meio de seu construtor ou de um método `setter`. Em seguida,
o cliente chama o método `do_some_business_logic()` do `Context`, que 
utiliza o algoritmo selecionado para ordenar a lista e imprime o resultado.


# Referências:
- [Strategy in Python](https://refactoring.guru/design-patterns/strategy/python/example)
