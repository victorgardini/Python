# Sobre o Design Pattern Adapter
O padrão Adapter é um padrão estrutural que permite que objetos com 
interfaces incompatíveis trabalhem juntos. Ele converte a interface
de uma classe em outra interface que os clientes esperam encontrar. 
Isso permite que as classes trabalhem juntas, mesmo que não tenham 
uma interface compatível.

Em termos simples, o padrão Adapter é usado quando precisamos 
adaptar uma interface existente para que ela seja compatível 
com outra interface que precisamos usar.


# Sobre a Implementação Realizada
Neste exemplo, temos a classe `Adaptee`, que representa a interface 
incompatível que precisamos adaptar, e a classe `Target`, que 
representa a interface que precisamos usar.

Em seguida, temos a classe `Adapter`, que implementa a interface 
`Target` e utiliza a classe `Adaptee` para converter sua interface 
em uma interface compatível. O método request do `Adapter` chama
o método `specific_request` da classe `Adaptee` e retorna o 
resultado formatado como uma string.

No código principal, criamos uma instância de `Adaptee` e uma
instância de `Adapter`, passando a instância de `Adaptee` como 
parâmetro para o construtor. Em seguida, chamamos o método `request`
da instância de `Adapter` e imprimimos o resultado.

O padrão `Adapter` nos permite adaptar uma interface existente para 
que ela seja compatível com outra interface que precisamos usar. 
Isso nos permite reutilizar código existente em novas situações e 
torna nosso código mais flexível e extensível. No entanto, o 
padrão pode introduzir alguma sobrecarga e complexidade, pois 
precisamos criar uma classe adaptadora para cada classe que 
precisamos adaptar. Por isso, é importante usar o padrão com 
cuidado e considerar outras abordagens de design se necessário.


# Referências:
- [Adapter in Python](https://refactoring.guru/design-patterns/adapter/python/example)