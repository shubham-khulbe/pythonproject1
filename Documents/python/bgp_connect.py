from datetime import datetime
from sys import exit
from netmiko import ConnectHandler
from devices import *

device_list = [cisco_ios1, cisco_ios2, cisco_ios3]

def check_bgp(net_connect, cmd='show run | inc router bgp'):
	output = net_connect.send_command_expect(cmd)
	return 'bgp' in output
"""
def bgp_remove():
	ans = True
	while ans:
		input_hostname = input("Enter the hostname you want to remove BGP from " )

"""

def remove_bgp_config(net_connect, cmd='no router bgp', as_number=''):
	for device in device_list:
		print (device)
		as_number = device.pop('as_number')
		bgp_cmd = "{} {}".format(cmd, str(as_number))
		cmd_list = [bgp_cmd]
		output = net_connect.send_config_set(cmd_list)
		print (output)



def main():
	#device_list = [cisco_ios1, cisco_ios2, cisco_ios3]
	start_time = datetime.now()
	#print
	for device in device_list:
		#print(device)
		as_number = device.pop('as_number')
		net_connect = ConnectHandler(**device)
		net_connect.enable()
		print( "{}: {}".format(net_connect.device_type, net_connect.find_prompt()))
		if check_bgp(net_connect):
			#print(check_bgp(net_connect))
			print("BGP is already active")

		else:
			#print(check_bgp(net_connect))
			print("no BGP")

	print( "Time elapsed: {}\n".format(datetime.now() - start_time))
	ans = True
	while ans:
		print("""
			1. REMOVE BGP FROM ALL DEVICES
			2. EXIT
			""")
		ans = input("What would you like to do? ")
		if ans =="1":
			remove_bgp_config(net_connect,as_number = as_number)
		elif ans =="2":
			print(" Good Bye ")
			exit()
		else:
			print("Please enter a valid input")
	#print( "Time elapsed: {}\n".format(datetime.now() - start_time))


main()
