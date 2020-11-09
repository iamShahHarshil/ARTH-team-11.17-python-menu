import os

def hadoopmenu():
	while True:
		os.system("tput setaf 3")
		print('''
		\n\t HADOOP MENU
		----------------------------------------------\n
		Press 1: To configure hadoop Name Node
		Press 2: To configure hadoop data Node
		Press 3: To configure client node
		Press 4: To see hadoop report 
		Press 5: For checking if node is active or not
		Press 6: For Starting node
		Press 7: for stopping node
		Press 8: To list all files in cluster
		Press 9: upload file in cluster
		Press 10: To remove file from cluster
		Press 11: To read a file from cluster on your cli
		Press 12: For hadoop -fs help
		Press 13: upload empty file in cluster
		Press 0 : To exit this menu.		
		''')
		print("\n\tNote: You may need to enter the password multiple times.\n")
		os.system("tput setaf 2")
		ch = input("\nEnter your choice:")
		os.system("tput setaf 7")

		if ch == "1":

			NameNode_IP = input("Provide IP at which you want to configure the Namenode:")
#copy namenode_setup.py into instance to execute 
			os.system("scp namenode-setup.py root@{}:/root".format(NameNode_IP))
#install python3 on the instance in case if not installed
			os.system("ssh root@{} yum install python3 -y".format(NameNode_IP))
#setup namenode's core-site.xml and hdfs-site.xml
			os.system("ssh root@{} python3 namenode-setup.py".format(NameNode_IP))
#format the namenode
			os.system("ssh root@{} namenode -format".format(NameNode_IP))
#start the namenode
			os.system("ssh root@{} hadoop-daemon.sh start namenode".format(NameNode_IP))


		elif ch == "2":	
			Datanode_IP = []
		#	counter_datanode = int(input("\tHow many datanode you want to configure: "))
		#	for i in range(0,counter_datanode):
			dip = input("\tProvide IP at which you want to configure the Datanode: ")
		#	Datanode_IP.append(dip)
			os.system("scp datanode-setup.py root@{}:/root/".format(dip))
			os.system("ssh root@{} yum install python3 -y".format(dip))
			os.system("ssh root@{} python3 datanode-setup.py".format(dip))
#setup datanode's core-site.xml and hdfs-site.xml 
			os.system("ssh root@{} hadoop-daemon.sh start datanode".format(dip))	
#start the datanode

		elif ch == "3":
			Client_IP = []
			counter_client = int(input("\t\t\tHow many client you want to configure: "))
			for i in range(0,counter_client):
				c_ip = input("\t\t\tGive IP at which you want to configure client:")
				Client_IP.append(c_ip)
				os.system("scp client-setup.py root@{}:/root/".format(Client_IP[i]))
				os.system("ssh root@{} yum install python3 -y".format(Client_IP[i]))

			os.system("ssh root@{} python3 client-setup.py".format(Client_IP[i]))
#setup datanode core-site.xml and hdfs-site.xml

		elif ch == "4":
			dip = input("\tProvide IP for which you want to generate report ")
			os.system("ssh root@{} hadoop dfsadmin -report | less".format(dip))

		elif ch == "5":
			dip = input("\tProvide IP at which you want to check status")
			os.system("ssh root@{} jps".format(dip))

		elif ch == "6":
			print("\nWhich one ?\n1) Namenode\n2) Datanode\n0) exit")
			node=input("answer 1/2 ? :")
			if node == "1":
				dip = input("\tProvide IP for namenode that you wish to start ")
				os.system("ssh root@{} hadoop-daemon.sh start namenode".format(dip))
			elif node == "2":
				dip = input("\tProvide IP at which you want to start the Datanode: ")
				os.system("ssh root@{} hadoop-daemon.sh start datanode".format(dip))

			elif node == "0":
				break
			else:
				print("Enter correct option")

	
		elif ch == "7":
			print("\nWhich one ?\n1) Namenode\n2) Datanode\n0) exit")
			node=input("answer 1/2 ? :")
			if node == "1":
				dip = input("\tProvide IP for namenode ")
				os.system("ssh root@{} hadoop-daemon.sh stop namenode".format(dip))
			elif node == "2":
				dip = input("\tProvide IP for datanode")
				os.system("ssh root@{} hadoop-daemon.sh stop datanode".format(dip))

			elif node == "0":
				break
			else:
				print("Enter correct option")

		elif ch == "8":
			os.system("hadoop fs -ls /")

		elif ch == "9":
			print("\n1) Create file and upolad\n2) upload existing file\n0) exit this menu")
			file_o=input("which one:")
			if file_o == "1":
				dip = input("\tProvide IP of node from which you wish to upload file")
				filename1 = input("write file name with extension: ")
				os.system("ssh root@{} vim {}".format(dip,filename1))
				upload = input("Press y to upload:")
				if upload.lower() == "y":
					os.system("ssh root@{} hadoop fs -put {} /".format(dip,filename1))
				else:
					break
			elif file_0 == "2":
				dip = input("\tProvide IP of node from which you wish to upload file")
				filename2 = input("Enter your file name that you want to upload:")
				os.system("ssh root@{} hadoop fs -put {} /".format(dip,filename2))

			elif file_0 == "0":
				break
			else:
				print("Enter correct option")


		elif ch == "10":
			remfile = input("Enter file name that you wish to delete:")
			os.system("hadoop fs -rm /{}".format(remfile))

		elif ch == "11":
			readfile = input("Enter file name that you wish to read:")
			os.system("hadoop fs -cat /{}".format(readfile))

		elif ch == "12":
			os.system("hadoop fs -help")

		elif ch == "13":
			fname = input("Enter file name:")
			os.system("hadoop fs -touchz /{}".format(fname))

		elif ch == "0":
			break
	
		else:
			os.system("tput setaf 1")
			print("\nEnter correct option")

