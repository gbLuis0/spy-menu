#!/usr/bin/env python3
from requests import get
import datetime
from os import system,execv
import sys
from random import randint,choice
from pyshorteners import Shortener

#cores
f = '\033[m'
vermelho = '\033[31m'
verde = '\033[92;1m'
amarelo = '\033[33m'
azul = '\033[34m'
a = '\033[94;1m'
al = '\033[34;4m'
roxo = '\033[35m'
ciano = '\033[96;1m'
per = '\033[37;7m'
b = '\033[1m'

#def
def restart():
	execv(sys.executable, ['python3'] + sys.argv)
def clear():
	system('cls||clear')
def enter():
	input(f'\nenter para continuar')
def banner():
	system('cat banner | lolcat')
def temp():
	time = datetime.datetime
	date = datetime.date
	hora = time.today().hour
	minute = time.today().minute
	dia = date.today().day
	mes = date.today().month
	ano = date.today().year
	data = f'{verde}Data📆:\033[m \033[1;4m{dia}/{mes}/{ano}\033[m'
	horas = f'{verde}Hora⌚:\033[m \033[1;4m{hora}:{minute}\033[m'
	print(f'{data}\n{horas}')
def avs():
	print(f'{amarelo}Quando digitar a url e der enter, espere uns segundos{f}')

#

clear()
banner()
temp()
try:
	opc = input(f'\n⟬ {a}1{f} ⟭ ━ {a}PAR OU ÍMPAR{f}\n⟬ {a}2{f} ⟭ ━ {a}JOKENPÔ{f}\n⟬ {a}3{f} ⟭ ━ {a}BHASKARA{f}\n⟬ {a}4{f} ⟭ ━ {a}ENCURTA LINK{f}\n⟬ {a}5{f} ⟭ ━ {a}MEU IP{f}\n\n⟬ {a}0{f} ⟭ ━ {a}SAIR{f}\n⟬ {a}98{f} ⟭ ━ {a}ATUALIZAR{f}\n⟬ {a}99{f} ⟭ ━ {a}DIVULGAÇÃO{f}\n\n➤ ').strip().lower()
except:
	restart()
if opc == '':
        restart()
if opc[0] == '1':
	n = npc = c = 0
	ppc = p = ''
	while True:
	    clear()
	    npc = randint(0, 10)
	    system('figlet -f smslant "P ou I?" | lolcat')
	    n = int(input(f'número maior que 10 ou menor que zero para sair\n\033[37;7mNúmero de {f}\033[42m0{f}\033[37;7m a {f}\033[42m10{f} >> '))
	    if n > 10 or n < 0:
	    	restart()
	    s = n + npc
	    p = input(f'Par ou Ímpar? [{azul}p{f}/{azul}i{f}] ').strip().lower()[0]
	    while not p in 'pi':
	        p = input(f'{vermelho}Opção inválida!{f}\nPar ou Ímpar? [{azul}p{f}/{azul}i{f}] ').strip().lower()[0]
	    if p == 'p':
	    	ppc = 'Ímpar'
	    	p = 'Par'
	    else:
	    	ppc = 'Par'
	    	p = 'Ímpar'
	    s = npc + n
	    if ppc == 'Par' and s % 2 == 0 or ppc == 'Ímpar' and s % 2 != 0:
	    	print(f'{vermelho}VOCÊ PERDEU{f}\n\033[4mComputador{f}: {verde}{ppc}{f}, {verde}{npc}{f}')
	    	print(f'\033[4mVocê{f}: {vermelho}{p}{f}, {vermelho}{n}{f}')
	    else:
	    	print(f'{verde}VOCÊ VENCEU{f}')
	    	print(f'\033[4mComputador{f}: {vermelho}{ppc}{f}, {vermelho}{npc}{f}')
	    	print(f'\033[4mVocê{f}: {verde}{p}{f}, {verde}{n}{f}')
	    enter()
elif opc[0] == '2':
	jkp = {'1':'PEDRA','2':'PAPEL','3':'TESOURA'}
	nmr = ['1','2','3']
	while True:
		opcpc = choice(nmr)
		clear()
		system("figlet -f banner 'JOKENPO' | lolcat")
		print(f'''⟬ {ciano}1{f} ⟭ ━ {ciano}PEDRA{f}
⟬ {ciano}2{f} ⟭ ━ {ciano}PAPEL{f}
⟬ {ciano}3{f} ⟭ ━ {ciano}TESOURA{f}
\n⟬ {ciano}0{f} ⟭ ━ {ciano}SAIR{f}''')
		opc = input(f'\n{vermelho}>>>{f} ').strip()[0]
		if opc == '2' and opcpc == '1' or opc == '1' and opcpc == '3' or opc == '3' and opcpc == '2':
			print(f'Computador: \033[41m{jkp[opcpc]}{f}')
			print(f'Você: \033[42m{jkp[opc]}{f}\n')
			print(f'{verde}VOCÊ GANHOU!{f}')
		elif opc == '1' and opcpc == '2' or opc == '3' and opcpc == '1' or opc == '2' and opcpc == '3':
			print(f'Computador: \033[42m{jkp[opcpc]}{f}')
			print(f'Você: \033[41m{jkp[opc]}{f}\n')
			print(f'{vermelho}VOCÊ PERDEU!{f}')
			print(f'{amarelo}Na próxima você consegue...{f}')
		elif opc == opcpc:
			print(f'Computador: \033[44m{jkp[opcpc]}{f}')
			print(f'Você: \033[44m{jkp[opc]}{f}')
			print(f'{amarelo}EMPATE{f}')
		elif opc == '0':
			restart()
		else:
			print(f'\033[4mOps, verifique se selecionou a opção correta...{f}')
		enter()
