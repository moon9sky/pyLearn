import requests
from datetime import datetime
from urllib.request import urlopen
from urllib import request
from urllib.parse import urlsplit
from os.path import basename
from urllib.error import HTTPError
from bs4 import BeautifulSoup
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Cookie":"_gat=1; 711139627=6e16Lomm9yZybx0QbWFXR6kcHvt%2FD17YWg6tvaw4; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1472131824362; _ga=GA1.2.1849853486.1453643018; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1471761239,1471788385,1471957084,1472131823; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1472131825"}

file = open('./pages.txt','w')
url = "http://jandan.net/ooxx"
startTime = datetime.now()
req = session.get(url,headers=headers)
endTime = datetime.now()
print("打开页面，用时：",(endTime-startTime))
bsObj = BeautifulSoup(req.text,"lxml")
address = bsObj.findAll("a",{"class":"previous-comment-page"})[0]
imgs = bsObj.findAll("a",{"class":"view_img_link"})
for x in imgs:
    try:
        reqImg = request.Request(x['href'])
        reqImg.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36")
        print("正在下载"+x['href'])
        startTime = datetime.now()
        img_data = urlopen(reqImg).read()
        endTime = datetime.now()
        print("下载完成，用时：",(endTime-startTime))
        file_name = basename(urlsplit(x['href'])[2])
        startTime = datetime.now()
        output = open('./img/'+file_name,'wb')
        output.write(img_data)
        output.close()
        endTime = datetime.now()
        print("保存完成，用时：",(endTime-startTime))
    except HTTPError as e:
        print(e)


for x in range(5):
    url = address['href']
    req = session.get(url,headers=headers)
    bsObj = BeautifulSoup(req.text,"lxml")
    if len(bsObj.findAll("a",{"class":"previous-comment-page"}))>0:
        address = bsObj.findAll("a",{"class":"previous-comment-page"})[0]
    else:
        address=0
    imgs = bsObj.findAll("a",{"class":"view_img_link"})
    for x in imgs:
        try:
            reqImg = request.Request(x['href'])
            reqImg.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36")
            print("正在下载" + x['href'])
            startTime = datetime.now()
            img_data = urlopen(reqImg).read()
            endTime = datetime.now()
            print("下载完成，用时：",(endTime-startTime))
            startTime = datetime.now()
            file_name = basename(urlsplit(x['href'])[2])
            output = open('img/'+file_name,'wb')
            output.write(img_data)
            output.close()
            endTime = datetime.now()
            print("保存完成，用时：",(endTime-startTime))
        except HTTPError as e:
            print(e)


