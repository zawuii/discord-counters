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
    if message.content.startswith('start'):
        await message.channel.send("1")
    if message.content.startswith('resume'):
        try:
            await message.channel.send(message.content.replace('resume', ''))
        except TypeError:
            return
        except ValueError:
            return
        except discord.errors.Forbidden:
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


client.run('Nzk2MDk3MjU2NjA0MzAzNDgw.X_S9WA.6lKBKA1sQ6KURKYEvZD6R4hhrtA')
