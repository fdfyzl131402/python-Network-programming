import socket


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定本地信息
    tcp_server_socket.bind(("192.168.111.128", 7788))
    # 3.将默认的套接字由主动设置为被动 listen
    tcp_server_socket.listen(128)
    while True:
        # 4.等待客户端的连接
        print("---------等待客户端响应----------")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("--------接收到了---------")
        print(client_addr)
        # 循环目的，为同一个客户端服务多次
        while True:
            # 接受客户端的数据
            recv_date = new_client_socket.recv(1024)
            print("客户端发来的请求是:%s" % (recv_date.decode("gbk")))
            # 利用判断，判断客户端是发送过来数据 还是close关闭了客户端
            if recv_date:
                # 发送一部分数据给客户端
                new_client_socket.send("hahahahahaha".encode("utf-8"))
            else:
                break
        # 关闭套接字
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()