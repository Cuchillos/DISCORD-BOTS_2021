#!/usr/bin/env python
#_*_ coding: utf8 _*_

#########IMPORTANTE########
import discord
from discord.ext import commands
#########IMPORTANTE########

import dns.resolver
import requests
from bs4 import BeautifulSoup
import os
from os import path
import urllib
import urllib.request
import json
import socket
import time
import warnings
warnings.simplefilter("ignore", UserWarning)
from Wappalyzer import WebPage, Wappalyzer

########Configuración##############

client = commands.Bot(command_prefix='!')

token = "YOUR_BOT_TOKEN_HERE"

@client.event
async def on_ready():
    print("Estoy listo :)")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!ayuda", url="https://www.twitch.tv/cuchillop"))

########Comandos##############

#########ayuda#############
@client.command()
async def ayuda(ctx):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        embed = discord.Embed(
            title="Comandos disponibles:",
            description="-----⬇️⬇️⬇️-----",
            colour=discord.Colour.red()
        )

        embed.set_thumbnail(url="https://www.reachfirst.com/wp-content/uploads/2018/08/Web-Development.jpg")
        embed.add_field(name="!ayuda", value="Todos los comandos disponibles 😎")
        embed.add_field(name="!dns_web 'WEB'", value="Obtener toda la información de los dns de una web")
        embed.add_field(name="!ip_history 'WEB'", value="Obtener todo el historial de todas las ip que ha tenido (de una web)")
        embed.add_field(name="!whois 'WEB'", value="Obtener la información de una web (Dueño, nº de telefono, ...)")
        embed.add_field(name="!geolocator 'WEB'", value="Obtener la localización de una web (País, ciudad, ...)")
        embed.add_field(name="!cabeceras 'WEB'", value="Obtener las cabeceras de una web")
        embed.add_field(name="!wappalyzer 'WEB'", value="Obtener las tecnologías de una web")
        embed.add_field(name="!versión 'WEB'", value="Obtener la versión de una web")
        embed.add_field(name="!users 'WEB'", value="Obtener los admins de una web (la mayoría de webs son de wordpress)(webs no tan famosas)")
        embed.add_field(name="!theme 'WEB'", value="Buscar los temas de una web")
        embed.add_field(name="!plugin 'WEB'", value="Buscar los plugins de una web (no encuentra todos los plugins, solo algunos)")
        embed.add_field(name="!subdominio 'WEB'", value="Fuerza bruta de subdominios (solo para usuarios con el rol 🦿 )")
        embed.set_footer(text="👨‍💻cuchillo#7116 está programando más comandos...👨‍💻")

        await ctx.send(embed=embed)

    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

#########ayuda#############

