#!/usr/bin/env python
#_*_ coding: utf8 _*_

import json
import requests
from requests.structures import CaseInsensitiveDict

url = "https://counts.live/api/tiktok-follower-count/cegamer_yt/live"

headers = CaseInsensitiveDict()
headers["authority"] = "counts.live"
headers["cache-control"] = "max-age=0"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.259"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "none"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-user"] = "?1"
headers["sec-fetch-dest"] = "document"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = "ezCMPCCS=false; ezds=ffid%3D1%2Cw%3D1536%2Ch%3D864; ezohw=w%3D1495%2Ch%3D762; ezoadgid_207814=-1; ezoref_207814=; ezoab_207814=mod1; ezepvv=28; ezovid_207814=1664995538; ezovuuid_207814=dbb3e490-b8df-4f83-6f2d-980016ae7e89; active_template::207814=pub_site.1621178030; ezopvc_207814=3; ezovuuidtime_207814=1621178030"
headers["if-none-match"] = 'W/"a7-K6HrM4vQ0GKucBHt4IxyuljvVow-gzip"'


resp = requests.get(url, headers=headers)

resp = json.loads(resp.text)

print(resp['data']['followers'])
