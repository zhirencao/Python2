# UDP服务端填自己IP可以发送接收，UDP客户端填对方IP可以发送，不能接收
import socket
import threading


def send_msg(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    while True:

        print("1: 发送数据")
        print("2: 退出程序")
        op = input("请输入操作序号:")
        if op == "1":
            # 1. 输入对方的ip地址
            dest_ip = input("\n请输入对方的ip地址:")
            # 2. 输入对方的port
            dest_port = int(input("\n请输入对方的port:"))
            while True:
                # 3. 从键盘输入数据
                msg = input("\n请输入要发送的数据:")
                if msg:
                    # 4. 发送数据
                    udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))
                else:
                    # 要是没有输入内容则认为是要重新输入ip、port
                    break
        elif op == "2":
            break

    udp_socket.close()


def recv_msg(udp_socket):
    """接收数据并显示"""
    while True:
        try:
            # 1. 接收数据
            recv_msg = udp_socket.recvfrom(1024)
        except:
            break
        else:
            # 2. 解码
            recv_ip = recv_msg[1]
            recv_msg = recv_msg[0].decode("utf-8")
            # 3. 显示接收到的数据
            print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(("", 7890))

    # 3. 创建一个新的线程，用来接收数据
    udp_r = threading.Thread(target=recv_msg, args=(udp_socket,))

    # 4. 创建一个新的线程，用来发送数据
    udp_s = threading.Thread(target=send_msg, args=(udp_socket,))

    # 5. 运行创建的子线程
    udp_r.start()
    udp_s.start()

if __name__ == "__main__":
    main()