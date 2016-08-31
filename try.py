import requests
import gzip
from datetime import datetime
from urllib.request import urlopen
from urllib import request
from urllib.parse import urlsplit
from os.path import basename
from urllib.error import HTTPError
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Cookie":"__cfduid=d128b406705c93694c4a8a6030b4529b81470453446; CzG_fid19=1472565927; CzG_fid33=1472564697; CzG_fid4=1472489014; __utma=26781301.628974373.1471063336.1471063336.1472564550.2; __utmc=26781301; __utmz=26781301.1471063336.1.1.utmcsr=91porn.com|utmccn=(referral)|utmcmd=referral|utmcct=/v.php; CzG_auth=9fb1Tr7iRduDYbCxpHpFOUsaTUN7K%2BbWSDnPGNgk3k2Yike%2BabqV00nD5jDVR1FB8nECQtHUDl1ETpXDvgtD4qyFzlNl; CzG_sid=VxxPI1; CzG_fid17=1472567012; CzG_oldtopics=D209069D209124D209223D209157D204118D209567D206248D209474D209445D; smile=1D1; checkpm=1; CzG_visitedfid=17D19D33D21; CzG_onlineusernum=4247; AJSTAT_ok_pages=14; AJSTAT_ok_times=2",
           "Host":"91.t9h.club",
           "Upgrade-Insecure-Requests":1,
           "Accept-Language":"zh-CN,zh;q=0.8",
            }

rootUrl = "http://91.t9h.club/forumdisplay.php?fid=17"

session = requests.Session()


def ungzip(data):
    try:        # 尝试解压
        data = gzip.decompress(data)
    except:
        print("解压缩错误")
    return data

def openUrl(url):
    try:
        req = session.get(url,headers=headers)
        req = ungzip(req)
        webContent = BeautifulSoup(req.text,"lxml")
        print(req.text)
        # address = webContent.findAll("a",{"class":"previous-comment-page"})[0]
        # imgs = webContent.findAll("a",{"class":"view_img_link"})
        # return address['href'],imgs
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

openUrl(rootUrl)
# for x in imgs:
#     imgName,imgData = downLoadPic(x['href'])
#     savePic(imgData,imgName)
#
# while(nextUrl != ""):
#     nextUrl,imgs = openUrl(nextUrl)
#     for x in imgs:
#         imgName,imgData = downLoadPic(x['href'])
#         savePic(imgData,imgName)


