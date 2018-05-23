
from datetime import datetime
from sys import exit
from netmiko import ConnectHandler
from devices import *

device_list = [cisco_ios1, cisco_ios2, cisco_ios3]
file_name =''

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
	#device_list_for_remove = [cisco_ios1, cisco_ios2, cisco_ios3]
	for device in device_list:
		#print (device)
		as_number = device.pop('as_number')
		net_connect = ConnectHandler(**device)
		net_connect.enable()
		bgp_cmd = "{} {}".format(cmd, str(as_number))
		cmd_list = [bgp_cmd]
		output = net_connect.send_config_set(cmd_list)
		print (output)
		device['as_number'] = as_number

def configure_bgp(net_connect, file_name=''):
	"""Configure BGP on device."""
	file_num = 0
	for device in device_list:
		file_num +=1
		device_type = net_connect.device_type
		print(device_type)
		file_name = 'bgp_' + device_type.split("_ssh")[0]+ str(file_num) + '.txt'
		print(file_name)
		as_number = device.pop('as_number')
		net_connect = ConnectHandler(**device)
		net_connect.enable()
		try:
			output = net_connect.send_config_from_file(config_file=file_name)
			print (output)
		except IOError:
			print ("Error reading file: {}".format(file_name))

		device['as_number'] = as_number
def main():
	#device_list_for_main = [cisco_ios1, cisco_ios2, cisco_ios3]
	start_time = datetime.now()
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
		device['as_number'] = as_number
	print( "Time elapsed: {}\n".format(datetime.now() - start_time))
	ans = True
	while ans:
		print("""
			1. REMOVE BGP FROM ALL DEVICES
			2. CONFIGURE BGP ON ALL DEVICES
			3. EXIT
			""")
		ans = input("What would you like to do? ")
		if ans =="1":
			remove_bgp_config(net_connect,as_number = as_number)
		elif ans =="2":
			# Configure BGP
        		output = configure_bgp(net_connect, file_name)
        		print (output)
		elif ans =="3":
			print(" Good Bye ")
			exit()
		else:
			print("Please enter a valid input")
	#print( "Time elapsed: {}\n".format(datetime.now() - start_time))


main()
