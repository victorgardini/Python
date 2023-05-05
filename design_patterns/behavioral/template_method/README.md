# Sobre o Design Pattern Template Method
O Template Method é um padrão de projeto comportamental que define o 
esqueleto de um algoritmo em uma classe base, delegando a implementação
de alguns passos para as subclasses. O objetivo é permitir que as 
subclasses alterem certas etapas do algoritmo sem alterar sua estrutura
geral.


# Sobre a Implementação Realizada
Na classe `AbstractClass`, há um método `template_method()` que define a 
estrutura geral do algoritmo, que é composto por chamadas a operações 
primitivas abstratas (`required_operations1()` e `required_operations2()`) e
operações básicas (`base_operation1()`, `base_operation2()` e 
`base_operation3()`). Além disso, existem dois "hooks" (`hook1()` e `hook2()`)
que fornecem pontos de extensão para subclasses em locais cruciais do 
algoritmo, mas que já têm implementações padrão vazias.

As subclasses `ConcreteClass1` e `ConcreteClass2` implementam as 
operações primitivas abstratas de acordo com suas necessidades específicas.
Além disso, `ConcreteClass2` substitui o `hook1()` para fornecer uma 
implementação específica.

A função `client_code()` é responsável por executar o método 
`template_method()` da classe `AbstractClass`. Este método é executado por
uma instância de uma das subclasses concretas, sem que o cliente precise
saber qual a classe concreta está sendo utilizada.

Outro exemplo de uso desse design pattern seria um framework de construção de casas, 
onde a classe `AbstractClass` poderia ser `HouseBuilder`, que define
a estrutura geral da construção de uma casa (por exemplo, preparar o terreno,
construir a fundação, construir as paredes, etc.) e as subclasses concretas 
poderiam ser `BrickHouseBuilder` e `WoodenHouseBuilder`, que implementam
as operações primitivas abstratas de acordo com o tipo de casa a ser construída.

Esse padrão é particularmente útil quando várias classes diferentes compartilham
a mesma estrutura básica de algoritmo, mas diferem nos detalhes de como esses
algoritmos são executados. O Template Method permite encapsular a estrutura
comum do algoritmo em uma classe base e permitir que as subclasses definam 
as diferenças específicas em seus próprios métodos implementados. Isso ajuda
a reduzir a duplicação de código e a aumentar a coesão entre as classes 
relacionadas.


# Referências:
- [Template Method in Python](https://refactoring.guru/design-patterns/template-method/python/example)
