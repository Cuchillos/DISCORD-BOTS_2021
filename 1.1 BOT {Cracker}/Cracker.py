#!/usr/bin/env python
#_*_ coding: utf8 _*_

##########################
from random import random
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord_buttons_plugin import *
from dpymenus import Page, PaginatedMenu
#from hostbot import keep_alive

import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import os
##########################

client = commands.Bot(command_prefix='!', help_command=None)
buttons = ButtonsClient(client)
token = "YOUR_BOT_TOKEN_HERE"


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!ayuda", url="https://www.twitch.tv/cuchillop"))
    print("Estoy listo :D")


headers = CaseInsensitiveDict()
headers["authority"] = "getgamez.net"
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
headers["referer"] = "https://getgamez.net/"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = 'quads_browser_width=1536; gt3-window-size={"width":1481,"height":762,"orientation":"landscape","ratio":"1.944"}'

headersg = CaseInsensitiveDict()
headersg["authority"] = "getgamez.net"
headersg["cache-control"] = "max-age=0"
headersg["sec-ch-ua"] = '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"'
headersg["sec-ch-ua-mobile"] = "?0"
headersg["upgrade-insecure-requests"] = "1"
headersg["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
headersg["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headersg["sec-fetch-site"] = "same-origin"
headersg["sec-fetch-mode"] = "navigate"
headersg["sec-fetch-user"] = "?1"
headersg["sec-fetch-dest"] = "document"
headersg["accept-language"] = "es-ES,es;q=0.9"
headersg["cookie"] = 'quads_browser_width=1536; quads_browser_width=1536; gt3-window-size={"width":1481,"height":762,"orientation":"landscape","ratio":"1.944"}'


@client.command()
async def game(ctx, *, game: str):
    if ctx.message.channel.id == 862051117349339136:
        embed = discord.Embed(
            title="Espera...",
            description="Esto puede tardar unos minutos",
            color=discord.Color.orange()
        )
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        msg = await ctx.send(embed=embed)


        game = game.replace(' ', '+')

        url = f"https://getgamez.net/?s={game}&post_type=post"

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html5lib')

        n_g = game.replace('+', ' ')
        n_g = n_g.upper()
        pag0 = Page(title=n_g, description='\u200b', color=discord.Color.green())

        for x in soup.find_all('span', class_='count main-color'):
            pag0.add_field(name="Recursos:", value=f"Se han encontrado ***{x.get('data-total')}***  recursos", inline=False)

        pag0.add_field(name="Descargar:", value="!des_game [nº] [nombre del juego]")

        for x in soup.find_all('span', class_='page-number'):
            pagess = x.get_text()
            pagess = pagess.replace(' 1                ', ' 0 ')
            pagess = pagess.replace('Page', "Página")
            pagess = pagess.replace("of ", 'de ')
            pagess = pagess.replace("              ", '')

            pag0.set_footer(text=pagess)

            pages = pagess.split('de ')
            pages = pages[1]
            pages = pages.replace(" ", '')
            pages = int(pages)

        p = 0
        v = 1
        pos = 0
        n = 1
        em = [pag0]
        try:
            while p != pages:
                p += 1

                url = f"https://getgamez.net/page/{p}/?s={game}&post_type=post"

                resp = requests.get(url, headers=headers)
                soup = BeautifulSoup(resp.text, 'html5lib')

                va = f"{v}"
                pa = f"pag{va}"
                pa = Page(title=n_g, description="\u200b", color=discord.Color.blue())

                for x in soup.find_all('a', class_='thumb hover-effect'):
                    for z in x.find_all('span'):
                        pa.add_field(name=f"{n}. {z.get('aria-label')}", value="\u200b", inline=False)
                        n +=1

                pagess = pagess.replace(f" {pos} ", f' {p} ')
                pa.set_footer(text=pagess)

                em.append(pa)

                v +=1
                pos +=1

            menu = PaginatedMenu(ctx)
            menu.add_pages(em)
            await msg.delete()
            await menu.open()

        except:
            embed = discord.Embed(
                title=n_g,
                description='NO SE HAN ENCONTRADO RESULTADOS',
                color=discord.Color.red()
            )
            await msg.delete()
            await ctx.send(embed=embed)


@client.command()
async def des_game(ctx, pos: int, *, game: str):  # sourcery no-metrics
    if ctx.message.channel.id == 862051117349339136:
        embed = discord.Embed(
            title="Espera...",
            description="Esto puede tardar unos minutos",
            color=discord.Color.orange()
        )
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        msg = await ctx.send(embed=embed)

        game = game.replace(' ', '+')

        n_g = game.replace('+', ' ')
        n_g = n_g.upper()

        url = f"https://getgamez.net/?s={game}&post_type=post"


        ga = 0
        p = 0
        pos = int(pos)
        repeat = True
        while repeat:
            p += 1


            url = f"https://getgamez.net/page/{p}/?s={game}&post_type=post"

            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'html5lib')

            for x in soup.find_all('a', class_='thumb hover-effect'):
                ga +=1
                if ga == pos:

                    for z in x.find_all('span'):
                        ga_n = z.get('aria-label')

                    link = x.get('href')


                    respg = requests.get(link, headers=headersg)
                    soupg = BeautifulSoup(respg.text, 'html5lib')

                    for x in soupg.find_all('time'):
                        for z in x.find_all('svg'):
                            date = z.next_sibling

                    for x in soupg.find_all('span', class_='download'):
                        for z in x.find_all('svg'):
                            downloads = z.next_sibling


                    ##
                    embed = discord.Embed(
                        title=ga_n,
                        description=f"📅 {date}⠀⠀|⠀⠀ 📥{downloads}",
                        color=discord.Color.random()
                    )
                    ##

                    f = open('sr.txt', '+a', encoding='utf-8')              

                    for x in soupg.find_all('ul'):
                        if (
                            x.get('id', [])
                            not in [
                                'menu-main',
                                'menu-helpful-links',
                            ]
                            and 'sub-menu' not in x.get('class', [])
                        ) and 'OS' in x.get_text():

                            for z in x.find_all('li'):
                                f.write(z.get_text() + '\n')
                            f.close()

                            with open('sr.txt', 'r', encoding='utf-8') as f:
                                fw = f.read()

                                embed.add_field(name='System Requirements:', value=fw, inline=False)

                            f.close()

                            os.remove('sr.txt')

                            break

                    for x in soupg.find_all('meta'):
                        if x.get('property') == 'og:image':
                            thumb = x.get('content')
                            embed.set_thumbnail(url=thumb)
                

                    for x in soupg.find_all('a'):
                        if x.get('target') == '_blank' and x.get_text() in [
                            'Wait for Crack ⏱ Check Crack-Status',
                            'FREE DOWNLOAD',
                        ]:

                            des_url = x.get('href')

                            await msg.delete()

                            await buttons.send(
                                embed = embed,
                                channel = ctx.channel.id,
                                components = [
                                    ActionRow([
                                            Button(
                                                    label = "DESCARGAR",
                                                    style = ButtonType().Link,
                                                    url = des_url
                                                )
                                        ])
                                ]

                                )



                    repeat = False
                    break

                elif ga > pos:
                    embed = discord.Embed(
                        title=n_g,
                        description='NO SE HA ENCONTRADO NINGÚN RESULTADO',
                        color=discord.Color.red()
                    )
                    embed.add_field(name='Comando:', value='!des_game [nº] [nombre del juego]')
                    embed.add_field(name='[nº]', value='El número de la posición del juego ```Comando: !game [nombre del juego]```')

                    await msg.delete()
                    await ctx.send(embed=embed)

                    repeat = False
                    return


            if p > pos:
                embed = discord.Embed(
                    title=n_g,
                    description='NO SE HA ENCONTRADO NINGÚN RESULTADO',
                    color=discord.Color.red()
                )
                embed.add_field(name='Comando:', value='!des_game [nº] [nombre del juego]')
                embed.add_field(name='[nº]', value='El número de la posición del juego ```Comando: !game [nombre del juego]```')

                await msg.delete()
                await ctx.send(embed=embed)

                repeat = False
                return


@client.command()
async def ayuda(ctx):
    if ctx.message.channel.id == 862051117349339136:
        ayuda = Page(title="AYUDA", description="Estos son los comandos disponibles:", color=discord.Color.gold())
        ayuda.add_field(name="!game [nombre del juego/programa]", value="Buscar los juegos/programas disponibles", inline=False)
        ayuda.add_field(name="!des_game [nº posición en !game [nombre del juego]] [nombre del juego/programa]", value="Descargar el juego/programa", inline=False)
        ayuda.add_field(name='!problemas', value='Solucinar los problemas más comunes', inline=False)
        ayuda.add_field(name="En las siguientes páginas hay preguntas frecuentes 🡆", value="\u200b", inline=False)
        ayuda.set_footer(text="Página 0 de 6")

        ayuda1 = Page(title="¿Cómo descargar, instalar y jugar a un juego?", description='Cómo descargar e instalar un juego (Guía)', color=discord.Color.green())
        ayuda1.add_field(name='Paso 1 - Elige el juego que quieres descargar', value='Busca el juego que quieras con el comando ``!game [juego]``, y luego pone el comando ``!des_game [nº] [juego]`` para descargar el juego.', inline=False)
        ayuda1.add_field(name='Paso 2 - Descargar el juego', value='Ahora puedes descargar el juego en shareurl.cc (para los archivos más grandes, dividimos el archivo en partes de 5 GB). Es importante que hayas descargado todas las partes (si son varias). De lo contrario, el juego no funciona. Puedes elegir entre diferentes filehosters (mega.nz, megaup.net, uploaded.net y otros).', inline=False)
        ayuda1.add_field(name='Paso 3 - Descomprimir los archivos', value='Después de descargar los ficheros (archivos) hay que descomprimirlos. Si hay varios archivos, hay que descomprimirlos todos al mismo tiempo. Si no puedes descomprimirlos, necesitarás [WinRar](https://shareurl.cc/bucket/ee702a6b-8b04-4f28-ac55-6eb6d8d407d2) para solucionarlo.', inline=False)
        ayuda1.add_field(name='Paso 4 - Instalar el juego', value='Una vez descomprimidos todos los archivos, encontrarás un archivo ISO. Puedes abrir el archivo ISO con un doble clic. El archivo ISO contiene un programa de instalación. Puedes iniciar el setup e instalar el juego.\n**A veces no es necesaria la instalación y puedes iniciar el juego directamente desde un lanzador.**', inline=False)
        ayuda1.add_field(name='Paso 5 - Crackear y jugar al juego', value='Después de instalar el juego tienes que copiar todos los archivos de la carpeta "SKIDROW" o "CODEX" o "CRACK" o "PLAZA" o "CPY" o "TiNYiSO" en la carpeta de instalación del juego. Si lo has hecho, podrás jugar al juego de forma gratuita.', inline=False)
        ayuda1.set_footer(text='Página 1 de 6')

        ayuda2 = Page(title="¿Dónde puedo encontrar la clave de descifrado o la contraseña de mega.nz?", description='Si necesita una clave de descifrado (para mega.nz) siempre encontrará la clave en shareurl.cc. Mira aquí:', color=discord.Color.green())
        ayuda2.set_image(url='https://getgamez.net/wp-content/uploads/2019/06/mega.nz-getgamez-key.png')
        ayuda2.set_footer(text='Página 2 de 6')

        ayuda3 = Page(title="¿Por qué hay que dividir el juego en 5GB / parte?", description='La mayoría de los proveedores de intercambio de archivos han limitado el límite de subida a 5 GB por archivo. Para poder utilizar el mayor número posible de proveedores de intercambio de archivos, hemos fijado el límite por archivo en 5 GB.', color=discord.Color.green())
        ayuda3.set_footer(text='Página 3 de 6')

        ayuda4 = Page(title="¿En qué idioma están disponibles los cracks?", description='Los cracks están disponibles en su mayoría en los idiomas que soportan el juego original.', color=discord.Color.green())
        ayuda4.set_footer(text='Página 4 de 6')

        ayuda5 = Page(title="¿Es legítimo y seguro? ¿Puedo tener malware?", description='Todos los archivos son analizados en busca de virus y malware antes de ser cargados y publicados. Así que puedes descargar los archivos de forma segura.', color=discord.Color.green())
        ayuda5.set_footer(text='Página 5 de 6')

        ayuda6 = Page(title="Consejos (opcional)", description='\u200b', color=discord.Color.green())
        ayuda6.add_field(name="Utilice siempre una VPN.", value="Cuando descargues archivos, utiliza siempre una VPN para que seas anónimo en la red y nadie pueda rastrearlos. [Aquí encontrarás la mejor VPN con la mayor velocidad de descarga.](https://windscribe.com)", inline=False)
        ayuda6.add_field(name="¡MEGA.NZ sin límites! (sin cuenta premium)", value='Aquí tienes una forma de descargar todos los archivos de mega.nz que quieras sin necesidad de tener una cuenta. [DESCARGAR](https://shareurl.cc/bucket/e9c8b1ab-c868-4964-a39f-7576c05ee0cf)', inline=False)
        ayuda6.set_footer(text='Página 6 de 6')


        menu = PaginatedMenu(ctx)
        menu.add_pages([ayuda, ayuda1, ayuda2, ayuda3, ayuda4, ayuda5, ayuda6])
        await menu.open()

@client.command()
async def problemas(ctx):
    if ctx.message.channel.id == 862051117349339136:
        pro = Page(title='Solucionar los problemas', description="Estos son los problemas más comunes\n🢂", color=discord.Color.gold())
        pro.set_footer(text="Página 0 de 4")

        pro1 = Page(title="“Faltan archivos .DLL o el error .DLL no se encuentra”", description="Cuando hayas instalado un juego en tu ordenador, es posible que te aparezca el error 'Missing .DLL File'. Para solucionar este problema debes tener instalado DirectX en tu ordenador. Asegúrate siempre de tener instalada la última versión de los siguientes programas para solucionar cualquier error de 'Sistema' y otro tipo de problemas.\n\nSi tienes un error de 'pantalla negra', estos programas deberían arreglar ese problema también. Asegúrese de descargar e instalar todos los siguientes programas para actualizar el controlador de su GPU:\n\nDirectX: https://www.microsoft.com/en-us/download/confirmation.aspx?id=35\nvcredist_x86: https://www.microsoft.com/en-us/download/confirmation.aspx?id=5555\nvcredist_x64: https://www.microsoft.com/en-us/download/confirmation.aspx?id=14632\n\nSi el error 'Missing .DLL File' persiste, asegúrese de que su software antivirus o Windows Defender está desactivado. Estos programas antivirus pueden haber eliminado un archivo .DLL específico en tu ordenador, que es la causa de este error. Una vez deshabilitados los programas, reinstala el juego y el problema debería solucionarse.", color=discord.Color.green())
        pro1.set_footer(text='Página 1 de 4')

        pro2 = Page(title="“Extraer archivos .Zip, .Iso y .Rar en Windows o Mac”", description='Cuando has descargado un juego, en la mayoría de las ocasiones tienes que extraer el archivo. Para ello necesitarás el programa gratuito llamado WinRAR. Puedes descargar WinRAR [aquí](https://shareurl.cc/bucket/ee702a6b-8b04-4f28-ac55-6eb6d8d407d2). Una vez instalado el programa, haz clic con el botón derecho del ratón en el archivo que quieras extraer y haz clic en "Extraer aquí".', color=discord.Color.green())
        pro2.set_footer(text='Página 2 de 4')

        pro3 = Page(title="“Mi juego se bloquea o no se guarda”", description='En algunos casos el juego que has instalado puede no funcionar en tu ordenador. Hay una solución fácil para esto que siempre deberías usar para cualquier juego:\n\nHaz clic con el botón derecho del ratón en el juego que quieres jugar > Propiedades > Compatibilidad > Haz clic en "Ejecutar este programa como administrador" > Haz clic en Aplicar y Aceptar.', color=discord.Color.green())
        pro3.set_footer(text='Página 3 de 4')

        pro4 = Page(title="“Cuando inicio un juego se abre la tienda de Steam”", description="Asegúrate de que si el instalador muestra 'CODEX' o 'PLAZA', tendrás que hacer clic en 'Copiar el contenido del directorio CODEX a installdir' antes de hacer clic en el botón Instalar. En algunos casos tendrás que copiar manualmente los 'archivos crack' a la carpeta de instalación del juego.\n\nTambién ten en cuenta que tu antivirus puede haber eliminado archivos .dll específicos que hacen que el juego funcione. Asegúrate de desactivarlos para que no borren ningún archivo .dll. Todos los archivos están 100% limpios, así que no tienes que preocuparte.", color=discord.Color.green())
        pro4.set_footer(text='Página 4 de 4')


        menu = PaginatedMenu(ctx)
        menu.add_pages([pro, pro1, pro2, pro3, pro4])
        await menu.open()


#keep_alive()

client.run(token)