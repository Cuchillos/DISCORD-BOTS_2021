#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
import discord
from discord.ext import commands
import time
###################################

client = commands.Bot(command_prefix='!', help_command=None)
token = "YOUR_BOT_TOKEN_HERE"


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="sorteos", url="https://www.twitch.tv/cuchillop"))
    print("Estoy listo :)")


@client.command()
async def sorteo(ctx):

    ajustes = open('ajustes.txt', 'r')
    ajustes = ajustes.read()
    ajustes = str(ajustes)

    sorteo = ajustes.split('/')[0]

    if sorteo == 'True':
        people_r = open('participantes.txt', 'r')
        people_r = people_r.read().splitlines()


        if str(ctx.message.author) in people_r:
            await ctx.send("***Ya has participado en este sorteo :v***")

        else:
            authorr = ctx.message.author

            author_id = ctx.author.id
        
            author = str(ctx.message.author)

            people = open('participantes.txt', '+a')
            people.write(f'{author}\n')
            people.close()

            titulo = ajustes.split('/')[1]

            embed = discord.Embed(
                title = f'🎉{titulo}🎉',
                description = '🎊 🎊',
                color = discord.Color.red()
            )
            embed.add_field(name='Adivina un número del 1 al 20', value='Si aciertas el número y eres la primera persona, te llevas el premio!!', inline=False)
            embed.add_field(name='\u200b', value='Tienes 3 oportunidades, rápido!!', inline=False)
            embed.set_footer(text="👨‍💻cuchillo#7116👨‍💻")

            await ctx.send(embed=embed)

            time.sleep(1)

            await ctx.send("A continuación pon el número...")

            número = ajustes.split('/')[4]
            intento = 3

            ganador_r = open("ganador.txt", 'r')
            ganador_r = ganador_r.read().splitlines()

            while intento != 0:
                if ctx.message.author != client.user and ctx.message.channel.type == discord.ChannelType.private:

                        def check(m):
                            ajustes_r = open('ajustes.txt', 'r')
                            ajustes_r = ajustes_r.read()

                            ganador_r = open("ganador.txt", 'r')
                            ganador_r = ganador_r.read()

                            return m.author == authorr and m.channel.type == discord.ChannelType.private

                        msg = await client.wait_for('message', check=check)

                        ajustes_r = open('ajustes.txt', 'r')
                        ajustes_r = ajustes_r.read()
                        ganador_r = open("ganador.txt", 'r')
                        ganador_r = ganador_r.read()


                        if ajustes_r == '...':
                            await ctx.send(f"Tarde, ya ha ganado {ganador_r}")
                            break
                        
                        else:
                            if author_id == ctx.author.id:
                        
                                if msg.content == número:
                                    ajustes_w = open('ajustes.txt', 'w')
                                    ajustes_w.write('...')
                                    ajustes_w.close()

                                    ganador_w = open('ganador.txt', 'w')
                                    ganador_w.write(author)
                                    ganador_w.close()

                                    participantes_w = open('participantes.txt', 'w')
                                    participantes_w.write('')
                                    participantes_w.close()

                                    correo = ajustes.split('/')[2]
                                    contraseña = ajustes.split('/')[3]

                                    await ctx.send("***GG, has ganado!!***")
                                    time.sleep(1.2)
                                    await ctx.send(f"*Aquí tienes el premio:*\n\nCorreo: ||{correo}||\nContraseña: ||{contraseña}||")
                                    await ctx.send(".\n\n***Recuerda poner captura de pantalla en Pruebas***")
                                    break

                                else:
                                    intento -=1
                                    if intento == 0:
                                        await ctx.send("**F, no has tenido suerte**")
                                        break
                                    else:
                                        await ctx.send(f'**F, intentalo de nuevo**\n*Te quedan {intento} oportunidades!*')

                            else:
                                pass


                else: 
                    pass
            


    else:
        await ctx.send("***NO HAY SORTEOS DISPONIBLES, ESPERA A QUE cuchillo#7116 HAGA UNO***")


@client.command()
async def start(ctx, *, sorteo=None):

    if ctx.author.id == 698930869586362470:
        ajustes = open('ajustes.txt', 'w')
        ajustes.write(sorteo)
        ajustes.close()
        await ctx.send("***Sorteo añadido correctamente :)***")
    else:
        pass


client.run(token)