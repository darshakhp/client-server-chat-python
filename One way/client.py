import socket
Sock_Client=socket.socket()
host=socket.gethostname()
port=3333
x=""
Sock_Client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Sock_Client.connect((host,port))
while x!="exit":
	x = Sock_Client.recv(1024)
	print x 
Sock_Client.close()