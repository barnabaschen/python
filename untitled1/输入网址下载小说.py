import requests
import re

#下载小说首页

novel_url='https://www.biquge.info/22_22533/'

response=requests.get(novel_url)
#处理字符编码
#乱码处理也可以用response.encoding=response.apparent_encoding
response.encoding='utf-8'
html=response.text
title=re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
#非贪婪匹配 .*？
#print(html)
fb=open('%s.txt'%title,'w',encoding='utf-8')

chapter_info_list=re.findall(r'''<a href="(.*?.html)" title="(.*?)">''',html)
for chapter_info in chapter_info_list:
    chapter_st=chapter_info[0]
    chapter_head=chapter_info[1]
    if 'http' not in chapter_st:
        chapter_url="https://www.biquge.info/22_22533/%s"%chapter_st
        response_chapter_url=requests.get(chapter_url)
        response_chapter_url.encoding=response.apparent_encoding
        # 下载章节页面
        chapter_page=response_chapter_url.text
        content = chapter_page
        res_url = r'<div id="content">(.*?)</div>'
        chapter_content = re.findall(res_url, content, re.I | re.S | re.M)[0]

        chapter_content = chapter_content.replace(' ', '')
        chapter_content = chapter_content.replace('&nbsp;', '')
        chapter_content = chapter_content.replace('<br/>', '')

        fb.write(chapter_head)
        fb.write('\n')
        fb.write(chapter_content)
        fb.write('\n')
        print(chapter_url)  # http://www.biquge.info/10_10237%s'%chapter_url






#数据写入
