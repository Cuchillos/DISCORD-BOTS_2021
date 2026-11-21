#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
import discord
from discord.ext import commands

import requests
import os
##############################

client = commands.Bot(command_prefix='!', help_command=None)
token = "YOUR_BOT_TOKEN_HERE"


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!ayuda", url="https://www.twitch.tv/cuchillop"))
    print("Estoy listo :)")


@client.command()
async def ayuda(ctx):
    role = discord.utils.get(ctx.guild.roles, id=812326538506141726)
    if role in ctx.message.author.roles and ctx.message.channel.id == 834920006214221874:

        embed = discord.Embed(
        title = "Comando:",
        description = "Como se utiliza?",
        colour = discord.Colour.green()
            )

        embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://www.qrtag.net/api/qr_10.png?url=https://youtu.be/35XFAkwmU4c")
        embed.add_field(name="!qr [link] [con o sin] [tamaño] [png o svg]", value="!qr [Link completo de la web] [CON fondo transparente o SIN fondo transparente(blanco)] [Tamaño de la imagen (poner un número) (recomendado: 10)] [Formato de la imagen (png o svg)]")
        embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

        await ctx.send(embed=embed)

    elif role in ctx.message.author.roles and ctx.message.channel.id == 816064923435401287:
        pass
    else:
        await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")


@client.command()
async def qr(ctx, link=None, transparente=None, tamaño=None, formato=None):
    role = discord.utils.get(ctx.guild.roles, id=812326538506141726)
    if role in ctx.message.author.roles and ctx.message.channel.id == 834920006214221874:
        trans = ['con', 'sin']
        form = ['png', 'svg']
        size = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
        if link == None or 'http' not in link:
            await ctx.send(f"**Pon la página web completa :v {ctx.message.author.mention}**\n*Ejemplo: https://example.com*")
        elif transparente == None or transparente not in trans:
            await ctx.send(f"**Indica si quieres que sea CON transparencia o SIN transparencia :v {ctx.message.author.mention}**\n*Ejemplo: con*")
        elif tamaño == None or tamaño not in size:
            await ctx.send(f"**Indica el tamaño de la imagen (entre el 3 y el 25 (recomendado: 10)) :v {ctx.message.author.mention}**\n*Ejemplo: 10*")
        elif formato == None or formato not in form:
            await ctx.send(f"**Indica el formato de la imagen, png o svg :v {ctx.message.author.mention}**\n*Ejemplo: png*")
        else:
            if transparente == 'con':
                try:
                    response = requests.get(f"https://qrtag.net/api/qr_transparent_{tamaño}.{formato}?url={link}")

                    f = open(f'QR.{formato}','wb')
                    f.write(response.content)
                    f.close()

                    await ctx.author.send(f"{link} ⤵️")
                    await ctx.author.send(file=discord.File(f'QR.{formato}'))
                    await ctx.send(f"***Código QR ✅\n{ctx.message.author.mention} md***")
                    os.remove(f'QR.{formato}')
                except:
                    await ctx.send("***Código QR ❌***\n*Ha ocurrido un error*")

            else:
                try:
                    response = requests.get(f"https://qrtag.net/api/qr_{tamaño}.{formato}?url={link}")

                    f = open(f'QR.{formato}','wb')
                    f.write(response.content)
                    f.close()

                    await ctx.author.send(f"{link} ⤵️")
                    await ctx.author.send(file=discord.File(f'QR.{formato}'))
                    await ctx.send(f"***Código QR ✅\n{ctx.message.author.mention} md***")
                    os.remove(f'QR.{formato}')
                except:
                    await ctx.send(f"***Código QR ❌***\n*Ha ocurrido un error*\n{ctx.message.author.mention}")

    elif role in ctx.message.author.roles and ctx.message.channel.id == 816064923435401287:
        pass

    else:
        await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")


client.run(token)
