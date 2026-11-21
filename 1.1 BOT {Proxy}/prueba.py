#!/usr/bin/env python
#_*_ coding: utf8 _*_


import urllib.request
import json
from bs4 import BeautifulSoup

req = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?id=UCSTzojy6x8xj9yPv_eUjS9Q&key=AIzaSyAVB1kbiCc0jUxcTsDOwY--eYSejIL0bME&part=statistics')


req = json.loads(req.read())


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

followers = abs(int(req['items'][0]['statistics'].get('subscriberCount')))

print(f"YT Cegamer: {human_format(followers)}")


import requests
from requests.structures import CaseInsensitiveDict

url = "https://counts.live/twitch-follower-count/cegamer69"

headerstk = CaseInsensitiveDict()
headerstk["authority"] = "www.tiktok.com"
headerstk["cache-control"] = "max-age=0"
headerstk["upgrade-insecure-requests"] = "1"
headerstk["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.259"
headerstk["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headerstk["sec-fetch-site"] = "same-origin"
headerstk["sec-fetch-mode"] = "navigate"
headerstk["sec-fetch-user"] = "?1"
headerstk["sec-fetch-dest"] = "document"
headerstk["accept-language"] = "es-ES,es;q=0.9"
headerstk["cookie"] = "tt_webid_v2=6953698522756613637; tt_webid=6953698522756613637; tt_csrf_token=DTgssWbTe3RBww75nEsl2dUM; csrf_session_id=4e6567ce9d7a4dfc89356ffaf5c6afd3; s_v_web_id=verify_knrv3v3i_rGQAWrLM_FbEP_4N3v_AcIg_zXpLyR9P4NVB; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22version%22:%22v2%22}; MONITOR_WEB_ID=6953698522756613637; passport_csrf_token=d1125206c664911231c534e006536dca; passport_csrf_token_default=d1125206c664911231c534e006536dca; passport_auth_status=e2a637a8b8fba1b5b92071fe0f70b07e%2C; passport_auth_status_ss=e2a637a8b8fba1b5b92071fe0f70b07e%2C; store-idc=maliva; store-country-code=es; ttwid=1%7CUonCXIvO9UDMchd9mnndXwx_C1AGtwPM4Sibt3dV960%7C1619220996%7C15ec820ecee784c61e5f99bb6efae9f6ffe0b0cf8feefd90cc19bddd0e63f7e4; cmpl_token=IGNORE; sid_guard=837cd255570f34614821e08bbfb647f9%7C1619221025%7C5184000%7CTue%2C+22-Jun-2021+23%3A37%3A05+GMT; uid_tt=fb966c0a5a4fe030c675c5904dd9a44a92ad5fc604685594ada8d90154ce4d51; uid_tt_ss=fb966c0a5a4fe030c675c5904dd9a44a92ad5fc604685594ada8d90154ce4d51; sid_tt=837cd255570f34614821e08bbfb647f9; sessionid=837cd255570f34614821e08bbfb647f9; sessionid_ss=837cd255570f34614821e08bbfb647f9; odin_tt=7aa0fd553e167e9f6424a3554a818bf3190f6fba74bfd2e96e42e5e5be50698f77d5273a2f062fce95ea0aa2d7e19cb72c918ca7fb4b8029c37f6d6065dfcbbdc0782ac8ddefbdf9d04b1541e3d827f7; R6kq3TV7=ACL2ult5AQAA3wQGuO6QquuAlZ84iAASAck5dnjAazLROL9hken3GnwDkWjk|1|0|1ffb348b43121afeeaa7d6698ce3454fdccff991; bm_sz=BF52DCB88C0E26FEEAAFAA8D7AD7261D~YAAQja2O1Ad02Fd5AQAApQKaXAsjmmdPdWAEIWWBEfZW/3LW/y3cODjN/GU3PZ2ZsS2qzgZi/woQS6JCPnL5x791o2BIPdOTe1KDgbESqvm0K+Bd2/Toy20JG9UiHPibJyRaL3VgJG3CzaeesQuGqwsPD3V/UwsJm5dUpqW63RqkDnQQat+AWgJXPpAek/2p; _abck=433EEF3FB390FD5F849286B6B7600A99~0~YAAQja2O1Ah02Fd5AQAApQKaXAW7OLVKpzfcqoBptCCN0dUDxvLJ3UFmvBinQXofO47r+PgTNFbnaXea8IJ9LO036FzniXqhSIgx7OJMip9gxpeZX65bRmV5VCvCjA+nfFrKbRVjkRwmH8kJKySaCcV/JPJnrvU6SI9iDKDQI4z3e2++n2LUGOqrVfQA0pnSWrmunhvC6RnqrAbLF5HUf+MJ2/2xBwvG6I5nqiqbX+bu84UfKcIWt4Jka48V33OqaNKl+NlV1dEaCcC3G4gUFHUJ9pi4s/4GReoLvEJGCoVi7gjoWmEbzzZWO0F+kPboHdf3nr6li2sOH5oaAfb1EGKhYwjRYcttIU61V3YVfpBQvgv2ZZEEZxLqvkEXyFr4a/eOKGI=~-1~-1~-1; ak_bmsc=495BD7C29D5FCE22EACBA634AD278CE8D48EADBF8C65000040E79A60CD90F66C~plR70fws6+7feVIDSKxtyiqKJ+RQ1M9QkVmhLkALJYAxaGYnoQ4VlDd618u1L0KSxD58RNjI0V1a+AfdgIn6WwgCVEcQr3FMTTdC/Tt0wOZZxnw5ZR4cCubr+u7d0uM2yoDno4T7Tlq4n5YsdId0lS7cuvNmLff12L7aEBybdN6kdMETY9oU7WTPkH9Z8RIAKpyyOdGH5rtH9JdnTO0gwQnaUqzESPA9eBxNfcWmUYscM=; bm_sv=1BAACF48CAD6ED571C9B97BEEE5EDE82~nIsKyjhfVlIBYJPiU218m0AGvJiiTl0MvyMa93oi0bI+Gv/PlmIzcUgplvXjRhqXOsiFPSJpUFZKRZr/WU3NQJ53LZqWRAPQ6rArgP74sM+Xlwv+aaHgrSddYd1ZnNJchXzc050dCP3J+/2QHCp2tndOh02YTZCDhltfNcvIUII="


resp = requests.get(url, headers=headerstk)
soup = BeautifulSoup(resp.text, 'html5lib')

for x in soup.find('script', {"id": "__NEXT_DATA__"}):
    x = json.loads(x)

    followers = x['props']['pageProps']['rs']['live']['followers']

    print(followers)

