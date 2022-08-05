import socket


# 1. 创建TCP套接字
server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定本地信息
server_s.bind(("", 9456))     #主机地址有没有都可以，192.168.0.115

# 3. 设置为被动的
server_s.listen(128)

# 4. 等待客户端链接
new_s, client_info = server_s.accept()

# 5. 用新的套接字为已经连接好的客户端服务器            必须禁用虚拟网卡后才能广播，我的电脑上安装了vmware,所以我需要禁用它的网卡
while True:
    recv_content = new_s.recv(1024)
    print("%s>>>%s" % (str(client_info), recv_content.decode("gbk")))

    if not recv_content:
        # 当客户端调用了close后，recv返回值为空，此时服务套接字就可以close了
        # 6. 关闭服务套接字
        new_s.close()
        break

# 7. 关闭监听套接字
server_s.close()