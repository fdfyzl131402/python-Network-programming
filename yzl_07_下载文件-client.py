import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.输入服务器的ip和port
    server_ip = input("请输入服务器的ip")
    server_port = int(input("请输入服务器的port"))
    # 3.连接到服务器
    tcp_socket.connect((server_ip, server_port))
    # 4.输入要下载文件的名字
    download_file_name = input("请输入要下载的名字")
    # 5.将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))
    # 6.接收服务器中的数据
    recv_date = tcp_socket.recv(1024)   # 1024----> 1k , 则1024*1024 ---->1M
    if recv_date:
        # 7.保存数据到一个文件中
        with open("[附件]" + download_file_name, "wb")as f:
            f.write(recv_date)
    # 8.关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()