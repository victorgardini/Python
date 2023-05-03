# Sobre o Design Pattern Bridge
O padrão Bridge é um padrão estrutural que permite que uma abstração
e sua implementação possam variar independentemente. Ele separa uma
interface de uma classe abstrata de sua implementação, permitindo
que elas possam mudar independentemente uma da outra.

Em termos simples, o padrão Bridge é usado quando queremos evitar 
o vínculo permanente entre a abstração e sua implementação.


# Sobre a Implementação Realizada
Temos a classe abstrata `Implementor`, que representa a implementação 
da abstração. Em seguida, temos as classes `ConcreteImplementorA` e 
`ConcreteImplementorB`, que implementam essa abstração.

A classe `Abstraction` é a classe abstrata que define a interface da
abstração, e ela tem uma instância de `Implementor` como membro de 
dados. A classe `RefinedAbstraction` é uma classe concreta que estende 
a classe `Abstraction` para fornecer operações adicionais.

No código principal, criamos uma instância de `ConcreteImplementorA`
e uma instância de `Abstraction` passando a instância de 
`ConcreteImplementorA` como parâmetro para o construtor. Em seguida, 
chamamos o método `operation` da instância de `Abstraction` e 
imprimimos o resultado.

Em seguida, criamos uma instância de `ConcreteImplementorB` e uma 
instância de `RefinedAbstraction` passando a instância de 
`ConcreteImplementorB` como parâmetro para o construtor. Chamamos 
o método `operation` da instância de `RefinedAbstraction` e 
imprimimos o resultado.

O padrão Bridge permite que a abstração e sua implementação 
possam mudar independentemente uma da outra. Isso torna nosso 
código mais flexível e extensível, permitindo que adicionemos 
novas funcionalidades sem afetar a estrutura da classe abstrata.
No entanto, o padrão pode introduzir alguma sobrecarga e complexidade, 
pois precisamos criar uma classe separada para cada combinação de
abstração e implementação. Por isso, é importante usar o padrão com
cuidado e considerar outras abordagens de design se necessário.


# Referências:
- [Bridge in Python](https://refactoring.guru/design-patterns/bridge/python/example)