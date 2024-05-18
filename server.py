'''Create a basic text-based chat application in Python where two users can exchange messages in real-time using
 the command line. Implement a simple client-server model for message exchange.'''


import socket
import threading

HOST='127.0.0.1'
PORT=1234
LISTENER_LIMIT=5
active_clients=[]


def listen_msg(client,user_name):
    while 1:
        message=client.recv(2048).decode("utf-8")
        if message!='':
            final_msg=user_name + '~' + message
            send_msg_all(final_msg)
        
        else:
            print(f"The message send from client {user_name} is empty")


def send_msg_to_client(client,message):
    client.sendall(message.encode())





def send_msg_all(message):
    for user in active_clients:
        send_msg_to_client(user[1],message)

     



def handle_client(client):
    while 1:
        user_name=client.recv(2048).decode('utf-8')
        if user_name != '':
            active_clients.append((user_name,client))
            # prompt_message="SERVER"+f"{user_name} added to the chat"
            # send_msg_all(prompt_message)
            break
        else:
            print("Client username is empty")



    threading.Thread(target=listen_msg,args=(client,user_name)).start()

    

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"running server {HOST} {PORT}")
    try:
        server.bind((HOST,PORT))
    except:
        print(f"Cannot bind host {HOST} and port {PORT}")
        
    server.listen(LISTENER_LIMIT)

    while 1:
        client,address=server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=handle_client,args=(client,)).start()


if __name__=='__main__':
    main()