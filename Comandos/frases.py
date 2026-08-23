import random
import discord
from discord.ext import commands

#Lista
lista_frases = ['Eu só falo pq ta ruim, se tivesse bom eu não comentava.',
          'Eu to na call tetsuya',
          'Interessante, interesante, interesante.',
          'Cometa sukoku',
          'Coisa boa',
          'Ja ouviu falar do evento que esta ocorrendo no servidor?']

#Comando para sortear frases aleatorias de uma lista
@commands.command()
async def frases(ctx):
    frase_sorteada = random.choice(lista_frases)
    await ctx.send(frase_sorteada)

async def setup(bot):
    bot.add_command(frases)
