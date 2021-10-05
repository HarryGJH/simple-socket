# TCP server
import socket

def tcp_server(host,port):
    mySocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)   # TCP
    print("Start listening on %s : %d" %(host,port))
    mySocket.bind((host,port))
    
    mySocket.listen(1)
    print("Waiting for connection.......")
    conn,addr = mySocket.accept()

    login=False
    username=conn.recv(1024).decode()
    password=conn.recv(1024).decode()
    if username=="abc" and password=="123456":
        login=True
        conn.send(str(login).encode())
    
    print("Connected by: " + str(addr))
    print("Receiving.......")
    while login:
        msg=conn.recv(1024).decode()
        print(msg)
        conn.send("! Message received !---from server".encode())
        if msg=="q":
            print("Closing connection.......")
            break
    else:
        print("Login error!")
    conn.close()
    print("Connection closed!")
        

if __name__=='__main__':
    host="127.0.0.1"
    port=8080
    tcp_server(host,port)