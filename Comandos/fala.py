from discord.ext import commands 

# Define o comando 'fala', que repete o texto enviado pelo usuário
@commands.command()
async def fala(ctx, *, texto):
    await ctx.send(texto)
    await ctx.message.delete()

# Registra o comando no bot
async def setup(bot):
    bot.add_command(fala)
