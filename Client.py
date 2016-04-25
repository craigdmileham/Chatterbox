import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (socket.gethostbyname('cmileham'), 9000)

print("Connecting...")

client_sock.connect(server_address)

print("Connected to server")

while True:
    message = input("Type message to send: ")
    message = bytes(message, encoding='UTF-8')
    client_sock.sendall(message)
    #recvd_message = client_sock.recv(4096)
