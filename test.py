import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url="http://ip.tool.lu"
resp=requests.get(url=url)
print(resp.text)
