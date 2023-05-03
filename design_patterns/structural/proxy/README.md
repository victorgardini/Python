# Sobre o Design Pattern Proxy
O padrão Proxy é um padrão de design estrutural que fornece um objeto
substituto ou intermediário que controla o acesso a outro objeto, 
permitindo adicionar funcionalidade extra ou realizar tarefas 
adicionais antes ou depois da chamada ao objeto real.

# Sobre a Implementação Realizada
Temos a classe `Subject`, que é uma interface que define a operação que o
cliente deseja realizar. A classe `RealSubject` implementa a interface
`Subject` e fornece a implementação real da operação. A classe `Proxy` 
também implementa a interface `Subject` e fornece uma implementação 
substituta da operação, mas delega a chamada ao objeto `RealSubject` real.

No código principal, criamos uma instância de `RealSubject` e passamos-a 
para o construtor de `Proxy`. Em seguida, chamamos o método `request` 
no objeto `Proxy`. O objeto `Proxy` primeiro verifica se o cliente tem acesso
e, se sim, chama o método `request` no objeto `RealSubject` real. Antes
e depois da chamada, o objeto `Proxy` também executa algumas tarefas adicionais,
como verificar acesso e registrar acesso.

O resultado é que o objeto `Proxy` atua como um intermediário 
entre o cliente e o objeto real, adicionando funcionalidades extras 
e controlando o acesso ao objeto real.

O padrão Proxy é útil quando você deseja controlar o acesso a um objeto
ou adicionar funcionalidades extras, mas não deseja modificar
o objeto real ou criar uma nova subclasse. Com o padrão Proxy, você pode 
adicionar essas funcionalidades extras sem modificar o objeto real, tornando 
o código mais flexível e fácil de manter.

# Referências:
- [Proxy in Python](https://refactoring.guru/design-patterns/proxy/python/example)