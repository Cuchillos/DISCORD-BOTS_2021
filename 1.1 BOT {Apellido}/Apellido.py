#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
from os import name
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
#import hostbot
#from hostbot import keep_alive

from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict
###################################

client = commands.Bot(command_prefix='!', help_command=None)
token = "YOUR_BOT_TOKEN_HERE"


##############################
headersbear = CaseInsensitiveDict()
headersbear["authority"] = "forebears.io"
headersbear["cache-control"] = "max-age=0"
headersbear["upgrade-insecure-requests"] = "1"
headersbear["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285"
headersbear["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headersbear["sec-fetch-site"] = "none"
headersbear["sec-fetch-mode"] = "navigate"
headersbear["sec-fetch-user"] = "?1"
headersbear["sec-fetch-dest"] = "document"
headersbear["accept-language"] = "es-ES,es;q=0.9"
headersbear["if-none-match"] = '"60c0c0c8-387a"'
headersbear["if-modified-since"] = 'Wed, 09 Jun 2021 13:23:20 GMT'
###############
headersplus = CaseInsensitiveDict()
headersplus["authority"] = "www.plusesmas.com"
headersplus["cache-control"] = "max-age=0"
headersplus["upgrade-insecure-requests"] = "1"
headersplus["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285"
headersplus["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headersplus["sec-fetch-site"] = "none"
headersplus["sec-fetch-mode"] = "navigate"
headersplus["sec-fetch-user"] = "?1"
headersplus["sec-fetch-dest"] = "document"
headersplus["accept-language"] = "es-ES,es;q=0.9"
headersplus["cookie"] = "overlayerPubli=1; cX_S=kqfb98cfqpsvz86q; cX_P=kqfb98cgyy779jr1"
###################################



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!ayuda", url="https://www.twitch.tv/cuchillop"))
    print("Estoy listo :)")


#847487045207064596
@client.command()
async def ayuda(ctx):
    if ctx.message.channel.id == 847487045207064596:
        embed = discord.Embed(
            title='Comando',
            description="Comandos disponibles:",
            color=discord.Color.random()
            )

        embed.set_thumbnail(url='https://uploadgerencie.com/imagenes/orden-apellidos.png')
        embed.add_field(name="!apellido [apellido]", value="Información sobre un apellido", inline=False)
        embed.set_footer(text="👨‍💻cuchillo#7116 está programando más comandos...👨‍💻")

        await ctx.send(embed=embed)
    else:
        await ctx.send(f"***Bro {ctx.message.author.mention}, vete al canal adecuado :v***")


@commands.cooldown(1, 30, commands.BucketType.user)
@client.command()
async def apellido(ctx, apellido=None):
    if ctx.message.channel.id == 847487045207064596:
        if apellido == None:
            await ctx.send("Indica un apellido :v\nComando: ```!apellido [apellido]```")
        else:
            true = 0

            embed = discord.Embed(
                title=apellido,
                description="Información del apellido:",
                color=discord.Color.random()
            )
            
            ######################################################################
            urlbear = f"https://forebears.io/es/surnames/{apellido}"
            reqbear = requests.get(urlbear, headers=headersbear)
            soupbear = BeautifulSoup(reqbear.text, 'html5lib')

            urlplus = f"https://www.plusesmas.com/escudos/apellidos/?q={apellido}"
            respplus = requests.get(urlplus, headers=headersplus)
            soupplus = BeautifulSoup(respplus.text, 'html5lib')
            ######################################################################
            ##
            origen = ''
            try:
                for x in soupplus.find_all('p', class_="text-center"):
                    origen = x.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
            except:
                pass
            if origen == '':
                embed.add_field(name="Origen:", value="No se ha encontrado ningún origen", inline=False)
            else:
                embed.add_field(name="Origen:", value=origen, inline=False)
                true =+1                
            ##
            definicion = ''
            try:
                for x in soupbear.find_all('h4', class_='desktop-only mt-2'):
                    definicion = x.next_sibling.get_text()
            except:
                pass
            try:
                for x in soupbear.find_all('h4', class_='desktop-only mt-2 mb-4'):
                    definicion = x.next_sibling.get_text()
            except:
                pass

            if definicion == '':
                embed.add_field(name="Definición:", value="No se ha encontrado ninguna definición", inline=False)
            else:
                embed.add_field(name="Definición:", value=definicion, inline=False)
                true =+1
            ##
            comun = ''
            try:
                for x in soupbear.find_all('div', class_="statistic-number"):
                    comun = x.get_text()
            except:
                pass
            if comun == '':
                embed.add_field(name="Común en el mundo:", value="No se ha encontrado ninguna posición", inline=False)
            else:
                embed.add_field(name='Común en el mundo:', value=f"Es el {comun} más común en el Mundo", inline=False)
                true =+1
            ##
            gente = ''
            try:
                for x in soupbear.find_all('span', class_="accent"):
                    gente = x.get_text()
            except:
                pass
            if gente == '':
                embed.add_field(name="Personas:", value="No se ha encontrado ninguna persona", inline=False)
            else:
                embed.add_field(name='Personas:', value=f"Aproximadamente {gente} personas llevan este apellido", inline=False)
                true =+1
            ##
            frecuente = ''
            densidad = ''
            try:
                for x in soupbear.find_all('div', class_="title"):
                    if "La más frecuente en: " == x.get_text():
                        frecuente = x.next_sibling.get_text()
                    elif "La densidad más alta en: " == x.get_text():
                        densidad = x.next_sibling.get_text()
            except:
                pass
            if frecuente == '':
                embed.add_field(name="Frecuente:", value="No se ha encontrado ninguna nación frecuente", inline=False)
            else:
                embed.add_field(name="Frecuente:", value=f"La nación donde hay más gente con el apellido:  {frecuente}", inline=False)
                true =+1

            if densidad == '':
                embed.add_field(name="Densidad:", value="No se ha encontrado ningun porcentaje", inline=False)
            else:
                embed.add_field(name="Densidad:", value=f"La nación donde el porcentaje de personas con el apellido es mayor:  {densidad}", inline=False)
                true =+1
            ##
            escudo = ''
            try:
                for x in soupplus.find_all('p', class_="text-center"):
                    for i in x.find_all('img', class_="img-fluid"):
                        escudo = i.get('src')
            except:
                pass
            if escudo == '':
                embed.add_field(name="No se ha encontrado ningún escudo", value="\u200b", inline=False)
            else:
                embed.set_image(url=escudo)
                true =+1

            if true == 0:
                embede = discord.Embed(
                    title="ERROR",
                    description="NO EXISTE EL APELLIDO",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embede)
            else:
                await ctx.send(embed=embed)
    else:
        await ctx.send(f"***Bro {ctx.message.author.mention}, vete al canal adecuado :v***")

@apellido.error
async def apellido_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.random()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)


#keep_alive()

client.run(token)