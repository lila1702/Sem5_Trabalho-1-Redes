'''
Lila Maria Salvador Frazão - 510809
'''

import socket

HOST = 'localhost'
PORT = 2017

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen()
print ('Aguardando conexão...')

client, ender = server_socket.accept()
print ('Conectado em ', ender)

while(True):
    data = client.recv(1024)
    if not data:
        print ("Fechando a conexão")
        client.close()
        break
    client.sendall(data)