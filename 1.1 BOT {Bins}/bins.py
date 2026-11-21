#!/usr/bin/env python
#_*_ coding: utf8 _*_

########################################
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, cooldown, BucketType
import random
import string
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import json
import hostbot
from hostbot import keep_alive
########################################

client = commands.Bot(command_prefix='!', help_command=None)
token = "YOUR_BOT_TOKEN_HERE"


headers = CaseInsensitiveDict()
headers["authority"] = "bincheck.io"
headers["cache-control"] = "max-age=0"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "none"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-user"] = "?1"
headers["sec-fetch-dest"] = "document"
headers["accept-language"] = "es-ES,es;q=0.9"
headers["cookie"] = "XSRF-TOKEN=eyJpdiI6IkFwdnoxbDBYQm5qZUN3RDdaRkZENkE9PSIsInZhbHVlIjoiRWV1cGwyYzZvVXVsTGIxRUJRS3QvUWZDQ0Q5SVd4dE1BZ3VMM1N3TXVMdmRnM1c5bmpuZ0MvVlBrRUVFcmY4UVp5RzVGbWhET09sdUdiT1BLVTMwcEk4ZStsZlV3dUJHYmZnM01NRjlmMlRhSUR1bUkxZkQ2dUx6QjZCMWRyOVAiLCJtYWMiOiJmYjQ2YjFkZjkyMjE2ZGEwOTM5MWJhMTJiZDAxY2JlMDQ1MTkwYTc3ODg5MjJhOTVlNzNlMGExMDBmZThkZDQzIn0%3D; laravel_session=eyJpdiI6InU0ZVNnK1NWTG5pRWFWTUZVOUJ4YlE9PSIsInZhbHVlIjoieHpOLzhMMzU2cDFlRUc1RmErYi9kc04wQnZ0YmJScFVyR2NOMjBuNWlVcmF2VU5zVmV6RUZjNTV2TXpsaUJBTDVQaURFVk14U09kcTBpK3hzZVF4N2NQclh6T1dCMWhsNXU2dk1PMTk2a0tPNU9kaXlPT1VpWU94cGRQUVl3NFYiLCJtYWMiOiJmMTc0ODkyNjA5ZGQyYWEwMTRiNWJjMjhhMWFjMjY0M2RkMjY4NTkxYmM4NzlhZWZhZmM1NDYwNTZlMDE0MDRlIn0%3D"


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!ayuda", url="https://www.twitch.tv/cuchillop"))
    print("LISTO UwU")



@client.command()
@has_permissions(administrator=True)
async def canal(ctx, channel: discord.TextChannel):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    creado = 0

    for x in content:
        if server in x:
            try:
                update = content[x]['Canal']


                with open('servidores.json', 'r+') as file:
                    content = file.read()
                    file.seek(0)
                    content = content.replace(f'{update}', f'{channel.id}')
                    file.write(content)
                    file.close()

                await ctx.send("**✅ Se ha actulizado el canal correctamente ✅**")
            except:
                await ctx.send("**❌ ERROR: No se ha podido actualizar el canal (contacta con cuchillo#7116) ❌**")

        else:

            if creado == 0:
                try:
                    with open('servidores.json', 'r+') as file:
                        content = json.load(file)

                        nuevo = {f"{server}": {"Canal": f"{channel.id}", "Premium": "False"}}
                        content.update(nuevo)
                        file.seek(0)
                        json.dump(content, file)

                        file.close()

                    await ctx.send("**✅ Se ha establecido correctamente el canal ✅**")

                    creado +=1
                        
                except:
                    await ctx.send("**❌ ERROR: No se ha podido establecer el canal (contacta con cuchillo#7116) ❌**")

