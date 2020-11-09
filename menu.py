import os 
import subprocess
import getpass
from os import system


def serverfun():
	while True:
		os.system("tput setaf 3")
		system("clear")
		print("""
		\n
		\t WEB-SERVER MENU 
		-------------------------------------------\n
		Type capital R to go to remote main menu
		Type capital M to go back to main menu
		Press 1: to configure apache web server
		Press 2: to create a web page 
		Press 3: to start web server
		Press 4: to stop web server
		Press 5: to remove web server
		press 6: to permanentlay enable web server
		Press 7: to show status of Web server 
		Press 0: to exit this menu
		""")
		print()
		os.system("tput setaf 2")
		ch1 = input("Enter your choice:")
		print(ch1)
		os.system("tput setaf 7")

		if ch1 == "R":
			ip=input("Enter remote ip here: ")
			mainmenuremote(ip)



		elif ch1 == "1":
			os.system("yum install httpd")
			que = input("do you want to create a web page now ? ( y/n )")
			if que.lower() == "y":
				os.chdir("/var/www/html")
				os.system("pwd")
				print("create your web page here")
				name=input("\nEnter name for your web page:")
				os.system("vim {}.html".format(name))
			else:
				print("apache web server installed.")
				os.system("rpm -q httpd")
				que1 = input("Do you want to start web server now? (y/n)")
				if que1.lower() == "y":
					print("starting web server")
					os.system("systemctl start httpd")
					os.system("systemctl status httpd")

		elif ch1 == "2":
			os.chdir("/var/www/html")
			os.system("tput setaf 4")
			print("\nyou are in following directory")
			os.system("pwd")
			os.system("tput setaf 7")
			print("create your web page here")
			name=input("\nEnter name for your web page:")
			os.system("vim {}.html".format(name))

		elif ch1 == "3":
			print("starting web server")
			os.system("systemctl start httpd")
			os.system("systemctl status httpd")
		elif ch1 == "4":
			print("Stopping web server")
			os.system("systemctl stop httpd")

		elif ch1 == "5":
			print("removing web server")
			os.system("yum remove httpd")
			os.system("rpm -q httpd")

		elif ch1 == "6": 
			print("starting web server permenantly")
			os.system("systemctl enable httpd")


		elif ch1 == "7":
			os.system("rpm -q httpd")
			os.system("systemctl status httpd")
			

		elif ch1 == "0":
			os.system("tput setaf 7")
			break
		
		elif ch1 == "M":
			mainmenu()


		else:
			os.system("tput setaf 1")		
			print("enter a valid choice from menu:")




def serverfunrem(ip):
	while True:
		os.system("tput setaf 3")
		system("clear")
		print("""
		\n
		\t REMOTE WEB-SERVER MENU 
		-------------------------------------------\n
		Type capital L to go to local main menu
		Type capital M to go back to main menu
		Press 1: to configure apache web server 
		Press 3: to start web server
		Press 4: to stop web server
		Press 5: to remove web server
		press 6: to permanentlay enable web server
		Press 7: to show status of Web server 
		Press 0: to exit this menu
		""")
		print()
		os.system("tput setaf 2")
		ch1 = input("Enter your choice:")
		print(ch1)
		os.system("tput setaf 7")

		if ch1 == "L":
			mainmenulocal()



		elif ch1 == "1":
			os.system("ssh {} yum install httpd".format(ip))
			print("apache web server installed.")
			os.system("ssh {} rpm -q httpd".format(ip))
			que1 = input("Do you want to start web server now? (y/n)")
			if que1.lower() == "y":
				print("starting web server")
				os.system("ssh {} systemctl start httpd".format(ip))
				os.system("ssh {} systemctl status httpd".format(ip))

		

		elif ch1 == "3":
			print("starting web server")
			os.system("ssh {} systemctl start httpd".format(ip))
			os.system("ssh {} systemctl status httpd".format(ip))
		elif ch1 == "4":
			print("Stopping web server")
			os.system("ssh {} systemctl stop httpd".format(ip))

		elif ch1 == "5":
			print("removing web server")
			os.system("ssh {} yum remove httpd".format(ip))
			os.system("ssh {} rpm -q httpd".format(ip))

		elif ch1 == "6": 
			print("starting web server permenantly")
			os.system("ssh {} systemctl enable httpd".format(ip))


		elif ch1 == "7":
			os.system("ssh {} rpm -q httpd".format(ip))
			os.system("ssh {} systemctl status httpd".format(ip))
			

		elif ch1 == "0":
			os.system("tput setaf 7")
			break
		
		elif ch1 == "M":
			mainmenuremote(ip)


		else:
			os.system("tput setaf 1")		
			print("enter a valid choice from menu:")





