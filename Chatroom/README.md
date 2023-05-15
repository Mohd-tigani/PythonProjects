
# Client and Server Chatroom
### Description
Created and designed a Multithreaded Chatroom where Multiple client users can join the chatroom.
Designed in Python using the Socket Library.

This is a server-client chatroom program developed in Python. The server program allows multiple clients to connect and chat with each other, while the client program connects to the server to participate in the chatroom.

### Server code

The server code is responsible for creating a socket object, binding it to a specific IP address and port, and listening for incoming client connections. When a client connects, the server adds the client socket object to a list of connected clients. The server also creates a new thread for each client connection, which listens for incoming messages from that client. When a message is received from a client, the server broadcasts it to all other connected clients. If a client disconnects, the server removes their socket object from the list of connected clients.

Here's an overview of how the server code works:

The server creates a socket using the socket.socket() function. It uses the AF_INET address family and SOCK_STREAM socket type for TCP/IP communication.

The server sets the SO_REUSEADDR socket option using setsockopt() to allow the reuse of the local address after the server is terminated.

The server binds the socket to a specific IP address and port number using the bind() function. In this code, the IP address is set to '127.0.0.1' (localhost), and the port is set to 12000. You can modify these values as needed.

The server starts listening for incoming client connections using the listen() function. The parameter 10 specifies the maximum number of queued connections.

The server maintains a list list_of_clients to keep track of all connected clients.

The clientthread() function is responsible for handling each client connection. It runs in a separate thread for each connected client. Upon a new client connection, it sends a welcome message to the client and broadcasts a notification to all other connected clients that a new client has joined.

The main server loop continuously accepts new client connections using the accept() function. When a new connection is accepted, it adds the client's socket object to the list_of_clients, starts a new thread to handle the client, and prints a message to the console indicating that a client has joined.

Inside the client thread, it receives messages from the client using recv() and broadcasts the message to all other connected clients using the broadcast() function. If a client disconnects, it sends a leave notification to all other clients, removes the client's socket object from the list_of_clients, and breaks the loop to exit the thread.

The broadcast() function sends a message to all clients except the sender. It iterates through the list_of_clients and uses the send() function to send the message to each client. If any error occurs while sending the message, it removes the client's socket object from the list_of_clients.

The remove() function is responsible for removing a client's socket object from the list_of_clients.

The server continues running until it is terminated.

### Client code
The client communicates with a server over TCP/IP sockets to exchange messages with other clients in the chatroom.

The client creates a socket and connects to the server using the specified IP address and port number.

The client enters a loop to continuously listen for input from the user and messages from the server.

Inside the loop, the client creates a list of possible input streams, consisting of the standard input (user input) and the server socket.

The client uses the select system call to monitor the input streams for any activity.

If the server sends a message, the client receives it using the recv function and displays it on the console. If the message is empty, indicating that the server is down, the client displays an error message and exits.

If the user enters a message in the console, the client sends it to the server using the send function.

The client then displays the sent message with a "<You>" prefix on the console.
  
The loop continues, allowing the client to send and receive messages until it is manually terminated.
  
Once the client is terminated, the client socket is closed.
  
Note: Make sure to have the server running and reachable at the specified IP address and port number before running the client code.
### Requirments

Python 3.x
socket module
select module
sys module
Must be run on ubuntu to function.