@client.command()
async def dns_web(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Quita el 'https://www.' al final de la web. ejemplo: example.com\nComprueba si la web esta bien escrita")

        elif "https://www." in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el 'https://www.' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")
        
        elif "https://" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el 'https://' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")
    
        elif "/" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el '/xxxxxxx' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")


        else:
            await ctx.send("Espera...\nTiempo aproximado 1 minuto")

            embed = discord.Embed(
                title=f"Información obtenida de {web}:",
                description="-----⬇️⬇️⬇️-----",
                colour=discord.Colour.blue()
            )

            n = "Host Address IPv4"
            try:
                a = dns.resolver.resolve(web,"A")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Host Address IPv6"
            try:
                a = dns.resolver.resolve(web,"AAAA")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Authoritative name server"
            try:    
                a = dns.resolver.resolve(web,"NS")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mail destination"
            try:
                a = dns.resolver.resolve(web,"MD")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mail forwarder"
            try:                            
                a = dns.resolver.resolve(web,"MF")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Canonical name for an alias"
            try:                            
                a = dns.resolver.resolve(web,"CNAME")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Start of a zone of authority"
            try:                            
                a = dns.resolver.resolve(web,"SOA")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mailbox domain name"
            try:                            
                a = dns.resolver.resolve(web,"MB")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mail group member"
            try:                            
                a = dns.resolver.resolve(web,"MG")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mail rename domain name"
            try:                            
                a = dns.resolver.resolve(web,"MR")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Null RR"
            try:                            
                a = dns.resolver.resolve(web,"NULL")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Well known service description"
            try:                            
                a = dns.resolver.resolve(web,"WKS")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Domain name pointer"
            try:                            
                a = dns.resolver.resolve(web,"PTR")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Host information"
            try:                            
                a = dns.resolver.resolve(web,"HINFO")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Domain name pointer"
            try:                            
                a = dns.resolver.resolve(web,"PTR")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mailbox or mail list information"
            try:                            
                a = dns.resolver.resolve(web,"MINFO")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)
        
            
            n = "Mail exchange"
            try:                            
                a = dns.resolver.resolve(web,"MX")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Text strings"
            try:                            
                a = dns.resolver.resolve(web,"TXT")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)
            
            
            n = "Transfer of an entire zone"
            try:                            
                a = dns.resolver.resolve(web,"AXFR")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mailbox-related records"
            try:                            
                a = dns.resolver.resolve(web,"MAILB")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)

            
            n = "Mail agent RR"
            try:                            
                a = dns.resolver.resolve(web,"MAILA")
                embed.add_field(name=n, value='\u200b')
                for x in a:
                    embed.add_field(name='\u200b', value=f"{x}", inline=False)

            except:
                embed.add_field(name=f"ERROR: No se ha podido obtener la consulta '{n}' :c", value='\u200b', inline=False)


            embed.set_footer(text="Créditos: cuchillo#7116")

            await ctx.send(ctx.message.author.mention + "  |  Mira md")
            await ctx.author.send(embed=embed)

    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def ip_history(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Quita el 'https://' al final de la web. ejemplo: example.com\nComprueba si la web esta bien escrita")
        
        elif "https://" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el 'https://' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")
    
        elif "/" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el '/xxxxxxx' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")

        else:
            await ctx.send("Espera...\nTiempo aproximado 30 segundos")
        
            try:
                embed = discord.Embed(
                    title=f"Historial de las ips de {web}:",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.green()
                )

                header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

                peticion = requests.get(url=f"https://viewdns.info/iphistory/?domain={web}",headers=header)

                soup = BeautifulSoup(peticion.text,'html5lib')

                a = soup.find(id="null")
                b = a.find(border="1")

                titulo = 0
                for x in b.find_all('tr'):
                    if titulo == 0:
                        origen = "      " + x.get_text("    |    ")
                        sin_l = origen.splitlines()
                        todo1 = str(sin_l).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                        embed.add_field(name=todo1, value='\u200b', inline=False)
                        titulo += 1
                    else:
                        origen = "->  " + x.get_text("  |  ")
                        sin_l = origen.splitlines()
                        todo = str(sin_l).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                        embed.add_field(name='\u200b', value=todo, inline=False)
            except:
                embed = discord.Embed(
                    title=f"ERROR {web}",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se han encontrado ips",value="Intenta con otra web :c", inline="False")
            try:
                embed.set_footer(text="Créditos cuchillo#7116")
                await ctx.author.send(embed=embed)
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
            except:
                await ctx.author.send(f"***Historial de las ips de {web}:***")
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                titulo = 0
                for x in b.find_all('tr'):
                    if titulo == 0:
                        origen = "      " + x.get_text("    |    ")
                        sin_l = origen.splitlines()
                        todo1 = str(sin_l).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                        await ctx.author.send(todo1)
                        titulo += 1
                    else:
                        origen = "->  " + x.get_text("  |  ")
                        sin_l = origen.splitlines()
                        todo = str(sin_l).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                        await ctx.author.send(todo)
                await ctx.author.send("Créditos cuchillo#7116")

    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def whois(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Quita el 'https://' al final de la web. ejemplo: example.com\nComprueba si la web esta bien escrita")
        
        elif "https://" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el 'https://' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")
    
        elif "/" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el '/xxxxxxx' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")

        else:
            await ctx.send("Espera...\nTiempo aproximado 30 segundos")
        
            try:
                embed = discord.Embed(
                    title=f"Whois de {web}:",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.blue()
                )

                url = requests.get(f"https://www.whois.com/whois/{web}")

                soup = BeautifulSoup(url.text,'html5lib')


                for x in soup.find_all('pre'):
                    info = x.get_text()
                
                a = open(f'Info-{web}-.txt','+a')
                a.write(info)
                a.close()
                

                embed.set_footer(text="Créditos cuchillo#7116")

                await ctx.author.send(embed=embed)
                await ctx.author.send(file=discord.File(f'Info-{web}-.txt'))
                await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR {web}",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha podido hacer el whois",value="Intenta con otra web :c", inline="False")
                embed.set_footer(text="Créditos cuchillo#7116")
                await ctx.author.send(embed=embed)
            
            os.remove(f"Info-{web}-.txt")

    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def geolocator(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Quita el 'https://' al final de la web. ejemplo: example.com\nComprueba si la web esta bien escrita")
        
        elif "https://" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el 'https://' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")
    
        elif "/" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("1.Quita el '/xxxxxxx' al final de la web. ejemplo: example.com")
            await ctx.send("2.Comprueba si la web esta bien escrita")

        else:
            await ctx.send("Espera...\nTiempo aproximado 20 segundos")
        
            try:
                embed = discord.Embed(
                    title=f"Geolocalización de {web}:",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.blue()
                )

                webb = socket.gethostbyname(web)

                url = f"https://ipinfo.io/{webb}/json"
                a = urllib.request.urlopen(url)
                j = json.loads(a.read())

                for datos in j:
                    embed.add_field(name='\u200b', value=f"{datos} : {j[datos]}", inline=False)
                
                embed.set_footer(text="Créditos cuchillo#7116")

                await ctx.author.send(embed=embed)
                await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR {web}",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha podido geolocalizar",value="Intenta con otra web :c", inline="False")
                embed.set_footer(text="Créditos cuchillo#7116")
                await ctx.author.send(embed=embed)

    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def cabeceras(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" not in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Pon la url completa (con el https://), ejemplo: https://example.com")

        else:
            await ctx.send("Espera...\nTiempo aproximado 15 segundos")

            try:
                try:
                    embed = discord.Embed(
                        title=f"Cabeceras de {web}:",
                        description="-----⬇️⬇️⬇️-----",
                        colour=discord.Colour.blue()
                    )
                    embed.add_field(name="Cabeceras:",value='\u200b')

                    url = requests.get(url=web)
                    cabeceras = dict(url.headers)
                    for x in cabeceras:
                        embed.add_field(name='\u200b', value=x + ' : ' + cabeceras[x], inline=False)
                    embed.set_footer(text="Créditos: cuchillo#7116")
                    await ctx.author.send(embed=embed)
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")

                except:
                    await ctx.author.send(f"***Cabeceras de {web}***")
                    url = requests.get(url=web)
                    cabeceras = dict(url.headers)
                    for x in cabeceras:
                        await ctx.author.send(x + ' : ' + cabeceras[x])
                    await ctx.author.send(".\nCréditos: cuchillo#7116")
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")
            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ninguna cabecera",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)


    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def wappalyzer(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" not in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Pon la url completa (con el https://), ejemplo: https://example.com")

        else:
            await ctx.send("Espera...\nTiempo aproximado 15 segundos")

            try:
                embed = discord.Embed(
                    title=f"Tecnologías de {web}:",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.gold()
                )
                embed.add_field(name="Tecnología encontrada:",value='\u200b')
                wappalyzer = Wappalyzer.latest()
                webb = WebPage.new_from_url(web)
                tecnologias = wappalyzer.analyze(webb)
                for x in tecnologias:
                    embed.add_field(name='\u200b', value=x, inline=False)

                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ninguna tecnología",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                
    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def versión(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" not in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Pon la url completa (con el https://), ejemplo: https://example.com")

        else:
            await ctx.send("Espera...\nTiempo aproximado 15 segundos")

            try:
                embed = discord.Embed(
                    title=f"Versión de {web}",
                    description="-----⬇️⬇️⬇️-----",
                    color=discord.Colour.orange()
                )

                url = web
                cabecera = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
                peticion = requests.get(url=url,headers=cabecera)
                soup = BeautifulSoup(peticion.text,'html5lib')
                for x in soup.find_all('meta'):
                    if x.get('name') == 'generator':
                        version = x.get('content')
                
                embed.add_field(name="Versión:", value=version, inline=False)
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ninguna versión",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                
    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)
@client.command()
async def version(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" not in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Pon la url completa (con el https://), ejemplo: https://example.com")

        else:
            await ctx.send("Espera...\nTiempo aproximado 15 segundos")

            try:
                embed = discord.Embed(
                    title=f"Versión de {web}",
                    description="-----⬇️⬇️⬇️-----",
                    color=discord.Colour.orange()
                )

                url = web
                cabecera = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
                peticion = requests.get(url=url,headers=cabecera)
                soup = BeautifulSoup(peticion.text,'html5lib')
                for x in soup.find_all('meta'):
                    if x.get('name') == 'generator':
                        version = x.get('content')
                
                embed.add_field(name="Versión:", value=version, inline=False)
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ninguna versión",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                
    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def users(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" not in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Pon la url completa (con el https://), ejemplo: https://example.com")
   
        else:
            await ctx.send("Espera...\nTiempo aproximado 15 segundos")

            try:
                try:
                    embed = discord.Embed(
                        title=f"Admins de {web}",
                        description="-----⬇️⬇️⬇️-----",
                        color=discord.Colour.orange()
                    )

                    url = urllib.request.urlopen(f"{web}/wp-json/wp/v2/users")

                    embed.add_field(name="     User     |     Name     |     Url     |     Description     |     Link", value='\u200b', inline=False)
                    for u in json.loads(url.read()):
                        user = u['slug']
                        name = u['name']
                        url = u['url']
                        description = u['description']
                        link = u['link']

                        embed.add_field(name='\u200b', value=f"{user} | {name} | {url} | {description} |    {link}", inline=False)

                    embed.set_footer(text="Créditos: cuchillo#7116")
                    await ctx.author.send(embed=embed)
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")

                except:
                    url = urllib.request.urlopen(f"{web}/wp-json/wp/v2/users")
                    await ctx.send(f"***Admins de {web}***")

                    await ctx.author.send("*     User     |     Name     |     Url     |     Description     |     Link*")
                    for u in json.loads(url.read()):
                        user = u['slug']
                        name = u['name']
                        url = u['url']
                        description = u['description']
                        link = u['link']

                        await ctx.author.send(f"{user} | {name} | {url} | {description} | {link}")

                    await ctx.author.send("Créditos: cuchillo#7116")
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ningun admin",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                
    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def theme(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" not in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Pon la url completa (con el https://), ejemplo: https://example.com")

        else:
            await ctx.send("Espera...\nTiempo aproximado 15 segundos")

            try:
                embed = discord.Embed(
                    title=f"Temas de {web}:",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Tema encontrado:",value='\u200b')


                themes_all = []

                header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
                peticion = requests.get(url=web,headers=header)

                soup = BeautifulSoup(peticion.text,'html5lib')
                for enlace in soup.find_all('link'):
                    if '/content/themes/' in enlace.get('href'):
                        the = enlace.get('href')
                        the = the.split('/')
                        if 'themes' in the:
                            pos = the.index('themes')
                            theme = the[pos+1]
                            embed.add_field(name='\u200b', value=theme, inline=False)
                            themes_all.append(theme)
                    elif '/wp-content/themes/' in enlace.get('href'):
                        the = enlace.get('href')
                        the = the.split('/')
                        if 'themes' in the:
                            pos = the.index('themes')
                            theme = the[pos+1]
                            embed.add_field(name='\u200b', value=theme, inline=False)
                            themes_all.append(theme)

                if themes_all == []:
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")
                    embed = discord.Embed(
                        title=f"ERROR ({web})",
                        description="-----⬇️⬇️⬇️-----",
                        colour=discord.Colour.red()
                    )
                    embed.add_field(name="No se ha encontrado ningun tema",value='\u200b')
                    embed.set_footer(text="Créditos: cuchillo#7116")
                    await ctx.author.send(embed=embed)
                else:
                    embed.set_footer(text="Créditos: cuchillo#7116")
                    await ctx.author.send(embed=embed)
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ningun tema",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                
    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def plugin(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" not in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Pon la url completa (con el https://), ejemplo: https://example.com")

        else:
            await ctx.send("Espera...\nTiempo aproximado 1 minuto")

            try:
                embed = discord.Embed(
                    title=f"Plugins de {web}:",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.purple()
                )
                embed.add_field(name="Plugin encontrado:",value='\u200b', inline=False)


                plugins_all = []

                header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
                peticion = requests.get(url=web,headers=header)

                soup = BeautifulSoup(peticion.text,'html5lib')
                for enlace in soup.find_all('link'):
                    if '/wp-content/plugins/' in enlace.get('href'):
                        the = enlace.get('href')
                        the = the.split('/')
                        if 'plugins' in the:
                            pos = the.index('plugins')
                            plugin = the[pos+1]
                            embed.add_field(name='\u200b', value=plugin, inline=False)
                            plugins_all.append(plugin)
                    elif '/content/mu-plugins/' in enlace.get('href'):
                        thes = enlace.get('href')
                        thes = thes.split('/')
                        if 'mu-plugins' in thes:
                            poss = thes.index('mu-plugins')
                            plugin = thes[poss+1]
                            embed.add_field(name='\u200b', value=plugin, inline=False)
                            plugins_all.append(plugin)

                scripts = soup.find_all('script',{"src":True})
                for enlaces in scripts:
                    if '/wp-content/plugins/' in enlaces.get('src'):
                        thes = enlaces.get('src')
                        thes = thes.split('/')
                        if 'plugins' in thes:
                            poss = thes.index('plugins')
                            plugins = thes[poss+1]
                            embed.add_field(name='\u200b', value=plugins, inline=False)
                            plugins_all.append(plugins)
                    elif '/content/mu-plugins/' in enlaces.get('src'):
                        thes = enlaces.get('src')
                        thes = thes.split('/')
                        if 'mu-plugins' in thes:
                            poss = thes.index('mu-plugins')
                            plugins = thes[poss+1]
                            embed.add_field(name='\u200b', value=plugins, inline=False)
                            plugins_all.append(plugins)

                if plugins_all == []:
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")
                    embed = discord.Embed(
                        title=f"ERROR ({web})",
                        description="-----⬇️⬇️⬇️-----",
                        colour=discord.Colour.red()
                    )
                    embed.add_field(name="No se ha encontrado ningun plugin",value='\u200b')
                    embed.set_footer(text="Créditos: cuchillo#7116")
                    await ctx.author.send(embed=embed)
                else:
                    embed.set_footer(text="Créditos: cuchillo#7116")
                    await ctx.author.send(embed=embed)
                    await ctx.send(ctx.message.author.mention + "  |  Mira md")

            except:
                await ctx.send(ctx.message.author.mention + "  |  Mira md")
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ningun plugin",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                
    else:
        avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
        priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
        if priaviso_role in ctx.message.author.roles:
            await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
            await ctx.send(ctx.message.author.mention)
            await ctx.send("20")
            time.sleep(5)
            await ctx.send("15")
            time.sleep(5)
            await ctx.send("10")
            time.sleep(5)
            await ctx.send("5")
            time.sleep(5)
            await ctx.send("Adiós...")
            await ctx.send(ctx.message.author.mention)
            await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
            await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

        elif avisado_role in ctx.message.author.roles:
            await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
            await ctx.message.author.add_roles(priaviso_role)
            await ctx.send(ctx.message.author.mention)
        else:
            await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
            await ctx.message.author.add_roles(avisado_role)
            await ctx.send(ctx.message.author.mention)

@client.command()
async def subdominio(ctx, web=None):
    user_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
    if user_role in ctx.message.author.roles and ctx.message.channel.id == 826032253154754560:
        if web==None:
            await ctx.send("Escoje una web :v")
            await ctx.send("Comprueba si la web esta bien escrita y completa")

        elif "https://" in web:
            await ctx.channel.purge(limit=1)
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Quita el https://, ejemplo: example.com")
        
        elif "www." in web:
            await ctx.send(ctx.message.author.mention)
            await ctx.send("Quita el www, ejemplo: example.com")

        else:
            await ctx.send(ctx.message.author.mention + "  |  Mira md")
            await ctx.send("Tiempo aproximado 1 hora")
            await ctx.send("EN PROGRESO...")

            embed = discord.Embed(
                title=f"Escaneando {web}:",
                description="-----⬇️⬇️⬇️-----",
                colour=discord.Colour.gold()
            )
            await ctx.author.send(embed=embed)

            wordlist = open('subdominios.txt','r')
            wordlist = wordlist.read().splitlines()

            lista = []

            barra = await ctx.author.send("Espera... |                    |0/9985")####################

            progreso = 1

            for l in wordlist:
                if progreso == 998:
                    await barra.edit(content=f"Espera... |#         |{progreso}/9985")
                elif progreso == 1997:
                    await barra.edit(content=f"Espera... |##        |{progreso}/9985")
                elif progreso == 2994:
                    await barra.edit(content=f"Espera... |###       |{progreso}/9985")
                elif progreso == 3992:
                    await barra.edit(content=f"Espera... |####      |{progreso}/9985")
                elif progreso == 4990:
                    await barra.edit(content=f"Espera... |#####     |{progreso}/9985")
                elif progreso == 5988:
                    await barra.edit(content=f"Espera... |######    |{progreso}/9985")
                elif progreso == 6986:
                    await barra.edit(content=f"Espera... |#######   |{progreso}/9985")
                elif progreso == 7984:
                    await barra.edit(content=f"Espera... |########  |{progreso}/9985")
                elif progreso == 8982:
                    await barra.edit(content=f"Espera... |######### |{progreso}/9985")
                elif progreso == 9985:
                    await barra.edit(content=f"Espera... |##########|{progreso}/9985")

                else:
                    await barra.edit(content=f"Espera... |          |{progreso}/9985")

                try:
                    dns.resolver.resolve(f'{l}.{web}','A')
                    lista.append(f'{l}.{web}')
                except:
                    pass

                progreso +=1


            if len(lista) > 0:
                embed = discord.Embed(
                    title=f"Subdominios de {web}:",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.gold()
                )
                embed.add_field(name="Número de subdominios posibles:",value=f'{len(lista)}', inline=True)

                for e in lista:
                    embed.add_field(name='\u200b',value=f'{e}', inline=False)
                    print(e)
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)

            else:
                embed = discord.Embed(
                    title=f"ERROR ({web})",
                    description="-----⬇️⬇️⬇️-----",
                    colour=discord.Colour.red()
                )
                embed.add_field(name="No se ha encontrado ningun subdominio",value='\u200b')
                embed.set_footer(text="Créditos: cuchillo#7116")
                await ctx.author.send(embed=embed)
                
    else:
        perm_role = discord.utils.get(ctx.guild.roles, id=826037853431660584)
        if perm_role in ctx.message.author.roles:
            await ctx.send("***BRO! NO TIENES PERMISOS PARA USAR ESTE COMANDO\nsorry***")
            await ctx.send(ctx.message.author.mention)
        else:
            avisado_role = discord.utils.get(ctx.guild.roles, id=826043570720473118)
            priaviso_role = discord.utils.get(ctx.guild.roles, id=826062532132864021)
            if priaviso_role in ctx.message.author.roles:
                await ctx.send("***BRO!! ADIÓS :[\nTE VOY HA EXPULSAR DEL SERVER\nTE DEJO 20 SEGUNDOS PARA DESPEDIRTE***")
                await ctx.send(ctx.message.author.mention)
                await ctx.send("20")
                time.sleep(5)
                await ctx.send("15")
                time.sleep(5)
                await ctx.send("10")
                time.sleep(5)
                await ctx.send("5")
                time.sleep(5)
                await ctx.send("Adiós...")
                await ctx.send(ctx.message.author.mention)
                await ctx.message.author.kick(reason="Ha intentado utilizar los comandos del web-scraper 3 veces, y le he avisado")
                await ctx.send("https://media.tenor.co/videos/46adbf6d8c643cdc65e4b2cbbfa95b64/mp4")

            elif avisado_role in ctx.message.author.roles:
                await ctx.send("***QUE HACES?!! A LA PROXIMA TE EXPULSO DEL SERVER :V\nTE VOY HA PONER EL ROL ':|'***")
                await ctx.message.author.add_roles(priaviso_role)
                await ctx.send(ctx.message.author.mention)
            else:
                await ctx.send("***QUE HACES?! NO TIENES PERMISOS PARA USAR ESTE COMANDO :V\nTE VOY HA PONER EL ROL ':v'***")
                await ctx.message.author.add_roles(avisado_role)
                await ctx.send(ctx.message.author.mention)


client.run(token)

