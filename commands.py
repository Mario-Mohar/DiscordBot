import discord

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

BotCommands = ['!commands', '!news']

@bot.event
async def commands():
    global BotCommands
    print (BotCommands)