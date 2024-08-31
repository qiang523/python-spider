import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
import time

headers={'agent-user':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
os.makedirs('../../爬取成功/小说',exist_ok=True)


def get_soup(url):
    r=requests.get(url,headers=headers,stream=True)
    r.encoding='gbk'
    soup=BeautifulSoup(r.text,'lxml')
    return soup
def get_content(chapter_link,chapter_name):
    soup=get_soup(chapter_link)
    content=soup.find('div',class_='novel_content').text
    chapter_name=chapter_name
    f=open(f'../../爬取成功/小说/{chapter_name}.txt','a',encoding='utf-8')
    f.write(chapter_name)
    f.write(content)

# def func(z):
#      return get_content1(z[0],z[1])
#
# def get_content1(x,y):
#     return get_content(x,y)

if __name__=='__main__':

    sever='http://www.quanben.co/files/article/html/0/5/index.html'
    four_chapters=get_soup(sever).find_all('div',class_='novel_list',limit=2)
    chapters_infos=[]
    for chapters in four_chapters:
        for chapter in chapters.find_all('a'):
            chapter_link = sever[:-10] + chapter['href']
            chapters_infos.append((chapter_link,chapter.string))

    # pool=Pool(4)
    # for i in chapters_infos:
    #     pool.apply_async(get_content(i[0],i[1]))
    with ProcessPoolExecutor() as pool:
        pool.map(get_content,chapters_infos)
    t_end = time.time()
    # print(t_start-t_end)

