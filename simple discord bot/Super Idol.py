import discord
from discord.ext.commands import Bot
import random

Super_idol = Bot(command_prefix='s!')
command_list = {'hello', 'flip'}

master = ['Hello master <3',
          'I love you master,'
          ' you are the best',
          'Awww master talked to me >///<',
          'How was your day master?']

pleb = ['I am not talking to plebs',
        'You are not my master, don\'t talk to me',
        'Fuck off']


@Super_idol.event
async def on_ready():
    print('Logged in as')
    print(Super_idol.user.id)
    print(Super_idol.user.name)
    print('--------------------')

    game = discord.Game()
    game.name = f"Type s!help for help."
    await Super_idol.change_presence(game=game)


@Super_idol.event
async def on_message(message):

    #COMMANDS
    if message.content.upper().startswith('S!HELP'):
        await Super_idol.send_message(message.channel, 'commands:\n'
                                                       's!coin (flips a coin) \n'
                                                       's!icon (returns your profile picture)')
    if message.content.upper().startswith('S!COIN'):
        coin = random.choice(['***Heads***', '***Tails***'])
        result = "Your result was " + coin
        await Super_idol.send_message(message.channel, result)
    elif message.content.upper().startswith('S!ICON'):
        avatar = message.author.avatar
        user_id = message.author.id
        await Super_idol.send_message(message.channel, 'https://cdn.discordapp.com/avatars/'
                                      + user_id
                                      + '/'
                                      + avatar
                                      + '.png')
    elif message.content.upper().startswith('S!PLAY'):
        await Super_idol.send_message(message.channel, 'not implemented')

    if master_mentioned(message.content):
        if message.author.id != '311020380460679168':
            await Super_idol.send_message(message.channel, 'Don\'t talk to my master')

    if message.author.bot:
        return
    elif mentioned_in(message.content):
        if message.author.id == '311020380460679168':
            await Super_idol.send_message(message.channel, random.choice(master))
        else:
            await Super_idol.send_message(message.channel, random.choice(pleb))


def mentioned_in(message):
    message = str(message)
    if message.find('<@353975426877489153>') != -1:
        return True
    else:
        return False


def master_mentioned(message):
    message = str(message)
    if message.find('<@!311020380460679168>') != -1:
        return True
    else:
        return False


Super_idol.run('MzUzOTc1NDI2ODc3NDg5MTUz.DI3h3A.YTLkB0i0Op4iEFd9--UlYIOYjng')
