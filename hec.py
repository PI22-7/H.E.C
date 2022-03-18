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
    
#def get_pid(name):
#    return check_output(["pidof,name"])


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
    embed.add_field(name='valheim', value='starts the valheim server', inline=False)
    embed.add_field(name='starbound', value='starts the starbound server', inline=False)
    embed.add_field(name='terraria', value='starts the terraria server', inline=False)
    embed.add_field(name='minecraft', value='starts the minecraft server', inline=False)
    embed.add_field(name='projectzomboid', value='starts the zomboid server', inline=False)
    embed.add_field(name='stop', value='stops any/all servers running', inline=False)
    await ctx.send(embed=embed)
    await ctx.send('more game support coming soon')


# piggybacks off linuxgsm for start/stop functionalities 
@bot.command() 
async def stop(ctx):
    global serverstatus
    if serverstatus == 'running starbound':
        os.system('cd ~ && ./starboundserver stop')
        await ctx.send('starbound server shut down')
        await bot.change_presence(activity=discord.Game(name='Idle'))
        serverstatus = 'free'

    elif serverstatus == 'running terraria':
        os.system('cd ~ && ./terraria stop')
        await ctx.send('terraria server shutting down')
        await bot.change_presence(activity=discord.Game(name='Idle'))
        serverstatus = 'free'

    elif serverstatus == 'running minecraft':
        os.system('cd ~ && ./minecraftserver stop')   
        await ctx.send('minecraft server shutting down')
        await bot.change_presence(activity=discord.Game(name='Idle'))
        serverstatus = 'free'
  
    elif serverstatus == 'running project zomboid':
        os.system('cd ~ && ./pzserver stop')
        await ctx.send('project zomboid server shutting down')
        await bot.change_presence(activity=discord.Game(name='Idle'))
        serverstatus = 'free'

    elif serverstatus == 'running valheim':
        os.system('cd ~ && ./valheimserver stop')
        await ctx.send ('valheim server shutting down')
        await bot.change_presence(activity=discord.Game(name='Idle'))
        serverstatus = 'free'

    else:
        ctx.send('no server running')
    
    await ctx.send('done')

# again uses linuxgsm's start command as well as preventing other server launches (max 1 at once)
@bot.command()
async def starbound(ctx):
    global serverstatus
    if serverstatus == 'free':
        await ctx.send('commencing starbound launch')
        os.system ('cd ~ && ./starboundserver start')
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
        os.system ('cd ~ && ./terrariaserver start')
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
        os.system ('cd ~ && ./minecraftserver start')
#        print('vanilla minecraft server spooling up')
        await bot.change_presence(activity=discord.Game(name='vanilla minecraft'))
        serverstatus = 'running minecraft'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')

#first implementation of linuxGSM, simplifies shit A lot!!!
@bot.command()
async def projectzomboid(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~ && ./pzserver start')
        await ctx.send('starting projectzomboid server')
        await bot.change_presence(activity=discord.Game(name='project zomboid'))
        serverstatus = 'running project zomboid'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')

@bot.command()
async def valheim(ctx):
    global serverstatus
    if serverstatus == 'free':
        os.system('cd ~ && ./valheimserver start')
        await ctx.send('starting valheim server')
        await bot.change_presence(activity=discord.Game(name='project zomboid'))
        serverstatus = 'running valheim'
    else:
        await ctx.send('server is busy use "$kill" to kill any instances')




# runs from api key file output, closes api key file
bot.run(key)
apiKey.close()