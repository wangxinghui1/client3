import socket
import time
addr=("10.0.0.25",8000)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
#cmd =":BZ00\r\n"
while True:
    #s.sendall(cmd.encode())
   # time.sleep(1)
    a1=s.recv(1024)
    print(a1)