#swag omo sexual

elif opc[0] == '3':
	while True:
		clear()
		system('cat bannerb | lolcat')
		a = int(input(f'Digite 0 para sair\n{per}Coeficiente A:{f} '))
		if a == 0:
                        restart()
		b = int(input(f'{per}Coeficiente B:{f} '))
		if b == 0:
			restart()
		c = int(input(f'{per}Coeficiente C:{f} '))
		if c == 0:
			restart()
		delta = ((b)**2) -  (4)*(a)*(c)
		if delta == 0:
			print(f'{a}A equação tem duas raízes reais e iguais!{f}')
			baskara = (-(b))/(2*a)
			print(f'{verde}Delta:{f} {delta}')
			print(f'{verde}Baskara:{f} {baskara:.1f}')
		elif delta < 0:
			print(f'{vermelho}A equação não tem raízes reais{f}')
			print(f'{verde}Delta:{f} {delta}')
		elif delta > 0:
			print(f'{a}A equação tem duas raízes reais e distintas!{f}')
			print(f'{verde}Delta:{f} {delta}')
			baskara1p = (-(b) + (delta**0.5))/(2*a)
			baskara2n = (-(b) - (delta**0.5))/(2*a)
			print(f"Baskara X': {baskara1p}")
			print(f"Baskara X'': {baskara2n} ")
		enter()

elif opc[0] == '4':
	while True:
	    clear()
	    print(f'\033[4m{amarelo}escolha como o seu link será encurtado{f}')
	    opc = input(f'⟬ {verde}1{f} ⟭ ━ {verde}Clck.ru{f}\n⟬ {verde}2{f} ⟭ ━ {verde}TinyUrl.com{f}\n⟬ {verde}3{f} ⟭ ━ {verde}Qps.ru{f}\n⟬ {verde}4{f} ⟭ ━ {verde}Chilp.it{f}\n⟬ {verde}5{f} ⟭ ━ {verde}Is.gd{f}\n\n⟬ {verde}0{f} ⟭ ━ {verde}SAIR{f}\n⟬ {verde}i{f} ⟭ ━ {verde}INFO{f}\n{vermelho}>>>{f} ').strip()[0]
	    if opc == '1':
	        avs()
	        url = input('URL: ').strip()
	        enc = Shortener().clckru.short(url)
	        print(f'{azul}Url encurtada{f} >>> {enc}')
	    elif opc == '2':
	        avs()
	        url = input('URL: ').strip()
	        enc = Shortener().tinyurl.short(url)
	        print(f'{azul}Url encurtada{f} >>> {enc}')
	    elif opc == '3':
	        avs()
	        url = input('URL: ').strip()
	        enc = Shortener().qpsru.short(url)
	        print(f'{azul}Url encurtada{f} >>> {enc}')
	    elif opc == '4':
	        avs()
	        url = input('URL: ').strip()
	        enc = Shortener().chilpit.short(url)
	        print(f'{azul}Url encurtada{f} >>> {enc}')
	    elif opc == '5':
	        avs()
	        url = input('URL: ').strip()
	        enc = Shortener().isgd.short(url)
	        print(f'{azul}Url encurtada{f} >>> {enc}')
	    elif opc == '0':
	    	restart()
	    elif opc == 'i':
	    	print('\033[1mSe aparecer a pré-visualização da url, tente por outro encurta!\033[m')
	    else:
	        print('Ops, opção inválida...')
	    enter()
elif opc[0] == '5':
#baiano gay
	ip = get('https://ipinfo.io/what-is-my-ip').json()
	print(f'{b}Seu endereço ip:{f} \033[4m{ip["ip"]}{f}')
	for cha in ip:
		print(f'{verde}{cha}:{f} {ip[cha]}')
	enter()
	restart()
elif opc[0] == '0':
	clear()
	print('\033[93;1mSpy deixou um abraço, volte sempre :)\033[m')
elif opc[:2] == '98':
	system('chmod +x atu.sh && cd && cp spy-menu/atu.sh .')
	system('cd && bash atu.sh')
elif opc[:2] == '99':
	clear()
	system('figlet "G i t H u b" | lolcat')
	print(f'{amarelo}!{f}{verde}Copie e cole a URL no seu navegador{f}{amarelo}!{f}\n')
	print(f'{b}Spyware:{f}\n{al}https://github.com/Spyware0{f}\n')
	print(f'{b}MrDiniz:{f}\n{al}https://github.com/mrdiniz88{f}\n')
	print(f'{b}Swag Baby:{f}\n{al}https://github.com/Swag666baby{f}\n')
	print(f'{b}Matheus-Joestar:{f}\n{al}https://github.com/Matheus-Joestar{f}\n')
	print(f'{b}Peagah:{f}\n{al}https://github.com/TrollPH{f}\n')
	print(f'{b}Dio Brando:{f}\n{al}https://github.com/DioBruh{f}\n')
	print(f'{b}AthenaD3V:{f}\n{al}https://github.com/AthenaD3V{f}\n')
	print(f'{b}Jankess Softwares:{f}\n{al}https://github.com/AsmInstrutor{f}\n')
	print(f'{b}AkTr_:{f}\n{al}https://github.com/AkTr-Team{f}\n')
	print(f'{b}Lacoste:{f}\n{al}https://github.com/lacostehype{f}\n')
	enter()
	restart()

else:
	restart()
