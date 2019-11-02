#小說園改17K 修羅武神

import requests
from bs4 import BeautifulSoup as bs
import os #路徑、資料夾操作
import random
import time

url = 'http://www.17k.com'
User_Agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Mobile Safari/537.36',]
request_headers = {'User-Agent':'random(User_Agent)'}

###取得原始碼並存檔
html = requests.get(url + '/list/493239.html', headers = request_headers)
#print (html.text)
'''
index_file = open(r'D:/Users/Python範例/index.txt' ,'wb') #r或R表示該字符串是非轉義的原始字符串
                                                          #u或U表示該字符串是unicode字符串
index_file.write(html.content)
index_file.close()
###開啟檔案用with as 可以確定關閉檔案。
with open('D:/Users/Python範例/index.txt', mode ='r', encoding ='utf-8') as f:
    date = f.read()
    #print(date)
'''
###解析
soup = bs(html.content,'lxml')
date = []
for tag in soup.select('dd a'):
    #print(tag)
    if tag.get('title') :#過濾多餘內容用
        link = url + str(tag.get('href')) #取得網址
        #print(link)
        title = tag.get_text('herf') #取得標題
        title = title.replace('herf','').replace(' ','').replace('\n','').replace('\t','')#replace() 取代。去除不要的字串
        #print(title)
        date.append(link)
        date.append(title)
#print(date)
date = date[28:-24:1]#取得我要的部分,[28:-24:1]去青天玄外傳
'''
###資料存檔_檢查前後章節和網址
linkfile = open(r'D:/Users/Python範例/link_title.txt' , mode = 'a',encoding = 'utf-8')
#print(linkfile) #開啟檔案'前後'可以先確認讀取編碼。
linkfile.writelines(date)
linkfile.close()
'''
#選章節處理(匹配索引位置)
def filelist():
    mypath = 'C:/Users/jimmy2799/Desktop/修羅武神/'
    f = os.listdir(mypath)
    print(f)
    return f
shi = date.index(filelist()[-1].replace('.txt',''))+1#現有名稱位址+1
print('檔案章節:'+ str(shi))
print('最大章節:'+ str(len(date)))
###取章節內容源碼
for i in date[shi::2]:#8304=4150章 8282=4139章
    #print(i)
    content_link = requests.get(i, headers = request_headers)
    content_link.encoding = 'utf-8'
    #print(content_link.text)
    ###解析
    content = bs(content_link.text,'lxml')
    tag_h1 = content.find('h1')#標題
    title = tag_h1.text.replace(' ','').replace('\n','')#拿來當檔名
    print('正在下載：'+ title)
    content1 = content.find('div',class_="readAreaBox content")#class是Python的保留字，所以Beautiful Soup改以class_
    #print(content1.text[:-70])
    '''
    content1 = content.get_text('x')#'get_text'取代html標籤
    content2 = content1.split('div')[200:-605]#想不到怎麼過濾，所以去頭去尾取中間 415>>403
    content3 = [x for x in content2 if x !='\n']#去掉多於物件
    '''
    #存入內容    
    f = open('C:/Users/jimmy2799/Desktop/修羅武神/{}.txt'.format(title), mode ='w', encoding ='utf-8')
    f.write(content1.text[:-70])
    f.close()
    time.sleep(1.1)
print('下載完成')
#input('Enter鍵離開')
'''
try:  
except Exception as e:
    print(e)
'''   
