# Auther: Jay Kumar
# Email: ad.jaybhagat@gmail.com
# Discription: This system is made for the linux os (Ubuntu 20.04)

import os
import pyttsx3

print(".....Welcome to the User Friendly Task Handler of Linux.....")
pyttsx3.speak("Welcome to the User Friendly Task Handler of Linux")
def main():
	while True:
		p =  input("Enter the task: ")
		a = p.lower()
		if ("dont" in a) or ("do not" in a) or ("did not" in a):
			print("Please Try again :")
			pyttsx3.speak("Please try again.")
			print("Do You Like to Continue (Yes/No): ")
			pyttsx3.speak("Do You Like To Continue!(Yes or No):")
			s = input("Your Answer: ")
			opt = s.lower()
			if (opt == 'yes'):
				main()
			elif (opt == 'no'):
				print("\n")
				print("Terminating....")
				break
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
		elif 'studio' in a:
			os.system('vscode')
		else:
			print("Service Not Available")
			pyttsx3.speak("Services Not Available.")
			print("You Like To Konw the Services!(Yes/No)")
			pyttsx3.speak("Do You Like To Konw the Services!(Yes or No):")
			s = input("Your Answer: ")
			opt = s.lower()
			if (opt == 'yes'):
				menu()
			elif (opt == 'no'):
				print("Do you like to Terminate (Yes/No)")
				pyttsx3.speak("Do You Like To Terminate Yes or No")
				q = input("Your Answer: ")
				w = q.lower()
				if w == 'yes':
					print("\n")
					print("Terminating....")
					break
				else:
					main()
def exit():
    print("\n Thank You Using the system")
    pyttsx3.speak("Thank You For using the system!")

def menu():
    print("The Below Are The Services That You can Use.")
    pyttsx3.speak("The Below Are The Services That You can Use")
    print(" Chrome \n Sublime Text 3 \n VLC Player \n Ecplise Editor \n Firefox Browser \n Camera \n Apache Netbeans \n Oracle VirtualBox \n Pycharm \n Text Editor \n Jupyter Notebook \n Spyder For Python \n Visual Studio Code")

main()
exit()