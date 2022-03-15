# H.E.C (Hardware External Controller)
    A discord bot written in python intended to run on a linux server, allowing discord server memebers to spool up servers remotley

    **warning** this script gives a sizeable quantity of control to any discord user on your server with access to the bot
    the script should prevent users from starting more then one server at a time, but only allow people you trust these stupid powers

## Please follow the following steps for a full installation:

### Dependencies
* Linux (ubuntu >18, debian >10, or centos 8 is preferable, in that order) (please see LinuxGSM's site for its recomendations)
* python 3
* python-pip
* discord.py
* linuxGSM (as well as its required dependencies, which can be found here https://linuxgsm.com/, select a game server and see its listed dependencies)
* git (it helps but you cooould do it without)

### Discord
 For this to work you'll need a discord bot with an api key,
 an actual guide on how to do this is here -> https://discordpy.readthedocs.io/en/stable/discord.html
 but i'll just assume you know how to do that (because i'm a terrible teacher :P )
 now that you have that sweet api key make a file called *checks notes* 'DiscordApiKey.txt' (case sensitive), and then paste the key in there and save it (hold onto this for later)

### Steam User
 This part is simple: simply go into you terminal and add a user with
 `sudo adduser steam`
 Then give sudo permissions
 `sudo usermod -a -G sudo steam`
 Lastly swap to them
 `su - steam`

### 