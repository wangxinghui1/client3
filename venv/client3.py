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
    cmd4=":SL01\r\n"
    cmd5=":SL02\r\n"
    cmd6 = ":SL03\r\n"
    cmd7 = ":SL11\r\n"
    cmd8= ":SL12\r\n"
    cmd9= ":SL13\r\n"
    cmd10= ":SL00\r\n"
    cmd11 = ":SL10\r\n"
    cmd12=":BZ01\r\n"
    cmd13=":BZ00\r\n"
    phone.sendall(cmd.encode()) #发送
    time.sleep(1)
    header_lens=phone.recv(1024)
    print(header_lens)
    if header_lens== b':BP01;BPOK\r\n\r\n->':
        phone.sendall(cmd4.encode())
        time.sleep(1)
        header_lens1=phone.recv(1024)
        print(header_lens1)
        if header_lens1 == b':SL01;SLOK\r\n\r\n->':
            phone.sendall(cmd5.encode())
            time.sleep(1)
            header_lens2 = phone.recv(1024)
            print(header_lens2)
            if header_lens2 == b':SL02;SLOK\r\n\r\n->':
                phone.sendall(cmd6.encode())
                time.sleep(1)
                header_lens3 = phone.recv(1024)
                print(header_lens3)
                if header_lens3 == b':SL03;SLOK\r\n\r\n->':
                    phone.sendall(cmd1.encode())
                    time.sleep(1)
                    header_lens4 = phone.recv(1024)
                    print(header_lens4)
                    if header_lens4 == b':BP00;BPOK\r\n\r\n->':
                        phone.sendall(cmd10.encode())
                        time.sleep(1)
                        header_lens5 = phone.recv(1024)
                        print(header_lens5)
                    if header_lens5== b':SL00;SLOK\r\n\r\n->':
                        phone.sendall(cmd2.encode())
                        time.sleep(1)
                        header_lens6 = phone.recv(1024)
                        print(header_lens6)
                        if header_lens6 == b':BP11;BPOK\r\n\r\n->':
                            phone.sendall(cmd7.encode())
                            time.sleep(1)
                            header_lens7 = phone.recv(1024)
                            print(header_lens7)
                            if header_lens7 == b':SL11;SLOK\r\n\r\n->':
                                phone.sendall(cmd8.encode())
                                time.sleep(1)
                                header_lens8= phone.recv(1024)
                                print(header_lens8)
                                if header_lens8 == b':SL12;SLOK\r\n\r\n->':
                                    phone.sendall(cmd9.encode())
                                    time.sleep(1)
                                    header_lens9= phone.recv(1024)
                                    print(header_lens9)
                                    if header_lens9 == b':SL13;SLOK\r\n\r\n->':
                                        phone.sendall(cmd3.encode())
                                        time.sleep(1)
                                        header_lens10 = phone.recv(1024)
                                        print(header_lens10)
                                        if header_lens10==b':BP10;BPOK\r\n\r\n->':
                                            phone.sendall(cmd11.encode())
                                            time.sleep(1)
                                            header_lens11=phone.recv(1024)
                                            print(header_lens11)
                                            if header_lens11 == b':SL10;SLOK\r\n\r\n->':
                                                phone.sendall(cmd12.encode())
                                                time.sleep(1)
                                                header_lens12 = phone.recv(1024)
                                                print(header_lens12)
                                                if header_lens12 == b':BZ01;BZOK\r\n\r\n->':
                                                    phone.sendall(cmd13.encode())
                                                    time.sleep(1)
                                                    header_lens12 = phone.recv(1024)
                                                    print(header_lens12)

    if a==1000:
        break
    else:
        continue