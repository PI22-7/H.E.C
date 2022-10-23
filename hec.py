import os
import discord
import aiomcrcon
from aiomcrcon import Client
from discord.ext import commands

# TODO
# readability > slight preformance increases, if I wanted performance id use C :P
# rust remake when?


# bot prefix + apikey read output
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)
apiKey = "discordApiKey.txt"
rconKey = "rconKey.txt"
serverstatus = 'free'
bot.remove_command('help')

# Reads from the apikey file (discordApiKey.txt)
with open(apiKey) as f:
    key = f.read()

with open(rconKey) as d:
    pwod = d.read()


# def get_pid(name):
#    return check_output(["pidof,name"])


# advanced ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! My latency is {0}ms'.format(round(bot.latency * 1000)))


# shows manual entry in an embeded format
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=11768407)
    embed.add_field(name='help', value='displays this menu', inline=False)
    embed.add_field(name='ping', value='pong with latency', inline=False)
    embed.add_field(name='valheim', value='starts the valheim server', inline=False)
    embed.add_field(name='starbound', value='starts the starbound server', inline=False)
    embed.add_field(name='terraria', value='starts the terraria server', inline=False)
    embed.add_field(name='minecraft', value='starts the minecraft server', inline=False)
    embed.add_field(name='projectzomboid', value='starts the zomboid server', inline=False)
    embed.add_field(name='stop', value='stops any/all servers running', inline=False)
    await ctx.send(embed=embed)
    await ctx.send('more game support coming soon')


# piggybacks off linuxgsm for start/stop functionalities
# this is the logic behind our stop command
@bot.command()
async def stop(ctx):
    if serverstatus == 'running starbound':
        await stop_starbound(ctx)
    elif serverstatus == 'running terraria':
        await stop_terraria(ctx)
    elif serverstatus == 'running minecraft':
        await stop_minecraft(ctx)
    elif serverstatus == 'running zomboid':
        await stop_zomboid(ctx)
    elif serverstatus == 'running valheim':
        await stop_valheim(ctx)
    elif serverstatus == 'running vintagestory':
        await stop_vintagestory(ctx)
    else:
        await idle(ctx)


async def stop_starbound(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/starbound && ./starboundserver stop')
    await ctx.send('starbound server shut down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_terraria(ctx):
    global serverstatus
    os.system('cd/H.E.C/terraria ~ && ./terrariaserver stop')
    await ctx.send('terraria server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_minecraft(ctx):
    global serverstatus
    os.system('cd/H.E.C/papermc ~ && ./pmcserver stop')
    await ctx.send('minecraft server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_zomboid(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/projectZomboid && ./pzserver stop')
    await ctx.send('project zomboid server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_valheim(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/valheim && ./vhserver stop')
    await ctx.send('valheim server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_vintagestory(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/vintageStory && ./vintsserver stop')
    await ctx.send('vintage story server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


@bot.command()
#^ forgot this so tequilla :(
# hopefully no tequilla
async def stop_moddedmc(ctx):
    global serverstatus
    client = Client("192.168.0.35", 25566, pwod)
    await client.connect()
    await client.send_cmd("stop")
    await ctx.send('moddedmc server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def idle(ctx):
    await ctx.send('no server running')
    await bot.change_presence(activity=discord.Game(name='Idle'))


# again uses linuxgsm's start command as well as preventing other server launches (max 1 at once)
@bot.command()
async def starbound(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.send('commencing starbound launch')
        os.system('cd ~/H.E.C/starbound && ./starboundserver start')
        #        print('starbound server spooling up')
        await bot.change_presence(activity=discord.Game(name='starbound'))
        serverstatus = 'running starbound'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


@bot.command()
async def terraria(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.send('commencing terraria server launch')
        os.system('cd ~/H.E.C/terraria && ./terrariaserver start')
        #        print('terraria server spooling up')
        await bot.change_presence(activity=discord.Game(name='terraria'))
        serverstatus = 'running terraria'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


@bot.command()
async def minecraft(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.send('commencing vanilla minecraft server launch')
        os.system('cd ~/H.E.C/papermc && ./pmcserver start')
        #        print('vanilla minecraft server spooling up')
        await bot.change_presence(activity=discord.Game(name='vanilla minecraft'))
        serverstatus = 'running minecraft'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


# yann says im drunk so i shouldnt comment this
@bot.command()
async def moddedmc(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.send('commencing stoneblock minecraft server launch')
        os.system('cd ~/H.E.C/moddedmc/1.12.2/stoneBlock2 && ./start.sh &')
        #        print('modded minecraft server spooling up')
        await bot.change_presence(activity=discord.Game(name='modded minecraft'))
        serverstatus = 'running minecraft'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


# first implementation of linuxGSM, simplifies shit A lot!!!
@bot.command()
async def zomboid(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~/H.E.C/projectZomboid && ./pzserver start')
        await ctx.send('starting projectzomboid server')
        await bot.change_presence(activity=discord.Game(name='project zomboid'))
        serverstatus = 'running zomboid'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


@bot.command()
async def valheim(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~/H.E.C/valheim && ./vhserver start')
        await ctx.send('starting valheim server')
        await bot.change_presence(activity=discord.Game(name='valheim'))
        serverstatus = 'running valheim'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


@bot.command()
async def vintagestory(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~/H.E.C/vintageStory && ./vintsserver start')
        await ctx.send('starting vintage story server')
        await bot.change_presence(activity=discord.Game(name='vintage story'))
        serverstatus = 'running vintagestory'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


# runs from api key file output, closes api key file
bot.run(key)
apiKey.close()
rconKey.close()
