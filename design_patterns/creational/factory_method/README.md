# Sobre o Design Pattern Factory Method
O padrão de design Factory Method é um padrão de criação que define uma interface para criar um objeto,
mas permite que as subclasses decidam qual classe criar. Isso permite que uma classe deferisse a
criação de objetos para suas subclasses.

Em termos simples, o Factory Method é um método que cria objetos sem expor a lógica de criação para o
cliente e permite que as subclasses decidam quais objetos criar.


# Sobre a Implementação Realizada
Temos uma classe abstrata `Animal` que define um método abstrato `make_sound`. 
As classes `Cat` e `Dog` herdam de `Animal` e implementam o método 
`make_sound` de acordo com o som que fazem.

Em seguida, temos a classe abstrata `AnimalFactory` que define o método 
abstrato `create_animal`. As classes `CatFactory` e `DogFactory` herdam
de `AnimalFactory` e implementam o método `create_animal` para criar
instâncias de `Cat` e `Dog`, respectivamente.

Por fim, temos uma função `get_animal_sound` que recebe uma instância
de `AnimalFactory` como argumento, cria uma instância de `Animal`
usando o método `create_animal` da fábrica e chama o método
`make_sound` para obter o som do animal.


# Referências:
- [Factory Method in Python](https://refactoring.guru/design-patterns/factory-method/python/example)