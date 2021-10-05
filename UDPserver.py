# UDP server
import socket

def udp_server(host,port):
    mySocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)   # UDP
    print("Start server on %s : %d" %(host,port))
    mySocket.bind((host,port))
    print("Waiting for connection.......")

    login=False
    username=mySocket.recvfrom(1024)[0].decode()
    password,addr=mySocket.recvfrom(1024)
    password=password.decode()
    if username=="abc" and password=="123456":
        login=True
        mySocket.sendto(str(login).encode(),addr)
    else:
        login=False
        mySocket.sendto(str(login).encode(),addr)

    while login:
        msg,addr=mySocket.recvfrom(1024)
        print("Receiving from %s: "%str(addr))
        print(msg.decode())        
        if msg.decode()=="q":
            print("Closing connection.......")
            break
        mySocket.sendto("! Message received !---from server".encode(),addr)
    else:
        print("Login error!")

    print("Connection closed!")
    mySocket.close()
        
if __name__=='__main__':
    host="127.0.0.1"
    port=8080
    udp_server(host,port)