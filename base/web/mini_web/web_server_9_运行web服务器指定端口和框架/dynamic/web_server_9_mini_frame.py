import re

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route("/login.htm")
def login():
    return "login"


@route("/search.htm")
def search():
    # with try except finally  默认帮我们写好了finally
    with open("./template/search.html") as f:
        content = f.read()
    return content


@route("/index.htm")
def index():
    with open("./template/index.html") as f:
        content = f.read()
    my_stock_info = "哈哈这里是本月名称..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content


@route("/center.htm")
def center():
    with open("./template/center.html") as f:
        content = f.read()
    my_stock_info = "这里是从mysql查询出来的数据..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content


# URL_FUNC_DICT = {
#     "/index.py": index,
#     "/center.py": center,
#     "/login.py": login,
#     "/search.py": search
# }


def application(env, start_response):
    start_response('200 OK', {("Content-Type", "text/html;charset=utf-8")})
    file_name = env["PATH_INFO"]

    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常: %s" % str(ret)
    """
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    elif file_name == "/search.py":
        return search()
    else:
        return "Hello World!我爱你"
    """
