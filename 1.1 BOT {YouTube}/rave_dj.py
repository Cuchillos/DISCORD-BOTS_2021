#!/usr/bin/env python
#_*_ coding: utf8 _*_

import json
import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.red.wemesh.ca/ravedj/dj/self/content"

headers = CaseInsensitiveDict()
headers["authority"] = "api.red.wemesh.ca"
headers["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headers["wemesh-platform"] = "Android"
headers["sec-ch-ua-mobile"] = "?0"
headers["client-version"] = "5.0"
headers["authorization"] = "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc3MTBiMDE3ZmQ5YjcxMWUwMDljNmMzNmIwNzNiOGE2N2NiNjgyMTEiLCJ0eXAiOiJKV1QifQ.eyJwcm92aWRlcl9pZCI6ImFub255bW91cyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS93ZW1lc2gtaW5jIiwiYXVkIjoid2VtZXNoLWluYyIsImF1dGhfdGltZSI6MTYyNjY1NTc4NCwidXNlcl9pZCI6ImFaZVgxeGpTcE1Vd0FxRjM3bkVVdk54NDNYZTIiLCJzdWIiOiJhWmVYMXhqU3BNVXdBcUYzN25FVXZOeDQzWGUyIiwiaWF0IjoxNjI2NjU1Nzg0LCJleHAiOjE2MjY2NTkzODQsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiYW5vbnltb3VzIn19.ZLe7HBzrWvrTA35i4V5zHgTKqkIDxAcdfjHG815Qp27bglojlNFJzCNffvzFxs7HhtL8MFSWXK6V_0caqCShs7KJlrWNBkM_NooJQqQiWvt7PLqtlpGyBdNdKDRrM44GjZsT8_FWPMm1l4Kbj_MFTk77UM9aoyOytjhQow4eOlHLdSBjkAD9JsnOpzbep27tluQ90Xw6Rl3IcOl81Gtp0z8T1K4WryjJU6B7R8e5LQ_zCJ1LFNQJG-SJSPE3lFUkV9rgH65TG5jCmV0Jz2w3mZFgwWRgjez_gsv1iZl_PafCRt98Da7L9i8woADlLdrF5mMcJt0UpU2DRhK1xF3-uA"
headers["content-type"] = "application/json"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.227"
headers["wemesh-api-version"] = "5.0"
headers["accept"] = "*/*"
headers["origin"] = "https://rave.dj"
headers["sec-fetch-site"] = "cross-site"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://rave.dj/"
headers["accept-language"] = "es-ES,es;q=0.9"

data = '{"style":"MASHUP","title":null,"media":[{"providerId":"QLz9VaksClg","provider":"YOUTUBE"},{"providerId":"tbneQDc2H3I","provider":"YOUTUBE"}]}'


resp = requests.post(url, headers=headers, data=data)

json = json.loads(resp.text)

print(json['data']['urls']['default'])