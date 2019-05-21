#小說園改17K 修羅武神

import requests
from bs4 import BeautifulSoup as bs
import os #路徑、資料夾操作

url = 'http://www.17k.com'
request_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

###取得原始碼並存檔
url2 = requests.get(url + '/list/493239.html', headers = request_headers)
#url2.encoding = 'gbk' #需要時才使用
#print (url2.text)
index_file = open(r'D:/Users/Python範例/index.txt' ,'wb') #r或R表示該字符串是非轉義的原始字符串
                                                          #u或U表示該字符串是unicode字符串
index_file.write(url2.content)
index_file.close()

###開啟檔案用with as 可以確定關閉檔案。
with open('D:/Users/Python範例/index.txt', mode ='r', encoding ='utf-8') as f:
    date = f.read()
    #print(date)
###解析
soup = bs(date,'lxml')
for tag in soup.find_all('dd'): #上一層
    for tag in tag.find_all('a'): #下一層
        #print(tag)
        if tag.get('title') :#過濾多餘內容用
            link = url + str(tag.get('href'))+ ',' #取得網址
            #print(link)
            title = tag.get_text('herf') + ',' #取得標題
            title = title.replace('herf','').replace(' ','').replace('\n','').replace('\t','')#replace() 取代。去除不要的字串
            #print(title)
            ###資料存檔
            linkfile = open(r'D:/Users/Python範例/link_title.txt' , mode = 'a', encoding = 'utf-8')
            #print(linkfile) #開啟檔案'前後'可以先確認讀取編碼。
            linkfile.write(link)
            linkfile.write(title)
            linkfile.close()

###下一步取要的部分        
with open('D:/Users/Python範例/link_title.txt', mode = 'r', encoding = 'utf-8') as g:
    date = g.read().split(',')#字串分段，返回一個列表
    date = date[18:-25:1]#取得我要的部分,[18:-25:1]去青天玄外傳
    #print(date)

#選章節處理(匹配索引位置)
def filelist():
    mypath = 'C:/Users/jimmy2799/Desktop/修羅3496/'
    f = os.listdir(mypath)
    #print(f)
    return f
shi = date.index(filelist()[-2].replace('.txt',''))+1#現有名稱位址+1 無法找出最後一個中文數字檔案
print(shi)

###取章節內容源碼
count = 0
for i in date[shi::2]:#6840 對應3719章
    #print(i)
    content_link = requests.get(i, headers = request_headers)
    #print(content_link.text)
    count += 1
    linkfile = open(r'D:/Users/Python範例/content_code{}.txt'.format(count), mode = 'wb')
    #print(linkfile) 
    linkfile.write(content_link.content)
    linkfile.close()
    
    ###解析
    with open('D:/Users/Python範例/content_code{}.txt'.format(count), mode ='r', encoding ='utf-8') as f:
        date = f.read()
    content = bs(date,'lxml')
    tag_h1 = content.find('h1')#標題
    title = tag_h1.text.replace(' ','').replace('\n','')#拿來當檔名
    #print(title)
    content1 = content.get_text('div').replace('\u3000',' ')
    content2 = str(content1.split('div')[196:-403])#想不到怎麼過濾，所以去頭去尾取中間 415>>403
    content3 = content2.replace("'",'')
    #print(type(content2))
    #存入內容    
    f = open('C:/Users/jimmy2799/Desktop/修羅3496/{}.txt'.format(title), mode ='w', encoding ='utf-8')
    f.write(content3)
    f.close()
    #最後刪除不要的檔案
    os.remove('D:/Users/Python範例/content_code{}.txt'.format(count))    
os.remove('D:/Users/Python範例/link_title.txt')

print('下載完成')
input('任意鍵離開')

'''
try:  
except Exception as e:
    print(e)
'''   
