'''
Real-World Example: MultiThreading for I/O-bound tasks
Scenario: Web Scraping
Web Scraping oftnen involves making numerous netwerk requests to fetch web pages.
These tasks are I/O bound because they spend a lot of time wating for responess from
servers. 
MultiThreading can signinficantly improve the performnace by allowing multiple web pages to be
fetched concurrently.
'''


'''
https://docs.langchain.com/oss/python/langchain/overview

https://docs.langchain.com/oss/python/langchain/agents

https://docs.langchain.com/oss/python/langchain/tools

'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://docs.langchain.com/oss/python/langchain/overview',

    'https://docs.langchain.com/oss/python/langchain/agents',

    'https://docs.langchain.com/oss/python/langchain/tools'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {(len(soup.text))} characters form {url}')



threads=[]

for url in urls:
    t=threading.Thread(target=fetch_content,args=(url,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

print('All web page fetched') 