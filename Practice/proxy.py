import requests
from bs4 import BeautifulSoup
import os
class Proxy:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        self.proxyurl = "http://www.xicidaili.com/wn/"
        self.testurl = "https://www.google.com/"
    def ipproxy(self,page):
        #f = open('proxy.txt','w+')
        s=requests.session()
        iphtml = s.get(self.proxyurl + str(page),headers=self.headers)
        soup = BeautifulSoup(iphtml.text,"html parser")
        trs = soup.find('table',id='ip_list').find_all('tr')
        items = []
        for tr in trs[1:]:
            tds = tr.find_all('td')
            ip = tds[1].text.strip()
            prot = tds[2].text.strip()
            protocol = tds[5].text.strip()
            i = ('%s=%s:%s'%(protocol,ip,prot))
            items.append([i])
            #f.write('%s=%s:%s\n'%(protocol,ip,prot))
            #print('%s=%s:%s'%(protocol,ip,prot))
        return items
    def testproxy(self,page):
        proxylist = self.ipproxy(page)
        for iplist in proxylist:
            protocol,ip = ''.join(iplist).split('=')
            #print(protocol,ip)
            proxies = {"http": ip}
            try:
                requests.get(self.testurl,headers=self.headers,proxies=proxies,timeout=3)
            except Exception:
                print(u'这个ip不行、换下一个')
            else:
                print(u'这个IP好使、他是：',proxies)
                f = open('proxy.txt','a')
                f.write(str(ip)+'\n')
                f.close()

    def proxypage(self,start,end):
        for i in range(start,end+1):
            self.testproxy(i)

proxy =Proxy()
proxy.proxypage(1,2)