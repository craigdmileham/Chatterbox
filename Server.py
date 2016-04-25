# Server STREAM socket
import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000

serv_sock.bind((socket.gethostbyname('cmileham'), port))

serv_sock.listen(2)

print("Server Started on port " + str(port))

print("Waiting for a connection")
conn, client_address = serv_sock.accept()
print("Connected to " + str(client_address))

while True:

    recvd_message = conn.recv(4096)
    recvd_message = recvd_message.decode(encoding = 'UTF-8')
    print(str(client_address) + " said: " + recvd_message)
