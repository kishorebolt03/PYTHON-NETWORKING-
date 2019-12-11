 #!/usr/bin/python3
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '192.168.43.199'
port = 123

server.bind((host,port))

server.listen() #<(number of maximum connections)>
message = ''
clientsocket , address =  server.accept()
print("Connected by " + str(address))
message  = "\nHELLO\r\n"
while  True and message !='exit':
    print("client from server....\n")

    message=clientsocket.recv(4096).decode('ascii')
    print("client : " + message)
    message = input("Server : ")
    clientsocket.send(message.encode('ascii'))
    print()

server.close()
