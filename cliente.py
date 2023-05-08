'''
Lila Maria Salvador Frazão - 510809
'''
import socket
from time import sleep
from random import randrange

HOST = '127.0.0.1'
PORT = 2017

# Loop infinito
while(True):
    # Conexão com o servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    print(f"Conexão realizada com {HOST} e {PORT}")
    
    # Para fins de variação no resultado, eu fiz com que houvesse 15% de chance do número gerado
    # forçadamente ter no máximo 10 casas
    chance = randrange(0, 100)
    tam_num = randrange(1, 30+1)
    if(chance > 85):
        num_client = str(randrange(0, 10**10))
    else:
        num_client = str(randrange(0, 10**tam_num))
    
    print(f"O número gerado {num_client} de tamanho {len(num_client)} foi enviado...")

    # Envia para o servidor
    client_socket.sendall(str.encode(num_client))
    # Recebe a resposta do servidor
    data = client_socket.recv(1024)

    print(f"O Servidor decretou que o retorno adequado é: {data.decode()}\nFIM\n")
    # Fecha a conexão
    client_socket.close()
    # Pausa o programa por 10 segundos, e depois tudo se repete
    sleep(10)