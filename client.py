import socket                   # Import socket module
import sys

# Create a socket object
s = socket.socket()

# get the host, port and filename from the command
host = sys.argv[2]     
port = sys.argv[3]              
filename = sys.argv[1]

# print the name of the file
print(filename)

# coonecnt to the server
s.connect((host, int(port)))

# send file name to the server
s.sendall(filename.encode())

f = open(filename,'rb')

# send the data inside the file
print 'Sending...'
data = f.read(1024)
while (data):
    print 'Sending...'
    s.send(data)
    data = f.read(1024)
f.close()

# finish the process
print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(1024)
s.close()

