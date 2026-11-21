#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

game = input("Introduce el juego:> ")
game = game.replace(' ', '+')

url = f"https://getgamez.net/?s={game}&post_type=post"

headers = CaseInsensitiveDict()
headers["authority"] = "getgamez.net"
headers["cache-control"] = "max-age=0"
headers["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headers["sec-ch-ua-mobile"] = "?0"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-user"] = "?1"
headers["sec-fetch-dest"] = "document"
headers["referer"] = "https://getgamez.net/"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = 'quads_browser_width=1536; gt3-window-size={"width":1481,"height":762,"orientation":"landscape","ratio":"1.944"}'

headersg = CaseInsensitiveDict()
headersg["authority"] = "getgamez.net"
headersg["cache-control"] = "max-age=0"
headersg["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headersg["sec-ch-ua-mobile"] = "?0"
headersg["upgrade-insecure-requests"] = "1"
headersg["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headersg["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headersg["sec-fetch-site"] = "same-origin"
headersg["sec-fetch-mode"] = "navigate"
headersg["sec-fetch-user"] = "?1"
headersg["sec-fetch-dest"] = "document"
headersg["accept-language"] = "es-ES,es;q=0.9"
headersg["cookie"] = 'quads_browser_width=1536; quads_browser_width=1536; gt3-window-size={"width":1481,"height":762,"orientation":"landscape","ratio":"1.944"}'

resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html5lib')

for x in soup.find_all('span', class_='count main-color'):
    print(f"{x.get('data-total')} recursos encontrados")

for x in soup.find_all('span', class_='page-number'):
    pages = x.get_text()
    print(pages)

    pages = pages.split('of ')
    pages = pages[1]
    pages = pages.replace(" ", '')
    pages = int(pages)

print()
print()

p = 0

while p != pages:
    p += 1

    url = f"https://getgamez.net/page/{p}/?s={game}&post_type=post"

    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'html5lib')

    for x in soup.find_all('a', class_='thumb hover-effect'):

        for z in x.find_all('span'):
            print(z.get('aria-label'))

        link = x.get('href')

        print()


        respg = requests.get(link, headers=headersg)

        soupg = BeautifulSoup(respg.text, 'html5lib')

        print("System Requirements:")
        for x in soupg.find_all('ul'):
            if (
                x.get('id', [])
                not in [
                    'menu-main',
                    'menu-helpful-links',
                ]
                and 'sub-menu' not in x.get('class', [])
            ) and 'OS' in x.get_text():

                for z in x.find_all('li'):
                    print(z.get_text())
                break

        print()
        for x in soupg.find_all('a'):
            if x.get('target') == '_blank' and x.get_text() in [
                'Wait for Crack ⏱ Check Crack-Status',
                'FREE DOWNLOAD',
            ]:

                print(x.get('href'))

        print()
        print()
        print()
    
