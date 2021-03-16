import struct
lst  = [1,2,4,3,5,]
lst1  = [1,2,4,3,5,7,8,9,]
a = struct.pack('i',len(lst))#将列表的长度转化为固定的4字节
b = struct.pack('i',len(lst1))
print(a,len(a))
print(b,len(b))