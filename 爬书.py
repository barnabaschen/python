import requests
from pyquery import PyQuery as pq

serve="https://www.ibiquge.net"
novel_link='https://www.ibiquge.net/23_23646/'


response = requests.get(novel_link)
response.encoding=response.apparent_encoding
doc = pq(response.text)
title1 = doc('#info > h1:nth-child(1)').text()
print(title1)
links = doc('dl>dd a ')

for link in links.items():
    print(serve+link.attr.href)

    response = requests.get(serve+link.attr.href)
    response.encoding = response.apparent_encoding
    # print(response.text)
    doc = pq(response.text)
    title = doc('.bookname > h1:nth-child(1)').text()
    content = doc('div#content').text()
    content = content.replace('天才一秒记住本站地址：[笔趣阁] https://www.ibiquge.net/最快更新！无广告！', '')
    content = content.replace(' ', '')
    content = content.replace('&nbsp;', '')

    with open('%s.txt'%title1,mode='a+',encoding='utf-8')as f:
       f.write(title)
       f.write('\n')
       f.write(content)
       f.write('\n')
       f.write('\n')

#




