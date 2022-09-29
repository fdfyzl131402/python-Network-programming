import socket


def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定一个本地信息
    local_address = ("192.168.111.128", 7788)
    udp_socket.bind(local_address)

    # 3.接受数据
    while True:
        # recv_date  储存的是一个元组(接受到的数据，发送方的（ip，port）)

        recv_date = udp_socket.recvfrom(1024)
        recv_msg = recv_date[0]  # 储存接受到的数据
        recv_addr = recv_date[1]  # 发送方的ip和port

        # 4.打印接收到的数据
        # print(recv_date)
        # print("%s:%s" % (str(recv_addr), recv_msg.decode("utf-8")))
        print("%s:%s" % (str(recv_addr), recv_msg.decode("gbk")))
        if len(recv_msg) > 10:
            break
    # 5.关闭
    udp_socket.close()


if __name__ == "__main__":
    main()
