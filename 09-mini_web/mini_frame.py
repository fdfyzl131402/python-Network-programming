import time


def login():
    return "----login---welcome to my website....%s " % time.ctime()


def register():
    return "----register---welcome to my website....%s " % time.ctime()


def profile():
    return "----profile----welcome to my website....%s " % time.ctime()


def application(file_name):
    if file_name == "/login.py":
        return login()

    elif file_name == "/register.py":
        return register()
    else:
        return "not found 404"


