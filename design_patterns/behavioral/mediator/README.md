# Sobre o Design Pattern Mediator
O padrão Mediator é um padrão de design comportamental que permite 
que objetos se comuniquem indiretamente, através de um objeto mediador, 
em vez de se comunicarem diretamente uns com os outros.


# Sobre a Implementação Realizada
Temos a classe `Mediator`, que é a interface do mediador, que define um 
método `send_message()` para enviar mensagens entre os objetos colegas. 
A classe `Colleague` é a interface para os objetos colegas, que definem
métodos `send()` e `receive()` para enviar e receber mensagens, 
respectivamente. As classes `ConcreteColleague1` e `ConcreteColleague2`
implementam a interface `Colleague` para fornecer comportamentos 
específicos para cada objeto colega. Finalmente, a classe 
`ConcreteMediator` implementa a interface `Mediator` para fornecer a
lógica do mediador.

No código principal, criamos um objeto `ConcreteMediator` e dois objetos
colegas, `ConcreteColleague1` e `ConcreteColleague2`. Adicionamos os dois
objetos colegas ao objeto `ConcreteMediator` e, em seguida, cada objeto 
colega envia uma mensagem ao outro. Quando uma mensagem é enviada, ela
é enviada para todos os outros objetos colegas registrados com o objeto
`ConcreteMediator`, exceto o remetente original.

O padrão Mediator é útil quando você deseja fornecer uma maneira de objetos
se comunicarem indiretamente, sem se comunicarem diretamente uns com os outros.
O padrão Mediator ajuda a reduzir o acoplamento entre objetos e facilita
a manutenção


# Referências:
- [Mediator in Python](https://refactoring.guru/design-patterns/mediator/python/example)
