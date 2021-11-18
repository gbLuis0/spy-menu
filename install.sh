#!/bin/bash
clear
apt-get update
apt-get upgrade -y
apt-get install python figlet ruby -y
pip install pyshorteners requests
gem install lolcat
clear
echo -e '\e[92;1mDependências instaladas com sucesso :]\e[m'
