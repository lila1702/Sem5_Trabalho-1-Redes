'''
Lila Maria Salvador Frazão - 510809
'''

import socket
from random import randint

HOST = '127.0.0.1'
PORT = 2017

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

num_client = randint(0, 999999999999999999999999999999)

#num_client = str(num_client)

print(f"O número gerado foi: {num_client}")

client_socket.sendall(num_client)
data = client_socket.recv(1024)

print('Mensagem ecoada:', data.decode())