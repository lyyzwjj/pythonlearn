def application(env, start_response):
    start_response('200 OK', {("Content-Type", "text/html;charset=utf-8")})
    file_name = env["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    elif file_name == "/search.py":
        return search()
    else:
        return "Hello World!我爱你"


def index():
    return "index"


def login():
    return "login"


def search():
    # with try except finally  默认帮我们写好了finally
    with open("./template/search.html") as f:
        content = f.read()
    return content
