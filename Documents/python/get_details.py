import json
from napalm import get_network_driver
from sys import exit
from devices_get_details import *

"""
host_ip = input("Please enter your host device's IP : ")
user_name = input ("Please enter your host device's USERNAME : ")
pass_word = input("Please enter your PASSWORD : ")
secret_pass = input("Please enter your enable PASSWORD : ")

driver = get_network_driver('ios')
optional_argument = {'secret' : secret_pass}
r3 = driver(hostname=host_ip,username=user_name,password=pass_word,optional_args=optional_argument)

r3.open()

"""
def ind_details():
	host_ip = input("Please enter your host device's IP : ")
	user_name = input ("Please enter your host device's USERNAME : ")
	pass_word = input("Please enter your PASSWORD : ")
	secret_pass = input("Please enter your enable PASSWORD : ")

	driver = get_network_driver('ios')
	optional_argument = {'secret' : secret_pass}
	router = driver(hostname=host_ip,username=user_name,password=pass_word,optional_args = optional_argument)

	router.open()
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
			info.general_facts(router,host_ip)
		elif ans=="2":
			info.interface_info(router,host_ip)
		elif ans=="3":
			info.mac_address_table(router,host_ip)
		elif ans=="4":
			info.arp_table(router,host_ip)
		elif ans =="5":
			info.display_neighbors(router,host_ip)
		elif ans=="6":
			main_menu()
		else:
			print("Please enter a valid option")
			ans = True

def main_menu():
	choice = True
	while choice:
		print("""
			1. GET INFORMTION FOR ALL DEVICES
			2. GET INFORMATION FOR A PARTICULAR DEVICE
			3. EXIT
		""")
		choice = input("Please choose one option")
		if choice == "1":
			combined_information()
		elif choice == "2":
			ind_details()
		elif choice == "3":
			print("Good Bye")
			exit()
		else:
			print("Enter a valid option")
			choice = True

class Get_facts():
	def __init__(self):
		pass

	def general_facts(self,router,host_ip):
		ios_output = router.get_facts()
		print ('\n'*50)
		print ('#'*15,' GENERAL INFORMATION FOR {}'.format(host_ip),'#'*15,'\n')
		print(json.dumps(ios_output, indent =5 ))

	def interface_info(self,router,host_ip):
		ios_output = router.get_interfaces()
		print ('\n'*50)
		print ('#'*15,' INTERFACES FOR {}'.format(host_ip),'#'*15,'\n')
		print(json.dumps(ios_output, indent = 5))

	def mac_address_table(self,router,host_ip):
		ios_output = router.get_mac_address_table()
		print ('\n'*50)
		print ('#'*15,' MAC ADDRESS TABLE FOR {}'.format(host_ip),'#'*15,'\n')
		print(json.dumps(ios_output, indent = 5))

	def arp_table(self,router,host_ip):
		ios_output = router.get_arp_table()
		print ('\n'*50)
		print ('#'*15,' ARP TABLE FOR {}'.format(host_ip),'#'*15,'\n')
		print(json.dumps(ios_output, indent = 5))

	def display_neighbors(self,router,host_ip):
		ios_output = router.get_lldp_neighbors()
		print ('\n'*50)
		print ('#'*15,' NEIGHBORS FOR {}'.format(host_ip),'#'*15,'\n')
		print(json.dumps(ios_output, indent =5))

info = Get_facts()


def combined_information():
	device_list = [cisco_ios1,cisco_ios2,cisco_ios3,cisco_ios4]
	driver = get_network_driver('ios')
	ans = True
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
			for device in device_list:
				optional_argument = {"secret" : device['secret']}
				r = driver(device['ip'],device['username'],device['password'],optional_args = optional_argument)
				r.open()
				info.general_facts(r,device['ip'])
		elif ans=="2":
			for device in device_list:
                                optional_argument = {"secret" : device['secret']}
                                r = driver(device['ip'],device['username'],device['password'],device['secret'],optional_args=optional_argument)
                                r.open()
                                info.interface_info(r,device['ip'])
		elif ans=="3":
			for device in device_list:
                                optional_argument = {"secret" : device['secret']}
                                r = driver(device['ip'],device['username'],device['password'],device['secret'],optional_args=optional_argument)
                                r.open()
                                info.mac_address_table(r,device['ip'])
		elif ans=="4":
			for device in device_list:
                                optional_argument = {"secret" : device['secret']}
                                r = driver(device['ip'],device['username'],device['password'],device['secret'],optional_args=optional_argument)
                                r.open()
                                info.arp_table(r,device['ip'])
		elif ans =="5":
			for device in device_list:
                                optional_argument = {"secret" : device['secret']}
                                r = driver(device['ip'],device['username'],device['password'],device['secret'],optional_args=optional_argument)
                                r.open()
                                info.display_neighbors(r,device['ip'])
		elif ans =="6":
			main_menu()
		else :
			print("Please enter a valid option")
			ans = True
		

	#device_list = [cisco_ios1,cisco_ios2,cisco_ios3,cisco_ios4]
	#for device in device_list:
	#	r = driver(device)
	#	r.open()

main_menu()
