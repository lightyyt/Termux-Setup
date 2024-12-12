from os import system, chdir, path
from sys import exit
from pyfiglet import Figlet

def cls():
	system("clear")


def secret(cmd):
	return system(cmd+"> /dev/null 2>&1")

def install(package, hide=False):
	if hide:
		waiting()
		system("pkg install -y "+package+"> /dev/null 2>&1")
	else:
		system("pkg install -y "+package)


doom = Figlet(font="doom")
tiny = Figlet(font="small")

S_BOLD = "\x1b[1m"
S_CLR = "\x1b[0m"
C_GRAY = "\x1b[90m"
C_RED = "\x1b[31m"
C_LIME = "\x1b[92m"
C_YELLOW = "\x1b[93m"
C_CYAN ="\x1b[96m"

def title():
	print(S_BOLD+C_LIME, end="")
	print(doom.renderText("Termux"))
	print(doom.renderText("Setup"))
	print(C_CYAN+tiny.renderText("v.1.0"))
	print(S_CLR, end="")

def waiting():
	cls()
	print(doom.renderText("This could \ntake some\ntime..."))


def install_shell():
	cls()
	while True:
		title()
		print("Select Shell: ")
		print("")
		print("1) Bash (Preinstalled)")
		print("2) Z-Shell (Easy to Use)")
		print("3) Fish (Beginner-Friendly)")
		print(C_YELLOW+"*) Go Back"+S_CLR)
		_inp = input()

		try:
			_inp = int(_inp)
		except:
			continue #If Not int, retry
		
		if _inp == 1:
			system("chsh -s bash")
			cls()
		elif _inp == 2:
			install("zsh", True)
			system("chsh -s zsh")
			cls()
		elif _inp == 3:
			install("fish", True)
			system("chsh -s fish")
			cls()
		else:
			break
			
def setup_repo():
	system("termux-change-repo")
	
def style_shell():
	if secret("git help") != 0:
		print("git is required. Want to install git now? [Y/N]")	
		if input() == "Y":
			install("git", True)
			cls()
		else:
			return
	
	secret("git clone https://github.com/adi1090x/termux-style ~/termux-style")
	system("cd ~/termux-style && ./install")
	system("termux-style")
	#My Favs are: color 83, font 4
	
def install_progs():
	cls()
	while True:
		title()
		print("Select Program: ")
		print("")
		print("1) Vi")
		print("2) Vi-Mproved (Vim)")
		print("3) NeoVim ")
		print("4) Python 3")
		print("5) Git (Recommended)")
		print("6) zoxide (Replacement for cd)")
		print("7) Fun Commands (cowsay, toilet, figlet)")
		print("8) TMux (Recommended)")
		#print("9) Shell Additions (la)")
		print(C_YELLOW+"*) Go Back"+S_CLR)
		
		_inp = input()

		try:
			_inp = int(_inp)
		except:
			continue #If Not int, retry
		
		if _inp == 1:
			install("x11-repo", True)
			install("vim-gtk", True)
			cls()
		elif _inp == 2:
			install("vim", True)
			cls()
		elif _inp == 3:
			install("neovim", True)
			cls()
		elif _inp == 4:
			install("python3", True)
			cls()
		elif _inp == 5:
			install("git", True)
			cls()
		elif _inp == 6:
			install("zoxide", True)
			cls()
		elif _inp == 7:
			install("cowsay", True)
			install("toilet", True)
			install("figlet", True)
			cls()
		elif _inp == 8:
			install("tmux", True)
			cls()
		else:
			break
	
def install_mods():
	waiting()
	secret("pkg update")
	system("pkg upgrade +y")
	


while True:
	cls()
	title()


	print("What would you like to do?")
	print("")
	print("1) Install Shell")
	print("2) Setup Repo")
	print("3) Style Shell")
	print("4) Install Programs")
	print("5) Update Modules")
	print(C_YELLOW+"*) Exit"+S_CLR)
	print(C_GRAY+"* means any number not listed"+S_CLR)
	inp = input()

	try:
		inp = int(inp)
	except:
		continue #If Not int, retry

	if inp == 1:
		install_shell()
	elif inp == 2:
		setup_repo()
	elif inp == 3:
		style_shell()
	elif inp == 4:
		install_progs()
	elif inp == 5:
		install_mods()
	else:
		print("Goodbye!")
		exit()

