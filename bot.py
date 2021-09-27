# PeppersBot.py

import os
import random

import var

import discord
from discord import message
from discord.ext import commands

from dotenv import load_dotenv

#Sacar informacion delicada del .env

load_dotenv()
TOKEN = os.getenv('token')
SERVIDOR = os.getenv('servidor')


bot = commands.Bot(command_prefix="!")

#Informacion de la conexión por consola

@bot.event
async def on_ready():
    servidor = discord.utils.get(bot.guilds, name=SERVIDOR)
    print("\n", bot.user, " se ha conectado al servidor ", servidor.name, " con una ID ", servidor.id, "\n" )

#Código para que el bot liste los usuarios

#    print("Lista de usuarios: \n" )
#    for usuario in servidor.members:
#        print("\t -",usuario.name, ' ')

#Decir cosas

@bot.event
async def on_message(mensaje):
    if mensaje.author == bot.user:
        return
    saludosDeBot = [
        "Hola Juan Carlos, ¿cómo estás chupapijas?",
        "ola k ase",
        "Léete Mistborne",
        "Léete Berserk",
        "Mi nombre es " + var.nombreBot + ", relaciones cibernéticas-humanas",
        "Permíteme contarte mi teoría sobre el último capítulo de One Piece"
    ]
    if (var.nombreBot + " dime algo").lower() in mensaje.content.lower():
        respuesta = random.choice(saludosDeBot)
        await mensaje.channel.send(respuesta)

    #Recuerda poner esta cosa en todos los on_message o los comandos explotan
    await bot.process_commands(mensaje)

#Comandos del bot

@bot.command(name="anilist", help="Envía el AniList del mayor crítico de anime y manga jamás conocido.")
async def comando(ctx):
    anilist = "https://anilist.co/user/TommyPepperoni/"
    respuesta = anilist
    await ctx.send(respuesta)

@bot.command(name="dados", help="Lanza dados. Nomenclatura clásica de rol. EJ: 3d6")
async def roll(ctx, inputDados: str):
    
    arrayInput = inputDados.split("d")

    cantidadDados = int(arrayInput[0])
    carasDado = int(arrayInput[1])

    if cantidadDados < 1 or carasDado < 1:
        await ctx.send("Las caras y la cantidad de dados tienen que ser mayores a 0.")

    elif cantidadDados > 30 or carasDado > 1000:
        await ctx.send("No pidas lanzamientos de más de 30 dados o de dados con más de 1000 caras.")

    else:
        cadena = ""

        for x in range(1,cantidadDados+1):
            x = random.randrange(1,carasDado+1)
            cadena += " " 
            cadena += str(x)

        await ctx.send(cadena)

bot.run(TOKEN)
