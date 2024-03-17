import requests
from bs4 import BeautifulSoup as bs

import numpy as np

# arr=[]
URL = ['https://www.babycheramy.lk/',
        'https://www.babycheramy.lk/getting-pregnant',
        'https://www.babycheramy.lk/pregnancy-week-by-week',
        'https://www.babycheramy.lk/baby-development-stages',
        'https://www.babycheramy.lk/toddler',
        'https://www.babycheramy.lk/preschooler',
        'https://www.babycheramy.lk/products',
        'https://www.babycheramy.lk/parenting-guide'
        ]


def url():
    
    results=[]
    for url in range(0,8):
        req = requests.get(URL[url])
        soup = bs(req.text, 'html.parser')

        for link in soup.find_all('a'):
    
            results.append(link.get('href'))
    results = list(set(results))
            
            
    print(results)
    print('\n')

def text():         
     print('imagess')

def image():
   
  

    for url in range(0,8):
        req = requests.get(URL[url])
        soup = bs(req.text, 'html.parser')

        images = soup.find_all('img')
        print(images)

        element = soup.select('.artical-image')    
        print(element)



url()
text()
image()