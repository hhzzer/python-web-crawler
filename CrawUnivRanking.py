#!/url/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import  bs4
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(html,ulist):
    #file = "/tmp/zuihaodaxuepaiming2016.html"
    #soup = BeautifulSoup(open(file), "html.parser")
    soup = BeautifulSoup(html)
    for tr in soup.tbody.children:
        if isinstance(tr,bs4.element.Tag):
          tds = tr.contents
          ulist.append([tds[0].string,tds[2].string,tds[5].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^10}\t{:^10}".format("排名","学校","分数"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^10}\t{:^10}".format(u[0],u[1],u[2]))

def main():
    uinfo = []
    url ="http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(html,uinfo)
    printUnivList(uinfo,20)


def test():
    ulist = []
    file = "/tmp/zuihaodaxuepaiming2016.html"
    soup = BeautifulSoup(open(file),"html.parser")
    #print(soup.tbody.find_all('tr')[1])
    #print(type(soup.tbody.children))
    for tr in soup.tbody.children:
        if isinstance(tr,bs4.element.Tag):
          tds = tr.contents
          ulist.append([tds[0].string,tds[2].string,tds[4].string,tds[5].string])

    print(ulist)

#test()
main()