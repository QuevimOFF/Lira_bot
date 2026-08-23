import os 
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

# Ativar a permissão de leitura de mensagens
intents = discord.Intents.default()
intents.message_content = True

# Criar o bot com o prefixo 'ml!' e as intenções definidas
bot = commands.Bot(command_prefix='ml!', intents=intents)

# Mostra o bot ta vivo no console
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Hentai"))
    
    print('To ficando cada dia mais careca')

# Carregar os comandos do bot
async def carregar_comandos():
    for arquivo in os.listdir('./Comandos'):    
        if arquivo.endswith('.py'):
            nome = arquivo[:-3] # retira os 3 ultimos caracteres
            await bot.load_extension(f'Comandos.{nome}')
            print(f'Comando carregado: {nome}')

# Iniciar o bot
async def main():
    async with bot:
        await carregar_comandos()
        await bot.start(os.getenv('DISCORD_TOKEN'))
        
if __name__ == '__main__':
    asyncio.run(main())
