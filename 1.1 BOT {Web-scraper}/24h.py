#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import time
from datetime import datetime


while True:
    try:
        r = requests.get('https://sdjnbnoasjdpasocjasdui7656a54sd86anaihiscr4aper.chchillo.repl.co', timeout=5)

        if r.status_code != 200:
            now = datetime.now()
            ahora = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('Registro(Web-Scraper).txt','+a', encoding="utf-8") as x:
                x.write(f"[{ahora}] 》BOT OFFLINE\n\n")
        else:
            now = datetime.now()
            ahora = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('Registro(Web-Scraper).txt','+a', encoding="utf-8") as x:
                x.write(f"[{ahora}] 》BOT ONLINE\n")

        time.sleep(30)
    except:
        now = datetime.now()
        ahora = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('Registro(Web-Scraper).txt','+a', encoding="utf-8") as x:
            x.write(f"[{ahora}] 》ERROR NO SE HA PODIDO CONECTAR\n")
        time.sleep(30)
        pass

    try:
        r = requests.get('https://lsdhfiulahshyaspidfyasuidfyiasdu8fyiasudyfiawgbeirbveihack3r.chchillo.repl.co', timeout=5)

        if r.status_code != 200:
            now = datetime.now()
            ahora = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('Registro(HACK3R).txt','+a', encoding="utf-8") as x:
                x.write(f"[{ahora}] 》BOT OFFLINE\n\n")
        else:
            now = datetime.now()
            ahora = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('Registro(HACK3R).txt','+a', encoding="utf-8") as x:
                x.write(f"[{ahora}] 》BOT ONLINE\n")

        time.sleep(30)
    except:
        now = datetime.now()
        ahora = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('Registro(HACK3R).txt','+a', encoding="utf-8") as x:
            x.write(f"[{ahora}] 》ERROR NO SE HA PODIDO CONECTAR\n")
        time.sleep(30)
        pass

    try:
        r = requests.get('https://lsdhfiulahshyaspidfyasuidfyiasdu8fyiasudyfiawgbeirbveihack3r.chchillo.repl.co', timeout=5)

        if r.status_code != 200:
            pass
        else:
            pass

        time.sleep(30)
    except:
        pass
        time.sleep(30)
        pass

