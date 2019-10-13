#-*- coding:UTF-8 -*
from bs4 import BeautifulSoup
import requests, sys
"""
类说明：下载《笔趣阁》网小说 一念永恒
Parameter:
无
Returns:
无
Modify
2019-10-07
"""
class downloader(object):
    def __init__(self):
        self.server='https://www.ibiquge.net/'
        self.target='https://www.ibiquge.net/0_79/'
        self.name=[]#存章节名字
        self.urls=[]#存放章节链接
        self.nums=0#章节数

    def get__download_url(self):
        response=requests.get(url=self.target)
        response.encoding = response.apparent_encoding
        html = response.text
        print(html)
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', id='list')
        a_bf=BeautifulSoup(str(div[0]))
        print(a_bf)
        a=a_bf.find_all('a')
        print(a)
        self.nums=len(a[15:])
        print(self.nums)

        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server+each.get('href'))
            print(self.server+each.get('href'))
"""
获取章节内容
Parameter
target-下载连接（string）
Return
text--章节内容（string）
Modify
20191007      
"""
def get_contents(self,target):
       req = requests.get(url=target)
       html = req.text
       bf = BeautifulSoup(html)
       texts = bf.find_all('div', class_='showtxt')
       texts = texts[0].text.replace('\xa0' * 8, '\n\n')
       return texts
"""
函数说明:将爬取的文章内容写入文件
Parameters: name - 章节名称(string)
path - 当前路径下,小说保存名称(string)
text - 章节内容(string)
Returns:   
无        
Modify:
20191007
"""
def writer(self, name, path, text):
       write_flag = True
       with open(path, 'a', encoding='utf-8') as f:
           f.write(name + '\n')
           f.writelines(text)
           f.write('\n\n')

if __name__ == "__main__":
    dl=downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
         dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
         sys.stdout.write("已下载:%.3f%%"% float(i/dl.nums) + '\r')
sys.stdout.flush()
print('《一年永恒》下载完成')



