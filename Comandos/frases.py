import random
import discord
from discord.ext import commands

# Lista de frases que o comando pode escolher aleatoriamente
lista_frases = ['Eu só falo pq ta ruim, se tivesse bom eu não comentava.',
          'Eu to na call tetsuya',
          'Interessante, interesante, interesante.',
          'Cometa sukoku',
          'Coisa boa',
          'Ja ouviu falar do evento que esta ocorrendo no servidor?']

# Comando que envia uma frase aleatória da lista
@commands.command()
async def frases(ctx):
    frase_sorteada = random.choice(lista_frases)
    await ctx.send(frase_sorteada)

# Registra o comando para que o bot possa carregá-lo corretamente
async def setup(bot):
    bot.add_command(frases)
