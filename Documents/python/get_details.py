import json
from napalm import get_network_driver
from sys import exit

host_ip = input("Please enter your host device's IP : ")
user_name = input ("Please enter your host device's USERNAME : ")
pass_word = input("Please enter your PASSWORD : ")
secret_pass = input("Please enter your enable PASSWORD : ")

driver = get_network_driver('ios')
optional_argument = {'secret' : secret_pass}
r3 = driver(hostname=host_ip,username=user_name,password=pass_word,optional_args=optional_argument)

r3.open()

def menu():
	ans=True
	while ans:
		print ("""
    		1. Show general information 
    		2. Show Interfaces
    		3. Show Mac-address table
    		4. Show ARP table
		5. Show Neighbors
		6. Exit
    		""")
		ans=input("What would you like to do? ")
		if ans=="1":
			general_facts()
		elif ans=="2":
			interface_info()
		elif ans=="3":
			mac_address_table()
		elif ans=="4":
			arp_table()
		elif ans =="5"
			display_neighbors()
		elif ans=="6":
			print("\n Good Bye")
			exit()	
		else:
			print("Please enter a valid option")

def general_facts():
	ios_output = r3.get_facts()
	print ('\n'*50)
	print ('#'*15,' GENERAL INFORMATION ','#'*15,'\n')
	print(json.dumps(ios_output, indent =5 ))

def interface_info():
	ios_output = r3.get_interfaces()
	print ('\n'*50)
	print ('#'*15,' INTERFACES ','#'*15,'\n')
	print(json.dumps(ios_output, indent = 5))

def mac_address_table():
	ios_output = r3.get_mac_address_table()
	print ('\n'*50)
	print ('#'*15,' MAC ADDRESS TABLE ','#'*15,'\n')
	print(json.dumps(ios_output, indent = 5))

def arp_table():
	ios_output = r3.get_arp_table()
	print ('\n'*50)
	print ('#'*15,' ARP TABLE ','#'*15,'\n')
	print(json.dumps(ios_output, indent = 5))

def display_neighbors():
	ios_output = r3.get_lldp_neighbors()
	print ('\n'*50)
	print ('#'*15,' NEIGHBORS ','#'*15,'\n')
	print(json.dumps(ios_output, indent =5))
	
menu()
