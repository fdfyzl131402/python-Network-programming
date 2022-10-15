import socket
import time

tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_server.bind(("192.168.111.128", 7788))
tcp_socket_server.listen(128)
tcp_socket_server.setblocking(False)  # 设置套接字为非堵塞的方式
client_socket_lists = list()
while True:

    time.sleep(0.5)

    try:
        new_socket, client_addr = tcp_socket_server.accept()
    except Exception as ret:
        print("----没有新的客户端到来-----")
    else:
        print("----只要没有异常，那么说明有新的客户端到来")
        new_socket.setblocking(False)
        client_socket_lists.append(new_socket)

    for client_socket in client_socket_lists:
        try:
            recv_date = client_socket.recv(1024)
        except Exception as ret:
            print(ret)
            print("----对方没有发送过来数据----")
        else:
            if recv_date:
                print("----接受到对方的数据----")
                print(recv_date)
            else:
                # 对方调用了close， 导致recv返回空
                client_socket_lists.remove(client_socket)
                client_socket.close()
                print("对方断开了连接")