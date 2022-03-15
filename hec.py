from http import server
import os
import subprocess
from subprocess import check_output
import time
import discord
from discord.ext import commands

# TODO
# This is an excessive amount of "if" statements, prob could use a better implementation
# This is to be regarded as a human limitation -> i'll keep learning and see what i can do to improve my shitty code :P

# bot prefix + apikey read output
bot = commands.Bot(command_prefix='$')
apiKey = "discordApiKey.txt"
serverstatus = 'free'

# Reads from the apikey file (discordApiKey.txt)
with open(apiKey) as f:
    key = f.read()
    
def get_pid(name):
    return check_output(["pidof,name"])


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


# piggybacks off linuxgsm for start/stop functionalities 
@bot.command() 
async def stop(ctx):
    global serverstatus
    if serverstatus == 'running starbound':
        os.system('')
        await ctx.send('starbound server shut down')

    elif serverstatus == 'running terraria':
        os.system('')
        await ctx.send('terraria server shutting down')

    elif serverstatus == 'running minecraft':
        os.system('./minecraftserver stop')   
        await ctx.send('minecraft server shutting down')
  
    elif serverstatus == 'running project zomboid':
        os.system('./pzserver stop')
        await ctx.send('project zomboid server shutting down')
    else:
        ctx.send('no server running')
    
    serverstatus = 'free'
    await ctx.send('done')

# again uses linuxgsm's start command as well as preventing other server launches (max 1 at once)
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

        os.system('./pzserver start')

    else:
        await ctx.send('server is busy use "$kill" to kill any instances')




# runs from api key file output, closes api key file
bot.run(key)
apiKey.close()