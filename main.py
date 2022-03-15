# import socket module
from socket import *
import sys  # In order to terminate the program

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
server_socket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
server_port = 4096
server_socket.bind(('', server_port))
server_socket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = server_socket.accept()
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(4096).decode()
        filename = message.split()[1]
        f = open(filename, 'r', encoding='utf-8')

        # Store the entire content of the requested file in a temporary variable
        Output_data = f.read()

        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n")

        # Send the content of the requested file to the client
        for i in range(0, len(Output_data)):
            connectionSocket.send(Output_data[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        print("IOERROR")
        connectionSocket.send("HTTP/1.1 404 FILE NOT FOUND \r\n\r\n")

    # Close client socket
    connectionSocket.close()

    server_socket.close()
    sys.exit()
