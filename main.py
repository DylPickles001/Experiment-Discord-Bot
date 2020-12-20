import discord
import os


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}                    '.format(client))


#Action made by bot
@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

#Runs bot
client.run(os.getenv('TOKEN'))