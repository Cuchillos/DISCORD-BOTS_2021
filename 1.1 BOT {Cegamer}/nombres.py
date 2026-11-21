#!/usr/bin/env python
#_*_ coding: utf8 _*_


from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict

url = "https://forebears.io/es/surnames/prieto"

headers = CaseInsensitiveDict()
headers["authority"] = "forebears.io"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.267"
headers["cache-control"] = "max-age=0"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-dest"] = "document"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["accept-encoding"] = "gzip, deflate, br"
headers["x-requested-with"] = "XMLHttpRequest"



resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html5lib')


for x in soup.find_all('h4', {'class': 'desktop-only mt-2 mb-4'}):
    definicion = x.next_sibling.get_text()

    print(definicion)

for x in soup.find_all('tr'):
    if x.get('data-pid'):
        try:
            p = x.next_sibling
            p = p.next_sibling
            pais = p.next_sibling
            
            porcentaje = pais.next_sibling

            print(porcentaje.get_text())
        except:
            pass