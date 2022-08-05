from socket import *

# 1. 创建socket
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 2. 链接服务器
tcp_client_socket.connect(("192.168.0.101", 8080))

# 提示用户输入数据
send_data = input("请输入要发送的数据：")

# 3. 向服务器发送数据
tcp_client_socket.send(send_data.encode("utf-8"))

# 4. 关闭套接字
tcp_client_socket.close()