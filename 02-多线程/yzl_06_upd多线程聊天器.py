import socket
import threading


def recv_msg(udp_socket):
    # 接收数据
    while True:
        recv_date = udp_socket.recvfrom(1024)
        print(recv_date[0].decode("gbk"))


def send_msg(udp_socket, dest_ip, dest_port):
    # 发送数据
    while True:
        send_date = input("请输入你要发送的数据：")
        udp_socket.sendto(send_date.encode("gbk"), (dest_ip, dest_port))


def main():
    """聊天器的总体流程"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("192.168.111.128", 7890))

    # 接受对方的ip和port
    dest_ip = input("请输入你的ip：")
    dest_port = int(input("请输入你的port："))

    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()