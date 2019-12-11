 #!/usr/bin/python3
import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 123

clientsocket.connect(('192.168.43.199',port))
clientsocket.send("hi server \n".encode('ascii'))
message=''
while True and message !='exit':
    print("Waiting from server....\n")
    message=clientsocket.recv(4096).decode('ascii')
    print("server : "+ message)
    if message == 'exit':
        exit()
    message = input("Client : ")
    clientsocket.send(message.encode('ascii'))
    print()
clientsocket.close()