@canal.error
async def canal_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("***NO TIENES PERMISOS PARA USAR ESTE COMANDO :V***")



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def ayuda(ctx):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    for x in content:
        if server in x:
            dispo += 1
            channel = content[x]['Canal']
            channel = int(channel)

            if ctx.message.channel.id == channel:
                embed = discord.Embed(
                    title = 'Comandos:',
                    description = "Estos son los comandos disponibles:",
                    color = discord.Color.purple()
                )
                embed.set_thumbnail(url='https://android-top.com/img/jwOjOUKTI2i61Gnn_IdzRFBWhAT60zDNhS7-PJx5AM0/fill/240/240/no/1/aHR0cHM6Ly9wbGF5LWxoLmdvb2dsZXVzZXJjb250ZW50LmNvbS9ReHh3SXk3Y1pHWEFPem9OYmN3SmJpRXBVb1RtdTdaMHZsZWZZUUxPWWdSMDhXUmhsWXVTWDVOMzNENTY5SWdjTnVR.png')
                embed.add_field(name="!m [cantidad]", value="Generar bins de Mastercard")
                embed.add_field(name="!v [cantidad]", value="Generar bins de Visa")
                embed.add_field(name="!ae [cantidad]", value="Generar bins de American Express")
                embed.add_field(name="!d [cantidad]", value="Generar bins de Discover")
                embed.add_field(name="!dc [cantidad]", value="Generar bins de Diners Club*")
                embed.add_field(name="!checker [bin]", value="Verificar si un bin es válido", inline=False)
                embed.set_footer(text="👨‍💻cuchillo#7116 está programando...👨‍💻")

                await ctx.send(embed=embed)



            else:
                await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")

            break


        else:
            pass

        
    if dispo == 0:
        await ctx.send("***No se ha establecido ningún canal, avisa al admin\n```Comando:\n!canal #canal```***")

@ayuda.error
async def ayuda_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.blue()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def checker(ctx, bin=None):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    for x in content:
        if server in x:
            dispo += 1
            channel = content[x]['Canal']
            channel = int(channel)

            if ctx.message.channel.id == channel:
                if bin == None:
                    await ctx.send(f"***:V {ctx.message.author.mention}***")
                
                else:

                    try:
                        int(bin)

                        
                        await ctx.message.delete()

                        await ctx.send(f"*Verificando bin {ctx.message.author.mention}...*\nMira md")

                        resp = requests.get(f"https://bincheck.io/bin/{bin}", headers=headers)
                        soup = BeautifulSoup(resp.text, 'html5lib')


                        correct = 0
                        for x in soup.find_all('h4', class_='alert-heading'):
                            if 'invalid!' in x.get_text():
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=bin)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)
                                correct =+1
                                break

                        if correct == 0:
                            embed = discord.Embed(
                                title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                description = "BIN válido",
                                color = discord.Color.green()
                            )
                            embed.add_field(name="Bin:", value=bin, inline=False)

                            for x in soup.find_all('td', width="40%"):
                                if x.get_text() == 'Card Brand':
                                    embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                elif x.get_text() == 'Card Type':
                                    embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                elif x.get_text() == 'Card Level':
                                    embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                elif x.get_text() == 'Issuer Name / Bank':
                                    embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                elif x.get_text() == 'ISO Country Name':
                                    embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                else:
                                    pass

                            embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                            await ctx.author.send(embed=embed) 


                        else:
                            embed = discord.Embed(
                                title = "❌INVÁLIDO❌",
                                description = "BIN inválido",
                                color = discord.Color.red()
                            )
                            embed.add_field(name="Bin:", value=bin)
                            embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                            await ctx.author.send(embed=embed)

                    except:
                        await ctx.send(f"***BRO {ctx.message.author.mention}, eso no es un bin :v!!***")

                    dispo += 1

            else:
                await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")
            
            break

        else:
            pass

        
    if dispo == 0:
        await ctx.send("***No se ha establecido ningún canal, avisa al admin\n```Comando:\n!canal #canal```***")

@checker.error
async def checker_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.blue()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def m(ctx, cantidad=None):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    for x in content:
        if server in x:
            dispo += 1
            channel = content[x]['Canal']
            channel = int(channel)
            premium = content[x]['Premium']

            if ctx.message.channel.id == channel:
                try:
                    cantidad = int(cantidad)
                except:
                    pass

                if premium == "False":
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 5 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 5 BINS :v ({ctx.message.author.mention})*\nPara generar más el servidor tiene que ser PREMIUM")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        Mastercard = 1
                        gg = 0
                        while Mastercard <= cantidad:
                            CodigosMastercard = "5" + ('').join(random.choices(string.digits, k=5))

                            resp = requests.get(f"https://bincheck.io/bin/{CodigosMastercard}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosMastercard)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosMastercard, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1
                                Mastercard += 1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosMastercard)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)
                                Mastercard += 1                           

                            

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")
                else:
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 10 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 10 BINS :v ({ctx.message.author.mention})*")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        Mastercard = 1
                        gg = 0
                        while Mastercard <= cantidad:
                            CodigosMastercard = "5" + ('').join(random.choices(string.digits, k=5))

                            resp = requests.get(f"https://bincheck.io/bin/{CodigosMastercard}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosMastercard)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosMastercard, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1
                                Mastercard += 1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosMastercard)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                               
                                Mastercard += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")

            else:
                await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")
            
            break

        else:
            pass

        
    if dispo == 0:
        await ctx.send("***No se ha establecido ningún canal, avisa al admin\n```Comando:\n!canal #canal```***")

