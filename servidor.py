'''
Lila Maria Salvador Frazão - 510809
'''
import socket
import string
from random import choice

# Diz se o número de seu parâmetro é par ou ímpar
def numero_string_par_impar(num):
    if(int(num) % 2 == 0):
        return "PAR"
    else:
        return "ÍMPAR"

# Gera uma string de letras aleatórias com o tamanho de acordo com o número de casas do número
def gerar_string_len_num(num):
    tam = len(num)
    nova_string = "".join(choice(string.ascii_letters) for x in range(tam))
        
    return nova_string

HOST = 'localhost'
PORT = 2017

# Loop infinito
while(True):
    # Disponibiliza o servidor como local para conectar-se
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    # Procura por conexões
    server_socket.listen()
    print ('Aguardando conexão...')

    # Aceita a conexão do cliente
    client, ender = server_socket.accept()
    print (f"Conectado em {ender}")
    
    # Recebe dados do cliente
    data = client.recv(1024)
    # Decodifica
    dado_de_data = data.decode()
    # Se o número recebido do cliente tiver até 10 casas, vai para a função par ou ímpar
    if(len(dado_de_data) <= 10):
        dado_par_impar = numero_string_par_impar(dado_de_data)
        print(f"\nPara o número de até 10 dígitos {dado_de_data}, o retorno é: {dado_par_impar}")
        client.sendall(dado_par_impar.encode())
    # Caso contrário, vai para a função de gerar uma string aleatória
    else:
        nova_string = gerar_string_len_num(dado_de_data)
        print(f"\nPara o número de mais que 10 dígitos {dado_de_data}, o retorno é: {nova_string}")
        client.sendall(nova_string.encode())
    # Em ambos os casos, enviam de volta para o cliente os seus resultados