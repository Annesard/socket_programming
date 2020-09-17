import socket                   
import os.path

# Create a socket object
port = 60000                   
s = socket.socket()             
host = '172.31.17.55'       

# Bind to the port
s.bind((host, port))

# Now wait for client connection.
s.listen(5)                     
print ("Server listening....")

while True:
     # Establish connection with client.
    c, addr = s.accept()    
    
    # receive the file name
    filename = c.recv(1600)
    filename = filename.decode()
    name, format1 = filename.split(".")
    
    # check if there are files with same name
    if os.path.isfile(filename):
            name = name + "_copy"
            filename = name + "." + format1
            
    for i in range(100):
        if os.path.isfile(filename):
            name = name + str(i)
            filename = name + "." + format1
        
   
    f = open(filename,'wb')
    
    # receive data 
    print ('Got connection from', addr)
    print ("Receiving...")
    data = c.recv(1024)
    while (data):
        print ("Receiving...")
        f.write(data)
        data = c.recv(1024)
        print(len(l))
    f.close()
    print ("Done Receiving")
    
    # close the socket
    c.shutdown(socket.SHUT_WR)
    c.close()
 
