import requests
from bs4 import BeautifulSoup
import os
from contextlib import closing

headers={'agent-user':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
f=open(os.path.join('..','爬取成功','漫画','001.jpg'),'wb')
do={'Referer':'https://www.dmzj.com/view/yaoshenji/41917.html'}
def get_content(url):
    r=requests.get(serve,headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    with closing(requests.get(url, headers=do, stream=True)) as response:
        chunk_size = 1024
        f.write(response.iter_content(chunk_size=chunk_size))



if __name__=='__main__':
    serve='https://www.dmzj.com/info/yaoshenji.html'
    r=requests.get(serve,headers=headers)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.text,'lxml')
    contents=soup.find('div',class_='tab-content zj_list_con autoHeight').find_all('a')
    for content in contents[0:1]:
        url=content['href']
        chapter=content.find('span', class_='list_con_zj').text
        picture=get_content(url)

