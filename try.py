import requests
from datetime import datetime
from urllib.request import urlopen
from urllib import request
from urllib.parse import urlsplit
from os.path import basename
from urllib.error import HTTPError
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Cookie":"_gat=1; 711139627=6e16Lomm9yZybx0QbWFXR6kcHvt%2FD17YWg6tvaw4; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1472131824362; _ga=GA1.2.1849853486.1453643018; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1471761239,1471788385,1471957084,1472131823; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1472131825"}

rootUrl = "http://jandan.net/ooxx"
session = requests.Session()


def openUrl(url):
    try:
        req = session.get(url,headers=headers)
        webContent = BeautifulSoup(req.text,"lxml")
        address = webContent.findAll("a",{"class":"previous-comment-page"})[0]
        imgs = webContent.findAll("a",{"class":"view_img_link"})
        return address['href'],imgs
    except HTTPError as e:
        print(e)

def downLoadPic(url):
    try:
        reqImg = request.Request(url)
        reqImg.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36")
        file_name = basename(urlsplit(url)[2])
        img_data = urlopen(reqImg).read()
        return file_name,img_data
    except HTTPError as e:
        print(e)

def savePic(img,name):
    try:
        output = open('./img/'+name,'wb')
        output.write(img)
        output.close()
    except Exception as e:
        print(e)

nextUrl,imgs = openUrl(rootUrl)
for x in imgs:
    imgName,imgData = downLoadPic(x['href'])
    savePic(imgData,imgName)

while(nextUrl != ""):
    nextUrl,imgs = openUrl(nextUrl)
    for x in imgs:
        imgName,imgData = downLoadPic(x['href'])
        savePic(imgData,imgName)


