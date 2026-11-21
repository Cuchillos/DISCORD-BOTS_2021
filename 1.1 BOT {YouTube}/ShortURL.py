#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://bitly.com/data/anon_shorten"

headers = CaseInsensitiveDict()
headers["authority"] = "bitly.com"
headers["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headers["accept"] = "application/json, text/javascript, */*; q=0.01"
headers["x-xsrftoken"] = "1d87896122914167a4c27b18f9068531"
headers["x-requested-with"] = "XMLHttpRequest"
headers["sec-ch-ua-mobile"] = "?0"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headers["origin"] = "https://bitly.com"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://bitly.com/"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = "_xsrf=1d87896122914167a4c27b18f9068531; anon_u=cHN1X180NDI1ZWM4NS02OGE1LTQzNDMtYWM2My0zNGZhYjQxYjRjZmM=|1625330160|5315dbbdc10f6b07118fba0d030500a03b6ad770; _ga=GA1.2.1295377962.1625330147; _gid=GA1.2.397730991.1625330147; cookie_banner=1; anon_shortlinks=https://bit.ly/3hgQfwq"

data = "url=https%3A%2F%2Fwww.twitch.tv%2Fthegrefg"


resp = requests.post(url, headers=headers, data=data)

text = json.loads(resp.text)

print(text['data']['link'])