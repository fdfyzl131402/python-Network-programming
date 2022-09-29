import socket


def send_msg(udp_socket):
    # 对方ip和port
    send_ip = input("请输入ip")
    send_port = int(input("请输入port"))
    # 要发送的信息
    send_date = input("请输入要发送的信息")
    udp_socket.sendto(send_date.encode("utf-8"), (send_ip, send_port))


def recv_msg(udp_socket):
    recv_date = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_date[1]), recv_date[0].decode("gbk")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定
    udp_socket.bind(("192.168.111.128", 7788))

    while True:
        print("------udp聊天室-------")
        print("1.发送消息")
        print("2.接受消息")
        print("3.退出系统")
        op = input("请输入功能")
        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接收
            recv_msg(udp_socket)
        elif op == "3":
            break
        else:
            print("你输入的数字有误")


if __name__ == "__main__":
    main()