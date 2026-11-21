#!/usr/bin/env python
#_*_ coding: utf8 _*_

import discord
from discord.ext import commands
import time
import random
import string
import requests
from bs4 import BeautifulSoup
from mcstatus import MinecraftServer
import hostbot
from hostbot import keep_alive
from datetime import datetime



client = commands.Bot(command_prefix='!', help_command=None)

token = "YOUR_BOT_TOKEN_HERE"


@client.event
async def on_ready():
    print(f"Estoy listo :)".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!ayuda"))
'''    channelready = client.get_channel(804006326710829126)
    await channelready.send("ESTOY ONLINE!!")'''



@client.command()
async def reportar(ctx, member: discord.Member =None, *,reason =None):
    channel_report = client.get_channel(804061616819011604)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

    else:

        if member == None or member == ctx.message.author:
            await ctx.send("NO PUEDES REPORTARE A TI MISMO :V")
            return
        elif reason == None:
            await ctx.send("PORQUE LE REPORTAS? PON UN MENSAJE!!")
            return
        channelmods = client.get_channel(803749826373615638)
        embed = discord.Embed(
            title = "REPORTE:",
            description = "A continuación veras el reporte:",
            colour = discord.Colour.red()
                )
        embed.set_author(name=ctx.message.author, url="https://www.itmplatform.com/lib/uploads/36978940_m-300x230.jpg", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://www.reportedelectura.com/wp-content/uploads/2019/05/que-es-un-reporte.jpg")
        embed.add_field(name=member, value=reason)
        embed.set_footer(text="El reporte se ha enviado correctamente a los moderaores👨‍💻")
        
        await ctx.send(embed=embed)
        await channelmods.send(embed=embed)


@client.command()
async def banxd(ctx, member: discord.Member =None,):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        hack3r = discord.utils.get(ctx.guild.roles, id=802255880435138612)
        programador = discord.utils.get(ctx.guild.roles, id=803698587993243678)
        if member == None:
            await ctx.send("A QUIEN BANEAS? :V")
            return
        elif member == ctx.message.author or hack3r in member.roles:
            await ctx.send("TU ERES TONTO??")
            return
        elif programador in member.roles:
            await ctx.send("Al dueño no se le toca :V")
            await ctx.send(f"Te voy a banear {ctx.message.author.mention}")
            return
        await ctx.send(f"Baneando a {member.mention}...")
        time.sleep(1.5)
        await ctx.send("    3")
        time.sleep(1)
        await ctx.send("   2")
        time.sleep(1)
        await ctx.send("  1")


@client.command()
async def ayuda(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        embed = discord.Embed(
            title = "Comandos:",
            description = "Estos son los comandos disponibles:",
            colour = discord.Colour.blue()
                )

        embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://tecnonucleous.com/content/images/2018/09/powershell-comandos-red.jpg")
        embed.add_field(name="!blog", value="Blog de Cegamer 🧾")
        embed.add_field(name="!phishing", value="Que es? Para que sirve? 🖱️")
        embed.add_field(name="!hacking", value="Todo el hacking que hemos aportado al server ⌨️")
        embed.add_field(name="!bins", value="Que es? Para que sirve? 🖱️")
        embed.add_field(name="!shellphish", value="Herramienta de hacking (Phishing) 😎")
        embed.add_field(name="!saycheese", value="Herramienta de hacking (Sacar fotos) 😎")
        embed.add_field(name="!generador", value="Generador de códigos")
        embed.add_field(name="!banxd @usuario", value="Banear a alguien xd")
        embed.add_field(name="!server", value="Saber si el servidor de minecraft esta abierto o cerrado")
        embed.add_field(name="!plsserver", value="Solicitar que habran el servidor de minecraft")
        embed.add_field(name="!reportar @usuario Justificación", value="Reportar a alguien📝")
        embed.add_field(name="!reglas", value="Canal de las reglas del servidor 📝")
        embed.add_field(name="!mods", value="Todos los moderadores de este servidor 📝")
        embed.add_field(name="!bot", value="Información sobre mi (bot) 😏")
        embed.set_footer(text="👨‍💻Próximamente habrán más comandos...👨‍💻")

        await ctx.send(embed=embed)


@client.command()
async def blog(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("Blog Cegamer: En el blog encontrarás muchas cosas, sobre todo cosas de hacking.\nBlog: https://cegameryt.blogspot.com/")


@client.command()
async def phishing(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("Que es? Para que sirve? : Phishing es un término informático que distingue a un conjunto de técnicas que persiguen el engaño a una víctima ganándose su confianza haciéndose pasar por una persona, empresa o servicio de confianza, para manipularla y hacer que realice acciones que no debería realizar.")


@client.command()
async def hacking(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("**Hacking:**\nTodo el hacking que hemos aportado está en el canal <#789320785969283102> , cualquer pregunta se lo puedes preguntar a los MODERADORES")


@client.command()
async def bins(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("**Bin:**\nSe llaman así porque un BIN son los primeros seis números de una tarjeta que permiten a los bancos identificar el tipo de plástico, ya sea una tarjeta de crédito o débito.\n**Carding:**\nTraducción del inglés-Carding es un término que describe el tráfico de tarjetas de crédito, cuentas bancarias y otra información personal en línea. Las actividades también abarcan la adquisición de detalles y técnicas de lavado de dinero. Los sitios modernos de tarjetas han sido descritos como entidades comerciales de servicio completo.")


@client.command()
async def shellphish(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("ShellPhish:\n  -Definición: Es una herramienta de hacking, concretamente de phishing.\n  -Como usar shellphish: https://cegameryt.blogspot.com/2020/12/cuidado-asi-de-facil-hackean-cuentas-en.html")


@client.command()
async def saycheese(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("Saycheese:\n  -Definicion: Es una herramienta de hacking, concretamente para sacar fotos a alguien mediante un enlace web.\n  -Como usar saycheese: https://cegameryt.blogspot.com/2020/12/hackear-la-camara-de-cualquier.html")


@client.command()
async def mods(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        embed = discord.Embed(
            title="MODERADORES",
            description="Actualmente estos son los moderadores:",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url="https://image.freepik.com/vector-gratis/ilustracion-cabeza-gato-espia_68946-439.jpg")
        embed.add_field(name="JASA2347", value='\u200b', inline=False)
        embed.add_field(name="Mr.Cortez0110", value='\u200b', inline=False)
        embed.add_field(name="Murcielago sin alas", value='\u200b', inline=False)
        embed.add_field(name="29Davidm", value='\u200b', inline=False)
        embed.add_field(name="cuchillo", value='\u200b', inline=False)
        embed.set_footer(text="UwU")

        await ctx.send(embed=embed)


@client.command()
async def bot(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("Este bot esta creado por @cuchillo#7116, si quereis un bot para vuestro server de discord, contactarle 😉 !!")


@client.command()
async def reglas(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        await ctx.send("Canal de las reglas: <#626217429193850880> ")


@client.command()
async def generador(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        embed = discord.Embed(
            title = "GENERADOR:",
            description = "Estos son los comandos disponibles:",
            colour = discord.Colour.darker_grey()
                )

        embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://i.blogs.es/22f8f6/gifts-5817555_1920/1366_2000.jpg")
        embed.add_field(name="!googleplay", value="Generador de códigos Google Play")
        embed.add_field(name="!ps4", value="Generador de códigos PS4")
        embed.add_field(name="!steam", value="Generador de códigos Steam")
        embed.add_field(name="!amazon", value="Generador de códigos Amazon")
        embed.add_field(name="!netflix", value="Generador de códigos Netflix")
        embed.add_field(name="!spotify", value="Generador de códigos Spotify")
        embed.add_field(name="!nitro", value="Generador de códigos Discord Nitro")
        embed.add_field(name="!robux", value="Generador de códigos Roblox")
        embed.add_field(name="!whatsapp", value="Generador de enlaces de whatsapp")
        embed.add_field(name="- - - - - - - - - - - - ", value="IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!", inline=False)

        await ctx.send(embed=embed)


@client.command()
async def googleplay(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !googleplay Cantiad")
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !googleplay Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {cantidad} CÓDIGOS GOOGLE PLAY :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS GOOGLE PLAY :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.light_gray()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://www.frikipandi.com/wp-content/uploads/2020/12/google.png")
                embed.add_field(name="Google Play", value=f"Enviando {cantidad} códigos de Google play! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.light_gray()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://www.frikipandi.com/wp-content/uploads/2020/12/google.png")
                embed.add_field(name="Tus códigos de Google Play:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                ValorGooglePlay = 1
                while ValorGooglePlay <= quantity:
                    GooglePlay = ('').join(random.choices(string.digits, k=16))
                    await ctx.author.send(GooglePlay)
                    ValorGooglePlay += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("***IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!***")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def ps4(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !ps4 Cantiad")
            return
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !ps4 Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} CÓDIGOS PS4 :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS PS4 :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.dark_blue()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://i.pinimg.com/originals/ca/be/7a/cabe7a7e2371300bc8efa3f19e4808a2.jpg")
                embed.add_field(name="PS4", value=f"Enviando {quantity} códigos de PS4! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.dark_blue()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://i.pinimg.com/originals/ca/be/7a/cabe7a7e2371300bc8efa3f19e4808a2.jpg")
                embed.add_field(name="Tus códigos de PS4:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                ValorPS4 = 1
                while ValorPS4 <= quantity:
                    PS4 = ('').join(random.choices(string.ascii_uppercase, k=12))
                    await ctx.author.send(PS4)
                    ValorPS4 += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def steam(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !steam Cantiad")
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !steam Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} CÓDIGOS STEAM :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS STEAM :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.blue()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://mk0uploadvrcom4bcwhj.kinstacdn.com/wp-content/uploads/2018/12/SteamLogo.jpg")
                embed.add_field(name="Steam", value=f"Enviando {quantity} códigos de Steam! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.blue()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://mk0uploadvrcom4bcwhj.kinstacdn.com/wp-content/uploads/2018/12/SteamLogo.jpg")
                embed.add_field(name="Tus códigos de Steam:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                ValorSteam = 1
                while ValorSteam <= quantity:
                    Steam15 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
                    Steam25 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
                    Steam17 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=17))

                    vars = [Steam15, Steam25, Steam17]
                    codess = random.sample(vars, 1)
                    codesss = str(codess)
                    gg = codesss.replace('[', '').replace(']', '').replace("'", "")
                    await ctx.author.send(gg)
                    ValorSteam += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def amazon(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !amazon Cantiad")
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !amazon Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} CÓDIGOS AMAZON :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS AMAZON :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.orange()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1000px-Amazon_logo.svg.png")
                embed.add_field(name="Amazon", value=f"Enviando {quantity} códigos de Amazon! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.orange()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1000px-Amazon_logo.svg.png")
                embed.add_field(name="Tus códigos de Amazon:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                Valoramazon = 1
                while Valoramazon <= quantity:
                    Amazon = ('').join(random.choices(string.ascii_uppercase + string.digits, k=4)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=6)) + '-' + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
                    await ctx.author.send(Amazon)
                    Valoramazon += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def netflix(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !netflix Cantiad")
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !netflix Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} CÓDIGOS NETFLIX :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS NETFLIX :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.red()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwngDBuChyi5LOiP4Od1GOqyczL6Sx9I-Ujk6rCP0Sg=s900-c-k-c0x00ffffff-no-rj")
                embed.add_field(name="Netflix", value=f"Enviando {quantity} códigos de Netflix! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.orange()
                    )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwngDBuChyi5LOiP4Od1GOqyczL6Sx9I-Ujk6rCP0Sg=s900-c-k-c0x00ffffff-no-rj")
                embed.add_field(name="Tus códigos de Netflix:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                Valornetflix = 1
                while Valornetflix <= quantity:
                    Netflix = "LEQ" + ('').join(random.choices(string.ascii_uppercase, k=2)) + ('').join(random.choices(string.digits, k=6))
                    await ctx.author.send(Netflix)
                    Valornetflix += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def spotify(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !spotify Cantiad")
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !spotify Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} CÓDIGOS SPOTIFY :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS SPOTIFY :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.green()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://crudotransparente.com/wp-content/uploads/2020/04/spotify-logo.png")
                embed.add_field(name="Spotify", value=f"Enviando {quantity} códigos de Spotify! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.green()
                    )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://crudotransparente.com/wp-content/uploads/2020/04/spotify-logo.png")
                embed.add_field(name="Tus códigos de Spotify:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                Valorspotify = 1
                while Valorspotify <= quantity:
                    Spotify = ('').join(random.choices(string.digits, k=19))
                    await ctx.author.send(Spotify)
                    Valorspotify += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def nitro(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !nitro Cantiad")
            return
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !nitro Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} CÓDIGOS DISCORD NITRO :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS DISCORD NITRO :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.dark_magenta()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/775428276772274177/781962440870592542/discord-nitro-games-oyun-servisini-kapatiyor-687x400.jpg")
                embed.add_field(name="Discord Nitro", value=f"Enviando {quantity} códigos de Discord Nitro! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.dark_magenta()
                    )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/775428276772274177/781962440870592542/discord-nitro-games-oyun-servisini-kapatiyor-687x400.jpg")
                embed.add_field(name="Tus códigos de Discord Nitro:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                Valornitro = 1
                while Valornitro <= quantity:
                    Nitro = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters.upper(), k=1)) + ('').join(random.choices(string.ascii_letters + string.digits, k=15))
                    await ctx.author.send(Nitro)
                    Valornitro += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def robux(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !robux Cantiad")
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !robux Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} CÓDIGOS ROBLOX :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 CÓDIGOS ROBLOX :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.red()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://i.pinimg.com/originals/d2/99/71/d29971dbbf87af85cac585fbea487ac1.png")
                embed.add_field(name="Roblox", value=f"Enviando {quantity} códigos de Roblox! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.orange()
                    )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://i.pinimg.com/originals/d2/99/71/d29971dbbf87af85cac585fbea487ac1.png")
                embed.add_field(name="Tus códigos de Roblox:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                Valorroblox = 1
                while Valorroblox <= quantity:
                    Roblox = ('').join(random.choices(string.digits, k=3)) + "-" + ('').join(random.choices(string.digits, k=3)) + "-" + ('').join(random.choices(string.digits, k=4))
                    await ctx.author.send(Roblox)
                    Valorroblox += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS CÓDIGOS SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")


@client.command()
async def whatsapp(ctx, cantidad =None):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    else:
        try:
            quantity = int(cantidad)
        except:
            await ctx.send("Pon una cantidad :V\nComando: !whatsapp Cantiad")
        if cantidad == None:
            await ctx.send("Escoje una cantidad :V\nComando: !whatsapp Cantiad")
            return
        else:
            if quantity <= 0:
                await ctx.send(f"NO PUEDES GENERAR {quantity} ENLACES WHATSAPP :V")
                return
            elif quantity > 20:
                await ctx.send(f"NO PUEDES GENERAR MAS DE 20 ENLACES WHATSAPP :V")
                return
            else:
                embed = discord.Embed(
                    title = "GENERATOR",
                    colour = discord.Colour.green()
                        )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://1000marcas.net/wp-content/uploads/2019/11/WhatsApp-logo.png")
                embed.add_field(name="Whatsapp", value=f"Enviando {quantity} enlaces de Whatsapp! Revisa md!", inline=False)
                embed.add_field(name="Créditos: ", value="Discord: cuchillo#7116", inline=False)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                    title = "Codes",
                    colour = discord.Colour.orange()
                    )
                embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url="https://1000marcas.net/wp-content/uploads/2019/11/WhatsApp-logo.png")
                embed.add_field(name="Tus enlaces de Whatsapp:", value="↓", inline=False)
                await ctx.author.send(embed=embed)

                Valorwhatsapp = 1
                while Valorwhatsapp <= quantity:
                    population = string.ascii_letters + string.digits
                    whatsapp = "https://chat.whatsapp.com/" + ('').join(random.choices(population, k=22))
                    await ctx.author.send(whatsapp)
                    Valorwhatsapp += 1
                    
                await ctx.author.send(".")
                await ctx.author.send("IMPORTANTE: LOS ENLACES SON  RANDOM! PERO COINCIDEN EN LOS REALES! SOLO TIENES QUE TENER SUERTE!!")
                await ctx.author.send(".")
                await ctx.author.send("CREDITOS: cuchillo#7116 (Discord)")



@client.command()
async def server(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    
    else:
        server = MinecraftServer.lookup("ServidorDisCegamer.aternos.me")
        status = server.status()
        if status.players.online == 0:
            await ctx.send("El servidor esta CERRADO")
        else:
            await ctx.send("El servidor esta ABIERTO")
            await ctx.send(f"El servidor tiene {status.players.online} jugadores y respondió en {status.latency} ms")
            latency = server.ping()
            await ctx.send("El servidor respondió en {latency} ms")


@client.command()
async def plsserver(ctx):
    channel_report = client.get_channel(804006326710829126)
    if channel_report != ctx.message.channel:
        rolavisado = discord.utils.get(ctx.guild.roles, id=801904145631674419)
        rolprimera = discord.utils.get(ctx.guild.roles, id=801905767200325694)
        rolsegunda = discord.utils.get(ctx.guild.roles, id=801908448044122123)

        if rolsegunda in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL CONO DE LA VERGÜENZA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, CONO DE LA VERGÜENZA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!!")
            await channelfalta.send("MODERADORES, ATENTOS AL PERSONAJE!!")

        elif rolprimera in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL SEGUNDA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, SEGUNDA FALTA DE: ")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")

        elif rolavisado in ctx.message.author.roles:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL PRIMERA FALTA POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, PRIMERA FALTA DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")


        else:
            channelfalta = client.get_channel(803749826373615638)
            await ctx.send("SE TE HA AÑADIDO EL ROL AVISADO POR NO USAR BIEN LOS CANALES ADECUADOS ")
            await ctx.send(ctx.message.author.mention)
            await channelfalta.send("MODERADORES, AVISADO DE:")
            await channelfalta.send(ctx.message.author)
            await channelfalta.send("MODERADORES, AÑADIRLE EL ROL!")
    
    else:
        modchannel = client.get_channel(803749826373615638)
        embed = discord.Embed(
            title = "MINECRAFT",
            colour = discord.Colour.dark_green()
                )
        embed.set_author(name=ctx.message.author, url="https://youtu.be/sVhRpRYdfjU", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/512dVKB22QL._AC_UL600_SR600,600_.png")
        embed.add_field(name="Minecraft server", value=f"{ctx.message.author} ha solicitado que abran el servidor de minecraft.", inline=False)
        embed.set_footer(text="Se ha enviado correctamente al chat de los moderadores.")
        
        await ctx.send(embed=embed)
        await modchannel.send(embed=embed)


keep_alive()



client.run(token)
