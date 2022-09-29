import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
#     print ("missing arguments enter: <IP address> <port number>")
#     exit()
IP_address = '127.0.0.1'
Port = 12000
server.connect((IP_address, Port))

while True:
    # create a list to maintain possible input streams
    sockets_list = [sys.stdin, server]

    """ Two possible inputs scenarios. Either the
    user enters text to send to other clients, or the 
    server is sending a message to the client. """

    """ select system call returns from sockets_list, the stream 
    that is reader for input. So for example, if the server sent a message, then the if condition will hold true below. 
    If the user wants to send a message, the else
    condition will evaluate as true"""
    print("wait on select call...")
    read_sockets, write_sockets, error_sockets = select.select(sockets_list,[],[])#monitor server and standard input and return
    #wait if server comes first or user comes first
    print("select call returned")
    print("read_sockets: ", read_sockets)
    #print("write_sockets: ", write_sockets)
    #print("error_sockets: ", error_sockets)


    for socks in read_sockets:
        if socks == server:#if sever sends message first
            message = socks.recv(4096)
            if(len(message) != 0):
                print(message)
            # server sent empty message, print error and leave
            else:
                print("Server is down, join later once it is up!")
                exit()
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()

server.close()
