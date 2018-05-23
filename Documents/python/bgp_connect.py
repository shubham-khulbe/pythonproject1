
from datetime import datetime
from sys import exit
from netmiko import ConnectHandler
from devices import *

device_list = [cisco_ios1, cisco_ios2, cisco_ios3] # Devices added to the list
file_name =''

def check_bgp(net_connect, cmd='show run | inc router bgp'):
	""" CHECKS IF BGP EXIST OR NOT """
	output = net_connect.send_command_expect(cmd)
	return 'bgp' in output


def remove_bgp_config(net_connect, cmd='no router bgp', as_number=''):
	""" REMOVE BGP FROM ALL DEVICES IN THE GIVEN LIST ONE BY ONE """
	for device in device_list:
		as_number = device.pop('as_number') #Remove AS number from device info so that Connect handler can read arguments correctly
		net_connect = ConnectHandler(**device)
		net_connect.enable() # Entering enable mode
		bgp_cmd = "{} {}".format(cmd, str(as_number))
		cmd_list = [bgp_cmd]
		output = net_connect.send_config_set(cmd_list)
		print (output)
		device['as_number'] = as_number # adding AS number again to pass on to other functions

def configure_bgp(net_connect, file_name=''):
	"""Configure BGP on device."""
	file_num = 0
	for device in device_list:
		file_num +=1 # Iteration to keep the BGP commands file's number
		device_type = net_connect.device_type 
		print("\tConnecting {} : {}".format(device_type,device['ip']))
		file_name = 'bgp_' + device_type.split("_ssh")[0]+ str(file_num) + '.txt' #generates filename with file numbers 
		print("\tReading from the file : {} ".format(file_name))
		as_number = device.pop('as_number') # Removing AS number
		net_connect = ConnectHandler(**device)
		net_connect.enable() # Entering enable mode
		try:
			output = net_connect.send_config_from_file(config_file=file_name) #Sending commands from the file to the device
			print (output)
		except IOError:
			print ("Error reading file: {}".format(file_name))

		device['as_number'] = as_number # Adding back AS number for other functions
def main():
	""" Main fucntion to connect to devices , throw up menu for configurations """
	start_time = datetime.now()
	for device in device_list:
		
		as_number = device.pop('as_number')
		net_connect = ConnectHandler(**device)
		net_connect.enable()
		print( "{}: {}".format(net_connect.device_type, net_connect.find_prompt()))
		if check_bgp(net_connect):
			print("BGP is already active")

		else:
			print("no BGP")
		device['as_number'] = as_number
	print( "Time elapsed: {}\n".format(datetime.now() - start_time))

	""" Next block of code is to print our a menu and take input as "ans" """
	ans = True
	while ans:
		print("""
			1. REMOVE BGP FROM ALL DEVICES
			2. CONFIGURE BGP ON ALL DEVICES
			3. CHECK BGP
			4. EXIT
			""")
		ans = input("What would you like to do? ")
		if ans =="1":
			# Call remove_bgp
			remove_bgp_config(net_connect,as_number = as_number)
		elif ans =="2":
			# Call configure_bgp
        		output = configure_bgp(net_connect, file_name)
        		print (output)

		elif ans =="3":
			# Call self
			main()

		elif ans =="4":
			# Exit program
			print(" Good Bye ")
			exit()

		else:
			print("Please enter a valid input")
	#print( "Time elapsed: {}\n".format(datetime.now() - start_time))


main()
