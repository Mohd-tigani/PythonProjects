import socket
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# checks whether sufficient arguments have been provided
# first argument from command prompt is IP address
IP_address = '127.0.0.1'
# second argument from command prompt is port number
Port = 12000
# binds the server to an entered IP address and specified port number.
server.bind((IP_address, Port))
# listens for 10 active connections
server.listen(10)
list_of_clients = []
def clientthread(conn, addr):
    # sends a message to the client whose user object is conn
    conn.send("Welcome to Network Programming chatroom!")
    # broadcast to other that a new client has joined
    message_to_send = "<" + addr[0] +", " + str(addr[1]) + "> joined"
    broadcast(message_to_send, conn)

while True:
    try:
        message = conn.recv(4096)
        if message:
            # prints the message and address of the user who just sent the message
            print ("<" + addr[0] + ", " + str(addr[1]) + ">: " + message)
            # call broadcast function to send message to all other clients
            message_to_send = "<" + addr[0] +", " + str(addr[1]) + ">: " + message
            broadcast(message_to_send, conn)
        else:
            ''' message have no content if the connection is broken, then 
            send message to others and remove the connection'''
            print("connection : <" + addr[0] + ", " + str(addr[1]) + "> disconnected")
            message_to_send = "<" + addr[0] +", " + str(addr[1]) + "> left"
            broadcast(message_to_send, conn)
            remove(conn)
            break
    except:
        print("error occurred and ignored with: <" + addr[0] +", " + str(addr[1]) + "> connection")
        continue

""" broadcast function is used to broadcast a message to all
clients (but not the sender) """
def broadcast(message, connection):
    for client in list_of_clients:
        if client != connection:#if not the sender
            try:
                client.send(message)
            except:
                client.close()
                # if the link is broken, remove the client
                remove(client)

''' remove function to remove the object from the list of clients '''
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

print("Welcome to Network Programming chatroom!\nServer is waiting for clients...")
while True:

    """ accepts a connection request and stores two parameters:  
    conn socket object and addr of the connected client"""
    conn, addr = server.accept()

    """ maintains a list to keep track of all available clients in the chatroom"""
    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print (addr[0], addr[1], " joined")
    # creates an individual thread for every client
    start_new_thread(clientthread,(conn,addr))
conn.close()
server.close()
