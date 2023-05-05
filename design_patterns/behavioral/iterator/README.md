# Sobre o Design Pattern Iterator
O padrão Iterator é um padrão de design comportamental que fornece 
uma maneira de acessar sequencialmente elementos de um objeto agregado 
sem expor sua representação subjacente.


# Sobre a Implementação Realizada
Temos a classe `Iterator`, que é um iterador que percorre uma lista. 
A classe `MyList` é um objeto agregado que armazena uma lista de elementos 
e fornece um método `create_iterator()` que retorna um iterador para 
percorrer os elementos da lista.

O iterador mantém o estado de sua posição atual na lista e fornece um 
método `__next__()` para retornar o próximo elemento da lista. Quando a 
lista é percorrida até o final, a exceção `StopIteration` é levantada para 
sinalizar que a iteração está completa. O iterador também implementa o 
método `__iter__()`, que retorna ele próprio, permitindo que ele seja usado 
em uma declaração for para iterar sobre a lista.

No código principal, criamos um objeto `MyList` contendo uma lista de
números e, em seguida, criamos um iterador usando o método `create_iterator()`.
Finalmente, usamos uma declaração `for` para iterar sobre a lista e imprimir
cada elemento.

O padrão Iterator é útil quando você deseja fornecer uma maneira de acessar
sequencialmente os elementos de um objeto agregado sem expor sua 
representação subjacente. O padrão Iterator permite que você forneça
uma maneira padronizada de iterar sobre os elementos de um objeto, 
independentemente de como eles são armazenados ou organizados.


# Referências:
- [Iterator in Python](https://refactoring.guru/design-patterns/iterator/python/example)