def dockerrepo():
	repo = open('docker.repo','w')
	list1 = ["[docker-repo]\n","baseurl=http://download.docker.com/linux/centos/7/x86_64/stable \n","gpgcheck=0"]
	repo.writelines(list1)
	repo.close



def dockerfun():
	while True:
		os.system("tput setaf 3")
		system("clear")
		print("""
		\n\t\t\t\tDOCKER MENU
		---------------------------------------------\n
		Type capital R to go to remote main menu
		Type capital M to go back to main menu
		Press 1: To configure docker
		Press 2: To start docker service
		Press 3: To see status of docker service 
		Press 4: To Pull docker image 
		Press 5: To launch docker OS 
		Press 6: To get inside docker OS
		Press 7: To list all launched OS
		Press 8: For docker info 
		Press 9: TO remove docker OS
		Press 10: To remove all OS at once 
		Press 11: list all docker images present
		Press 12: remove docker image 
		Press 13: to stop docker service 
		Press 14: To REMOVE docker service 
		press 0: TO EXIT  this menu
		""")

		print()
		os.system("tput setaf 2")
		ch2 = input("Enter your choice:")
		print(ch2)
		os.system("tput setaf 7")

		if ch2 == "R":
			ip=input("Enter remote ip here: ")
			mainmenuremote(ip)

		elif ch2 == "1":
			os.system("tput setaf 4")
			print("--> This command will create a repo file for docker installation \n--> list that docker repo file \n --> And install docker-ce service")
			os.system("tput setaf 7")
			yes = input("Do you wish to continue(y/n):")
			if yes.lower() == "y":
				os.chdir("/etc/yum.repos.d/")
				os.system("pwd")
				rightdir = input("Is this correct directory for docker.repo file to be created (y/n)")
				if rightdir.lower() == "y":
					dockerrepo()
					os.system("cd")
					os.system("yum repolist")
					os.system("yum install docker-ce --nobest")
					os.system("rpm -q docker-ce")


		elif ch2 == "2":
			print("Starting docker service:")
			os.system("systemctl start docker")

		elif ch2 == "3":
			os.system("systemctl status docker")

		elif ch2 == "4":
			print("Press 1: To pull ubuntu OS image \n Press 2: To pull CentOS image")

			img = input("choose any one:")
			if img == "1":
				os.system("docker pull ubuntu:14.04")
			elif img == "2":
				os.system("docker pull centos")
			else:
				print("\nSelect correct option")


		elif ch2 == "5":
			os.system("tput setaf 4")
			print("--> This will launch new OS, boot it, logs you in and provide terminal to work on . To get out of that OS, type exit in terminal")
			print("1 --> centos\n2-->ubuntu\n0)Don't launch any OS")
			imglaunch = input("choose any one:")
			name1=input("type name for your OS:")
			os.system("tput setaf 7")
			if imglaunch == "1":
				os.system("docker run -it --name {} centos:latest".format(name1))
			elif imglaunch == "2":
				os.system("docker run -it --name {} ubuntu:14.04".format(name))
			elif imglaunch == "0":
				break

			else:
				print("\nChoose correct option") 
			

		elif ch2 == "6":
			os.system("docker start {}".format(name1))
			os.system("docker attach {}".format(name1))
				

		elif ch2 == "7":
			os.system("docker ps -a")

		elif ch2 == "8":
			os.system("docker info")

		elif ch2 == "9":
			os.system("docker ps -a")
			selectname = input("type in name of os that you like to remove. If there is no OS in above list, than type none")
			if selectname.lower() == "none":
				break
			else:
				os.system("docker rm {}".format(selectname))

		elif ch2 == "10":
			os.system("docker rm `docker ps -a -q`")


		elif ch2 == "11":
			os.system("docker images -a")

		elif ch2 == "12":
			print("\n1) centos\n2) ubuntu os\n0) exit")
			selectos = input("choose any one:")
			if selectos == "1":
				os.system("docker rmi centos")
			elif selectos == "2":
				os.system("docker rmi ubuntu:14.04")
			elif selectos == "0":
				break
			else:
				print("Enter correct options")
			
		elif ch2 == "13":
			os.system("systemctl stop docker")

		elif ch2 == "14":
			os.system("dnf remove docker")


		elif ch2 == "0":
			break

		elif ch2 == "M":
			mainmenulocal()
		
		else:
			os.system("tput setaf 1")
			print("Enter a valid choice from menu")



