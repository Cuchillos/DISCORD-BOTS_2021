#!/usr/bin/env python
#_*_ coding: utf8 _*_

#####################
import discord
from discord.ext import commands, tasks

import requests
from bs4 import BeautifulSoup
import urllib.request
import json
from requests.structures import CaseInsensitiveDict
#####################
import hostbot
from hostbot import keep_alive
#####################

client = commands.Bot(command_prefix='!', help_command=None)

token = "YOUR_BOT_TOKEN_HERE"

#############


urltw = "https://counts.live/twitch-follower-count/cegamer69"

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


peticionyt = req = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?id=UCSTzojy6x8xj9yPv_eUjS9Q&key=AIzaSyAVB1kbiCc0jUxcTsDOwY--eYSejIL0bME&part=statistics')
peticionyt = json.loads(peticionyt.read())


urlce = "https://counts.live/api/tiktok-follower-count/cegamer_yt/live"

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

respp = requests.get(urlce, headers=headers)
respce = json.loads(respp.text)

urlky = "https://counts.live/api/tiktok-follower-count/kreativity11/live"
respk = requests.get(urlky, headers=headers)
respky = json.loads(respk.text)



def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Cegamer", url="https://www.twitch.tv/cegamer69"))
    cegamerstat.start()
    print("Estoy listo :)")



@tasks.loop(seconds=1200)
async def cegamerstat():

    youtube = client.get_channel(833438870405120050)

    followers = abs(int(peticionyt['items'][0]['statistics'].get('subscriberCount')))

    await youtube.edit(name=f"YouTube: {human_format(followers)}")



    tiktok = client.get_channel(834111976040693860)
    await tiktok.edit(name=f"TikTok: {human_format(int(respce['data']['followers']))}")
                  


    twitch = client.get_channel(833429616558342144)
    for x in souptw.find('script', {"id": "__NEXT_DATA__"}):
        x = json.loads(x)

        followers = x['props']['pageProps']['rs']['live']['followers']

        await twitch.edit(name=f"Twitch: {followers}")

    


@client.command()
async def ayuda_cegamer(ctx):
    await ctx.send("UwU **Estoy recibiendo suscriptores**\n||Próximamente comandos exclusivos...||\n||*cuchillo#7116*||")


@client.command()
async def cegamer(ctx): 
    try:
      cegamerstat.start()
    except:
      pass

    followers = abs(int(peticionyt['items'][0]['statistics'].get('subscriberCount')))
    yt = f"{human_format(followers)}"


    tiktok = f"{human_format(int(respce['data']['followers']))}"
                  

    for x in souptw.find('script', {"id": "__NEXT_DATA__"}):
        x = json.loads(x)

        followers = x['props']['pageProps']['rs']['live']['followers']

        twitch = f"{followers}"

    embed = discord.Embed(
        title = 'CEGAMER',
        description = "SEGUIDORES DE CEGAMER",
        color = discord.Color.random()
    )
    embed.set_thumbnail(url='https://raw.githubusercontent.com/Cuchillos/cosas/main/cegamerbanner.png?token=APJ2VMFZS3WGTE2TOQGU3VTAXSWNG')
    embed.add_field(name="YouTube", value=f'Suscriptores: {yt}', inline=False)
    embed.add_field(name="Tiktok", value=f'Seguidores: {tiktok}', inline=False)
    embed.add_field(name="Twitch", value=f'Seguidores: {twitch}', inline=False)
    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

    await ctx.send(embed=embed)


@client.command()
async def kyliech11(ctx):
    tiktokky = f"{human_format(int(respky['data']['followers']))}"

    embed = discord.Embed(
            title = 'KylieCh11꒰⑅ᵕ༚ᵕ꒱˖♡',
            description = "SEGUIDORES DE KylieCh11꒰⑅ᵕ༚ᵕ꒱˖♡",
            color = discord.Color.random()
        )
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/689498880270008359/a51e123212d58e58b3ecbaf9246f2e87.png?size=256')
    embed.add_field(name="Tiktok (kreativity11)", value=f'Seguidores: {tiktokky}', inline=False)
    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

    await ctx.send(embed=embed) 


"""
keep_alive() 
client.run(token) """