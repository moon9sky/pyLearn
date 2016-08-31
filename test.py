import requests
from os.path import basename
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from urllib.request import urlopen

rootUrl = "http://91.t9h.club/forumdisplay.php?fid=17&filter=digest"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Cookie":"__cfduid=d128b406705c93694c4a8a6030b4529b81470453446; __utma=26781301.628974373.1471063336.1471063336.1472564550.2; __utmz=26781301.1471063336.1.1.utmcsr=91porn.com|utmccn=(referral)|utmcmd=referral|utmcct=/v.php; smile=1D1; CzG_sid=W676gF; CzG_cookietime=2592000; CzG_auth=a2a9lQdBFD35fd%2FOC%2F9Ehg6FHxp1V5ktUmwUM3%2BOskWI8uCuf78PYm05exY4bz%2FBlSVqLvibAMOWwoQLdvlIf2q2pUC0; CzG_visitedfid=17D4D19D33D21; AJSTAT_ok_pages=3; AJSTAT_ok_times=3",
           "Host":"91.t9h.club",
           "Upgrade-Insecure-Requests":1,
           "Accept-Language":"zh-CN,zh;q=0.8",
            }

session = requests.Session()
req = session.get(rootUrl,headers=headers)
webObj = BeautifulSoup(req.content.decode("utf-8"),"lxml")
table = webObj.find("table",{"summary":"forum_17"})
th = table.findAll("th",{"class":"subject"})
print(len(th))
all_href = []
for x in th:
    a = x.find("a")
    try:
        one_url = "http://91.t9h.club/"+a['href']
        all_href.append(one_url)
    except:
        print(11)
print(all_href)

def downLoadImg(url):
    try:
        file_name = basename(urlsplit(url)[2])
        print(file_name)
        imgData = session.get(url,headers=headers).content
        return imgData,file_name
    except:
        print("downLoad errr")

def savePic(img,name):
    try:
        output = open('./img/'+name,'wb')
        output.write(img)
        output.close()
    except Exception as e:
        print(e)

def openOnePage(url):
    req = session.get(url, headers=headers)
    webObj = BeautifulSoup(req.content.decode("utf-8"), "lxml")
    td = webObj.find("td", {"class": "t_msgfont"})
    if (td == None):
        print(td)
        return
    print(td)
    img_href = td.findAll("img")
    for x in img_href:
         if(x.has_attr("file")):
             img_url = "http://91.t9h.club/"+x['file']
             print(img_url)
             img_data,file_name = downLoadImg(img_url)
             savePic(img_data,file_name)

for i in all_href:
    openOnePage(i)