def dockerfunrem(ip):
	while True:
		os.system("tput setaf 3")
		system("clear")
		print("""
		\n\t\t\t\tREMOTE DOCKER MENU
		---------------------------------------------\n
		Type Capital L to go to local main menu
		Type capital M to go back to main menu
		Press 1: To configure docker
		Press 2: To start docker service
		Press 3: To see status of docker service 
		Press 4: To Pull docker image 
		Press 5: To launch docker OS 
		Press 6: To get inside docker OS
		Press 7: To list all launched OS
		Press 8: For docker info 
		Press 9: TO remove docker OS
		Press 10: To remove all OS at once 
		Press 11: list all docker images present
		Press 12: remove docker image 
		Press 13: to stop docker service 
		Press 14: To REMOVE docker service
		Press 15: To see if docker is installed or not
		press 0: TO EXIT  this menu
		""")

		print()
		os.system("tput setaf 2")
		ch2 = input("Enter your choice:")
		print(ch2)
		os.system("tput setaf 7")

		if ch2 == "L":
			mainmenulocal()

		elif ch2 == "1":
			os.system("tput setaf 4")
			print("--> This command will create a repo file for docker installation \n--> list that docker repo file \n --> And install docker-ce service")
			os.system("tput setaf 7")
			yes = input("Do you wish to continue(y/n):")
			if yes.lower() == "y":
				os.chdir("/etc/yum.repos.d/")
				os.system("pwd")
				rightdir = input("Is this correct directory for docker.repo file to be created (y/n)")
				if rightdir.lower() == "y":
					dockerrepo()
					os.system("scp docker.repo {}:/etc/yum.repos.d/".format(ip))
					os.system("cd")
					os.system("ssh {} yum repolist".format(ip))
					os.system("ssh {} yum install docker-ce --nobest".format(ip))
					os.system("ssh {} rpm -q docker-ce".format(ip))


		elif ch2 == "2":
			print("Starting docker service:")
			os.system("ssh {} systemctl start docker".format(ip))

		elif ch2 == "3":
			os.system("ssh {} systemctl status docker".format(ip))

		elif ch2 == "4":
			print("Press 1: To pull ubuntu OS image \n Press 2: To pull CentOS image")

			img = input("choose any one:")
			if img == "1":
				os.system("ssh {} docker pull ubuntu:14.04".format(ip))
			elif img == "2":
				os.system("ssh {} docker pull centos".format(ip))
			else:
				print("\nSelect correct option")


		elif ch2 == "5":
			os.system("tput setaf 4")
			print("--> This will launch new OS, boot it, logs you in and provide terminal to work on . To get out of that OS, type exit in terminal")
			print("1-->centos\n2-->ubuntu\n0-->Don't launch any OS")
			imglaunch = input("choose any one:")
			name1=input("type name for your OS:")
			os.system("tput setaf 7")
			if imglaunch == "1":
				os.system("ssh {} docker run  -i  --name {} centos:latest".format(ip,name1))
			elif imglaunch == "2":
				os.system("ssh {} docker run -i  --name {} ubuntu:14.04".format(ip,name))
			elif imglaunch == "0":
				break

			else:
				print("\nChoose correct option") 
			

		elif ch2 == "6":
			os.system("ssh {} docker ps -a".format(ip))
			name2=input("type name of OS you wish to go in :")
			os.system("ssh {} docker start {}".format(ip,name2))
			os.system("ssh {} docker attach {}".format(ip,name2))
				

		elif ch2 == "7":
			os.system("ssh {} docker ps -a".format(ip))

		elif ch2 == "8":
			os.system("ssh {} docker info".format(ip))

		elif ch2 == "9":
			os.system("ssh {} docker ps -a".format(ip))
			selectname = input("type in name of os that you like to remove. If there is no OS in above list, than type none")
			if selectname.lower() == "none":
				break
			else:
				os.system("ssh {} docker rm {}".format(ip,selectname))

		elif ch2 == "10":
			os.system("ssh {} docker rm `ssh {} docker ps -a -q` --force".format(ip,ip))


		elif ch2 == "11":
			os.system("ssh {} docker images -a".format(ip))

		elif ch2 == "12":
			print("\n1) centos\n2) ubuntu os\n0) exit")
			selectos = input("choose any one:")
			if selectos == "1":
				os.system("ssh {} docker rmi centos".format(ip))
			elif selectos == "2":
				os.system("ssh {} docker rmi ubuntu:14.04".format(ip))
			elif selectos == "0":
				break
			else:
				print("Enter correct options")
			
		elif ch2 == "13":
			os.system("ssh {} systemctl stop docker-ce".format(ip))

		elif ch2 == "14":
			os.system("ssh {} dnf remove docker-ce".format(ip))

		elif ch2 == "15":
			os.system("ssh {} rpm -q docker-ce".format(ip))


		elif ch2 == "0":
			break

		elif ch2 == "M":
			mainmenuremote(ip)
		
		else:
			os.system("tput setaf 1")
			print("Enter a valid choice from menu")






