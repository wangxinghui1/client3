# _*_ coding: utf-8 _*_
import socket
import struct
import json
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('10.0.0.25',8000)) #连接服
while True:
    # 发收消息
    cmd = input('请你输入命令>>：').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8')) #发送
    #先收报头
    unpack_res = struct.unpack('i',phone.recv(4))[0]
    #后收数据
    recv_size = 0
    total_data=b''
    while recv_size<unpack_res: #循环的收
        recv_data = phone.recv(1024) #1024只是一个最大的限制
        recv_size+=len(recv_data) #
        total_data+=recv_data #
    print('返回的消息：%s'%total_data.decode('gbk'))
phone.close()