# _*_ coding: utf-8 _*_
import json
import socket
import struct
import time
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
remoteAddr1=("10.0.0.25",8000)
try:
    phone.connect(remoteAddr1)
except Exception:
    print('[!] Server not found ot not open')
a = 0
while True:
    # 发收消息
   # cmd = input('请你输入命令>>：').strip()
   # if not cmd: continue
    a=a+1
    print(a)
    cmd =":BP01\r\n"
    cmd1=":BP00\r\n"
    cmd2=":BP11\r\n"
    cmd3=":BP10\r\n"
    phone.sendall(cmd.encode()) #发送
    time.sleep(1)
    header_lens=phone.recv(1024)
    print(header_lens)
    if header_lens==b':BP01;BPOK\r\n\r\n->':
        phone.sendall(cmd1.encode())
        time.sleep(1)
        header_lens2=phone.recv(1024)
        print(header_lens2)
        if header_lens2 == b':BP00;BPOK\r\n\r\n->':
            phone.sendall(cmd2.encode())
            time.sleep(1)
            header_lens3 = phone.recv(1024)
            print(header_lens3)
            if header_lens3== b':BP11;BPOK\r\n\r\n->':
                phone.sendall(cmd3.encode())
                time.sleep(1)
                header_lens4=phone.recv(1024)
                print(header_lens4)
    if a==1000:
        break
    else:
        continue

#continue




