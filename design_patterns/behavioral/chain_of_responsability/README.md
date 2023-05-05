# Sobre o Design Pattern Chain of Responsibility
O padrão Chain of Responsibility é um padrão de design comportamental 
que permite que um conjunto de objetos trate uma solicitação de forma
sequencial. Cada objeto na cadeia tem a oportunidade de lidar com a 
solicitação ou passá-la para o próximo objeto na cadeia.


# Sobre a Implementação Realizada
Temos a classe abstrata `Handler`, que define uma interface para tratar 
uma solicitação e armazena uma referência ao próximo objeto na cadeia.
A classe `ConcreteHandlerA`, `ConcreteHandlerB` e `ConcreteHandlerC` 
implementam a interface `Handler` e fornecem uma implementação específica 
da solicitação.

No código principal, criamos uma cadeia de objetos `Handler`, onde 
`handler_a` é o objeto principal. Ao chamar o método 
`handle_request` no objeto `handler_a`, ele tentará lidar com a
solicitação. Se não puder, ele passa a solicitação para o próximo
objeto na cadeia.

Neste exemplo, a solicitação "A" é tratada pelo `ConcreteHandlerA`, 
enquanto as solicitações "B" e "C" são passadas para o próximo objeto
na cadeia, que é `ConcreteHandlerB` e `ConcreteHandlerC`, respectivamente.

O padrão Chain of Responsibility é útil quando você tem um conjunto de 
objetos que podem lidar com uma solicitação de forma diferente, mas não 
sabe qual objeto específico lidará com a solicitação. Com o padrão 
Chain of Responsibility, você pode criar uma cadeia de objetos que 
tentarão lidar com a solicitação em ordem, até que um objeto na 
cadeia possa lidar com a solicitação ou até que a solicitação
não possa ser tratada por nenhum objeto na cadeia.

# Referências:
- [Chain of Responsability in Python](https://refactoring.guru/design-patterns/chain-of-responsibility/python/example)
