#!/usr/bin/env python
#_*_ coding: utf8 _*_

import json
import requests
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict



urltw = "https://counts.live/instagram-follower-count/oier.cuchillos"

headerstw = CaseInsensitiveDict()
headerstw["authority"] = "counts.live"
headerstw["cache-control"] = "max-age=0"
headerstw["upgrade-insecure-requests"] = "1"
headerstw["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.259"
headerstw["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headerstw["sec-fetch-site"] = "same-origin"
headerstw["sec-fetch-mode"] = "navigate"
headerstw["sec-fetch-user"] = "?1"
headerstw["sec-fetch-dest"] = "document"
headerstw["accept-language"] = "es-ES,es;q=0.9"
headerstw["cookie"] = "ezoadgid_207814=-1; ezoref_207814=google.com; ezoab_207814=mod11-c; ezepvv=0; ezovid_207814=1422350798; lp_207814=https://counts.live/twitch-follower-count; ezovuuid_207814=8e82dbad-cbe4-4f33-68f3-11b2d2807d1f; ezCMPCCS=false; ezds=ffid^%^3D1^%^2Cw^%^3D1536^%^2Ch^%^3D864; ezohw=w^%^3D1495^%^2Ch^%^3D762; active_template::207814=pub_site.1620682790; ezopvc_207814=4; ezovuuidtime_207814=1620682790"

resptw = requests.get(urltw, headers=headerstw)
souptw = BeautifulSoup(resptw.text, 'html5lib')

for x in souptw.find('script', {"id": "__NEXT_DATA__"}):
    x = json.loads(x)

    followers = x['props']['pageProps']['rs']['live']['followers']

    print(f"Instagram: {followers}")