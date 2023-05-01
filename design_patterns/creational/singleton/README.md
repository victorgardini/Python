# Sobre o Design Pattern Factory Method
O padrão Singleton é um padrão de criação que permite ter
apenas uma instância de uma classe em toda a aplicação, 
garantindo que não haja duplicação de recursos e que o 
objeto seja acessível de forma global.

Em termos simples, o padrão Singleton é usado quando queremos
garantir que uma única instância de uma classe seja criada e 
que essa instância seja compartilhada em toda a aplicação.

# Sobre a Implementação Realizada
Neste exemplo, temos a classe `Singleton`, que implementa a lógica
de criar uma única instância da classe.

O método `__new__` é responsável por verificar se já existe uma 
instância da classe `Singleton`. Se ainda não houver uma
instância, ele cria uma nova instância usando o método 
`super().__new__(cls)` e atribui essa instância à variável 
`_instance`. Se já houver uma instância, ele simplesmente
retorna a mesma instância.

No código principal, criamos duas instâncias de `Singleton` 
e verificamos se elas são iguais usando o operador `is`. Como 
a classe `Singleton` garante que apenas uma instância é criada,
as duas instâncias criadas são na verdade a mesma instância,
e a comparação retorna True.

O padrão `Singleton` nos permite garantir que apenas uma instância 
de uma classe seja criada e que essa instância seja compartilhada 
em toda a aplicação. Isso pode ajudar a evitar a duplicação de 
recursos e a garantir que o objeto seja acessível de forma global.

No entanto, o padrão `Singleton` pode tornar o código mais difícil 
de testar e pode levar a problemas de concorrência se vários threads 
tentarem acessar a instância ao mesmo tempo. Além disso, o padrão 
`Singleton` pode levar a problemas de acoplamento e tornar o 
código menos flexível. Por isso, é importante usar o padrão com 
cuidado e considerar outras abordagens de design se necessário.

# Referências:
- [Prototype](https://refactoring.guru/design-patterns/prototype/python/example)