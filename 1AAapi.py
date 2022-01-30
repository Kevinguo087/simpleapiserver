from wsgiref.simple_server import make_server
import requests
import json
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    #xiaoxi = "{"+"code:"+status+"data:"+"Hello!"
    #mes = ("你好")
    url = 'https://v1.hitokoto.cn/?c=i&encode=json'
    r = requests.get(url)
    j = json.loads(r.text)
    hi = j['hitokoto']
    fr1 = j['from']
    fr = "「"+fr1+"」"
    wh = j['from_who']
    li1 = j['uuid']
    li = "https://hitokoto.cn?uuid="+li1

    neirong1 = '{"code":200,"status":"OK","data":{"content":"'+hi+'","source":"'+wh+fr+'","link":"'+li+'"}}'
    neirong2 = str(neirong1)
    return[neirong2.encode('UTF-8')]

with make_server('', 8000, hello_world_app) as httpd:
    print("正在8000端口上运行一言服务")

    # Serve until process is killed
    httpd.serve_forever()