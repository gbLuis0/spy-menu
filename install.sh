#!/usr/bin/bash
clear
apt update
apt upgrade -y

pkg i python figlet ruby -y
pip install pyshorteners
pip install requests
gem install lolcat
clear
echo -e '\e[92;1mDependências instaladas com sucesso :]\e[m'

