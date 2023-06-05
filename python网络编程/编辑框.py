import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("---输入框--")
while True:
    data = input()
    client_socket.sendto(data.encode("gb2312"),("127.0.0.1",3456))
    if data == "88":
        break
client_socket.close()