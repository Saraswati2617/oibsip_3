
import socket
import threading
from server import send_msg_to_client

HOST='127.0.0.1'
PORT=1234



def listen_server(client):
    while 1:
        message=client.recv(2048).decode('utf-8')
        if message !='':
            user_name=message.split("~")[0]
            content=message.split('~')[1]
            print(f"[{user_name}] {content}")
        else:
            print("Message received from client is empty")




def send_server(client):
    while 1:
        message=input("Message: ")
        if message !='':
            client.sendall(message.encode())

        else:
            print("Empty message")
            exit(0)



def connect_server(client):
    user_name=input("Enter username: ")
    if user_name!='':
        client.sendall(user_name.encode())
    else:
        print("Username cannot be empty")
        exit(0)
    threading.Thread(target=listen_server, args=(client,)).start()
    

    send_server(client)


def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((HOST,PORT))
        print("running client")
    except:
        print(f"Cannot connect to server {HOST} {PORT}")


    connect_server(client)





if __name__ == '__main__' :
    main()