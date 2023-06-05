import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 12345))
serverSocket.listen(128)
print("等待客户端发起连接请求。。。")
conn, addr = serverSocket.accept()
print("客户端连接成功。。")
recv_data = conn.recv(1024)
print("接收到的数据为:", recv_data.decode('utf-8'))
conn.send("Thanks".encode('utf-8'))
conn.close()
serverSocket.close()
