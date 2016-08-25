import requests
import os
from urllib.request import urlopen
from urllib.parse import urlsplit
from os.path import basename
from urllib.error import HTTPError
from bs4 import BeautifulSoup
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Cookie":"3661916355=d1e4xlIB80LuAx8UN9flfgiXK%2FLt7a%2FifpVwl8X23Q; _gat=1; 3661916355=1ad9Dgz6RH6oSB9wAsq8VKECtejKUtJuCP2jE4Wt1g; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1472021389774; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1472019203,1472019540,1472021188,1472021391; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1472021391; _ga=GA1.2.1501173324.1463663963"}

file = open('./pages.txt','w')
url = "http://jandan.net/ooxx"
req = session.get(url,headers=headers)
bsObj = BeautifulSoup(req.text,"lxml")
address = bsObj.findAll("a",{"class":"previous-comment-page"})[0]
imgs = bsObj.findAll("a",{"class":"view_img_link"})
for x in imgs:
    try:
        img_data = urlopen(x['href']).read()
        file_name = basename(urlsplit(x['href'])[2])
        output = open('img/'+file_name,'wb')
        output.write(img_data)
        output.close()
    except:
        pass


for x in range(100):
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
            img_data = urlopen(x['href']).read()
            file_name = basename(urlsplit(x['href'])[2])
            output = open('img/'+file_name,'wb')
            output.write(img_data)
            output.close()
        except:
            pass


