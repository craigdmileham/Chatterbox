# Server STREAM socket
import socket
#Initialize server socket
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000
#Bind socket to Host and Port
serv_sock.bind((socket.gethostbyname('cmileham'), port))
#Set socket to listen for connections
serv_sock.listen(1)

print("Server Started on port " + str(port))

while True:
    print("Waiting for a connection")
    #Accept connection to Client
    conn, client_address = serv_sock.accept()
    print("Connected to " + str(client_address))

    while True:
        #Receive message from Client
        recvd_message = conn.recv(4096)
        #If no message is received, close connection
        if not recvd_message:
            print("Client has Disconnected")
            conn.close()
            break
        else:
        # Print message
            recvd_message = recvd_message.decode(encoding = 'UTF-8')
            print(str(client_address) + " said: " + recvd_message)
        #Get response from Server to Client
            rply_message = input("Type message to send: ")
            rply_message = bytes(rply_message, encoding = 'UTF-8')
            conn.sendall(rply_message)
