import getpass
import telnetlib
import sys

HOST = "192.168.122.122"
user = input("Enter your user name: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)


tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n" )
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii')+ b"\n" )

#tn.write("password \n")
tn.write(b"enable"+ b"\n")
tn.write(b"shubham"+ b"\n")
tn.write(b"conf t "+ b"\n")
tn.write(b"int Ethernet 3/3 "+ b"\n")
tn.write(b"ip address 192.168.125.126 255.255.255.0 "+ b"\n")
tn.write(b"no shutdown"+ b"\n")

tn.write(b"end"+ b"\n")
tn.write(b"exit"+ b"\n")
tn.write(b"exit"+b"\n")
print (tn.read_all().decode('ascii')) 
