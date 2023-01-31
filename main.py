import discord
import mykeys
from commands import BotCommands

my_secret_key = mykeys.secret_key

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
name = None
has_name = False
ask_for_name = False
command = '!bot'
roles = None
ask_for_role = False


@bot.event
async def on_ready():
    global roles, BotCommands
    roles = [role.name for role in bot.guilds[0].roles]
    print(f'{bot.user} is online!')
    print(f'Roles: {roles}')
    print(f'Commands: {BotCommands}')


@bot.event
async def on_message(msg):
    global name, ask_for_name, has_name, ask_for_role
    if msg.author == bot.user:
        return
    print('[New Message]', msg.content)

    if msg.content.startswith(command):
        await who(msg)
        return

    if not has_name:
        if not ask_for_name:
            ask_for_name = True
            await msg.channel.send(f'Whats your name?')
        else:
            name = msg.content
            has_name = True
            await msg.channel.send(f'Nice to meet you, ' + name + '!')

    elif not ask_for_role:
        ask_for_role = True
        role_list = '\n'.join(roles)
        await msg.channel.send(f'What role do you want to have?\n{role_list}')
    else:
        role = discord.utils.get(bot.guilds[0].roles, name=msg.content)
        if role:
            await msg.author.add_roles(role)
            await msg.channel.send(f'You are now a {role.name}!')
        elif
        else:
            await msg.channel.send(f'Role {msg.content} does not exist!')
    return


@bot.event
async def who(msg):
    global BotCommands
    if msg.content.startswith(command):
        await msg.channel.send(f'Du bist hier auf TheMo!\nFolgende Eingaben sind erlaubt {BotCommands}')


@bot.event
async def ask_role(msg):
    global ask_for_role
    ask_for_role = True
    await msg.channel.send(f'What role do you want to have?')


bot.run(my_secret_key)
