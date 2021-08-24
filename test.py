import requests
import socket
import socks
import re


url="http://ip.tool.lu"
resp=requests.get(url=url,verify=False,timeout=(3,3))
print(resp.text)

ex=r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
result=re.findall(ex,resp.text,re.S)
print(result[0])
url="http://pycn.yapi.3866866.com/login"
headers={
'POST':'/login HTTP/1.1',
'Host':'pycn.yapi.3866866.com',
'Content-Length': '47',
'Accept': 'text/html, */*; q=0.01',
'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHByX3RpbWUiOiIxNjI5NzgzMzIwIiwidWlkIjoiODczNyJ9.Zr8UqT2Wkug6y4RCOxLrdBof1r078eAgPfMM_mg2B2Y',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Origin': 'http://pc.py.cn',
'Referer': 'http://pc.py.cn/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Connection': 'close'

}

data={
'phone':'15238981687',
'password':'fmf123456',
'remember':0
}
resp=requests.post(url=url,headers=headers,data=data)

token=json.loads(resp.text)
token=token.get('ret_data').get("token")
print(token)

def setProxies():
    urlapi="http://tiqu.pyhttp.taolop.com/getip?count=1&neek=8737&type=1&yys=0&port=2&sb=&mr=1&sep=1&city=411200&time=2"
    proIp=requests.get(url=urlapi).text
    print(proIp)
    proIp=proIp.split(':')
    Ip=proIp[0]
    Port=proIp[1]
    print(proIp,Ip,Port)
    socks.set_default_proxy(socks.SOCKS5, Ip, int(Port))
    socket.socket = socks.socksocket
    return 1


def addWhite(IP):
    url="http://pycn.yapi.3866866.com/user/save_white_ip"
    headers={
    'POST':'/user/save_white_ip HTTP/1.1',
    'Host':'pycn.yapi.3866866.com',
    'Content-Length': '10',
    'Accept': 'text/html, */*; q=0.01',
    'Authorization':'Bearer '+token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://pc.py.cn',
    'Referer': 'http://pc.py.cn/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'close'

    }
    data={
                'ip':IP
   }
    resp=requests.post(url=url,headers=headers,data=data)
    print(resp.text)


def delWhile(IP):
    urlapi="http://pycn.yapi.3866866.com/index/index/del_white?neek=8737&appkey=63892542302d2904498fe7579e173ad1&white="+IP
    resp=requests.get(url=urlapi,verify=False,timeout=(3,3))
    print(resp.text)
    
addWhite(result[0])
setProxies()
proxies={'https':'https://127.0.0.1:10809'}
url="http://ip.tool.lu"
resp=requests.get(url=url,verify=False,timeout=(3,3))
print(resp.text)

delWhile(result[0])
