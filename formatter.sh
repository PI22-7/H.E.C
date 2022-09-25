#!/bin/bash
cd ~/H.E.C || exit
mkdir papermc terraria valheim starbound projectZomboid factorio dontStarveTogether satisfactory stationeers vintageStory

cd ~/H.E.C/papermc || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh pmcserver
./pmcserver install

cd ~/H.E.C/terraria || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh terrariaserver
./terrariaserver install

cd ~/H.E.C/valheim || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh vhserver
./vhserver install

cd ~/H.E.C/starbound || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh sbserver
./sbserver install

cd ~/H.E.C/projectZomboid || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh pzserver
./pzserver install

cd ~/H.E.C/factorio || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh fctrserver
./fctrserver install

cd ~/H.E.C/dontStarveTogether || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh dstserver
./dstserver install

cd ~/H.E.C/satisfactory || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh sfserver
./sfserver install

cd ~/H.E.C/stationeers || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh stserver
./stserver install

cd ~/H.E.C/vintageStory || exit
wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh vintsserver
./vintsserver install