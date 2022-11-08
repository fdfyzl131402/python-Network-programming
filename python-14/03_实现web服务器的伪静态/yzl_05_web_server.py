import socket
import re
import multiprocessing
import sys
# import time
# import dynamic.mini_frame


class WSGIServer(object):

    def __init__(self, port, app, static_path):
        # 1.创建套接字
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定本地信息
        self.tcp_server.bind(("192.168.111.128", port))
        # 3.转为监听
        self.tcp_server.listen(128)
        self.application = app
        self.status_path = static_path

    def service_client(self, new_socket):
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

        # 如果请求的资源不是以.html结尾的，那么请求的就是静态资源 （css, js, png等）
        if not file_name.endswith(".html"):
            try:
                f = open(self.status_path + file_name, "rb")
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

        else:
            # 如果请求的是以.py结尾的动态资源

            # body = "hahaha %s " % time.ctime()
            env = dict()
            env["PATH_INFO"] = file_name
            # {PATH_INFO: "file_name"}
            body = self.application(env, self.set_response_header)
            header = "HTTP/1.1 %s \r\n" % self.status
            for temp in self.headers:
                header += "%s:%s \r\n" % (temp[0], temp[1])
            header += "\r\n"
            response = header + body
            new_socket.send(response.encode("utf-8"))

        # 关闭套接字
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("server", "mini_web v1.0")]
        self.headers += headers

    def run_forever(self):
        """整体控制"""

        while True:
            # 4.等待客户端的到来
            new_socket, client_addr = self.tcp_server.accept()
            # 5.为客户端分配服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()

        # 关闭套接字
        self.tcp_server.close()


def main():
    """控制整体， 创建一个对象，调用这个对象的run_forever方法"""
    # sys.argv 给程序传参数
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])  # 7890
            frame_app_name = sys.argv[2]   # mini_frame:application
        except Exception as ret:
            print("端口输入错误...")
            return
    else:
        print("输入有误")
        print("格式为：python3 xxx.py 7890 mini_app_frame:application")
        return

    # mini_frame:application
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)  # mini_app_frame
        app_name = ret.group(2)  # application
    else:
        print("输入有误")
        print("格式为：python3 xxx.py 7890 mini_frame:application")
        return

    with open("web_server.conf") as f:
        conf_info = eval(f.read())
    # 此时 conf_info 是一个字典
    #   {
    # 	"dynamic_path":"./dynamic"
    # 	"static_path":"./static"
    # }

    sys.path.append(conf_info['dynamic_path'])
    # import frame_app_name -----> 找 frame_app_name
    frame = __import__(frame_name)  # 返回值标记着这个模块 mini_frame
    app = getattr(frame, app_name)  # app指向了 dynamic 下mini_frame 的 application函数
    wsgi_server = WSGIServer(port, app, conf_info['static_path'])
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()