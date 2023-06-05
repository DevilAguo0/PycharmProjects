import socket
sever_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sever_socket.bind(("127.0.0.1",3456))
print("---聊天室---")
while True:
    data,address = sever_socket.recvfrom(1024)
    print("%s:%s" % (address[0],address[1]))
    print("%s" % data.decode("utf-8"))
sever_socket.close()
