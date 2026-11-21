#!/usr/bin/env python
#_*_ coding: utf8 _*_
from __future__ import unicode_literals


################################
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord_buttons_plugin import *
from dpymenus import Page, PaginatedMenu
from discord import FFmpegPCMAudio
from discord.utils import get
#from hostbot import keep_alive

import youtube_dl
import time
import os
import json
import requests
from requests.structures import CaseInsensitiveDict
################################

client = commands.Bot(command_prefix='!', help_command=None)
buttons = ButtonsClient(client)
token = "YOUR_BOT_TOKEN_HERE"


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!ayuda", url="https://www.twitch.tv/cuchillop"))
    print("Estoy listo :)")


main = "https://yt1s.com/api/ajaxSearch/index"

headersm = CaseInsensitiveDict()
headersm["authority"] = "yt1s.com"
headersm["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headersm["accept"] = "*/*"
headersm["x-requested-with"] = "XMLHttpRequest"
headersm["sec-ch-ua-mobile"] = "?0"
headersm["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headersm["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headersm["origin"] = "https://yt1s.com"
headersm["sec-fetch-site"] = "same-origin"
headersm["sec-fetch-mode"] = "cors"
headersm["sec-fetch-dest"] = "empty"
headersm["referer"] = "https://yt1s.com/youtube-to-mp3/en12"
headersm["accept-language"] = "es-ES,es;q=0.9"
headersm["cookie"] = "__atssc=google%3B1; __atuvc=2%7C26; __atuvs=60df517e5aac0dff001"

last = "https://yt1s.com/api/ajaxConvert/convert"

headersl = CaseInsensitiveDict()
headersl["authority"] = "yt1s.com"
headersl["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headersl["accept"] = "*/*"
headersl["x-requested-with"] = "XMLHttpRequest"
headersl["sec-ch-ua-mobile"] = "?0"
headersl["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headersl["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headersl["origin"] = "https://yt1s.com"
headersl["sec-fetch-site"] = "same-origin"
headersl["sec-fetch-mode"] = "cors"
headersl["sec-fetch-dest"] = "empty"
headersl["referer"] = "https://yt1s.com/youtube-to-mp3/en12"
headersl["accept-language"] = "es-ES,es;q=0.9"
headersl["cookie"] = "__atssc=google%3B1; __atuvc=2%7C26; __atuvs=60df517e5aac0dff001"

short = "https://bitly.com/data/anon_shorten"

headerss = CaseInsensitiveDict()
headerss["authority"] = "bitly.com"
headerss["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headerss["accept"] = "application/json, text/javascript, */*; q=0.01"
headerss["x-xsrftoken"] = "1d87896122914167a4c27b18f9068531"
headerss["x-requested-with"] = "XMLHttpRequest"
headerss["sec-ch-ua-mobile"] = "?0"
headerss["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headerss["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headerss["origin"] = "https://bitly.com"
headerss["sec-fetch-site"] = "same-origin"
headerss["sec-fetch-mode"] = "cors"
headerss["sec-fetch-dest"] = "empty"
headerss["referer"] = "https://bitly.com/"
headerss["accept-language"] = "es-ES,es;q=0.9"
headerss["cookie"] = "_xsrf=1d87896122914167a4c27b18f9068531; anon_u=cHN1X180NDI1ZWM4NS02OGE1LTQzNDMtYWM2My0zNGZhYjQxYjRjZmM=|1625330160|5315dbbdc10f6b07118fba0d030500a03b6ad770; _ga=GA1.2.1295377962.1625330147; _gid=GA1.2.397730991.1625330147; cookie_banner=1; anon_shortlinks=https://bit.ly/3hgQfwq"

@client.command()
async def ayuda(ctx):
	if ctx.message.channel.id == 860949609362358312:
		embed = discord.Embed(
			title="Comandos:",
			description="Comandos disponibles:",
			color=discord.Color.random()
			)
		embed.add_field(name="!mp3 [url]", value="Descargar el audio de un video", inline=False)
		embed.add_field(name="!mp4 [url]", value="Descargar el video", inline=False)
		embed.set_thumbnail(url='https://logodownload.org/wp-content/uploads/2014/10/youtube-logo-6-2.png')
		embed.set_footer(text='👨‍💻cuchillo#7116‍‍👨‍💻')
		await ctx.send(embed=embed)
	else:
		await ctx.send("***BRO, vete al canal adecuado :v***")


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def mp3(ctx, url=None):
    if ctx.message.channel.id == 860949609362358312:

        if url is None or 'https://' not in url or 'youtu' not in url:
            await ctx.send("**Indica un video de youtube**\n*Comando:*```!mp3 https://youtu.be/XXXXXXXXX\n!mp3 https://www.youtube.com/watch?v=XXXXXXXXX```")
            return


        embed = discord.Embed(
        	title="DESCARGANDO... MP3",
        	description="Espera un poco...",
        	color=discord.Color.orange()
        	)
        msg = await ctx.send(embed=embed)

        ####
        try:

        	datam = f"q={url}&vt=mp3"
        	datam = datam.replace(':', '%3A').replace("/", '%2F')
        	respm = requests.post(main, headers=headersm, data=datam)

        	textm = json.loads(respm.text)
        	vid = textm['vid']

        	for x in textm['links']['mp3']:
        		num = x
        		break

        	k = textm['links']['mp3'][num]['k']
		####

        	datal = f"vid={vid}&k={k}"
        	datal = datal.replace("+", '%2B')

        	respl = requests.post(last, headers=headersl, data=datal)

        	textl = json.loads(respl.text)
        	mp3 = textl['dlink']
		####

        	datas = f"url={mp3}"
        	datas = datas.replace(':', '%3A').replace("/", '%2F')
        	resps = requests.post(short, headers=headerss, data=datas)

        	texts = json.loads(resps.text)

        	mp3url = texts['data']['link']
		####

        	embed = discord.Embed(
        		title="**MP3 DESCARGADO**",
				description=f"*{textm['title']}*",
        		color=discord.Color.green()
        		)
        	#embed.add_field(name="\u200b", value=f'[DESCARGAR]({mp3url})', inline=False)
        	embed.set_thumbnail(url=f"http://i3.ytimg.com/vi/{vid}/maxresdefault.jpg")
        	embed.set_footer(text='👨‍💻cuchillo#7116‍‍👨‍💻')

        	await msg.delete()

        	await buttons.send(
        		embed = embed,
        		channel = ctx.channel.id,
        		components = [
        			ActionRow([
        					Button(
        							label = "DESCARGAR",
        							style = ButtonType().Link,
        							url = mp3url
        						)
        				])
        		]

        		)




        except:
        	embed = discord.Embed(
        		title="**ERROR**",
        		description="*No se ha podido descargar*",
        		color=discord.Color.red()
        		)
        	embed.set_footer(text='👨‍💻cuchillo#7116‍‍👨‍💻')

        	await msg.edit(embed=embed)
    else:
        await ctx.send("***BRO, vete al canal adecuado :v***")

@mp3.error
async def mp3_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.random()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def mp4(ctx, url=None):
	if ctx.message.channel.id == 860949609362358312:

		if url is None or 'https://' not in url or 'youtu' not in url:
			await ctx.send("**Indica un video de youtube**\n*Comando:*```!mp4 https://youtu.be/XXXXXXXXX\n!mp3 https://www.youtube.com/watch?v=XXXXXXXXX```")
			return

		embed = discord.Embed(
			title="DESCARGANDO... MP4",
			description="Espera un poco...",
			color=discord.Color.orange()
			)
		msg = await ctx.send(embed=embed)

		####
		try:
			
			datam = f"q={url}&vt=mp4"
			datam = datam.replace(':', '%3A').replace("/", '%2F')
			respm = requests.post(main, headers=headersm, data=datam)

			textm = json.loads(respm.text)
			vid = textm['vid']

			for x in textm['links']['mp4']:
				num = x
				break

			k = textm['links']['mp4'][num]['k']

		####

			datal = f"vid={vid}&k={k}"
			datal = datal.replace("+", '%2B')

			respl = requests.post(last, headers=headersl, data=datal)

			textl = json.loads(respl.text)
			mp3 = textl['dlink']
			####

			datas = f"url={mp3}"
			datas = datas.replace(':', '%3A').replace("/", '%2F')
			resps = requests.post(short, headers=headerss, data=datas)

			texts = json.loads(resps.text)

			mp3url = texts['data']['link']
			####

			embed = discord.Embed(
				title="**MP4 DESCARGADO**",
				description=f"*{textm['title']}*",
				color=discord.Color.green()
				)
			#embed.add_field(name="\u200b", value=f'[DESCARGAR]({mp3url})', inline=False)
			embed.set_thumbnail(url=f"http://i3.ytimg.com/vi/{vid}/maxresdefault.jpg")
			embed.set_footer(text='👨‍💻cuchillo#7116‍‍👨‍💻')

			await msg.delete()

			await buttons.send(
				embed = embed,
				channel = ctx.channel.id,
				components = [
					ActionRow([
							Button(
									label = "DESCARGAR",
									style = ButtonType().Link,
									url = mp3url
								)
						])
				]

				)

		except:
			embed = discord.Embed(
				title="**ERROR**",
				description="*No se ha podido descargar*",
				color=discord.Color.red()
				)
			embed.set_footer(text='👨‍💻cuchillo#7116‍‍👨‍💻')

			await msg.edit(embed=embed)
	else:
		await ctx.send("***BRO, vete al canal adecuado :v***")

@mp4.error
async def mp4_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.random()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)


@client.command()
async def play(ctx, url=None):
	if ctx.message.channel.id == 860949609362358312:
		if url is None or 'https://' not in url or 'youtu' not in url:
			await ctx.send("**Indica un video de youtube**\n*Comando:*```!play https://youtu.be/XXXXXXXXX\n!play https://www.youtube.com/watch?v=XXXXXXXXX```")
			return

		embed = discord.Embed(
			title="CARGANDO...",
			description="Espera un poco...",
			color=discord.Color.orange()
			)
		msg = await ctx.send(embed=embed)

		####
#		try:
		
		datam = f"q={url}&vt=mp3"
		datam = datam.replace(':', '%3A').replace("/", '%2F')
		respm = requests.post(main, headers=headersm, data=datam)

		textm = json.loads(respm.text)
		vid = textm['vid']

		for x in textm['links']['mp3']:
			num = x
			break

		k = textm['links']['mp3'][num]['k']

	####

		datal = f"vid={vid}&k={k}"
		datal = datal.replace("+", '%2B')

		respl = requests.post(last, headers=headersl, data=datal)

		textl = json.loads(respl.text)
		mp3 = textl['dlink']
		####

		datas = f"url={mp3}"
		datas = datas.replace(':', '%3A').replace("/", '%2F')
		resps = requests.post(short, headers=headerss, data=datas)

		texts = json.loads(resps.text)

		mp3url = texts['data']['link']
		####

		connected = ctx.author.voice
		if not connected:
			await msg.delete()
			await ctx.send("Necesitas estar en un canal de voz para utilizar este comando!")
			return

		song_there = os.path.isfile(f"{ctx.message.guild.id}.mp3")
		try:
			if song_there:
				os.remove(f"{ctx.message.guild.id}.mp3")
		except PermissionError:
			await ctx.send("Espere a que termine la música que se está reproduciendo o utilice el comando 'stop'")
			return

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		
		def check_n(idd):
			for file in os.listdir("./"):
				if idd in file.title():
					print(file)
					name = file.title()
					name = name.replace('Mp3', 'mp3')
					os.rename(f"{name}", f"{ctx.message.guild.id}.mp3")
		
		if 'https://youtu.be/' in url:
			idr = url.split('be/')
			idr = idr[1]
			check_n(idr)

		elif 'https://www.youtube.com/watch?' in url:
			idr = url.split('?v=')
			idr = idr[1]
			check_n(idr)


		channel = ctx.message.author.voice.channel
		voice = get(client.voice_clients, guild=ctx.guild)

		if voice and voice.is_connected():
			await voice.move_to(channel)
		else:
			voice = await channel.connect()

		embed = discord.Embed(
			title="**REPRODUCIENDO**",
			description=f"*[{textm['title']}]({mp3url})*",
			color=discord.Color.green()
			)
		embed.set_thumbnail(url=f"http://i3.ytimg.com/vi/{vid}/maxresdefault.jpg")
		embed.set_footer(text='👨‍💻cuchillo#7116‍‍👨‍💻')

		await msg.edit(embed=embed)

		time.sleep(2)

		source = FFmpegPCMAudio(f"{ctx.message.guild.id}.mp3")
		voice.play(source)


#		except:
#			embed = discord.Embed(
#				title="**ERROR**",
#				description="*No se ha podido reproducir*",
#				color=discord.Color.red()
#				)
#			embed.set_footer(text='👨‍💻cuchillo#7116‍‍👨‍💻')
#
#			await msg.edit(embed=embed)

	else:
		await ctx.send("***BRO, vete al canal adecuado :v***")


#keep_alive()

client.run(token)