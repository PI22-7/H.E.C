# H.E.C (Hardware External Controller)
A discord bot written in python intended to run on a linux server, allowing discord server memebers to spool up servers remotley

**warning** this script gives a sizeable quantity of control to any discord user on your server with access to the bot
the script should prevent users from starting more then one server at a time, but only allow people you trust these stupid powers

this guide will assume that you have a very basic understanding of linux and good troubleshooting abilities

I only really plan on implementing games that I play, but i can be swaded with a feature request to add more games.

## Supported Games:
* Terraria (requires a steam account that owns it)
* Minecraft Java
* Project Zomboid
* Valheim
* Starbound

### Planned
* Dont Starve Together
* Factorio
* Satisfactory
* Vintage Story
* Stationeers

### On my radar
* Rust
* Dayz
* Papermc

# Installation Guide

## Dependencies
* Linux (ubuntu >18, debian >10, or centos 8 is preferable, in that order) (please see LinuxGSM's site for its recomendations)
* python 3
* python-pip
* discord.py
* git (it helps but you cooould do it without)

## Discord
 For this to work you'll need a discord bot with an api key,
 an actual guide on how to do this is here -> https://discordpy.readthedocs.io/en/stable/discord.html
 but i'll just assume you know how to do that (because i'm a terrible teacher :P )
 now that you have that sweet api key make a file called *checks notes* 'DiscordApiKey.txt' (case sensitive), and then paste the key in there and save it (hold onto this for later)

## Steam User
 This part is simple: simply go into you terminal and add a user with
 
    `sudo adduser steam`

 Then give sudo permissions
 
     `sudo usermod -a -G sudo steam`
 
 Lastly swap to them
 
     `su - steam`

## Downloading The Script
 Move to your home directory then clone the repos

    `cd ~`
    `git clone https://github.com/PI22-7/H.E.C.git `
    
 Cd into the cloned directory then copy the files and place them inside a new folder called 'hec' !(temporary will devise a better method of this later)!

    `cd ~ && touch hec`    

 Then place the API key within the new 'hec' folder

## Run The Script
 To run the script, start by making sure your in the correct directory (~/python/HEC)

 Next, run the following

    `python3 hec.py`

 You can also make this script start on launch for simplicity (the methods for this vary wildly but using systemd might be the best idea)
 this guide here should give a good starting point (https://www.howtogeek.com/687970/how-to-run-a-linux-program-at-startup-with-systemd/)

## LinuxGSM
 Now that the script indeed starts and your bot comes online, now is a good time to shut it down and begin the linux game server manager installation, I left this out of the depedencies as it needs to be installed in a specific way for the script to work

 Start by going to the website (https://linuxgsm.com/servers/) and look for a game server that you want to install (make sure my script supports it see above), now follow the given installation process, however **make sure to do the following** do not create a user for the server and let the script install to the default location (make sure you are in the steam users home directory 'cd ~' to get there), now that you know that continue by following the rest of the tutorial as normal  (https://linuxgsm.com/servers/) 

 now that that you have a game installed feel free to start the python script again
 congradulations! Your discord bot should work as expected