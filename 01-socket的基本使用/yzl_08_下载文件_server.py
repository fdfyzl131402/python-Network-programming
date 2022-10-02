import socket


def send_file_2_client(new_tcp_socket, new_tcp_addr):
    # 1.接受客户端发过来的要下载的文件名
    file_name = new_tcp_socket.recv(1024).decode("utf-8")
    print("客户端(%s)要下载的文件是%s" % (str(new_tcp_addr), file_name))
    # 2. 打开文件
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()

    except Exception as result:
        print("没有可下载的文件(%s)" % file_name)
    if file_content:
        # 3.发送文件的数据给客户端
        new_tcp_socket.send(file_content)


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定本地信息
    tcp_socket.bind(("192.168.111.128", 7788))

    # 3.将默认的套接字设置为被动
    tcp_socket.listen(128)
    while True:
        # 4.等待客户端的到来
        new_tcp_socket, new_tcp_addr = tcp_socket.accept()

        # 5.调用发送文件函数
        send_file_2_client(new_tcp_socket, new_tcp_addr)

        # 6.关闭套接字
        new_tcp_socket.close()
    tcp_socket.close()
    

if __name__ == "__main__":
    main()