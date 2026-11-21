#!/usr/bin/env python
#_*_ coding: utf8 _*_


import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438'}

req = requests.get('https://cursosdev.com/coupons', headers=header)
soup = BeautifulSoup(req.text, 'html5lib')

for line in soup.find_all('a', class_='c-card block bg-white shadow-md hover:shadow-xl rounded-lg overflow-hidden'):
    links = line.get('href')

req = requests.get(links, headers=header)
soup = BeautifulSoup(req.text, 'html5lib')

for lines in soup.find_all('h2', class_="text-3xl text-gray-800 font-bold mr-auto"):
    name = lines.get_text()
    name = name.replace("""[100% DESCT.°]
                                        """, '').replace("""
""", '')
    print(name)

for lines in soup.find_all('a'):
    if 'Aplicar' in lines.get_text():
        print(lines.get('href'))

for lines in soup.findAll('meta', {'name':'description'}):
    print(lines.get('content'))


for lines in soup.find_all('meta', property='og:image'):
    print(lines.get('content'))