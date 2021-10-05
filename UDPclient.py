# UDP client
import sys
import socket

def udp_client(host,port):
    mySocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)   # UDP

    login=False
    username=input("username: ")
    mySocket.sendto(username.encode(),(host,port))
    password=input("password: ")
    mySocket.sendto(password.encode(),(host,port))
    login=bool(mySocket.recvfrom(1024)[0].decode())
    
    while login:
        msg=input("(press q to quit) message: \n").encode()
        if msg.decode()=='q':
            mySocket.sendto(msg,(host,port))
            break
        mySocket.sendto(msg,(host,port))
        data,addr=mySocket.recvfrom(1024)
        print(data.decode(),"from server: ",addr)
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
        udp_client(host,port)
    else:
        sys.exit(1)