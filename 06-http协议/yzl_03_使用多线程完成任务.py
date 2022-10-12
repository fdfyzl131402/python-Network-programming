import socket
import re
import threading


def service_client(new_socket):
    """要服务的客户端"""
    # 1.接受客户端发送来的请求数据
    # GET / HTTP/1.1
    # ......
    request = new_socket.recv(1024).decode("utf-8")
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
        # 2.返回数据给客户端
        # 2.1 发送数据给客户端---- header
        response = "HTTP/1.1 200 OK \r\n"
        response += "\r\n"
        # 2.2 发送数据给客户端---- body
        # response += "<h1>h</h1>"
        # 把header发给客户端
        new_socket.send(response.encode("utf-8"))
        # 把body发送给客户端
        new_socket.send(html_content)
        # 关闭套接字
        new_socket.close()


def main():
    """整体控制"""
    # 1.创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定本地信息
    tcp_server.bind(("192.168.111.128", 7788))
    # 3.转为监听
    tcp_server.listen(128)
    while True:
        # 4.等待客户端的到来
        new_socket, client_addr = tcp_server.accept()
        # 5.为客户端分配服务
        p = threading.Thread(target=service_client, args=(new_socket,))
        p.start()
        # new_socket.close()   主线程挂了， 子线程必挂
    # 关闭套接字
    tcp_server.close()


if __name__ == "__main__":
    main()
