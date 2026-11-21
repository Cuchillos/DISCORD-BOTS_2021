#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup
import json
import mechanize
from requests.structures import CaseInsensitiveDict

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])




urlyt = "https://socialcounts.org/youtube-live-subscriber-count/UCSTzojy6x8xj9yPv_eUjS9Q"

headersyt = CaseInsensitiveDict()
headersyt["authority"] = "socialcounts.org"
headersyt["cache-control"] = "max-age=0"
headersyt["sec-ch-ua"] = '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"'
headersyt["sec-ch-ua-mobile"] = "?0"
headersyt["sec-ch-ua-platform"] = '"Windows"'
headersyt["upgrade-insecure-requests"] = "1"
headersyt["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"
headersyt["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headersyt["sec-fetch-site"] = "same-origin"
headersyt["sec-fetch-mode"] = "navigate"
headersyt["sec-fetch-user"] = "?1"
headersyt["sec-fetch-dest"] = "document"
headersyt["referer"] = "https://socialcounts.org/youtube-live-subscriber-count"
headersyt["accept-language"] = "es-ES,es;q=0.9"
headersyt["cookie"] = "__gads=ID=e70a06536d8fe400-227205b7e4ce00d8:T=1641695407:RT=1641695407:S=ALNI_MaovNjHM-Goep4Kv4LCa66c830M5g; __cf_bm=vU5rMP.RlwwXoOdEt_5zlQ7A1gSocT1b7ZcaGizBp24-1641695409-0-AQXB5yJrF6s/8HREFk6d58KCxIwpPkDjS5JYgimeU9fcKg46dZb2ioXfS6xekqY1LmKssvmhzKh+NtvwQzF1W6uJsSmEtevtHBUv+wbTpqDHDRNTBLC3ZESYagptg7396w=="

respyt = requests.get(urlyt, headers=headersyt)
soupyt = BeautifulSoup(respyt.text, 'html5lib')

for x in soupyt.find_all('p', class_='text-break'):
    subsyt = x.previous_sibling.text
    subsyt = subsyt.split(' ')[4]
    subsyt = int(subsyt)
    print(f"YouTube: {human_format(subsyt)}")




bustw = mechanize.Browser()
bustw.set_handle_robots(False)
bustw.set_handle_equiv(False)
bustw.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50')]
bustw.open("https://socialblade.com/twitch/user/cegamer69/realtime")

souptw = BeautifulSoup(bustw.response().read(), 'html5lib')
for x in souptw.find_all('p', id='rawCount'):
    tw = int(x.text)
    print(f"Twitch: {human_format(tw)}")


bustk = mechanize.Browser()
bustk.set_handle_robots(False)
bustk.set_handle_equiv(False)   
bustk.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50')]
bustk.open("https://www.tiktok.com/@cegamer.yt")

souptk = BeautifulSoup(bustk.response().read(), 'html5lib')
for x in souptk.find_all('strong'):
    if x.get('title') == "Followers":
        tk = x.text
        print(f"TikTok: {tk}")

