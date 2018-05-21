from datetime import datetime

from netmiko import ConnectHandler
from devices import cisco_ios1, cisco_ios2, cisco_ios3

def check_bgp(net_connect, cmd='show run | inc router bgp'):
	output = net_connect.send_command_expect(cmd)
	return 'bgp' in output

def main():
	device_list = [cisco_ios1, cisco_ios2, cisco_ios3]
	start_time = datetime.now()
	#print
	for a_device in device_list:
		net_connect = ConnectHandler(**a_device)
		net_connect.enable()
		print( "{}: {}".format(net_connect.device_type, net_connect.find_prompt()))
		if check_bgp(net_connect):
			print(check_bgp(net_connect))
			print("BGP is already active")
		else:
			print(check_bgp(net_connect))
			print("no BGP")

	print( "Time elapsed: {}\n".format(datetime.now() - start_time))



main()
