A discord bot written in python intended to run on a linux server, allowing discord server memebers to spool up servers remotley

**warning** this script gives a sizeable quantity of control to any discord user on your server with access to the bot
the script should prevent users from starting more then one server at a time, but only allow people you trust these stupid powers

written by yann rampitsch

## The following steps must be taken for a full installation:

## required programs ##
python 3
python-pip
discord.py
screen

a discord api key with a registered bot account

## add a steam user ##
this is important as the program will look within the steam users files for required programs
it is also important to give the steam user sudo priviliges


## give sudo priviliges
give sudo privilges by adding the steam user to the wheel group
* sudo usermod -a -G wheel 'youruserhere'
this must be done with root or a user already equiped with sudo access
if you are having trouble with this step verify you have your sudoers file setup correctly
* visudo
uncommment:

## adding steamcmd ##
(for debian):

    to add steamcmd add this string to 
    $ nano /etc/apt/sources.list 
        'deb http://ftp.de.debian.org debian buster main non-free'

    $ dpkg --add-architecture i386
    maybe use -> "apt-get install libc6:i386" as well
    $ apt-get update
    $ apt-get upgrade
    $ apt-get dist-upgrade

Next install steamcmd with apt
$ apt install steamcmd

(for arch):

    $ yay -S steamcmd

## folder structure ##
the program will look for games in
    /home/steam/.steam/steamapps/common/
the python script should be placed in
    /home/steam/hec/

you will also need to place you bot token in the /hec/ directory 
name the txt that key is placed in 'discordApiKey.txt'

## project zomboid ## 
$ steamcmd
> login anonymous
> app_update 380870 validate
> quit

port forward the following ports:
* 8766 UDP
* 16261 UDP

## terraria ##
coming soon

## minecraft ##
coming soon

## starbound ##
coming soon