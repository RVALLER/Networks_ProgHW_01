#import socket module
from socket import *
import sys # In order to terminate the program

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
server_socket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
server_port = 12000
server_socket.bind(('127.0.0.1', server_port))

while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = server_socket.accept()
    try:
    # Receives the request message from the client
    message = "Enter path for file: "
    filename = message.split()[1]
    f = open(filename)

    # Store the entire content of the requested file in a temporary variable
    Output_data = #Fill in start ... #Fill in end

# Send one HTTP header line into socket
    #Fill in start
    ...
    #Fill in end

#Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode()) connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
    #Send response message for file not found
    #Fill in start
    ...
    #Fill in end

    #Close client socket
    #Fill in start
    ...
    #Fill in end
    server_socket.close()
    sys.exit()
