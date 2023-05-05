# O que são Design Patterns

## Introdução

Design Patterns são soluções para problemas comuns que encontramos no desenvolvimento de software. Não são frameworks ou bibliotecas, mas sim uma abstração de soluções que podem ser aplicadas em diversos problemas.

## Por que utilizar Design Patterns?

* São soluções testadas e aprovadas por outros desenvolvedores;
* Podem ser facilmente reutilizadas;
* Facilitam a manutenção do software;
* São resilientes a mudanças;
* Podem ser aplicadas em diversos contextos.
* Melhoram a comunicação entre os membros de uma equipe, pois fornecem um vocabulário comum.

## Categorias de Design Patterns

* **Criação**: lidam com a criação de objetos;
* **Estruturais**: lidam com a composição de classes e objetos;
* **Comportamentais**: lidam com a comunicação entre objetos.

## Design Patterns Criacionais

* [**Factory Method**](/design_patterns/creational/factory_method): cria uma instância de diversas classes derivadas de uma classe base;
* [**Abstract Factory**](/design_patterns/creational/abstract_factory): cria uma instância de várias famílias de classes;
* [**Builder**](/design_patterns/creational/builder): separa a construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes representações;
* [**Prototype**](/design_patterns/creational/prototype): cria um novo objeto a partir de um objeto existente;
* [**Singleton**](/design_patterns/creational/singleton): garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela.


## Design Patterns Estruturais

* [**Adapter**](/design_patterns/structural/adapter): converte a interface de uma classe em outra interface que o cliente espera encontrar;
* [**Bridge**](/design_patterns/structural/bridge): separa uma abstração da sua implementação, de forma que ambas possam variar independentemente;
* [**Composite**](/design_patterns/structural/composite): compõe objetos em estruturas de árvore para representar hierarquias parte-todo;
* [**Decorator**](/design_patterns/structural/decorator): adiciona responsabilidades a um objeto dinamicamente;
* [**Facade**](/design_patterns/structural/facade): fornece uma interface unificada para um conjunto de interfaces em um subsistema;
* [**Proxy**](/design_patterns/structural/proxy): fornece um objeto substituto ou um marcador de localização para outro objeto para controlar o acesso a ele.

## Design Patterns Comportamentais

* [**Chain of Responsibility**](/design_patterns/behavioral/chain_of_responsibility): evita o acoplamento do remetente de uma solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar a solicitação;
* [**Command**](/design_patterns/behavioral/command): encapsula uma solicitação em um objeto, permitindo que você parametrize clientes com diferentes solicitações, enfileire ou registre solicitações e implemente recursos de cancelamento de operações;
* [**Iterator**](/design_patterns/behavioral/iterator): fornece uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representação subjacente;
* [**Mediator**](/design_patterns/behavioral/mediator): permite que você reduza as dependências caóticas entre objetos. O padrão restringe as comunicações diretas entre os objetos e os força a colaborar apenas por meio de um objeto mediador;
* [**Memento**](/design_patterns/behavioral/memento): permite que você salve e restaure o estado anterior de um objeto sem revelar os detalhes de sua implementação;
* [**Observer**](/design_patterns/behavioral/observer): permite que objetos publiquem alterações de estado para outros objetos que os estejam observando;
* [**State**](/design_patterns/behavioral/state): permite que um objeto altere seu comportamento quando seu estado interno muda;
* [**Strategy**](/design_patterns/behavioral/strategy): permite que você defina uma família de algoritmos, coloque-os em classes separadas, faça seus objetos intercambiáveis;
* [**Template Method**](/design_patterns/behavioral/template_method): define o esqueleto de um algoritmo em uma operação, adiando alguns passos para subclasses. O padrão permite que as subclasses redefinam certos passos de um algoritmo sem alterar a estrutura do próprio algoritmo;
* [**Visitor**](/design_patterns/behavioral/visitor): permite que você separe algoritmos dos objetos nos quais eles operam.


## References

* [Design Patterns](https://refactoring.guru/design-patterns)
* [Faif Design Pattern GithubRepo](https://github.com/faif/python-patterns)
* [Dunossauro - Design Patterns](https://github.com/dunossauro/live-de-python/issues/52)
