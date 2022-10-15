import socket
import re
import select


def service_client(new_socket, request):
    """要服务的客户端"""
    # 1.接受客户端发送来的请求数据
    # GET / HTTP/1.1
    # ......
    # request = new_socket.recv(1024).decode("utf-8")
    # print(request)
    request_lines = request.splitlines()
    print(request_lines)
    print("")
    print(">" * 20)
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*" * 50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----not file found"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content
        response_header = "HTTP/1.1 200 OK \r\n"
        response_header += "Content_Length: %d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)
        # 关闭套接字
        # new_socket.close()


def main():
    """整体控制"""
    # 1.创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定本地信息
    tcp_server.bind(("192.168.111.128", 7788))
    # 3.转为监听
    tcp_server.listen(128)
    tcp_server.setblocking(False)
    # 创建一个epoll对象
    epl = select.epoll()
    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server.fileno(), select.EPOLLIN)
    fd_event_dict = dict()
    while True:

        fd_event_list = epl.poll()  # 默认会堵塞，直到os检测到有新的数据到来，通过事件通知方式告诉程序才解堵塞
        # [(fd, event),] (套接字对应的文件描述符， 这个文件到底是什么事件，例如可以recv的事件等)

        for fd, event in fd_event_list:
            # 等待客户端的到来
            if fd == tcp_server.fileno():
                new_socket, client_addr = tcp_server.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)  # 判断事件是否有输入
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经连接的客户端是否有数据到来
                recv_date = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_date:
                    service_client(fd_event_dict[fd], recv_date)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭套接字
    tcp_server.close()


if __name__ == "__main__":
    main()