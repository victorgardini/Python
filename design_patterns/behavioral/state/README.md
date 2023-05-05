# Sobre o Design Pattern State
O design pattern State permite que um objeto altere o seu comportamento
quando o seu estado interno é alterado. Isso pode ser alcançado através
da implementação de diferentes classes que representam cada estado 
possível do objeto, e permitindo que ele altere dinamicamente de estado
conforme necessário.


# Sobre a Implementação Realizada
No código, temos uma classe `Context`, que define a interface de interesse
para os clientes e mantém uma referência a uma instância de uma subclasse 
`State`, que representa o estado atual do contexto. A classe `Context`
também possui dois métodos, `request1()` e `request2()`, que delegam 
parte do comportamento para o objeto `State` atual.

A classe abstrata `State` define a interface para os estados concretos. Ela
possui um método `handle1()` e um método `handle2()`, que devem ser 
implementados pelos estados concretos. Além disso, a classe `State` 
possui uma referência de volta para o objeto `Context`, que pode ser 
usada pelos estados para transicionar o contexto para outro estado.

As classes `ConcreteStateA` e `ConcreteStateB` implementam os comportamentos 
associados a um estado específico do `Context`. No método `handle1()` da 
classe `ConcreteStateA`, por exemplo, temos a lógica que representa a 
transição do `Context` para o estado `ConcreteStateB`.

Ao executar o código, criamos um objeto `Context` e o configuramos com o
estado `ConcreteStateA`. Em seguida, chamamos os métodos `request1()` e
`request2()` do objeto `Context`, que delegam o comportamento para o
estado atual. Como o estado atual é `ConcreteStateA`, o método `handle1()`
é chamado e o estado do `Context` é alterado para `ConcreteStateB`. Em 
seguida, o método `request2()` é chamado, o que leva a uma chamada ao 
método `handle2()` do estado `ConcreteStateB`.


# Referências:
- [State in Python](https://refactoring.guru/design-patterns/state/python/example)