@m.error
async def m_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.blue()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def v(ctx, cantidad=None):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    for x in content:
        if server in x:
            dispo += 1
            channel = content[x]['Canal']
            channel = int(channel)
            premium = content[x]['Premium']

            if ctx.message.channel.id == channel:
                try:
                    cantidad = int(cantidad)
                except:
                    pass

                if premium == "False":
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 5 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 5 BINS :v ({ctx.message.author.mention})*\nPara generar más el servidor tiene que ser PREMIUM")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        Visa = 1
                        gg = 0
                        while Visa <= cantidad:
                            CodigosVisa = "4" + ('').join(random.choices(string.digits, k=5))

                            resp = requests.get(f"https://bincheck.io/bin/{CodigosVisa}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosVisa)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosVisa, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosVisa)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                               

                            Visa += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")
                else:
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 10 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 10 BINS :v ({ctx.message.author.mention})*")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        Visa = 1
                        gg = 0
                        while Visa <= cantidad:
                            CodigosVisa = "4" + ('').join(random.choices(string.digits, k=5))


                            resp = requests.get(f"https://bincheck.io/bin/{CodigosVisa}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosVisa)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosVisa, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosVisa)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                            

                            Visa += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")

            else:
                await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")

            break
        else:
            pass

        
    if dispo == 0:
        await ctx.send("***No se ha establecido ningún canal, avisa al admin\n```Comando:\n!canal #canal```***")

@v.error
async def v_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.blue()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def ae(ctx, cantidad=None):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    for x in content:
        if server in x:
            dispo += 1
            channel = content[x]['Canal']
            channel = int(channel)
            premium = content[x]['Premium']

            if ctx.message.channel.id == channel:
                try:
                    cantidad = int(cantidad)
                except:
                    pass
                if premium == "False":
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 5 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 5 BINS :v ({ctx.message.author.mention})*\nPara generar más el servidor tiene que ser PREMIUM")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        America = 1
                        gg = 0
                        while America <= cantidad:
                            CodigosAmerica = "37" + ('').join(random.choices(string.digits, k=4))


                            resp = requests.get(f"https://bincheck.io/bin/{CodigosAmerica}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosAmerica)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosAmerica, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosAmerica)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                            

                            America += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")
                else:
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 10 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 10 BINS :v ({ctx.message.author.mention})*")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        America = 1
                        gg = 0
                        while America <= cantidad:
                            CodigosAmerica = "37" + ('').join(random.choices(string.digits, k=4))

                            resp = requests.get(f"https://bincheck.io/bin/{CodigosAmerica}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosAmerica)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosAmerica, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosAmerica)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                                                        

                            America += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")

            else:
                await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")

            break

        else:
            pass

        
    if dispo == 0:
        await ctx.send("***No se ha establecido ningún canal, avisa al admin\n```Comando:\n!canal #canal```***")

@ae.error
async def ae_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.blue()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def dc(ctx, cantidad=None):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    for x in content:
        if server in x:
            dispo += 1
            channel = content[x]['Canal']
            channel = int(channel)
            premium = content[x]['Premium']

            if ctx.message.channel.id == channel:
                try:
                    cantidad = int(cantidad)
                except:
                    pass

                if premium == "False":
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 5 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 5 BINS :v ({ctx.message.author.mention})*\nPara generar más el servidor tiene que ser PREMIUM")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        Diners = 1
                        gg = 0
                        while Diners <= cantidad:
                            CodigosDiners = "36" + ('').join(random.choices(string.digits, k=4))

                            resp = requests.get(f"https://bincheck.io/bin/{CodigosDiners}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosDiners)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosDiners, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosDiners)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                            
                            

                            Diners += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")
                else:
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 10 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 10 BINS :v ({ctx.message.author.mention})*")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        Diners = 1
                        gg = 0
                        while Diners <= cantidad:
                            CodigosDiners = "36" + ('').join(random.choices(string.digits, k=4))

                            resp = requests.get(f"https://bincheck.io/bin/{CodigosDiners}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=CodigosDiners)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=CodigosDiners, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=CodigosDiners)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                                

                            Diners += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")

            else:
                await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")

            break

        else:
            pass

        
    if dispo == 0:
        await ctx.send("***No se ha establecido ningún canal, avisa al admin\n```Comando:\n!canal #canal```***")

@dc.error
async def dc_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.blue()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def d(ctx, cantidad=None):
    dispo = 0

    server = str(ctx.message.guild.id)

    with open('servidores.json') as file:
        content = json.load(file)
        file.close()

    for x in content:
        if server in x:
            dispo += 1
            channel = content[x]['Canal']
            channel = int(channel)
            premium = content[x]['Premium']

            if ctx.message.channel.id == channel:
                try:
                    cantidad = int(cantidad)
                except:
                    pass

                if premium == "False":
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 5 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 5 BINS :v ({ctx.message.author.mention})*\nPara generar más el servidor tiene que ser PREMIUM")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        discover = 1
                        gg = 0
                        while discover <= cantidad:
                            Codigosdiscover = "65" + ('').join(random.choices(string.digits, k=4))

                            resp = requests.get(f"https://bincheck.io/bin/{Codigosdiscover}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=Codigosdiscover)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=Codigosdiscover, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=Codigosdiscover)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                                

                            discover += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")
                else:
                    if cantidad == None:
                        await ctx.send(f"*Escoge una cantidad :v ({ctx.message.author.mention})*")
                    elif cantidad > 10 or cantidad <= 0:
                        await ctx.send(f"*SOLO PUEDES GENERAR ENTRE 1 Y 10 BINS :v ({ctx.message.author.mention})*")

                    else:
                        await ctx.send(f"*Generando bins...*\nMira md {ctx.message.author.mention}")

                        discover = 1
                        gg = 0
                        while discover <= cantidad:
                            Codigosdiscover = "65" + ('').join(random.choices(string.digits, k=4))

                            resp = requests.get(f"https://bincheck.io/bin/{Codigosdiscover}", headers=headers)
                            soup = BeautifulSoup(resp.text, 'html5lib')


                            correct = 0
                            for x in soup.find_all('h4', class_='alert-heading'):
                                if 'invalid!' in x.get_text():
                                    embed = discord.Embed(
                                        title = "❌INVÁLIDO❌",
                                        description = "BIN inválido",
                                        color = discord.Color.red()
                                    )
                                    embed.add_field(name="Bin:", value=Codigosdiscover)
                                    embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                    await ctx.author.send(embed=embed)
                                    correct =+1
                                    pass
                                    break

                            if correct == 0:
                                embed = discord.Embed(
                                    title = ":white_check_mark:VÁLIDO:white_check_mark:",
                                    description = "BIN válido",
                                    color = discord.Color.green()
                                )
                                embed.add_field(name="Bin:", value=Codigosdiscover, inline=False)

                                for x in soup.find_all('td', width="40%"):
                                    if x.get_text() == 'Card Brand':
                                        embed.add_field(name="Tarjeta:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Type':
                                        embed.add_field(name="Tipo:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Card Level':
                                        embed.add_field(name="Nivel:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'Issuer Name / Bank':
                                        embed.add_field(name="Banco:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    elif x.get_text() == 'ISO Country Name':
                                        embed.add_field(name="País:", value=f"{x.next_sibling.next_sibling.get_text()}", inline=False)
                                    else:
                                        pass

                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed) 
                                gg +=1


                            else:
                                embed = discord.Embed(
                                    title = "❌INVÁLIDO❌",
                                    description = "BIN inválido",
                                    color = discord.Color.red()
                                )
                                embed.add_field(name="Bin:", value=Codigosdiscover)
                                embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

                                await ctx.author.send(embed=embed)                                
                            

                            discover += 1

                        if gg >= 1:
                            await ctx.author.send("***GG, ahora solo tienes que probar en páginas web con pruebas gratuitas!!***\n||*🤫Los bins son privados y válidos🤫*||")
                        else:
                            await ctx.author.send("***F, no has tenido suerte***\n||*🍀Prueba otra vez, yo te doy suerte🍀*||")

            else:
                await ctx.send(f"***No tienes permisos\nNO estás en el canal adecuado :V {ctx.message.author.mention}***")

            break

        else:
            pass

        
    if dispo == 0:
        await ctx.send("***No se ha establecido ningún canal, avisa al admin\n```Comando:\n!canal #canal```***")

@d.error
async def d_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"BRO, vete más despacio!",
            description=f"Vuélvelo ha intentar en {error.retry_after:.2f}s.",
            color=discord.Color.blue()
            )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)




keep_alive()
client.run(token)