import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


headers={'agent-user':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
os.makedirs('../../爬取成功/小说',exist_ok=True)
def get_content(url):
    r=requests.get(url,headers=headers,stream=True)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.text,'lxml')
    return [soup.find('div',class_='bookname').find('h1').string,soup.find('div',id='content').text]

if __name__=='__main__':
    serve='https://www.xbiquge.la/'
    url='https://www.xbiquge.la/13/13959/'
    r=requests.get(url,headers=headers,stream=True)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.text,'lxml')
    chapters = soup.find('div', id='list').find_all('a',limit=2)
    for chapter in tqdm(chapters):
        f=open('../../爬取成功/小说/圣墟.txt','a',encoding='utf-8')
        f.write(get_content(serve+chapter['href'])[0])
        f.write('\n')
        f.write(get_content(serve+chapter['href'])[1])
        f.write('\n')

