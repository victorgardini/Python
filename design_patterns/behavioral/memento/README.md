# Sobre o Design Pattern Memento
O design pattern Memento é um padrão comportamental que permite que você
salve e restaure o estado anterior de um objeto sem revelar os detalhes 
de sua implementação interna. Ele permite que você faça isso sem violar
o encapsulamento, mantendo a coesão e isolando o objeto em questão.

O padrão é composto por três partes principais:
- Originator: que é o objeto que deseja salvar e restaurar seu estado anterior; 
- Memento: que é uma classe que contém o estado salvo do Originator; 
- Caretaker: que é responsável por armazenar e restaurar os estados dos 
Originators usando o Memento.


# Sobre a Implementação Realizada
Neste exemplo, a classe `Originator` é o objeto que desejamos salvar 
e restaurar seu estado anterior. A classe `Memento` é uma classe que 
representa o estado salvo do `Originator`. A classe `Caretaker` é 
responsável por armazenar e restaurar os estados dos `Originators` usando o 
`Memento`.

Para salvar o estado do `Originator`, a função `save_state_to_memento()` 
retorna um objeto `Memento` contendo o estado salvo. Para restaurar o
estado do `Originator`, a função `restore_state_from_memento()` recebe
um objeto `Memento` e restaura o estado salvo do `Originator`.

A classe `Caretaker` tem as funções backup e undo, que permitem salvar o
estado atual do `Originator` e restaurar o estado anterior, respectivamente.

O design pattern Memento é útil em situações em que é necessário armazenar
o estado interno de um objeto em diferentes momentos e recuperar um
desses estados anteriores posteriormente, sem quebrar o encapsulamento do objeto.


# Referências:
- [Mediator in Python](https://refactoring.guru/design-patterns/mediator/python/example)
