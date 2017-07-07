#!/url/bin/python
# -*- coding:utf-8 -*-
import requests
import os
import re
from bs4 import BeautifulSoup

def getHTMLText():
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:700]
    except:
        return "产生异常"

def getHTMLHead():
    try:
        r = requests.head(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.headers
    except:
        return "产生异常"

def searchBaidu():
    kv = {'wd':'python'}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.status_code)
    print(r.request.url)
    #print(r.text[:1000])
    print(len(r.text))


def downPic():
    root = "/home/hhzzer/Pictures/"
    url = "http://image.nationalgeographic.com.cn/2017/0704/20170704030835566.jpg"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")

def ipSearch():
    url = "http://site.ip138.com/"
    try:
        r = requests.get(url+'baidu.com'+'/')
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("爬取失败")

def bs4Learn():
    r = requests.get("http://python123.io/ws/demo.html")
    demo = r.text
    soup = BeautifulSoup(demo,"html.parser")
    print(soup.find_all(string = re.compile("python")))
    #for tag in soup.find_all(re.compile('link')):
     #   print(tag.name)

if __name__ == "__main__":
    url = "https://item.jd.com/4073319.html"
    #print(getHTMLText())
   #print(getHTMLHead())
    #r = requests.post('http://httpbin.org/post',data='abc')
    #print(r.text)
    #searchBaidu()
    #downPic()
    #ipSearch()
    bs4Learn()