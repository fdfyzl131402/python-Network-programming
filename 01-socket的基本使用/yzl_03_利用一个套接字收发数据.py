import socket


def main():
    # 创建一个套接字
    udp_use = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind绑定的是一个元组
    udp_use.bind(("192.168.111.128", 4545))
    # 获取目标ip和端口
    dest_ip = input("请输入ip地址：")
    dest_port = int(input("请输入端口号："))

    while True:

        # 从键盘获取数据
        udp_date = input("请输入你要发的消息：")
        if udp_date == "exit":
            break
        # 可以使用套接字收发数据
        # udp_use.sendto(b"hhh", ("10.66.118.104", 8080))
        udp_use.sendto(udp_date.encode("utf-8"), (dest_ip, dest_port))
        # 接受数据
        udp_recv = udp_use.recvfrom(1024)
        print(udp_recv)
    # 关闭套接自字
    udp_use.close()


if __name__ == "__main__":
    main()