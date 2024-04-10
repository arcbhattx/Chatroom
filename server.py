import socket
import threading


clients = [] #Users

def handle_client(client_socket):  #Handles client socket.
    while True: #loops and receives messages in form of data until client exits. 
        data = client_socket.recv(1024) 
        if not data: #if theres no data or in other words the client has closed connection then break out the loop for that client.
            break
        msg = data.decode('utf-8') #decodes that data so we can get the string message.

        user = ""

        for x in msg:
            if x == ":":
                break
            user += x

        for users in clients:
            if users != user:
                clients.append(user)
            else:
                break

        print(msg)  #prints received message to the server
        #response = "Server received your message: " + msg  
        #client_socket.sendall(response.encode('utf-8'))
        client_socket.sendall(msg.encode('utf-8')) #sends that data back to the client saying that it is recevied
    client_socket.close() #outside the loop closed client socket.



def main():  #main function to create a server sockeet that handles multiple clients.
    HOST = "127.0.0.1"
    PORT = 12345

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_socket.bind((HOST,PORT))

    server_socket.listen(5)

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_addr = server_socket.accept() #accepts client socket and whatever address they are from.
        #print(f"Accepted connection from {client_addr}")
        client_handler = threading.Thread(target=handle_client,args=(client_socket,))
            # This specifies the function that the thread will execute. In this case, it's handle_client
            #This provides the arguments to the handle_client function. args expects a tuple, hence the comma after client_socket. client_socket is presumably a socket object representing a connection to a client. So, the handle_client function is expected to take one argument, which is a client socket.
        client_handler.start()
            #just starts the threading.


if __name__ == "__main__":
    main() #calls main function when ran