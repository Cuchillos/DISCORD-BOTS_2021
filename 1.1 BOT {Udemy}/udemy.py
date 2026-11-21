#!/usr/bin/env python
#_*_ coding: utf8 _*_

####################################
import discord
from discord.ext import commands, tasks

import requests
from bs4 import BeautifulSoup
####################################

client = commands.Bot(command_prefix='!', help_command=None)
token = "YOUR_BOT_TOKEN_HERE"

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438'}
coockies1 = {'cookie':'__cfduid=dc60c771298f3185c45f38b23f3a6a47b1619785741; mtsnb_lastvisited=1619785744; wps_cookie_1588200093345=1; PHPSESSID=7feef57064180b41287d75b6acfb05ae; mtsnb_lastvisit_posts=%5B8%2C11%5D'}
coockies2 = {'cookie':'yandexuid=8513889701618773560; yuidss=8513889701618773560; yabs-sid=758279871618773560; i=AOydWrD5ULCnnawd0GlVA+T3P3WEWVWiI45vYWLujS7xS6NqLUNiRd6LiJpm8ILjcRifYrOlVK+P1OWYMFII8EoNhfs=; ymex=1650309560.yrts.1618773560#1650309560.yrtsi.1618773560'}

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="cursos", url="https://www.twitch.tv/cuchillop"))
    udemy.start()
    print("Estoy listo B)")


@tasks.loop(seconds=300)
async def udemy():
    cupones = []

    req = requests.get('https://www.onlinecourses.ooo/', headers=header, cookies=coockies1)
    soup = BeautifulSoup(req.text, 'html5lib')

    for curso in soup.find_all('a', rel='bookmark'):
        cursos = curso.get('title')
        cursos = cursos.replace('View the "', '').replace('" coupon page', '')
        link = curso.get('href')

        if cursos in cupones:
            pass
        else:
            cupones.append(cursos)

            req = requests.get(link, headers=header, cookies=coockies1)
            soup = BeautifulSoup(req.text, 'html5lib')

            n = 0
            for linea in soup.find_all('meta', property="og:image"):
                if n == 0:
                    imagen = linea.get('content')
                    n +=1
                else:
                    pass

            p = 0
            for lineas in soup.find_all('div', class_='text-box'):
                for lineass in lineas.find_all('p'):
                    if p == 0:
                        p +=1
                        pass
                    else:
                        descripcion = lineass.get_text()
            
            for line in soup.find_all('a', class_='coupon-code-link'):
                final = line.get('href')
                
            
            embed = discord.Embed(
                title = cursos,
                description = "Detalles",
                color = discord.Color.random()
            )
            embed.set_thumbnail(url=imagen)
            embed.add_field(name="Descripción:", value=descripcion, inline=False)
            embed.add_field(name="Curso:", value=final, inline=False)
            embed.add_field(name="Corre que se termina pronto la oferta!!", value='\u200b', inline=False)
            embed.set_footer(text="👨‍💻Dale gracias a cuchillo#7116‍‍👨‍💻")

            
            canal = client.get_channel(837765441383301160)
            await canal.send(embed=embed)
            await canal.send("- - - - - - - - - - - - - - - - - ")

########################################################################################################################

    req = requests.get('https://cursosdev.com/coupons', headers=header, cookies=coockies2)
    soup = BeautifulSoup(req.text, 'html5lib')

    for line in soup.find_all('a', class_='c-card block bg-white shadow-md hover:shadow-xl rounded-lg overflow-hidden'):
        links = line.get('href')

        req = requests.get(links, headers=header)
        soup = BeautifulSoup(req.text, 'html5lib')
        for lines in soup.find_all('h2', class_="text-3xl text-gray-800 font-bold mr-auto"):
            name = lines.get_text()
            cursos = name.replace("                           ", '').replace("[100% DESCT.°]", '').replace("""
        """, '')
    
        if cursos in cupones:
            pass
        else:
            cupones.append(cursos)

            for lines in soup.find_all('a'):
                if 'Aplicar' in lines.get_text():
                    linkfinal = lines.get('href')
            
            for lines in soup.findAll('meta', {'name':'description'}):
                descripcion = lines.get('content')
            
            for lines in soup.find_all('meta', property='og:image'):
                imagen = lines.get('content')

            embed = discord.Embed(
                title = cursos,
                description = "Detalles",
                color = discord.Color.random()
            )
            embed.set_thumbnail(url=imagen)
            embed.add_field(name="Descripción:", value=descripcion, inline=False)
            embed.add_field(name="Curso:", value=linkfinal, inline=False)
            embed.add_field(name="Corre que se termina pronto la oferta!!", value='\u200b', inline=False)
            embed.set_footer(text="👨‍💻Dale gracias a cuchillo#7116‍‍👨‍💻")

            canal = client.get_channel(837765441383301160)
            await canal.send(embed=embed)
            await canal.send("- - - - - - - - - - - - - - - - - ")


client.run(token)
