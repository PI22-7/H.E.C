# pycord go brrrrrr

import os
import discord
import aiomcrcon
from aiomcrcon import Client

# from discord.ext import commands


# intents = discord.Intents.all()
bot = discord.Bot()
apiKey = "discordApiKey.txt"
rconKey = "rconKey.txt"
serverstatus = 'free'
# bot.remove_command('')
# dw abt it


# Reads from the apikey file (discordApiKey.txt)
with open(apiKey) as f:
    key = f.read()

with open(rconKey) as d:
    pwod = d.read()


# def get_pid(name):
#    return check_output(["pidof,name"])

# advanced ping command, the description tag allows a mouse over disc of the cmd
@bot.slash_command(description="Sends the bots ping")
async def ping(ctx):
    await ctx.respond('Pong! My latency is {0}ms'.format(round(bot.latency * 1000)))


# Ignore this, its far too much effort rn

# shows manual entry in an embeded format
# @bot.command()
# async def help(ctx):
#   embed = discord.Embed(color=11768407)
#   embed.add_field(name='help', value='displays this menu', inline=False)
#   embed.add_field(name='ping', value='pong with latency', inline=False)
#   embed.add_field(name='valheim', value='starts the valheim server', inline=False)
#   embed.add_field(name='starbound', value='starts the starbound server', inline=False)
#   embed.add_field(name='terraria', value='starts the terraria server', inline=False)
#   embed.add_field(name='minecraft', value='starts the minecraft server', inline=False)
#   embed.add_field(name='projectzomboid', value='starts the zomboid server', inline=False)
#   embed.add_field(name='stop', value='stops any/all servers running', inline=False)
#   await ctx.respond(embed=embed)
#   await ctx.respond('more game support coming soon')


# piggybacks off linuxgsm for start/stop functionalities
# this is the logic behind our stop command
@bot.slash_command(description="Stops any running servers")
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
    elif serverstatus == 'running modded minecraft':
        await stop_moddedmc(ctx)
    else:
        await idle(ctx)


async def stop_starbound(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/starbound && ./starboundserver stop')
    await ctx.respond('starbound server shut down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_terraria(ctx):
    global serverstatus
    os.system('cd/H.E.C/terraria ~ && ./terrariaserver stop')
    await ctx.respond('terraria server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_minecraft(ctx):
    global serverstatus
    os.system('cd/H.E.C/papermc ~ && ./pmcserver stop')
    await ctx.respond('minecraft server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_zomboid(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/projectZomboid && ./pzserver stop')
    await ctx.respond('project zomboid server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_valheim(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/valheim && ./vhserver stop')
    await ctx.respond('valheim server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def stop_vintagestory(ctx):
    global serverstatus
    os.system('cd ~/H.E.C/vintageStory && ./vintsserver stop')
    await ctx.respond('vintage story server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


# removed 'interesting' comments
async def stop_moddedmc(ctx):
    global serverstatus
    client = Client("192.168.0.35", 25566, pwod)
    await client.connect()
    await client.send_cmd("stop")
    await ctx.respond('moddedmc server shutting down')
    await bot.change_presence(activity=discord.Game(name='Idle'))
    serverstatus = 'free'


async def idle(ctx):
    await ctx.respond('no server running')
    await bot.change_presence(activity=discord.Game(name='Idle'))


# again uses linuxgsm's start command as well as preventing other server launches (max 1 at once)
@bot.slash_command(description="starts a starbound server")
async def starbound(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.respond('commencing starbound launch')
        os.system('cd ~/H.E.C/starbound && ./starboundserver start')
        #        print('starbound server spooling up')
        await bot.change_presence(activity=discord.Game(name='starbound'))
        serverstatus = 'running starbound'
    else:
        await ctx.respond('server is busy use "$stop" to kill any instances')


@bot.slash_command(description="starts a terraria server")
async def terraria(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.respond('commencing terraria server launch')
        os.system('cd ~/H.E.C/terraria && ./terrariaserver start')
        #        print('terraria server spooling up')
        await bot.change_presence(activity=discord.Game(name='terraria'))
        serverstatus = 'running terraria'
    else:
        await ctx.respond('server is busy use "$stop" to kill any instances')


@bot.slash_command(description="starts a minecraft server")
async def minecraft(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.respond('commencing vanilla minecraft server launch')
        os.system('cd ~/H.E.C/papermc && ./pmcserver start')
        #        print('vanilla minecraft server spooling up')
        await bot.change_presence(activity=discord.Game(name='vanilla minecraft'))
        serverstatus = 'running minecraft'
    else:
        await ctx.respond('server is busy use "$stop" to kill any instances')


# nah lol
@bot.slash_command(description="starts a modded minecraft server")
async def moddedmc(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.respond('commencing stoneblock minecraft server launch')
        os.system('cd ~/H.E.C/moddedmc/1.12.2/stoneBlock2 && ./start.sh &')
        #        print('modded minecraft server spooling up')
        await bot.change_presence(activity=discord.Game(name='modded minecraft'))
        serverstatus = 'running modded minecraft'
    else:
        await ctx.respond('server is busy use "$stop" to kill any instances')


# first implementation of linuxGSM, simplifies shit A lot!!!
@bot.slash_command(description="starts a project zomboid server")
async def zomboid(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~/H.E.C/projectZomboid && ./pzserver start')
        await ctx.respond('starting projectzomboid server')
        await bot.change_presence(activity=discord.Game(name='project zomboid'))
        serverstatus = 'running zomboid'
    else:
        await ctx.respond('server is busy use "$stop" to kill any instances')


@bot.slash_command(description="starts a valheim server")
async def valheim(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~/H.E.C/valheim && ./vhserver start')
        await ctx.respond('starting valheim server')
        await bot.change_presence(activity=discord.Game(name='valheim'))
        serverstatus = 'running valheim'
    else:
        await ctx.respond('server is busy use "$stop" to kill any instances')


@bot.slash_command(description="starts a vintagestory server")
async def vintagestory(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~/H.E.C/vintageStory && ./vintsserver start')
        await ctx.respond('starting vintage story server')
        await bot.change_presence(activity=discord.Game(name='vintage story'))
        serverstatus = 'running vintagestory'
    else:
        await ctx.respond('server is busy use "$stop" to kill any instances')


# runs from api key file output, closes api key file
bot.run(key)
apiKey.close()
rconKey.close()
