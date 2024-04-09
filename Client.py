import socket
#import threading



user = input("Username:")

def main():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT  = 12345

    client_socket.connect((HOST,PORT)) #connects to the server.

    while True:
        msg = input("->")
        user_msg = user + ": "+ msg
        client_socket.sendall(user_msg.encode('utf-8'))  #sends whatever inputed message to the server.

        #Probaby used in future for 1 on 1 communication.
        """
        data = client_socket.recv(1024) #data received from the server.
        response = data.decode('utf-8') #decodes the server data
        print(f"Server response: {response}") 

        """
if __name__ == "__main__":
    main()

    