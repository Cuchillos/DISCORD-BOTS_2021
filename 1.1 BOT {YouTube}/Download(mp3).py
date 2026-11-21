#!/usr/bin/env python
#_*_ coding: utf8 _*_

import json
import requests
from requests.structures import CaseInsensitiveDict

main = "https://yt1s.com/api/ajaxSearch/index"

headers = CaseInsensitiveDict()
headers["authority"] = "yt1s.com"
headers["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headers["accept"] = "*/*"
headers["x-requested-with"] = "XMLHttpRequest"
headers["sec-ch-ua-mobile"] = "?0"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headers["origin"] = "https://yt1s.com"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://yt1s.com/youtube-to-mp3/en12"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = "__atssc=google%3B1; __atuvc=2%7C26; __atuvs=60df517e5aac0dff001"

data = "q=https://www.youtube.com/watch?v=SEpLtkQrb3o&vt=mp3"
data = data.replace(':', '%3A').replace("/", '%2F')

resp = requests.post(main, headers=headers, data=data)

data = json.loads(resp.text)

vid = data['vid']
print(data)

a = 0
for x in data['links']['mp4']:
    if a == 0:
        num = x
        a +=1

k = data['links']['mp4'][num]['k']


last = "https://yt1s.com/api/ajaxConvert/convert"

headers = CaseInsensitiveDict()
headers["authority"] = "yt1s.com"
headers["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headers["accept"] = "*/*"
headers["x-requested-with"] = "XMLHttpRequest"
headers["sec-ch-ua-mobile"] = "?0"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headers["origin"] = "https://yt1s.com"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://yt1s.com/youtube-to-mp3/en12"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = "__atssc=google%3B1; __atuvc=2%7C26; __atuvs=60df517e5aac0dff001"

data = f"vid={vid}&k={k}"
data = data.replace("+", '%2B')

resp = requests.post(last, headers=headers, data=data)

data = json.loads(resp.text)

print(data['dlink'])