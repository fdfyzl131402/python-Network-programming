def center():
    with open("./templates/center.html") as f:
        return f.read()


def index():
    with open("./templates/index.html") as f:
        return f.read()


URL_FUNC_DICT = {
    "./index.py": index,
    "./center.py": center
}


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])
    file_name = env["PATH_INFO"]
    # if file_name == "/index.py":
    #     return index()
    # elif file_name == "/center.py":
    #     return center()
    # else:
    #     return 'Hello World!,我是中国人'

    func = URL_FUNC_DICT[file_name]
    return func()
