import socket
import re


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
    client_socket_list = list()
    while True:
        # 4.等待客户端的到来
        try:
            new_socket, client_addr = tcp_server.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_date = client_socket.recv(1024).decode()
            except Exception as ret:
                pass
            else:
                if recv_date:
                    service_client(client_socket, recv_date)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭套接字
    tcp_server.close()


if __name__ == "__main__":
    main()