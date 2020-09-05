import time


def login():
    return "login    %s" % time.ctime()


def register():
    return "register    %s" % time.ctime()


def profile():
    return "profile    %s" % time.ctime()


def application(file_name):
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    elif file_name == "/profile.py":
        return profile()
    else:
        return "not found your bage..."
