# URL_FUNC_DICT = {
#     "/index.html": index,
#     "/center.html": center
# }
URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT[url] = index
        URL_FUNC_DICT[url] = func

        def call_func():
            return func()
        return call_func
    return set_func


@route("/center.html")
def center():
    with open("./templates/center.html") as f:
        return f.read()


@route("/index.html")
def index():
    with open("./templates/index.html") as f:
        return f.read()


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])
    file_name = env["PATH_INFO"]
    # if file_name == "/index.py":
    #     return index()
    # elif file_name == "/center.py":
    #     return center()
    # else:
    #     return 'Hello World!,我是中国人'

    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常 %s" % ret
