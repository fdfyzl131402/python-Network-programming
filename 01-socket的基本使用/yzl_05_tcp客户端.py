import socket


def main():
    # 1. 创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 链接服务器
    server_ip = input("请输入要连接的服务器：")
    server_port = int(input("请输入要连接的端口"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    # 3. 发送/接受数据
    send_date = input("请输入你要发送的信息")
    tcp_socket.send(send_date.encode("utf-8"))
    # 4.关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()