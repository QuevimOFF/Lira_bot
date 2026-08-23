from discord.ext import commands

@commands.command()
async def ping(ctx):
    latencia = round(ctx.bot.latency * 1000)
    await ctx.send(f"Latência: {latencia}ms")

async def setup(bot):
    bot.add_command(ping)
