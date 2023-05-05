# Sobre o Design Pattern Command
O padrão Command é um padrão de design comportamental que encapsula 
uma solicitação como um objeto, permitindo que você faça solicitações
de forma parametrizada e desfazê-las se necessário.


# Sobre a Implementação Realizada
Neste exemplo, temos a classe abstrata `Command`, que define uma
interface para executar um comando e desfazer um comando. A 
classe `AddCommand` implementa a interface `Command` e fornece uma 
implementação específica de adicionar um valor ao objeto `Receiver`.

A classe `Receiver` é o objeto que será afetado pelo comando e
fornece métodos para adicionar e remover valores.

A classe `Invoker` mantém uma lista de comandos e permite que você 
execute vários comandos ao mesmo tempo e desfaça o último comando.

No código principal, são criados dois objetos `AddCommand`, que então são
adicionados à lista de comandos do `Invoker` e, em seguida, são executados
todos os comandos na lista. O `Receiver` foi afetado por esses comandos
e agora contém os valores adicionados.

Finalmente, é desfeito o último comando adicionado, que remove o valor 
adicionado mais recentemente do Receiver.

O padrão Command é útil quando você precisa de um nível de abstração 
entre um objeto que solicita uma ação e o objeto que executa a ação.
Com o padrão Command, você pode encapsular solicitações como objetos,
permitindo que você as execute de forma parametrizada e desfazê-las 
se necessário.


# Referências:
- [Command in Python](https://refactoring.guru/design-patterns/command/python/example)
