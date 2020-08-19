# Auther: Jay Kumar
# Email: ad.jaybhagat@gmail.com
# Discription: This system is made for the linux os (Ubuntu 20.04)

import os

print(".....Welcome to the User Friendly Task Handler.....")
while True:
	a =  input("Enter the task: ")
	if 'chrome' in a:
		os.system('google-chrome')
	elif 'sublime' in a:
		os.system('subl')
	elif 'vlc' in a:
		os.system('vlc')
	elif 'eclipse' in a:
		os.system('eclipse')
	elif 'firefox' in a:
		os.system('firefox')
	elif 'camera' in a:
		os.system('cheese')
	elif 'netbeans' in a:
		os.system('netbeans')
	elif 'virtualbox' in a:
		os.system('virtualbox')
	elif 'pycharm' in a:
		os.system('pycharm-community')
	elif 'shotwell' in a:
		os.system('shotwell')
	elif 'text' and 'editor' in a:
		os.system('gedit')
	elif 'jupyter' in a:
		os.system('jupyter-notebook')
	elif 'spyder' in a:
		os.system('spyder')
	elif 'vscode' in a:
		os.system('vscode')
	else:
		print("Not Support")
		exit()