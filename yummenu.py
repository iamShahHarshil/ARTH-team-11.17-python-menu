import os
from os import system

def yummenu():
	ip=input("Enter ip of system where you wish to configure yum: ")
	os.system("scp yumrepo.py root@{}:/root".format(ip))
	os.chdir("/etc/yum.repos.d")
	os.system("ssh root@{} python3 /root/yumrepo.py".format(ip))
	os.chdir("/root")
	os.system("ssh root@{} yum repolist".format(ip))
	system("sleep 3")
