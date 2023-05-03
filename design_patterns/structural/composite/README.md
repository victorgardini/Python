# Sobre o Design Pattern Composite
O padrão Composite é um padrão de design estrutural que permite tratar 
objetos individuais e coleções de objetos de maneira uniforme. Ele 
permite compor objetos em estruturas de árvore para representar 
hierarquias inteiras.

Em outras palavras, o padrão Composite permite que você trate objetos 
individuais e grupos de objetos como se fossem a mesma coisa.

# Sobre a Implementação Realizada
Temos a classe abstrata `Component`, que define a interface para 
objetos individuais e coleções de objetos. A classe `Leaf` é um 
objeto individual e implementa a interface `Component`. A classe
`Composite` é uma coleção de objetos e também implementa a interface 
`Component`.

A classe `Composite` possui uma lista de objetos `Component`, que 
pode incluir tanto objetos individuais quanto outras coleções. O 
método `add` adiciona um novo componente à lista, e o método `remove`
remove um componente existente da lista.

O método `operation` em `Composite` itera sobre todos os componentes 
da lista e chama o método operation de cada um deles. O resultado 
é concatenado em uma única string e retornada.

No código principal, criamos três objetos `Leaf` e um objeto `Composite`. 
Adicionamos os objetos `Leaf` ao objeto `Composite` usando o método `add`. 
Em seguida, criamos outro objeto `Composite` e adicionamos dois objetos 
`Leaf` a ele. Finalmente, adicionamos o segundo objeto `Composite` ao
primeiro objeto `Composite`.

Em seguida, chamamos o método `operation` do objeto `Composite` e 
imprimimos o resultado. O resultado mostra que o método `operation` 
foi chamado em todos os objetos `Leaf` e objetos `Composite` em 
uma única chamada.

O padrão Composite é útil quando você precisa tratar objetos individuais 
e coleções de objetos de maneira uniforme. Ele permite que você crie uma 
estrutura em árvore de objetos, onde cada nó pode ser tratado como um 
objeto individual ou uma coleção de objetos. Isso torna o código mais 
flexível e extensível, permitindo que você adicione e remova objetos 
sem afetar a estrutura geral da árvore.


# Referências:
- [Composite in Python](https://refactoring.guru/design-patterns/composite/python/example)