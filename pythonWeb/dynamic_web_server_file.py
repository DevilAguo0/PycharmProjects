from socket import *
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./"
PORT = 8000


class HTTPServer(object):
    """初始化"""

    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, port):
        """绑定服务器地址"""
        self.server_socket.bind(("", port))

    def start(self):
        """启动服务器，处理请求"""
        self.server_socket.listen(128)
        print("服务器{}开启".format(PORT))
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("客户端连接到达:{}".format(str(client_address)))
            handle_client_process = Process(target=self.handle_client,
                                            args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

        def handle_client(self, client_socket):
            """处理已连接客户端的请求"""
            """获取客户端请求数据"""
            request_data = client_socket.recv(1024)
            request_lines = request_data.splitlines()
            if request_lines:
                request_start_line = request_lines[0]
                # 提取用户请求的文件名
                file_name = re.match(r'\w+\s+(/[^ ]*)\s', request_start_line.decode("gb2312")).group(1)
                if file_name.endswith(".py"):
                    # 执行文件
                    m = __import__(file_name[1:-3])
            # 定义环境变量(字典类型)
            env = {}
            response_body = m.application(env, self.start_response)
            response = self.response_headers + "\r\n" + response_body

        # 向客户端返回响应数据
        client_socket.sent(response.encode('gb2312'))
        # 关闭客户端连接
        client_socket.close

    def start_response(self, status, headers):
        """从web应用中获取响应码及响应体头域"""
        response_headers = "HTTP/1.1" + status + '\r\n'
        for hreader in headers:
            response_headers += "%s:%s\r\n" % hreader
        self.response_headers = response_headers

    def main(self):
        http_server = HTTPServer()
        http_server.bind(PORT)
        http_server.start()

    if __name__ == "__main__":
        main()
