from discord.ext import commands 

#Comando para o bot repetir o que o usuário digitar
@commands.command()
async def fala(ctx, *, texto):
    await ctx.send(texto)
    await ctx.message.delete()

async def setup(bot):
    bot.add_command(fala)
