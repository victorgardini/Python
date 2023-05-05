# Sobre o Design Pattern Observer
O design pattern Observer é usado para definir uma relação de 
dependência entre objetos de modo que, quando um objeto muda de estado, 
todos os seus dependentes são notificados e atualizados automaticamente.

O padrão Observer é composto por três elementos principais:
- Subject: objeto observado;
- Observer: objeto que está interessado em ser notificado de mudanças no Subject;
- E a interface Observer: definindo os métodos que o Subject pode chamar 
para notificar os Observers.


# Sobre a Implementação Realizada
O código define a classe abstrata `Subject` e a interface abstrata `Observer`.
A classe `ConcreteSubject` implementa a lógica de negócios e mantém uma lista 
de objetos `Observer` que se inscreveram para serem notificados sobre mudanças
de estado. A classe `ConcreteObserverA` e a classe `ConcreteObserverB` 
implementam a interface `Observer` e são notificadas pelo `ConcreteSubject`
quando o seu estado muda.

Quando o `ConcreteSubject` muda o seu estado, ele notifica todos os `Observers` 
registrados através do método `notify()`, que chama o método `update()` em cada
`Observer`.

O `ConcreteSubject` realiza uma ação de negócio importante e altera o seu estado.
Em seguida, notifica todos os `Observers` registrados. Os `ConcreteObserverA`
e `ConcreteObserverB` reagem de maneiras diferentes, dependendo do valor do 
estado do `ConcreteSubject`.

Este padrão é útil em situações onde existe um objeto que possui um estado
mutável e vários outros objetos que precisam ser notificados sobre mudanças 
neste estado. O padrão Observer ajuda a manter o baixo acoplamento 
entre os objetos, garantindo que o objeto que muda seu estado não 
precisa saber nada sobre os objetos que são notificados sobre essa mudança.


# Referências:
- [Observer in Python](https://refactoring.guru/design-patterns/observer/python/example)
