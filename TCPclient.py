# TCP client
import sys
import socket

def tcp_client(host,port):
    mySocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)   # TCP
    mySocket.connect((host,port))

    login=False
    username=input("username: ")
    mySocket.send(username.encode())
    password=input("password: ")
    mySocket.send(password.encode())
    login=bool(mySocket.recv(1024).decode())

    while login:
        msg=input("(press q to quit) message: \n").encode()
        if msg.decode()=='q':
            mySocket.send(msg)
            break
        mySocket.send(msg)
        print(mySocket.recv(1024).decode())
    else:
        print("Login error!")
        
    mySocket.close()
    sys.exit(1)

if __name__=='__main__':
    host="127.0.0.1"
    port=8080
    print("You are going to connect %s : %d" %(host,port))
    flag=input("Continue? y/n ")
    if flag=='y':
        tcp_client(host,port)
    else:
        sys.exit(1)