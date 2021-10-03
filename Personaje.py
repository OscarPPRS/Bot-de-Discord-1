import random
import discord
from discord import message
from discord import client
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import check

class Personaje:

    def __init__(self, nombre:str):

        self.nombre = nombre
        self.vida = 100
        self.ataque = 10
        self.evasion = 20
        self.precision = 10
        self.clase = "Guerrero"
        self.estaVivo = True   


    async def ComprobacionVida(self,ctx):
         
        if self.vida <= 0:
            self.estaVivo = False
            await ctx.send(self.nombre + " está inconsciente.")

    async def Atacar(self, objetivo, ctx):

        respuesta =""

        respuesta += ("Turno de " + self.nombre + ":\n\n")

        respuesta += (self.nombre + " intenta atacar a " + objetivo.nombre +"\n")

        dadoAtaque = random.randint(1,20)

        respuesta += ("Has sacado un " + str(dadoAtaque) + " en tu d20 para acertar el golpe.\n")

        await ctx.send(respuesta)

        respuesta = ""
        #Intentos de ataque

        if (dadoAtaque + self.precision) >= objetivo.evasion:

            respuesta += ("Has acertado el golpe!!!\n")

            #Daño del golpe

            dadoDanio = random.randint(1,8)

            respuesta +=("Has sacado un " + str(dadoDanio) + " en tu d8 para hacer daño al objetivo.\n")

            danioTotal = self.ataque + dadoDanio
            objetivo.vida -= danioTotal

            respuesta +=(objetivo.nombre + " recibe " + str(danioTotal) + " puntos de daño y ahora su vida es "+ str(objetivo.vida)+ "\n")

            await ctx.send(respuesta)
        else:
            await ctx.send(objetivo.nombre + " esquivó el golpe.")

        await ctx.send("----------------------------------------")
        
        await objetivo.ComprobacionVida(ctx)
       
    async def Combate(self, enemigo, ctx, bot):

        respuesta = ""

        await ctx.send(self.nombre + " HA ENTRADO EN COMBATE CON " + enemigo.nombre+ "\n")

        huida = False

        while self.estaVivo & enemigo.estaVivo:

            respuesta =""

            respuesta += "Atacar\n"

            respuesta += "Intentar huir\n"

            await ctx.send(respuesta)            

            accion = await bot.wait_for("message", check=check)

            #Atacar al enemigo

            if accion.content.lower() == "atacar":
                await self.Atacar(enemigo,ctx)

            #Intento de huida

            elif accion.content.lower() == "huir":
                intentoHuida = random.randint(1,6)
                if intentoHuida == 1:
                    await ctx.send(self.nombre + " escapa del combate como un cobarde.")
                    huida = True
                    break
                else:
                    await ctx.send("No has logrado escapar.")
            
            if self.estaVivo == False:
                break
            elif enemigo.estaVivo == False:
                break

            await enemigo.Atacar(self,ctx)

        #Resultados del encuentro
        
        if huida:           
            pass
        elif self.estaVivo:
            await ctx.send(self.nombre + " es el ganador.")

        elif enemigo.estaVivo:
            await ctx.send(enemigo.nombre + " es el ganador.")
        else:
            await ctx.send("Empate.")
            

            




        