def mainmenulocal():


	while True:
		
		os.system("tput setaf 3")
		system("clear")
		print("""
		\n
		\t\t\t MENU 
		\t-------------------------------------------\n
		\tType capital R to go to remote menu
		\tPress 1: to Enter web server menu
		\tPress 2: to Enter docker menu
		\tPress 3: to Enter hadoop menu
		\tPress 4: to Enter AWS menu
		\tPress 5: to configure yum
		\tPress 0: to exit
		""")
		print()
		os.system("tput setaf 2")
		ch = input("Enter your choice:")
		print(ch)
		os.system("tput setaf 7")

		if ch == "R":
			ip=input("Enter ip of remote here: ")
			mainmenuremote(ip)

		elif ch == "1":
			system("clear")
			serverfun()

		elif ch == "2":
			system("clear")
			dockerfun()

		elif ch == "3":
			import hadoop
			system("clear")
			hadoop.hadoopmenu()

		elif ch == "4":
			import AWS
			system("clear")
			AWS.awsmenu()

		elif ch == "5":
			import yummenu
			system("clear")
			yummenu.yummenu()



		elif ch == "0":
			os.system("tput setaf 7")
			exit()

		else:
			os.system("tput setaf 1")
			print("Enter a valid choice from menu")

def mainmenuremote(ip):


	while True:
		print("you are in this ip:root@{}".format(ip))
		os.system("tput setaf 3")
		system("clear")
		print("""
		\n
		\t\t\t REMOTE MENU 
		\t-------------------------------------------\n
		\tType capital L to go to local main menu
		\tPress 1: to Enter web server menu
		\tPress 2: to Enter docker menu
		\tPress 3: to Enter hadoop menu
		\tPress 4: to Enter AWS menu
		\tPress 5: to configure yum
		\tPress 0: to exit
		\tPress C: To go to local menu
		\tType ip: To change ip of remote connection
		""")
		print()
		os.system("tput setaf 2")
		ch = input("Enter your choice:")
		print(ch)
		os.system("tput setaf 7")

		if ch == "L":
			system("clear")
			mainmenulocal()

		elif ch == "1":
			system("clear")
			serverfunrem(ip)

		elif ch == "2":
			system("clear")
			dockerfunrem(ip)

		elif ch == "3":
			import hadoop
			system("clear")
			hadoop.hadoopmenu()

		elif ch == "4":
			import AWS
			system("clear")
			AWS.awsmenu()

		elif ch == "5":
			import yummenu
			system("clear")
			yummenu.yummenu()

		elif ch == "0":
			os.system("tput setaf 7")
			exit()
		elif ch == "C":
			mainmenulocal()

		elif ch.lower() == "ip":
			ip = input("Enter new ip for remote connection: ")
			mainmenuremote(ip)

		else:
			os.system("tput setaf 1")
			print("Enter a valid choice from menu")
		
system("clear")
password = getpass.getpass(prompt='Enter your password: ')
if password.lower()== 'hs':
	os.system("tput setaf 2")
	print("\t\t\tWELCOME\n")
	print("\n\t"+48*"-")
	print("\n\tARTH team 11.17 python automation task\n")
	os.system("tput setaf 1")
	print('''NOTE: Before using this menu driven program:
--> Make sure you have .iso file attached to your optical drives
--> For hadoop cluster configuration , hadoop and java rpm files should be downloaded and installed in your rhel8 system before hand
 --> For using apache menu, first configure yum from this menu itself
	''')
	os.system("tput setaf 7")
	r = input("Do you want to use this menu remotely or locally(r/l)? ")
	if r.lower() == "l":
		mainmenulocal()
	else:
		ip = input("Enter ip of remote:")
		mainmenuremote(ip) 
else:
	os.system("tput setaf 1")
	print("password incorrect !!")




