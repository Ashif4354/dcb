import discord
from discord.ext import commands

token = 'Nzg2MTU2NzQzMjYwMzczMDUy.X9CThQ.uXzlEj_6xYuI40V2TCM3vX0v9XA'
client = commands.Bot(command_prefix = '.')
words = ['ahto', 'kcuf', 'adnup']


@client.event
async def on_ready():
    print('BOT IS READY')

@client.event
async def on_message(message):
    author = message.author
    channel = message.channel
    content = message.content
    content = content.lower()
    output_message = 'MIND YOUR LANGUAGE {}'.format(author)
    
    
    for word in words:
        if word[::-1] in content:
            await channel.send(output_message)
            
    
client.run(token)


