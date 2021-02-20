import discord
from discord.ext import commands
from discord.utils import get



COMMANDS = ['!Настя', '!Крош', '!Общий']


def read_token():
    with open("token", "r") as f:
        lines = f.readline()
        return lines


token = read_token()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Настя') or message.content.startswith('!настя'):
        await message.channel.send('Алейкум Асалам Брат! <@414139850975870977>')

    if message.content.startswith('!Крош') or message.content.startswith('!крош') or message.content.startswith('!Крош') \
            or message.content.startswith('!краш') or message.content.startswith('!Краш'):
        await message.channel.send('Вот в наше время было лучше, <@466706497607565312>')

    if message.content.startswith('!Общий сбор') or message.content.startswith('!Общий'):
        await message.channel.send('А ну метнулись сюда кабанчиком, @everyone')

    if message.content.startswith('!Хелпани') or message.content.startswith('!хелп'):
        for c in COMMANDS:
            await message.channel.send(c)


client.run(token)
