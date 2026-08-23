import os 
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define as permissões que o bot precisa para funcionar corretamente
intents = discord.Intents.default()
intents.message_content = True

# Cria a instância do bot com o prefixo 'ml!' e as intenções configuradas
bot = commands.Bot(command_prefix='ml!', intents=intents)

# Evento acionado quando o bot entra online no Discord
@bot.event
async def on_ready():
    # Atualiza o status e a atividade exibida pelo bot
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="The coffin of andy and leyley"
        )
    )

    print('To ficando cada dia mais careca')

# Carrega todos os módulos de comando presentes na pasta 'Comandos'
async def carregar_comandos():
    for arquivo in os.listdir('./Comandos'):
        if arquivo.endswith('.py'):
            nome = arquivo[:-3]
            await bot.load_extension(f'Comandos.{nome}')
            print(f'Comando carregado: {nome}')

# Inicializa o bot e carrega os comandos antes de conectar
async def main():
    async with bot:
        await carregar_comandos()
        await bot.start(os.getenv('DISCORD_TOKEN'))

# Garante que o código só execute quando o arquivo for rodado diretamente
if __name__ == '__main__':
    asyncio.run(main())
