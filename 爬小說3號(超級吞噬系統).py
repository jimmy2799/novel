#小說狂人 超級吞噬系統

import requests
from bs4 import BeautifulSoup as bs
import os #路徑、資料夾操作
import random
import time

url = 'https:'
User_Agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Mobile Safari/537.36',]
request_headers = {'User-Agent':'random(User_Agent)'}

###取得原始碼並存檔
html = requests.get(url + '//czbooks.net/n/cpn569p', headers = request_headers)
#print (html.text)

###解析
soup = bs(html.content,'lxml')
date = []
datetag = soup.find('ul', class_ = "nav chapter-list")#過濾
for datetag2 in datetag.find_all('a'):#在過濾返回列表
    #print(datetag2)
    link = url + str(datetag2.get('href'))#取得網址
    #print(link)
    title = datetag2.get_text('herf') #取得標題
    #print(title)
    date.append(link)
    date.append(title)
#print(date)
#選章節處理(匹配索引位置)
def filelist():
    mypath = 'C:/Users/jimmy2799/Desktop/超級吞噬系統/'
    f = os.listdir(mypath)
    print(f)
    return f
shi = date.index(filelist()[-1].replace('.txt',''))#現有名稱位址
print('檔案章節位址:'+ str(shi))
print('最大章節位址:'+ str(len(date)))

###取章節內容源碼
for i in date[shi+1:2002:2]:#
    #print(i)
    content_link = requests.get(i, headers = request_headers)
    content_link.encoding = 'utf-8'
    #print(content_link.text)
    ###解析
    content = bs(content_link.text,'lxml')
    tag_h1 = content.find('div',class_="name")#標題
    title = tag_h1.text.replace('《超級吞噬系統》','')#拿來當檔名
    print('正在下載：'+ title)
    content1 = content.find('div',class_="content")#class是Python的保留字，所以Beautiful Soup改以class_
    #print(content1.text)
    #存入內容    
    f = open('C:/Users/jimmy2799/Desktop/超級吞噬系統/{}.txt'.format(title), mode ='w', encoding ='utf-8')
    f.write(content1.text+'\n'*2)
    f.close()
    time.sleep(1.1)
print('下載完成')
#input('Enter鍵離開')
'''
try:  
except Exception as e:
    print(e)
'''   
