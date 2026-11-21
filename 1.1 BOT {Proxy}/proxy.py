#!/usr/bin/env python
#_*_ coding: utf8 _*_

###############
import discord
from discord.ext import commands
import hostbot
from hostbot import keep_alive

from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict
import os
##############

client = commands.Bot(command_prefix='!', help_command=None)
token = "YOUR_BOT_TOKEN_HERE"


url = "https://github.com/DBcuCHxDillo/DatB4s3CuIYYoxD28/blob/main/UrIs-_prox3s.txt"

headers = CaseInsensitiveDict()
headers["authority"] = "github.com"
headers["cache-control"] = "max-age=0"
headers["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headers["sec-ch-ua-mobile"] = "?0"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-user"] = "?1"
headers["sec-fetch-dest"] = "document"
headers["referer"] = "https://github.com/DBcuCHxDillo/DatB4s3CuIYYoxD28/new/main"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = "_octo=GH1.1.1031489571.1624927415; tz=Europe%2FMadrid; _device_id=655ade7cbf417c4126aff6a33035ebfe; has_recent_activity=1; user_session=LX1tLCb18-A2d4SownTwZFIx4RB2AexCLgt2Q-TZxPFJDarh; __Host-user_session_same_site=LX1tLCb18-A2d4SownTwZFIx4RB2AexCLgt2Q-TZxPFJDarh; tz=Europe%2FMadrid; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=DBcuCHxDillo; _gh_sess=dQZnWEyfb2CKrN%2FoZvVdRuQstksKQbvOh1Zikw60rQQ8RdhnqIqcJp2vFNIjLVTVDrYY1oTbyadYp86USFViS3FnwmYXvHOBdndXNvV0jBpkjDGJXBPA34kaplg4JoZUnEbTOxjaHqT2%2FhPNonIsMGoAwZqlqGQJ3cKdoxLw%2FXn39D4agcJ9RSdUz8OHCNX%2BHMyIaUa40ZNK0Vmqj8wHd2ogVdeauG1dZSjKYKnj3oh7mOHp4ABMUd0nrR%2BBbtjcyW2SQOEZntj9Ot2AEfXOn%2BXymkZiTsXkNlTu%2FWqv5rXY2CYofR54uTq3owAVGlg0qvKJI2v8FcsBQl4Cb54VFf3uCHlmXCTi%2BhPiJ7ZwMUeyjWgaUVciNKXjbN7Td9E%2BYBIVTaluBlzr0CkQ%2FmhPXsXMFPRwPXBUGlSYn69WeSNT6Dnmn66eeqgOOWib4Rv6kVeuiz2hneprt%2FiFO93lmCZFAdUlu%2Fl2paVwloggIp3VnIPp9sRnXLKpzdt6MB7Age5qeaPi3gJwzDx4f4FPM558OrUrLVhnInjK57cIKzEi%2FzeIDpiPFLK%2BgWvBnquNbxcLtzVIVo2klfv%2FVL%2FdVYMRwdmnTqP9nEkc9%2F3V54OV7zppBoB0VvR4S7FQPgkjGy4%2F24lBY%2F7Z7kYhlLs6IJUNC6OFdmpF9anTBD9TlrfOyahoAtcLOuGwG78ezMq9tp9DTjklNjdSLO%2FTRLnVPSAQzMHgR9DQIql4IconFRstqzdUkmHo%2FJSIXZYGobxQfS58ZjVB7VE8g4HulNrWFE%2BOzpbZkc8FejutQi5Lq4iR0xRz0%2B6MwQcWSeWN9aEOUjIpGLSlei5QAGcExVvvfI%2BhJ253TrtVHyT9jXDP5O4yqRPmbasDzcxFusKhqHtieKzQauPCGbVVrMGeqI9MRiQaJph8q3KxxwzwJg%3D%3D--zNkCdA7Mo6%2BKMwMJ--ZsbdlC1X5SOoZ1DVOCsIYA%3D%3D"
headers["if-none-match"] = 'W/"fba8d023fafd8939a95871afb5302472"'



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!ayuda", url="https://www.twitch.tv/cuchillop"))
    print("LISTO ;)")

@client.command()
async def ayuda(ctx):
    role = discord.utils.get(ctx.guild.roles, id=812326538506141726)
    if role in ctx.message.author.roles and ctx.message.channel.id == 840728280574984192:
        embed = discord.Embed(
            title = 'Comandos:',
            description = "Comandos disponibles:",
            color = discord.Color.purple()
        )
        embed.set_thumbnail(url='https://www.bestproxyreviews.com/wp-content/uploads/2020/01/Web-Proxy-Server.jpg')
        embed.add_field(name="!http", value="Generar proxies http", inline=True)
        embed.add_field(name="!https", value="Generar proxies https", inline=True)
        embed.add_field(name="!socks4", value="Generar proxies SOCKS4", inline=True)
        embed.add_field(name="!socks5", value="Generar proxies SOCKS5", inline=True)
        embed.add_field(name="LAS PROXIES SON VÁLIDAS!", value="Aproximadamente te genera 2000 proxies válidas", inline=False)
        embed.set_footer(text="👨‍💻cuchillo#7116 está sacando proxies xd...👨‍💻")

        await ctx.send(embed=embed)

    else:
        await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")

