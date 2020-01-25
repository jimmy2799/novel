import os
def filelist():
    mypath = 'C:/Users/jimmy2799/Desktop/超級吞噬系統/'
    f = os.listdir(mypath)
    print(f)
    return f
    
for file_ in filelist():
    with open('C:/Users/jimmy2799/Desktop/超級吞噬系統/'+file_, "r+", encoding ='utf-8') as f:
        read_data = f.read()
        f.seek(0, 0)#讀寫偏移位置移到首行  
        f.write(read_data.replace('\n'*3,'\n'*2))
        f.truncate(f.tell())#truncate游標後斷點不要  #tell遊標位子