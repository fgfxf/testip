import requests
import socket
import socks

def setProxies():
    urlapi="http://tiqu.pyhttp.taolop.com/getip?count=1&neek=8737&type=1&yys=0&port=2&sb=&mr=1&sep=1&city=411200&time=2"
    proIp=requests.get(url=urlapi).text
    proIp=proIp.split(':')
    Ip=proIp[0]
    Port=proIp[1]
    socks.set_default_proxy(socks.SOCKS5, Ip, int(Port))
    socket.socket = socks.socksocket
    return 1



setProxies()
proxies={'https':'https://127.0.0.1:10809'}
url="http://ip.tool.lu"
resp=requests.get(url=url,verify=False,timeout=(3,3))
print(resp.text)
