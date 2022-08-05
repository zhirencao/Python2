
import socket
import threading


class HandleData(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        # 接收/发送数据
        while True:
            recv_content = self.client_socket.recv(1024)
            if len(recv_content) != 0:
                print(recv_content)
                self.client_socket.send(recv_content)
            else:
                self.client_socket.close()
                break

    def __del__(self):
        self.client_socket.close()



class TCPServer(threading.Thread):
    def __init__(self, port):
        # 调用父类的初始化方法
        # threading.Thread.__init__(self)
        super().__init__()

        # 创建套接字
        self.server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定本地信息
        self.server_s.bind(("", port))

        # 将套接字由默认的主动链接模式改为被动模式（监听模块）
        self.server_s.listen(128)


    def run(self):
        # 等待客户端进行链接
        while True:
            new_s, client_info = self.server_s.accept()
            print(client_info)

            # t = HandleData(new_s)
            # t.start()
            HandleData(new_s).start()

    def __del__(self):
        # 关闭套接字
        self.server_s.close()


def main():
    tcp_server = TCPServer(7788)  # 7788表示TCP要绑定的端口
    tcp_server.start()

if __name__ == '__main__':
    main()