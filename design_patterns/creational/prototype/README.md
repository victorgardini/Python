# Sobre o Design Pattern Factory Method
O padrão de design Prototype é um padrão de criação que permite criar 
novos objetos a partir de objetos existentes, clonando-os e
modificando-os conforme necessário. Isso pode ajudar a evitar 
a sobrecarga de criação de novos objetos e a complexidade da 
lógica de criação.

Em termos simples, o padrão Prototype é usado quando queremos 
criar um objeto a partir de um objeto existente, evitando a 
criação de um novo objeto do zero.

# Sobre a Implementação Realizada
Temos a classe `Prototype`, que é responsável por gerenciar os 
objetos registrados e clonar objetos existentes. A classe `Car` 
define o objeto a ser clonado.

No código principal, criamos uma instância de `Car` e definimos 
sua cor. Em seguida, criamos uma instância de `Prototype` 
e registramos o objeto `Car` clonável com o nome car. Em seguida, 
clonamos o objeto `Car` usando o método `clone` de `Prototype`
e passando o nome registrado para obter uma nova instância. 
Também podemos passar argumentos adicionais para atualizar os 
valores de atributos existentes.

Por fim, temos que o padrão `Prototype` pode levar a um grande 
número de objetos clonados, o que pode afetar o desempenho da
aplicação. Além disso, objetos clonados podem herdar referências 
a objetos compartilhados, o que pode levar a problemas se esses
objetos compartilhados forem modificados. Por isso, é importante
garantir que objetos compartilhados sejam imutáveis ou clonados 
profundamente.


# Referências:
- [Prototype](https://refactoring.guru/design-patterns/prototype/python/example)