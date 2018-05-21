from datetime import datetime

from netmiko import ConnectHandler
from devices import cisco_ios1, cisco_ios2, cisco_ios3


def main():
	device_list = [cisco_ios1, cisco_ios2, cisco_ios3]
	start_time = datetime.now()
	print
	for a_device in device_list:
		net_connect = ConnectHandler(**a_device)
		print( "{}: {}".format(net_connect.device_type, net_connect.find_prompt()))
	print( "Time elapsed: {}\n".format(datetime.now() - start_time))



main()