@client.command()
async def http(ctx):
    role = discord.utils.get(ctx.guild.roles, id=812326538506141726)
    if role in ctx.message.author.roles and ctx.message.channel.id == 812450049027997707:

        await ctx.send(f"*Generando proxies http...\n{ctx.author.mention}*")

        try:
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'html5lib')

            for x in soup.find_all('td'):
                if "LC1" in x.get('id', []):
                    url_http = x.get_text()

            http = requests.get(url_http)

            f = open('http_proxies.txt', '+a')
            for lines in http.text:
                f.write(lines.rstrip('\n'))
            f.close()


            await ctx.author.send(file=discord.File(f'http_proxies.txt'))
            os.remove('http_proxies.txt')
            await ctx.send(f"***:white_check_mark: Proxies *** *http* *** generados :white_check_mark: \nmira md{ctx.author.mention}***")

        except:
            await ctx.send(f"***:x: ERROR: no he podido generar proxies *** *http* *** :x:\n{ctx.author.mention}***")

    else:
        await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")


@client.command()
async def https(ctx):
    role = discord.utils.get(ctx.guild.roles, id=812326538506141726)
    if role in ctx.message.author.roles and ctx.message.channel.id == 840728280574984192:

        await ctx.send(f"*Generando proxies https...\n{ctx.author.mention}*")

        try:
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'html5lib')

            for x in soup.find_all('td'):
                if "LC2" in x.get('id', []):
                    url_http = x.get_text()

            https = requests.get(url_http)

            f = open('https_proxies.txt', '+a')
            for lines in https.text:
                f.write(lines.rstrip('\n'))
            f.close()

            await ctx.author.send(file=discord.File(f'https_proxies.txt'))
            os.remove('https_proxies.txt')

            await ctx.send(f"***:white_check_mark: Proxies *** *https* *** generados :white_check_mark: \nmira md {ctx.author.mention}***")

        except:
            await ctx.send(f"***:x: ERROR: no he podido generar proxies *** *https* *** :x:\n{ctx.author.mention}***")

    else:
        await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")


@client.command()
async def socks4(ctx):
    role = discord.utils.get(ctx.guild.roles, id=812326538506141726)
    if role in ctx.message.author.roles and ctx.message.channel.id == 840728280574984192:

        await ctx.send(f"*Generando proxies socks4...\n{ctx.author.mention}*")

        try:
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'html5lib')

            for x in soup.find_all('td'):
                if "LC3" in x.get('id', []):
                    url_http = x.get_text()

            https = requests.get(url_http)

            f = open('socks4_proxies.txt', '+a')
            for lines in https.text:
                f.write(lines.rstrip('\n'))
            f.close()

            await ctx.author.send(file=discord.File(f'socks4_proxies.txt'))
            os.remove('socks4_proxies.txt')

            await ctx.send(f"***:white_check_mark: Proxies *** *socks4* *** generados :white_check_mark: \nmira md {ctx.author.mention}***")

        except:
            await ctx.send(f"***:x: ERROR: no he podido generar proxies *** *socks4* *** :x:\n{ctx.author.mention}***")

    else:
        await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")


@client.command()
async def socks5(ctx):
    role = discord.utils.get(ctx.guild.roles, id=812326538506141726)
    if role in ctx.message.author.roles and ctx.message.channel.id == 840728280574984192:

        await ctx.send(f"*Generando proxies socks5...\n{ctx.author.mention}*")

        try:
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'html5lib')

            for x in soup.find_all('td'):
                if "LC4" in x.get('id', []):
                    url_http = x.get_text()

            https = requests.get(url_http)

            f = open('socks5_proxies.txt', '+a')
            for lines in https.text:
                f.write(lines.rstrip('\n'))
            f.close()

            await ctx.author.send(file=discord.File(f'socks5_proxies.txt'))
            os.remove('socks5_proxies.txt')

            await ctx.send(f"***:white_check_mark: Proxies *** *socks5* *** generados :white_check_mark: \nmira md {ctx.author.mention}***")

        except:
            await ctx.send(f"***:x: ERROR: no he podido generar proxies *** *socks5* *** :x:\n{ctx.author.mention}***")

    else:
        await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")


keep_alive()

client.run(token)