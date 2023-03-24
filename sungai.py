# modules !
import requests, os
from colorama import *
from colorama import Fore, Back, init

# Colors !
y = Fore.GREEN
n = Fore.RED
rs = Style.RESET_ALL

os.system('title Amazon Valid Email Checker')
os.system('cls')
print('''

    ___    __  ______ _____   ____  _   __
   /   |  /  |/  /   /__  /  / __ \/ | / /
  / /| | / /|_/ / /| | / /  / / / /  |/ / 
 / ___ |/ /  / / ___ |/ /__/ /_/ / /|  /  
/_/  |_/_/  /_/_/  |_/____/\____/_/ |_/   
                                          
Coder : Savage Benz
Telegram : @savagebenzoffcial
''')

list = input("Your Mail List : ")
link = "https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2FFoowin-Portable-Monitor-Display-Speaker%2Fdp%2FB09997HB8T%2Fref%3Dnav_ya_signin%3Fdchild%3D1%26keywords%3Dgaming%2Blaptops%26pf_rd_i%3D23508887011%26pf_rd_m%3DATVPDKIKX0DER%26pf_rd_p%3D434db2ed-6d53-4c59-b173-e8cd550a2e4f%26pf_rd_r%3D13Z0BD0XB6XMP1VGVWHM%26pf_rd_s%3Dmerchandised-search-5%26pf_rd_t%3D101%26qid%3D1628115073%26sr%3D8-1-spons%26psc%3D1%26spLa%3DZW5jcnlwdGVkUXVhbGlmaWVyPUEyMVpSV0NPVTc0Vk8xJmVuY3J5cHRlZElkPUEwMjg5MjY1MVRaVTczRUhaRjRQMCZlbmNyeXB0ZWRBZElkPUEwNzg5MzU3M0VJQTY5QUcwUDBQNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&prevRID=8FM5Q6W6QSF4FQFKHA7P&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
head = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')

while True:
	emm = list.readline().replace('\n','')
	if not emm:
		break
	lll = emm.strip().split(':')
	xxx = {'customerName':'ShitSvg','email': lll[0],'password':'SvGHereAah11','passwordCheck':'SvGHereAah11'}
	pp = s.post(link, headers=head, data=xxx).text
	if "You indicated you're a new customer, but an account already exists with the email address" in pp:
		print(f'{y}{emm} '+ f' =>{y} LIVE{rs}' + '             [ Savage Benz ]')
		live = open('live.txt', 'a+')
		live.write(emm + '\n')
	else:
		print(f'{n}{emm}' + f'{rs} => {n}DIE{rs}' + '             [ Savage Benz ]')
		die = open('die.txt', 'a+')
		die.write(emm + '\n')
input('Click Any Key for Exit ...!')


