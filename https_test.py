import urllib.request
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://aivicomm.jp/'
while True:
    with urllib.request.urlopen(url) as res:
       html = res.read().decode("utf-8")
       print(html)
       time.sleep(300)