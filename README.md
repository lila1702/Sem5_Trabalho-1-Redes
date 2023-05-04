# Trabalho Prático 1 - Redes de Computadores

O primeiro trabalho proposto pela professora Valéria para a disciplina de Redes de Computadores da UFC Russas.
O intuito do trabalho é praticar os conceitos vistos em sala de aula até então, sobre programação em sockets.

O trabalho consiste em duas aplicações, o do Cliente e o do Servidor.

## Cliente

O cliente funciona da seguinte forma:

- Vincula um endereço e porta padrões do formato TCP para conexão com o servidor;
- Irá gerar um número inteiro aleatório de até 30 casas (Para fins de variação nos resultados, eu fiz com que o programa tivesse 15% de chance de garantir um número gerado com até 10 casas);
- Envia este número para o servidor;
- Recebe o resultado do servidor e o imprime na tela;
- Fecha esta conexão;
- Repete todo este processo de 10 em 10 segundos.

## Servidor

O servidor funciona da seguinte forma:

- Vincula o endereço local e a porta do formato TCP definida ao servidor para poder ser buscada pelo clientes como ponto de conexão;
- Ao aceitar a solicitação de um cliente, o servidor entre em seu loop de receber e enviar respostas ao cliente;
- Do cliente, ele recebe um número, dependendo da quantidade de casas que o número possui as respostas variam entre:
- Resposta 1: Caso o número tenha até 10 casas, o servidor irá verificar se ele é par ou ímpar, e retornar o resultado dessa verificação para o cliente;
- Resposta 2: Caso o número tenha mais que 10 casas, o servidor irá gerar uma string de letras aleatórias, maiúsculas e minúsculas, com o mesmo tamanho aquele ao número de casas do número recebido do cliente;
- Continuará a fazer isso para toda nova conexão que for estabelecida.

### Feito Por:
Lila Maria
