Calculadora em Python

O script calculadora.py é uma aplicação simples em Python que permite ao usuário realizar operações matemáticas básicas de forma interativa no terminal.


Operações suportadas:
Adição (+)

Subtração (-)

Multiplicação (*)

Divisão (/)


Fluxo principal do programa:
O usuário é solicitado a inserir dois números.

Em seguida, escolhe a operação desejada.

O resultado é exibido na tela.

Após a operação, o usuário pode escolher se deseja realizar um novo cálculo ou encerrar o programa.


Tratamento de erros:
Divisão por zero: o programa verifica se o segundo número é zero em divisões e exibe uma mensagem de erro caso seja.

Entrada inválida: se o usuário digitar um valor que não seja um número, o programa captura o erro (ValueError) e solicita nova entrada.

Exemplo de uso:
$ python3 calculadora.py
Digite o primeiro número: 10
Digite o segundo número: 0
Escolha a operação (+, -, *, /): /
Erro: Divisão por zero não é permitida!
Deseja realizar outro cálculo? (s/n): s


Este projeto tem como objetivo reforçar conceitos de lógica de programação, estruturas de repetição, condicionais e tratamento de exceções em Python.
