import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 12345))
send_data = input("请输入要发送的数据：")
clientSocket.send(send_data.encode('gbk'))
recv_data = clientSocket.recv(1024)
print("接收到的数据是：{}".format(recv_data.decode('gbk')))
clientSocket.close()
#10.115.229.19