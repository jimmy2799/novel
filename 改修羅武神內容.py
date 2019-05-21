#改修羅武神文字檔 換行
import os

def filelist():
    mypath = 'C:/Users/jimmy2799/Desktop/修羅3496/'
    f = os.listdir(mypath)
    return f

for name in filelist():
    with open('C:/Users/jimmy2799/Desktop/修羅3496/{}'.format(name), mode ='r', encoding ='utf-8') as f:
        date = f.read().replace('\n','').split(',')
    f = open('C:/Users/jimmy2799/Desktop/修羅3496/{}'.format(name), mode ='w', encoding ='utf-8')
    for i in date:
        f.write(i+'\n')
        print(i)
    f.close()
