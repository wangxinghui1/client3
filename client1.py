# Socket client example in python

import socket  # for sockets
import sys  # for exit
import struct
import time

# create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('Socket Created')

host = '10.0.0.25';
port = 8000;

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    # could not resolve
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
s.connect((remote_ip, port))

print('Socket Connected to ' + host + ' on ip ' + remote_ip)

# Send some data to remote server
message = ":BP01\r\n"
try:
    # Set the whole string
    s.sendall(message)
except socket.error:
    # Send failed
    print('Send failed')
    sys.exit()

print('Message send successfully')


def recv_timeout(the_socket, timeout=2):
    # make socket non blocking
    the_socket.setblocking(0)

    # total data partwise in an array
    total_data = [];
    data = '';

    # beginning time
    begin = time.time()
    while 1:
        # if you got some data, then break after timeout
        if total_data and time.time() - begin > timeout:
            break

        # if you got no data at all, wait a little longer, twice the timeout
        elif time.time() - begin > timeout * 2:
            break

        # recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                # change the beginning time for measurement
                begin = time.time()
            else:
                # sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass

    # join all parts to make final string
    return ''.join(total_data)


# get reply and print
print(recv_timeout(s))

# Close the socket
s.close()