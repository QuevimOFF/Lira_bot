from discord.ext import commands

# Define o comando 'ping', que mostra a latência do bot
@commands.command()
async def ping(ctx):
    latencia = round(ctx.bot.latency * 1000)
    await ctx.send(f"Latência: {latencia}ms")

# Registra o comando para que ele possa ser usado pelo bot
async def setup(bot):
    bot.add_command(ping)
