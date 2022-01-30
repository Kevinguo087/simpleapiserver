from wsgiref.simple_server import make_server
import requests
import json
import datetime
def hello_world_1app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    #xiaoxi = "{"+"code:"+status+"data:"+"Hello!"
    #mes = ("你好")
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    smonth1 = len(str(month))
    if smonth1 < 2 :
        smonth = str(0)+str(month)
    date = smonth+str(day)
    url = 'https://baike.baidu.com/cms/home/eventsOnHistory/'+smonth+'.json'
    Headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 Edg/97.0.4692.99","Cookie":"__yjs_duid=1_c695298d251085442a9b6235ee3225591642848986968; BAIDUID=176FB070CAD0A450B8DC6ADB355F7211:FG=1; BAIDUID_BFESS=176FB070CAD0A450B8DC6ADB355F7211:FG=1; BIDUPSID=176FB070CAD0A450B8DC6ADB355F7211; PSTM=1643519249; BDRCVFR[ZdKQdWudTWY]=mk3SLVN4HKm; delPer=0; PSINO=2; H_PS_PSSID=35105_35776_34584_35491_35583_35245_35541_35796_35317_26350_35751_22159; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=ag8h018l2k80a18g241gvd7640r; channel=bing; baikeVisitId=2ee39586-3af1-49df-b138-0d4ee9cd8960; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1642848986,1642849059,1643552016; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1643552016; ab_sr=1.0.1_ZmVkMWUwMGVmMDgyNWI2MDg2OTM0OTc3NmMzMmVmMjhmYWRiNGM4NzdmMzVhMGZjMWFhMjIzY2Y0NDg0NWQ5OGU0NWU0N2I1MzNiMDZiY2IwY2Y2MWZiNjA1NGI5YTdl","X-Requested-With":"XMLHttpRequest","Referer":"https://baike.baidu.com/calendar/","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin"}
    r=requests.get(url=url,headers=Headers)
    j=json.loads(r.text)
    one = j[smonth]
    two = one[date]
    three = two[0]
    four = two[1]
    five = two[2]
    six = two[3]
    seven = two[4]
    eight = two[5]
    nine = two[6]
    ten = two[7]
    eleven = two[8]
    twelve = two[9]
    thirteen = two[10]
    fourteen = two[11]
    fifteen = two[12]
    sixteen = two[13]
    seventeen = two[14]
    re00 = three['title']
    re01 = three['year']
    re02 = three['desc']
    re10 = four['title']
    re11 = four['year']
    re12 = four['desc']
    re20 = five['title']
    re21 = five['year']
    re22 = five['desc']
    re30 = six['title']
    re31 = six['year']
    re32 = six['desc']
    re40 = seven['title']
    re41 = seven['year']
    re42 = seven['desc']
    re50 = eight['title']
    re51 = eight['year']
    re52 = eight['desc']

    neirong1 = re01+re00+re02+"更多……"+"\n"+re11+re10+re12+"更多……"+"\n"+re21+re20+re22+"更多……"+"\n"+re30+re31+re32+"更多……"+"\n"+re40+re41+re42+"更多……"+"\n"+re50+re51+re52+"更多……"+"\n"
    neirong2 = str(neirong1)
    return[neirong2.encode('UTF-8')]

with make_server('', 4500, hello_world_1app) as httpd:
    print("正在4500端口上运行历史上的今天服务")

    # Serve until process is killed
    httpd.serve_forever()