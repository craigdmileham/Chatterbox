#Client STREAM socket
import socket
#Initialize Client socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000
server_address = (socket.gethostbyname('cmileham'), port)

print("Connecting...")
#connect to server
client_sock.connect(server_address)

print("Connected to server")

while True:
    #Get message to send to Server
    message = input("Type message to send: ")
    message = bytes(message, encoding='UTF-8')
    #Send message to Server
    client_sock.sendall(message)
    #Receive response from Server
    recvd_message = client_sock.recv(4096)
    if not recvd_message:
        #If no message received, close connection
        print("Disconnected from Server")
        client_sock.close()
        break
    else:
        #If message received, print message
        recvd_message = recvd_message.decode(encoding = 'UTF-8')
        print("Server said: " + recvd_message)
