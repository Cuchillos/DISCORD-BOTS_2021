#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict

url = "https://forebears.io/es/surnames/perez"

headers = CaseInsensitiveDict()
headers["authority"] = "forebears.io"
headers["cache-control"] = "max-age=0"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "none"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-user"] = "?1"
headers["sec-fetch-dest"] = "document"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["if-none-match"] = '"60c0c0c8-387a"'
headers["if-modified-since"] = 'Wed, 09 Jun 2021 13:23:20 GMT'

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, 'html5lib')

for x in soup.find_all('h4', class_='desktop-only mt-2'):
    print("Definición:")
    print(x.next_sibling.get_text())

for x in soup.find_all('div', class_="statistic-number"):
    print(x.get_text() + " Más común apellido en el Mundo")

for x in soup.find_all('span', class_="accent"):
    print(f"Aproximadamente {x.get_text()} la gente que lleva este apellido")

for x in soup.find_all('div', class_="title"):
    if "La más frecuente en: " == x.get_text():
        print("La nación donde hay más gente con el apellido que cualquier otra: " + x.next_sibling.get_text())
    elif "La densidad más alta en: " == x.get_text():
        print("La nación donde el porcentaje de personas con este apellido es mayor: " + x.next_sibling.get_text())



url = "https://www.plusesmas.com/escudos/apellidos/?q=prieto"

headers = CaseInsensitiveDict()
headers["authority"] = "www.plusesmas.com"
headers["cache-control"] = "max-age=0"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "none"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-user"] = "?1"
headers["sec-fetch-dest"] = "document"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = "overlayerPubli=1; cX_S=kqfb98cfqpsvz86q; cX_P=kqfb98cgyy779jr1"


resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html5lib')


for x in soup.find_all('p', class_="text-center"):
    print(x.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text())


for x in soup.find_all('p', class_="text-center"):
    for i in x.find_all('img', class_="img-fluid"):
        print(i.get('src'))

