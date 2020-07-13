#must install packet below #You should consider upgrading via the 'python -m pip install --upgrade pip' command.
#pip install inputimeout
#pip install requests

import os
import requests
import sys,time

pingstatus = 1
response = 1

pingstatus2 = 1
response2 = 1



def check_ping():

	#enter your IP 
	hostname2 = "8.8.8.8"#google domain
	hostname = "216.58.196.46"#google domain
	# hostname = "172.0.0.0"#for test
	# hostname2 = "172.0.0.0"#for test
	os.system('cls')#clear screen
	
	#use global var in function
	global pingstatus
	global response

	global pingstatus2
	global response2
	
	#banner area
	print('#'*60)
	print('\n')
	print(" 											")
	print(" 											")
	print("												")
	print("												")
	print(" 											")
	print('\n')
	print('#'*60)
	

	response = os.system("ping -n 4 "+ hostname)#ping hostname

	response2 = os.system("ping -n 4 "+ hostname2)#ping hostname2
	
	
	if response == 0:#ping OK
		
		
		pingstatus = "your information ......Active"
	else:#ping lost
		pingstatus = "your information ......Error"


	if response2 == 0:
		
		
		pingstatus2 = "your information ......Active"
	else:
		pingstatus2 = "your information ......Error"

		
	print('\n')
	print('#'*60)
	print('\n')
	print(pingstatus)
	print('\n')
	print('#'*60)

	print('\n')
	print('#'*60)
	print('\n')
	print(pingstatus2)
	print('\n')
	print('#'*60)
	print('\n')
	

	#ENTER  key to EXIT
	
	from inputimeout import inputimeout, TimeoutOccurred
	try:
		something = inputimeout(prompt='>> ENTER key to EXIT or Waiting  5s for connect', timeout=5)
		sys.exit()
	except TimeoutOccurred:
		something = ''
	print(something)


	
		
	
	


	

#about line notify
url = 'https://notify-api.line.me/api/notify'
token = 'enter your token'#your token
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}



check_ping()


#ping loop zone

while True:
	if response == 0 :
		check_ping()	
		

	else :
		
		print('Ping timeout')
		break

#sent notify to your token	
msg = (pingstatus)
requests.post(url, headers=headers , data = {'message':msg})


while True:
	if response2 == 0 :
		check_ping()	
		

	else :
		
		print('Ping timeout')
		break
	
#test

msg = (pingstatus2)
requests.post(url, headers=headers , data = {'message':msg})

