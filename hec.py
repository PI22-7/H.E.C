from http import server
import os
import subprocess
import time
import discord
from discord.ext import commands

# bot prefix + apikey read output
bot = commands.Bot(command_prefix='$')
apiKey = "discordApiKey.txt"
serverstatus = 'free'

# Reads from the apikey file (discordApiKey.txt)
with open(apiKey) as f:
    key = f.read()
    
# basic ping command
@bot.command()
async def ping(ctx):
   await ctx.send('pong')

# shows manual entry in an embeded format
@bot.command()
async def man(ctx):
    embed = discord.Embed(color=11768407)
    embed.add_field(name='man', value='displays this manual entry', inline=False)
    embed.add_field(name='ping', value='pong', inline=False)
    embed.add_field(name='starbound', value='starts the starbound server', inline=False)
    embed.add_field(name='terraria', value='starts the terraria server', inline=False)
    embed.add_field(name='minecraft', value='starts the minecraft server', inline=False)
    embed.add_field(name='projectzomboid', value='starts the zomboid server', inline=False)
    embed.add_field(name='stop', value='stops any/all servers running', inline=False)
    await ctx.send(embed=embed)
    await ctx.send('more game support coming soon')

# kill command
@bot.command()
async def hardkill(ctx):
    os.system('killall screen')

# stop command
# uses a bash command to kill a process, prob a better way todo it tbh
@bot.command() #screen back into it?
async def stop(ctx):
    global serverstatus
    if serverstatus == 'running starbound':
        os.system('sudo screen -r sbscreen -X quit')
        await ctx.send('starbound server shut down')

    elif serverstatus == 'running terraria':
        os.system('sudo screen -r trscreen -X quit')
        await ctx.send('starbound server shut down')

    elif serverstatus == 'running minecraft':
        os.system('cd /opt/scripts/ && sudo ./mcstop.sh')   
        await ctx.send('starbound server shut down')

    elif serverstatus == 'running project zomboid':
        os.system('sudo screen -r pzscreen -X quit')
        await ctx.send('starbound server shut down')

    else:
        ctx.send('no server running')
    
    serverstatus = 'free'
    await ctx.send('done')

# spool up commands for various game servers -> adds current server the bots status
@bot.command()
async def starbound(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.send('commencing starbound launch')
        print('starbound server spooling up')
        await bot.change_presence(activity=discord.Game(name='starbound'))
        serverstatus = 'running starbound'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')

@bot.command()
async def terraria(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.send('commencing terraria server launch')
        print('terraria server spooling up')
        await bot.change_presence(activity=discord.Game(name='terraria'))
        serverstatus = 'running terraria'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')

@bot.command()
async def minecraft(ctx):
    global serverstatus 
    if serverstatus == 'free':
        await ctx.send('commencing vanilla minecraft server launch')
        print('vanilla minecraft server spooling up')
        os.system('cd /opt/scripts/ && sudo ./mcstart.sh ')
        await bot.change_presence(activity=discord.Game(name='vanilla minecraft'))
        serverstatus = 'running minecraft'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')

@bot.command()
async def projectzomboid(ctx):
    global serverstatus
    if serverstatus == 'free':
        print('zomboide server spooling up')
        await ctx.send('commencing project zomboid launch')
        await bot.change_presence(activity=discord.Game(name='project zomboid'))
        os.system('sudo screen -X quit') # cleans all other sessions before starting
        os.system('sudo screen -AmdS pzscreen bash ./pz.sh')
        serverstatus = 'running projectzomboid'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')


# runs from api key file output, closes api key file
bot.run(key)
apiKey.close()