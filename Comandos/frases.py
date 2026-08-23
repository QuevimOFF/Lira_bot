import random
import asyncio
from discord.ext import commands

# Lista de frases que o comando pode escolher aleatoriamente
lista_frases = ['Eu só falo pq ta ruim, se tivesse bom eu não comentava.',
          'Eu to na call tetsuya',
          'Interessante, interesante, interesante.',
          'Cometa sukoku',
          'Coisa boa',
          'Ja ouviu falar do evento que esta ocorrendo no servidor?']

lista_de_canais = [1307528000702513233, 1307528290353025075, 1541136836288577586]

# Evento de mandar mensagens aleatorias em canais aleatorios de tempos em tempos
async def loop_frases(bot):
    await bot.wait_until_ready()

    # Laço condicional que vai manter o loop ligado enquanto o bot estiver online
    while not bot.is_closed():
        # Manda a função dormir durante o tempo decidido
        tempo_espera = random.randint(1, 10)
        await asyncio.sleep(tempo_espera)

        # Sorteios
        sorteio_dos_canais = random.choice(lista_de_canais) # Canal sorteado
        frase_sorteada = random.choice(lista_frases) # Frase sorteada
        canal = bot.get_channel(sorteio_dos_canais) # Transformar o id em um canal do discord

        # Verificar se o canal existe, e enviar a frase
        if canal is not None:
            # Tenta enviar a menssagem
            try:
                await canal.send(frase_sorteada)
                print(f"Mensagem aleatória enviada no canal ID: {sorteio_dos_canais}")

            # Caso der erro ele não para o bot e sim volta para o começo do laço
            except Exception as erro:
                print(f"Erro ao enviar no canal {sorteio_dos_canais}. Erro: {erro}")
        else:
            print(f"Canal {sorteio_dos_canais} não foi encontrado.")

# Comando que envia uma frase aleatória da lista
@commands.command()
async def frases(ctx):
    frase_sorteada = random.choice(lista_frases)
    await ctx.send(frase_sorteada)

# Registra o comando para que o bot possa carregá-lo corretamente
async def setup(bot):
    bot.add_command(frases)
    bot.loop.create_task(loop_frases(bot))
