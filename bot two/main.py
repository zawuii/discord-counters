import discord
import time
client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        int(message.content)
        time.sleep(0.2)
        number = int(message.content)
        time.sleep(0.2)
        await message.channel.send(str(number + 1))
        time.sleep(0.2)
    except TypeError:
        return
    except ValueError:
        return
    except discord.errors.Forbidden:
        return

client.run('INSERT TOKEN HERE')
