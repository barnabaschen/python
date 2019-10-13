import requests
import re

#下载小说首页

novel_url='https://www.biquge.info/10_10582/'
response=requests.get(novel_url)
#处理字符编码
#乱码处理也可以用response.encoding=response.apparent_encoding
response.encoding='utf-8'
html=response.text
title=re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
#非贪婪匹配 .*？
#print(html)
content=html
res_url=r'<div id="list">(.*?)</dl>'
link = re.findall(res_url, content, re.I | re.S | re.M)[0]
#print(link)
chapter_info_list=re.findall(r'<a href="(.*?.html)" title="(.*?")>',link)
#数据写入

fb=open('%s.txt'%title,'w',encoding='utf-8')


for chapter_info in chapter_info_list:
    chapter_st=chapter_info[0]
    chapter_head=chapter_info[1]

    if 'http' not in chapter_st:
        chapter_url='https://www.biquge.info/10_10582/%s'%chapter_st
        print(chapter_url)
        # 下载章节页面                                                  #http://www.biquge.info/10_10237%s'%chapter_url
        chapter_response = requests.get(chapter_url)
        chapter_response.encoding = 'utf-8'
        chapter_html = chapter_response.text

        content = chapter_html
        res_url = r'<div id="content">(.*?)</div>'
        chapter_content = re.findall(res_url, content, re.I | re.S | re.M)[0]
        # 清洗数据

        chapter_content = chapter_content.replace(' ', '')
        chapter_content = chapter_content.replace('&nbsp;', '')
        chapter_content = chapter_content.replace('<br/>', '')

        fb.write(chapter_head)
        fb.write('\n')
        fb.write(chapter_content)
        fb.write('\n')


    # print(chapter_info_list)
    # chapter_info_list=r'<dd>(.*?)" title="(.*?)"</a></dd>'


link=('https://www.biquge.info/0_383/'+link.attr.href)
    response=requests.get(link)
    response.encoding=response.apparent_encoding
#print(response.text)
    doc=pq(response.text)
    title=doc('.bookname > h1:nth-child(1)').text()
    content=doc('#content').text()


    with open("title1.txt",mode='a+',encoding='utf-8')as f:
       f.write(title)
       f.write('\n')
       f.write(content)
       f.write('\n')

target = 'https://www.ibiquge.net/0_79/184944.html'
response = requests.get(target)
response.encoding = response.apparent_encoding
html = response.text
bf = BeautifulSoup(html)
texts = bf.find_all('div', id='content')
print(texts[0].text.replace('\xa0' * 8, '\n\n'))

#









