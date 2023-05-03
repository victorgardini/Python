# Sobre o Design Pattern Facade
O padrão Facade é um padrão de design estrutural que fornece uma 
interface simplificada para um conjunto de interfaces mais complexo.
Ele encapsula a complexidade subjacente e expõe uma interface mais 
fácil de usar para o cliente.

# Sobre a Implementação Realizada
Temos três classes de subsistema, `SubsystemA`, `SubsystemB` e `SubsystemC`.
Cada classe de subsistema tem seus próprios métodos `method_1` e `method_2`.

Em seguida, temos a classe `Facade`, que fornece uma interface simplificada
para as classes de subsistema. A classe `Facade` encapsula a complexidade
subjacente e expõe uma interface mais fácil de usar para o cliente.

O método `operation` da classe `Facade` chama os métodos relevantes dos 
objetos das classes de subsistema. O cliente pode simplesmente criar uma
instância da classe Facade e chamar o método operation para realizar as 
operações desejadas.

No código principal, criamos uma instância da classe `Facade` e chamamos
o método `operation`. O resultado é a chamada dos métodos relevantes das
classes de subsistema encapsulados pela classe `Facade`.

O padrão Facade é útil quando você tem um conjunto complexo de classes
e interfaces e deseja fornecer uma interface simplificada para o cliente.
Isso torna o código mais fácil de usar e mais fácil de manter.
Além disso, o padrão Facade ajuda a reduzir o acoplamento entre o cliente
e as classes de subsistema, o que torna o código mais flexível e mais fácil
de evoluir.


# Referências:
- [Facade in Python](https://refactoring.guru/design-patterns/facade/python/example)