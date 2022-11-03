def register():
    return "我是注册"


def index():
    return "我是主页"


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])
    file_name = env["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/register.py":
        return register()
    else:
        return 'Hello World!,我是中国人'

