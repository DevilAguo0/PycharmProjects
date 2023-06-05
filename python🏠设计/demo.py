def application(env, start_response):
    status = "200 OK"
    headers = [
        ("content-Type", "text/plain"),
    ]
    start_response(status, headers)
    return "<h1>hello itheima</h1>"


from socket import *

