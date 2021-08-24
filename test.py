import requests
import socket
import socks

url="http://ip.tool.lu"
resp=requests.get(url=url,verify=False,timeout=(3,3))
print(resp.text)

ex=r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
result=re.findall(ex,resp.text,re.S)
print(result[0])

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
    urlapi="http://pycn.yapi.3866866.com/index/index/save_white?neek=8737&appkey=63892542302d2904498fe7579e173ad1&white="+IP
    resp=requests.get(url=urlapi,verify=False,timeout=(3,3))
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
