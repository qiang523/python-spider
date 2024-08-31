import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from multiprocessing import Pool
import time
import math


def func(i):
    url="http://dh5.cntv.myalicdn.com/asp/h5e/hls/1200/0303000a/3/default/fb541bc36f704cf786f8d6d798af34e0/%d.ts"%i
    r=requests.get(url)
    ron=r.content
    with open("../../爬取成功/shipin.ts","wb") as f:
        f.write(ron)
if __name__=='__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    func(0)
    print("ok")